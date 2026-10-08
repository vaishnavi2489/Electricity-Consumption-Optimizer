# ⚡ Electricity Consumption Optimizer
### AI-Powered Household Energy Management System

An AI-powered web application for analyzing, forecasting, and optimizing household electricity consumption using **LSTM-based machine learning, anomaly detection, bill calculation, and interactive visualizations**.

---

## 🚀 Live Demo

🌐 **Live Application:**  
https://electricity-consumption-optimizer.onrender.com/

> The application is deployed on **Render** using Streamlit. Since it uses a free Render instance, the application may take a little time to load after a period of inactivity.

---

## 📌 Project Overview

The **Electricity Consumption Optimizer** helps users understand their household electricity usage and make better energy-management decisions.

The system provides:

- 📊 Daily, weekly, and monthly electricity consumption analysis
- 🤖 LSTM-based electricity consumption forecasting
- 🚨 Electricity usage anomaly detection
- 💰 Electricity bill estimation
- 📈 Interactive Plotly visualizations
- 💡 AI-based energy consumption insights
- ⚡ Electrical parameter analysis
- 📉 Historical consumption trends
- 🌐 Interactive Streamlit dashboard

---

## 🏗️ Project Structure

```text
electricity_optimizer/
│
├── data/
│   ├── generate_data.py
│   ├── electricity_data.csv
│   └── daily_clean.csv
│
├── models/
│   └── best_model.h5
│
├── app/
│   └── dashboard.py
│
├── data_preprocessing.py
├── train_model.py
├── main.py
├── requirements.txt
├── .python-version
├── render.yaml
└── README.md
```

---

## 🧠 Technologies Used

| Technology / Library | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data loading, cleaning, and analysis |
| NumPy | Numerical operations |
| Scikit-learn | Data preprocessing and scaling |
| TensorFlow | LSTM model development |
| Matplotlib | Training and evaluation plots |
| Plotly | Interactive data visualizations |
| Streamlit | Web dashboard |
| OpenPyXL | Spreadsheet file handling |
| Render | Cloud deployment |
| Git & GitHub | Version control and source code hosting |

---

## 📊 Dataset

The project works with electricity consumption data containing household energy usage and electrical parameters.

The project can use:

- UCI Household Electric Power Consumption dataset
- Generated/simulation electricity consumption data

### Dataset Generation

The project includes:

```text
data/generate_data.py
```

which can be used to generate sample electricity consumption data.

The generated dataset is stored in:

```text
data/electricity_data.csv
```

After preprocessing, the cleaned dataset is stored in:

```text
data/daily_clean.csv
```

---

## 🔄 System Workflow

```text
Electricity Consumption Data
            ↓
     Data Preprocessing
            ↓
       Data Cleaning
            ↓
    Daily Data Aggregation
            ↓
    Anomaly Detection
            ↓
      Bill Calculation
            ↓
     Feature Preparation
            ↓
      LSTM Forecasting
            ↓
      Model Evaluation
            ↓
   Streamlit Web Dashboard
            ↓
 Energy Consumption Insights
```

---

## 🤖 Machine Learning

The project uses a **Long Short-Term Memory (LSTM)** neural network for electricity consumption forecasting.

LSTM is suitable for this project because electricity consumption is a **time-series problem**, where previous consumption patterns can help predict future consumption.

The trained model is stored at:

```text
models/best_model.h5
```

The dashboard uses the trained model for predictions without retraining the model every time the application starts.

---

## 🚨 Anomaly Detection

The system identifies unusual electricity consumption patterns using statistical anomaly detection techniques.

This helps identify:

- Unusually high consumption
- Unusual daily usage patterns
- Potential energy wastage
- Abnormal consumption periods

---

## 💰 Electricity Bill Calculation

The application estimates electricity bills based on electricity consumption.

The dashboard provides:

- Energy consumption
- Estimated bill amount
- Daily/monthly consumption analysis
- Consumption-based insights

---

## 📊 Dashboard Features

The Streamlit dashboard provides multiple analysis sections.

### 📅 Monthly Summary

Provides an overview of:

- Total energy consumption
- Estimated electricity bill
- Average consumption
- Monthly trends

