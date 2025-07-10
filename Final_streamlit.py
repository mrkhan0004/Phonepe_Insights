# checkdata_app.py

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector
from sqlalchemy import create_engine
import json
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest

# ------------------------
# Database Connection
# ------------------------
engine = create_engine("mysql+mysqlconnector://root:Root@localhost/phonepe")

# ------------------------
# Helper Functions
# ------------------------
@st.cache_data()
def load_geojson():
    with open("india_state.geojson", "r") as f:
        return json.load(f)

@st.cache_data()
def get_states():
    geo = load_geojson()
    return sorted([f['properties']['NAME_1'].strip().title() for f in geo['features']])

@st.cache_data()
def load_query(query):
    return pd.read_sql(query, engine)

# ------------------------
# UI Layout
# ------------------------
st.set_page_config(page_title="PhonePe Data Insights", layout="wide")
st.title("📊 PhonePe Pulse - All-in-One Analysis App")

menu = st.sidebar.selectbox("Select Analysis", [
    "Home",
    "Customer Segmentation",
    "Fraud Detection",
    "Geographical Insights",
    "Insurance Insights",
    "Trend Analysis",
    "User Engagement",
    "Competitive Benchmarking"
])

geojson = load_geojson()
all_states = get_states()
base_df = pd.DataFrame({"state": all_states})

# ------------------------
# Home Page
# ------------------------
if menu == "Home":
    st.subheader("📌 Project Overview")
    st.markdown("""
    This app showcases 10+ business insights from PhonePe transaction data using real-time visualizations,
    including segmentation, fraud detection, trends, user behavior, and insurance adoption.
    """)

    # Show KPIs
    q1 = "SELECT COUNT(DISTINCT state) FROM aggregated_transaction"
    q2 = "SELECT SUM(transaction_amount) FROM aggregated_transaction"
    q3 = "SELECT SUM(registered_users) FROM aggregated_user"
    q4 = "SELECT SUM(insurance_count) FROM aggregated_insurance"

    st.metric("📍 States", pd.read_sql(q1, engine).iloc[0, 0])
    st.metric("💰 Total Transaction ₹", f"{pd.read_sql(q2, engine).iloc[0, 0]:,.0f}")
    st.metric("👥 Registered Users", f"{pd.read_sql(q3, engine).iloc[0, 0]:,}")
    st.metric("🛡️ Total Insured", f"{pd.read_sql(q4, engine).iloc[0, 0]:,}")

    st.markdown("---")  # horizontal line separator

    st.markdown("""
    This interactive dashboard provides a comprehensive analysis of the **PhonePe Pulse** dataset, offering deep insights into the evolving digital payment landscape of India. Leveraging real-time data extracted from PhonePe's open-source repository, this dashboard showcases trends and patterns in three critical domains:

1. **Digital Transactions** – Analyze the total volume and value of transactions across different states, years, and quarters to understand regional payment behavior and economic activity.
2. **User Growth** – Explore how the number of registered users has grown over time, state-wise and across various quarters, reflecting the rapid adoption of digital platforms for financial services.
3. **Insurance Adoption** – Understand how PhonePe users are increasingly engaging with insurance services, including state-wise distribution of insured individuals, total premium payments, and insurance type segmentation.

Key visualizations include:
- Top states by transaction amount
- Yearly and quarterly transaction growth
- Correlation heatmaps between users, transactions, and insurance
- Interactive choropleth maps for regional comparisons

Whether you are a **business analyst**, **policy maker**, **data science enthusiast**, or simply curious about India's fintech evolution, this dashboard enables you to explore the story of India's digital transformation powered by PhonePe.
    """)

    try:
        engine = create_engine("mysql+mysqlconnector://root:Root@localhost/phonepe")
        df = pd.read_sql("SELECT * FROM aggregated_transaction", engine)
        st.write("✅ Database connection successful!")
        st.write("📄 Sample data:", df.head())

        year = st.sidebar.selectbox("Select Year", sorted(df['year'].unique()))
        state = st.sidebar.selectbox("Select State", sorted(df['state'].unique()))

        # Filtered Data
        filtered_df = df[(df['year'] == year) & (df['state'] == state)]

        st.write(f"🔍 Filtered DataFrame size: {len(filtered_df)}")
        st.write("Filtered data:", filtered_df)

        # ✅ Bar Chart: Transaction Amount by Transaction Type
        st.subheader("📊 Transaction Trend by Type")

        # Convert to numeric
        filtered_df['transaction_amount'] = pd.to_numeric(filtered_df['transaction_amount'], errors='coerce')

        # Group & sum
        trend_data = filtered_df.groupby("transaction_type")["transaction_amount"].sum().reset_index()
        trend_data = trend_data.sort_values(by="transaction_amount", ascending=False)

        # Plot
        fig = px.bar(
            trend_data,
            x="transaction_type",
            y="transaction_amount",
            title=f"Total Transaction Amount by Type - {state.title()} ({year})",
            text_auto='.2s',
            color="transaction_type"
        )
        fig.update_layout(xaxis_title="Transaction Type", yaxis_title="Total Amount ₹")
        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"❌ Database connection failed: {e}")
        st.stop()


