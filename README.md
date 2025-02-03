# 🛒 Real-Time Sales Data Pipeline

## 🚀 Overview
This project implements an end-to-end real-time data pipeline to process simulated e-commerce sales transactions. The pipeline ingests, transforms, and stores data using **Python**, **Kafka**, **Apache Spark**, and **PostgreSQL**, with automation powered by **Apache Airflow**.

## 🛠️ Tech Stack
- **Python** (ETL Development)
- **Apache Kafka** (Real-Time Data Streaming)
- **Apache Spark** (Data Processing)
- **PostgreSQL** (Database for Storage)
- **Apache Airflow** (Workflow Orchestration)
- **SQL** (Data Analytics)

## 📊 Features
- Real-time data ingestion using Kafka producers and consumers
- Stream processing with Apache Spark
- Automated ETL workflows with Apache Airflow
- Analytical SQL queries for business insights (sales trends, top customers)

## ⚡ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/anqitwa/real-time-sales-pipeline.git
cd real-time-sales-pipeline
```

### 2️⃣ Start Services with Docker
```bash
docker-compose up -d
```
This will start Kafka, PostgreSQL, and Airflow.

### 3️⃣ Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Data Pipeline Manually (for Testing)
```bash
python data_ingestion/kafka_producer.py
python data_processing/spark_processing.py
python data_storage/postgres_loader.py
```

### 5️⃣ Automate with Airflow
- Access Airflow UI at: [http://localhost:8080](http://localhost:8080)
- Login (default credentials: `airflow/airflow`)
- Enable and trigger the `etl_pipeline` DAG

### 6️⃣ Run SQL Analytics
```bash
psql -U postgres -d salesdb -f sql_queries/analytics_queries.sql
```

## 📈 Sample SQL Analytics
- **Total Sales:** Calculate overall revenue.
- **Top Customers:** Identify high-value customers based on purchase history.
- **Sales Trends:** Track sales over time for business insights.

## 📦 Project Structure
```
real-time-sales-pipeline/
├── data_ingestion/           # Kafka Producer & Consumer Scripts
├── data_processing/          # Spark Processing Scripts
├── data_storage/             # PostgreSQL Loading Scripts
├── airflow_dags/             # Airflow DAGs
├── sql_queries/              # SQL Queries for Analytics
├── docker-compose.yml        # Docker for Kafka, PostgreSQL, Airflow
├── requirements.txt          # Python Dependencies
└── README.md                 # Documentation
```

## 🔑 Key Takeaways
- Real-time data streaming with Kafka
- Distributed data processing with Spark
- Automated ETL workflows with Airflow
- Data warehousing and analytics using PostgreSQL and SQL
