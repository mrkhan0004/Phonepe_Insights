# 📊 PhonePe Pulse Data Analysis & Interactive Dashboard

## 🔖 Project Title:
**PhonePe Pulse Data Visualization and Business Insights using Python, SQL, and Streamlit**

---

## 📌 Overview

This project transforms raw transaction data from the official **[PhonePe Pulse GitHub Repository](https://github.com/PhonePe/pulse)** into a powerful and interactive dashboard. Our goal is to derive **actionable business insights** through data extraction, transformation, and visualization, all powered by:

🔸 Python & SQL for ETL and analysis  
🔸 Streamlit for building a live interactive dashboard  
🔸 Plotly & Seaborn for rich, real-time data visualizations

> 💼 Business use cases include:
- 📍 Customer Segmentation  
- 🔐 Fraud Detection  
- 🛡️ Insurance Penetration Analysis  
- 🌎 State/District-wise Performance  
- 📈 Trend & Growth Insights  

---

## 📂 Data Source

- ✅ **Source**: [PhonePe Pulse GitHub](https://github.com/PhonePe/pulse)
- ✅ **Format**: Raw `.json` files
- ✅ **Categories Covered**:
  - Aggregated Transactions (state/year/quarter)
  - Aggregated Users (registrations, app opens)
  - Aggregated Insurance
  - Top Performing States/Districts

---

## 🛠️ Tech Stack

| Tool | Description |
|------|-------------|
| 🐍 Python | Main scripting language |
| 🗃️ MySQL | Data storage and querying |
| 🌐 Streamlit | Interactive dashboard UI |
| 📚 Libraries | `pandas`, `plotly`, `seaborn`, `matplotlib`, `json`, `os`, `glob`, `sqlalchemy`, `mysql-connector` |

---

## ⚙️ ETL Workflow

1. **Extract**: Parse and flatten nested `.json` files
2. **Transform**: Clean and shape the data into tabular format
3. **Load**: Insert into MySQL database with proper schema

> ✅ **Total Tables Created**: 9  
> (See: `aggregated_transaction`, `top_user`, `map_insurance`, etc.)

---

## 🧮 SQL Tables Created

```bash
aggregated_transaction     -- State-wise transaction volume and count  
aggregated_user            -- User data including app opens and registrations  
aggregated_insurance       -- Insurance count across states  

top_transaction            -- Top performing states/districts by transaction  
top_user                   -- Top states/districts by user activity  
top_insurance              -- Top insurance-adopted regions  

map_transaction            -- District-level transaction mapping  
map_user                   -- District-level user mapping  
map_insurance              -- District-level insurance mapping

Each table is normalized, indexed, and optimized for fast querying and real-time dashboard rendering.

📈 Key Business Insights Enabled
Here’s what this dashboard empowers businesses and analysts to uncover:

Use Case	Description
🎯 Customer Segmentation	Identify active regions, user demographics, and behavioral trends
🛡️ Insurance Penetration	Analyze adoption trends across regions and timeframes
🔐 Fraud Detection	Spot anomalies in transaction spikes or unusual patterns
🌐 Geo Performance	Understand district/state performance across quarters
📊 Growth Trends	Track how usage, users, and transactions evolved over time

📺 Streamlit Dashboard Features
🔍 State-wise Filtering

📆 Year and Quarter Selection

🌏 Choropleth Maps (State & District)

📊 Bar and Line Charts (Plotly)

📋 SQL-Driven Metrics

🧠 Business Intelligence Use Cases

🚀 How to Run This Project
✅ Prerequisites:
Python 3.8+

MySQL Server

All required libraries (see requirements.txt)

⚙️ Setup Instructions:
```bash
# Clone the repo git clone https://github.com/your-username/PhonePe-Pulse-Dashboard.git  
cd PhonePe-Pulse-Dashboard

# Create MySQL DB & load tables using Python scripts

# Launch the dashboard
streamlit run app.py
📌 Final Words
This project converts PhonePe's open-source data into business gold – with just Python, SQL, and Streamlit.

Whether you’re a data analyst, business strategist, or tech enthusiast – this dashboard is your gateway to decoding India’s digital payment trends!