# ------------------------
# Customer Segmentation
# ------------------------
elif menu == "Customer Segmentation":
    st.subheader("🧠 Customer Segmentation by State")
    df = load_query("SELECT state, SUM(transaction_count) AS transaction_count, SUM(transaction_amount) AS transaction_amount FROM aggregated_transaction GROUP BY state")
    df['state'] = df['state'].str.strip().str.title()
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df[['transaction_amount', 'transaction_count']])
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['cluster'] = kmeans.fit_predict(X_scaled)
    fig = px.scatter(df, x='transaction_amount', y='transaction_count', color='cluster', text='state')
    st.plotly_chart(fig, use_container_width=True)

# ------------------------
# Fraud Detection
# ------------------------
elif menu == "Fraud Detection":
    st.subheader("🚨 Suspicious Transaction Detection")
    df = load_query("SELECT * FROM aggregated_transaction")
    df['z_score'] = (df['transaction_amount'] - df['transaction_amount'].mean()) / df['transaction_amount'].std()
    outliers = df[df['z_score'].abs() > 3]
    st.dataframe(outliers[['state', 'year', 'quarter', 'transaction_amount']])
    st.markdown(f"Found {len(outliers)} suspicious transactions.")

# ------------------------
# Geographical Insights
# ------------------------
elif menu == "Geographical Insights":
    st.subheader("🗺️ State-wise Transaction Map")
    df = load_query("SELECT state, SUM(transaction_amount) AS transaction_transaction_amount FROM aggregated_transaction GROUP BY state")
    df['state'] = df['state'].str.strip().str.title()
    geo_df = base_df.merge(df, on='state', how='left')
    geo_df['transaction_transaction_amount'] = geo_df['transaction_transaction_amount'].fillna(0)
    fig = px.choropleth(
        geo_df,
        geojson=geojson,
        featureidkey='properties.NAME_1',
        locations='state',
        color='transaction_transaction_amount',
        color_continuous_scale='Viridis',
        title='Total Transaction transaction_amount by State'
    )
    fig.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig, use_container_width=True)

# ------------------------
# Insurance Insights
# ------------------------
elif menu == "Insurance Insights":
    st.subheader("🛡️ Insurance Premium Analysis")
    df = load_query("SELECT state, SUM(insurance_amount) AS total_premium FROM aggregated_insurance GROUP BY state")
    df['state'] = df['state'].str.strip().str.title()
    df['state'] = df['state'].replace({
        "Andaman & Nicobar Islands": "Andaman And Nicobar",
        "Delhi": "Nct Of Delhi",
        "Jammu & Kashmir": "Jammu And Kashmir"
    })
    geo_df = base_df.merge(df, on='state', how='left')
    geo_df['total_premium'] = geo_df['total_premium'].fillna(0)
    fig = px.choropleth(
        geo_df,
        geojson=geojson,
        featureidkey='properties.NAME_1',
        locations='state',
        color='total_premium',
        color_continuous_scale='Agsunset',
        title='State-wise Insurance Premium Paid'
    )
    fig.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig, use_container_width=True)

# ------------------------
# Trend Analysis
# ------------------------
elif menu == "Trend Analysis":
    st.subheader("📈 Transaction Trends Over Time")
    df = load_query("SELECT year, quarter, SUM(transaction_amount) AS total_amount FROM aggregated_transaction GROUP BY year, quarter")
    df['time'] = df['year'].astype(str) + '-Q' + df['quarter'].astype(str)
    fig = px.line(df, x='time', y='total_amount', markers=True, title='Quarterly Transaction Trend')
    st.plotly_chart(fig, use_container_width=True)

# ------------------------
# User Engagement
# ------------------------
elif menu == "User Engagement":
    st.subheader("📱 App Usage vs User Growth")
    df = load_query("SELECT year, quarter, state, registered_users, app_opens FROM aggregated_user")
    df['time'] = df['year'].astype(str) + '-Q' + df['quarter'].astype(str)
    agg = df.groupby('time').agg({'registered_users': 'sum', 'app_opens': 'sum'}).reset_index()
    fig, ax1 = plt.subplots(figsize=(12, 5))
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Registered Users", color="blue")
    ax1.plot(agg['time'], agg['registered_users'], color="blue", marker='o')
    ax2 = ax1.twinx()
    ax2.set_ylabel("App Opens", color="orange")
    ax2.plot(agg['time'], agg['app_opens'], color="orange", marker='s')
    ax1.tick_params(axis='x', rotation=45)
    st.pyplot(fig)


# Competitive Benchmarking
# ------------------------
elif menu == "Competitive Benchmarking":
    st.subheader("🏁 Simulated Comparison with Competitors")

    df = load_query("SELECT state, AVG(transaction_amount) AS avg_amount FROM aggregated_transaction GROUP BY state")
    df['state'] = df['state'].str.strip().str.title()

    # Simulate competitor data (Paytm)
    df['Others'] = np.random.uniform(50, 150, len(df))

    # Melt for grouped bar chart
    df = df.melt(id_vars='state', value_vars=['avg_amount', 'Others'], var_name='App', value_name='Amount')

    fig = px.bar(df, x='state', y='Amount', color='App', barmode='group', title="PhonePe vs Paytm (Simulated)")
    st.plotly_chart(fig, use_container_width=True)








