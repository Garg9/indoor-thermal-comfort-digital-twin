# 🏢 AI-Driven Indoor Thermal Comfort Prediction Using Digital Twin Concepts

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://indoor-thermal-comfort-digital-twin-mzd6xg7y6jepe7kts8xapf.streamlit.app/)

This project presents an **AI-based Digital Twin system** for predicting **indoor thermal comfort** under varying environmental and occupant conditions. By leveraging the **ASHRAE Global Thermal Comfort Database II**, the system simulates real-world thermal sensations to optimize indoor environments.

---

## 📖 Table of Contents
- [✨ Key Features](#-key-features)
- [🏗️ Project Architecture](#️-project-architecture)
- [🛠️ Tech Stack](#️-tech-stack)
- [📊 Dataset Info](#-dataset-info)
- [🚀 Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [🎮 How to Use](#-how-to-use)
- [📈 Results & Visualization](#-results--visualization)
- [👥 Contributing](#-contributing)
- [📄 License](#-license)

---

## ✨ Key Features
- **🧠 Machine Learning Prediction**: Accurately classifies thermal sensation (Cold, Neutral, Warm).
- **🔄 Digital Twin Simulation**: Scenario-based analysis of environmental changes (Temperature, Humidity, Airflow).
- **🖥️ Interactive Dashboard**: A premium Streamlit interface for real-time comfort analysis.
- **📊 Data-Driven Insights**: Built using the world-renowned ASHRAE dataset.
- **🛡️ Robust Training**: Includes advanced preprocessing and model validation pipelines.

---

## 🏗️ Project Architecture
The repository follows a clean, modular structure:
```text
indoor-thermal-comfort-digital-twin/
├── app/                    # Streamlit application
│   └── app.py              # Main dashboard script
├── data/                   # Dataset storage
│   └── sample_ashrae.csv   # ASHRAE Global Thermal Comfort Database
├── models/                 # Serialized ML models
├── src/                    # Core source code
│   ├── data_loader.py      # Data ingestion logic
│   ├── preprocessing.py    # Data cleaning & feature engineering
│   ├── eda.py              # Exploratory Data Analysis
│   ├── model_training.py   # Model training & evaluation
│   └── simulation_engine.py# Digital Twin simulation logic
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

---

## 🛠️ Tech Stack
| Category | Tools |
| :--- | :--- |
| **Language** | Python 3.9+ |
| **Data Processing** | Pandas, NumPy |
| **Machine Learning** | Scikit-learn, Joblib |
| **Visualization** | Matplotlib, Seaborn |
| **Web Interface** | Streamlit |

---

## 📊 Dataset Info
**ASHRAE Global Thermal Comfort Database II**
The project uses high-quality data from real buildings across diverse climates. 
**Key Parameters considered:**
- **Environmental**: Air Temperature (°C), Relative Humidity (%), Air Velocity (m/s), Radiant Temperature (°C).
- **Occupant**: Clothing Insulation (clo), Metabolic Rate (met).

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher installed.
- Git for repository management.

### Installation
1.  **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/indoor-thermal-comfort-digital-twin.git
    cd indoor-thermal-comfort-digital-twin
    ```

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

---

## 🎮 How to Use

### 1. Run the Streamlit Dashboard
Launch the interactive interface to explore predictions and simulations:
```bash
streamlit run app/app.py
```

### 2. Train the Model
If you wish to retrain the model with fresh data:
```bash
python src/model_training.py
```

### 3. Run Exploratory Analysis
Generate data insights and visualizations:
```bash
python src/eda.py
```

---

## 📈 Results & Visualization
The system provides several visualization tools:
- **Thermal Comfort Probability**: Pie charts showing prediction confidence.
- **Feature Importance**: Understanding which parameters (e.g., Temp vs. Humidity) affect comfort most.
- **Scenario Comparison**: Real-time graphing of comfort changes during simulations.

---

## 👥 Contributing
Contributions are welcome! Please follow these steps:
1. Fork the project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

---
**Maintained by [Aryan Garg]**
