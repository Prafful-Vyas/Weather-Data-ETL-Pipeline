Absolutely, Prafful! Here's a clean and professional README tailored for your **Weather Data ETL Pipeline** project, ideal for showcasing on GitHub or your portfolio:

---

# 🌦️ Weather Data ETL Pipeline – Apache Airflow on Astronomer

This project demonstrates a production-grade ETL pipeline using Apache Airflow to ingest, transform, and analyze weather-related data. Built with Astronomer CLI, it runs locally in a containerized environment and showcases dynamic task mapping and Python-native DAGs.

---

## 🚀 Features

- 🔄 ETL pipeline using Airflow’s TaskFlow API
- 🌍 Real-time data ingestion from Open Notify API
- 🧠 Dynamic task mapping to process astronaut data
- 🐳 Containerized deployment via Docker and Astronomer Runtime
- 🧪 Local development with full Airflow stack (Scheduler, Triggerer, Web UI, etc.)

---

## 📁 Project Structure

| Folder/File            | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| `dags/`                | Contains Python DAGs (e.g., `example_astronauts.py`)                        |
| `Dockerfile`           | Defines Astronomer Runtime environment                                      |
| `requirements.txt`     | Python dependencies for DAG execution                                       |
| `packages.txt`         | OS-level packages (optional)                                                |
| `airflow_settings.yaml`| Local-only config for Airflow Connections, Variables, and Pools             |
| `include/`             | Placeholder for additional project files                                    |
| `plugins/`             | Custom Airflow plugins (currently empty)                                    |

---

## 🛠️ Local Deployment

### 1. Start Airflow Locally
```bash
astro dev start
```

This spins up 5 containers:
- Postgres (metadata DB)
- Scheduler
- DAG Processor
- API Server (Web UI)
- Triggerer

Access the Airflow UI at:  
👉 [http://localhost:8080](http://localhost:8080)

### 2. Stop or Restart
```bash
astro dev stop
astro dev restart
```

---

## 📊 DAG Overview

The `example_astronauts` DAG:
- Queries the Open Notify API for current astronauts in space
- Uses dynamic task mapping to print a message for each astronaut
- Demonstrates Python-native DAG structure with Airflow’s TaskFlow API

---

## 📦 Requirements

- Docker
- Astronomer CLI (`pip install astronomer`)
- Python 3.8+

---

## 📎 Resources

- [Getting Started with Astronomer](https://www.astronomer.io/docs/learn/get-started-with-airflow)  
- [Deploy to Astronomer Cloud](https://www.astronomer.io/docs/astro/deploy-code/)  