### 📈 Daily / Weekly / Monthly Analysis

Interactive charts are provided to understand electricity consumption patterns over different time periods.

### ⚡ Electrical Parameters

The dashboard provides analysis of electrical parameters such as:

- Voltage
- Current
- Power
- Power Factor
- Frequency
- Energy consumption

### 🤖 AI Features

The application provides:

- LSTM-based forecasting
- Consumption insights
- Anomaly detection
- Energy optimization recommendations

### 💡 Energy Optimization

The system helps users understand their consumption behavior and provides insights that can help reduce unnecessary electricity usage.

---

## 📈 Expected Results

The model is designed to achieve approximately:

| Metric | Expected Range |
|---|---|
| MAE | ~0.4–0.6 kWh |
| RMSE | ~0.5–0.8 kWh |
| Forecasting Accuracy | ~92–96% |

Actual results may vary depending on the dataset and model training.

---

# 🛠️ Local Installation

## Step 1: Install Python

Install **Python 3.10 or later**.

Verify the installation:

```bash
python --version
```

---

## Step 2: Clone the Repository

```bash
git clone https://github.com/vaishnavi2489/Electricity-Consumption-Optimizer.git
```

Move into the project directory:

```bash
cd Electricity-Consumption-Optimizer
```

---

## Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment on Windows:

```bash
.venv\Scripts\activate
```

---

## Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 5: Run the Dashboard

The recommended way to run the deployed-style dashboard locally is:

```bash
streamlit run app/dashboard.py
```

The dashboard will normally be available at:

```text
http://localhost:8501
```

---

## ▶️ Run the Complete Project

To execute the complete local workflow:

```bash
python main.py
```

The workflow performs:

1. Dataset generation
2. Data preprocessing
3. Daily data aggregation
4. Anomaly detection
5. Electricity bill calculation
6. LSTM model training
7. Model evaluation
8. Streamlit dashboard launch

---

# 🌐 Render Deployment

The application is deployed as a **Streamlit Web Service on Render**.

### Deployment Platform

**Render**

### Python Version

```text
3.10
```

The Python version is specified using:

```text
.python-version
```

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
streamlit run app/dashboard.py --server.address 0.0.0.0 --server.port $PORT
```

### Render Configuration

The repository contains:

```text
render.yaml
```

which contains the deployment configuration.

```yaml
services:
  - type: web
    name: electricity-consumption-optimizer
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: streamlit run app/dashboard.py --server.address 0.0.0.0 --server.port $PORT
```

### Live Application

🚀 **https://electricity-consumption-optimizer.onrender.com/**

The deployed application directly launches the Streamlit dashboard and uses the pre-trained model:

```text
models/best_model.h5
```

The model is not retrained every time the Render service starts.

---

# 🔗 Project Links

### 🌐 Live Application

https://electricity-consumption-optimizer.onrender.com/

### 💻 GitHub Repository

https://github.com/vaishnavi2489/Electricity-Consumption-Optimizer

---

## 🎯 Project Objectives

The main objectives of this project are:

1. Analyze household electricity consumption.
2. Forecast future electricity usage using LSTM.
3. Detect unusual electricity consumption patterns.
4. Estimate electricity bills.
5. Visualize energy consumption through an interactive dashboard.
6. Provide useful energy-management insights.
7. Help users understand and optimize their electricity consumption.

---

## 🔮 Future Enhancements

Future versions of the project can include:

- Real-time IoT smart-meter integration
- Appliance-level energy consumption prediction
- Advanced deep learning models
- Weather-based electricity forecasting
- Personalized energy-saving recommendations
- Dynamic electricity tariff integration
- Mobile application
- User authentication and personalized dashboards
- Cloud database integration
- Automated monthly energy reports

---

## 👨‍💻 Project Type

**Undergraduate CSE / Machine Learning Project**

### Domain

**Artificial Intelligence | Machine Learning | Data Analytics | Energy Management**

### Built With

**Python + TensorFlow + Streamlit + Plotly**

---

## ⭐ Acknowledgement

This project was developed as an undergraduate research and application project to explore the use of machine learning and data analytics for household electricity consumption forecasting and optimization.

---

## 📄 License

This project is intended for educational and academic purposes.
