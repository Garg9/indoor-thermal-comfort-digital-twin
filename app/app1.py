# import streamlit as st
# import pandas as pd
# import joblib

# # Load trained model
# MODEL_PATH = "models/thermal_comfort_model.pkl"
# model = joblib.load(MODEL_PATH)

# st.set_page_config(
#     page_title="Indoor Thermal Comfort Digital Twin",
#     layout="centered"
# )

# st.title("🏢 AI-Based Indoor Thermal Comfort Digital Twin")
# st.markdown(
#     "This application simulates indoor thermal comfort using an "
#     "**AI-driven Digital Twin model**."
# )

# st.header("🔧 Set Indoor Environmental Conditions")

# # User inputs
# ta = st.slider("Air Temperature (°C)", 18.0, 35.0, 25.0)
# rh = st.slider("Relative Humidity (%)", 20.0, 90.0, 50.0)
# v = st.slider("Air Velocity (m/s)", 0.05, 0.60, 0.15)
# tr = st.slider("Radiant Temperature (°C)", 18.0, 35.0, 25.0)
# clo = st.slider("Clothing Insulation (clo)", 0.3, 1.5, 0.8)
# met = st.slider("Metabolic Rate (met)", 1.0, 2.5, 1.2)

# input_data = pd.DataFrame([{
#     "Air temperature (C)": ta,
#     "Relative humidity (%)": rh,
#     "Air velocity (m/s)": v,
#     "Radiant temperature (C)": tr,
#     "Clo": clo,
#     "Met": met
# }])

# st.divider()

# if st.button("🔍 Predict Thermal Comfort"):
#     prediction = model.predict(input_data)[0]

#     if prediction == "Cold":
#         st.warning("❄️ Predicted Comfort: COLD")
#     elif prediction == "Warm":
#         st.error("🔥 Predicted Comfort: WARM")
#     else:
#         st.success("✅ Predicted Comfort: NEUTRAL")

#     st.markdown(
#         f"""
#         **Model Output:**  
#         The Digital Twin predicts the indoor environment to be **{prediction}** 
#         under the given conditions.
#         """
#     )

# st.divider()
# st.caption("Final Year Project – AI-Driven Indoor Thermal Comfort Prediction")

def air_velocity_from_option(option):
    return {
        "Still Air (Fan OFF)": 0.1,
        "Fan LOW": 0.25,
        "Fan HIGH": 0.45
    }[option]


def humidity_from_option(option):
    return {
        "Dry": 35.0,
        "Comfortable": 50.0,
        "Humid": 65.0
    }[option]


def clo_from_option(option):
    return {
        "Light (T-shirt)": 0.5,
        "Normal (Office Wear)": 0.8,
        "Heavy (Jacket)": 1.2
    }[option]


def met_from_option(option):
    return {
        "Sitting": 1.0,
        "Office Work": 1.2,
        "Walking": 1.6
    }[option]


def air_velocity_from_option(option):
    return {
        "Still Air (Fan OFF)": 0.1,
        "Fan LOW": 0.25,
        "Fan HIGH": 0.45
    }[option]


def clo_from_option(option):
    return {
        "Light (T-shirt)": 0.5,
        "Normal (Office Wear)": 0.8,
        "Heavy (Jacket)": 1.2
    }[option]


def met_from_option(option):
    return {
        "Sitting": 1.0,
        "Office Work": 1.2,
        "Walking": 1.6
    }[option]


import streamlit as st
import pandas as pd
import joblib

# Load trained model
MODEL_PATH = "models/thermal_comfort_model.pkl"
model = joblib.load(MODEL_PATH)

st.set_page_config(
    page_title="Indoor Thermal Comfort Digital Twin",
    layout="wide",
    page_icon="🏢"
)

# ---------- HEADER ----------
st.title("🏢 AI-Based Indoor Thermal Comfort Digital Twin")
st.markdown(
    """
    This interactive system acts as a **Digital Twin** of an indoor environment.
    Adjust environmental parameters to **simulate and predict occupant thermal comfort** in real time.
    """
)

st.divider()

# ---------- SIDEBAR ----------
# st.sidebar.header("🔧 Indoor Environment Controls")

# preset = st.sidebar.selectbox(
#     "Choose a Scenario Preset",
#     ["Custom", "Office – Normal", "Office – Hot Afternoon", "Fan ON Scenario"]
# )

# # Default values
# ta, rh, v, tr, clo, met = 25.0, 50.0, 0.15, 25.0, 0.8, 1.2

# if preset == "Office – Normal":
#     ta, rh, v = 24.0, 45.0, 0.15
# elif preset == "Office – Hot Afternoon":
#     ta, rh, v = 30.0, 55.0, 0.10
# elif preset == "Fan ON Scenario":
#     ta, rh, v = 26.0, 50.0, 0.40

# ta = st.sidebar.slider("🌡️ Air Temperature (°C)", 18.0, 35.0, ta)
# rh = st.sidebar.slider("💧 Relative Humidity (%)", 20.0, 90.0, rh)
# v = st.sidebar.slider("🌬️ Air Velocity (m/s)", 0.05, 0.60, v)
# tr = st.sidebar.slider("🔥 Radiant Temperature (°C)", 18.0, 35.0, tr)
# clo = st.sidebar.slider("🧥 Clothing Insulation (clo)", 0.3, 1.5, clo)
# met = st.sidebar.slider("🏃 Metabolic Rate (met)", 1.0, 2.5, met)

# st.sidebar.header("🔧 Indoor Environment Controls")

# # Temperature & Humidity (direct human input)
# ta = st.sidebar.slider("🌡️ Air Temperature (°C)", 18.0, 35.0, 25.0)
# rh = st.sidebar.slider("💧 Relative Humidity (%)", 20.0, 90.0, 50.0)

# # Air velocity (human choice → system value)
# airflow_option = st.sidebar.selectbox(
#     "🌬️ Airflow Condition",
#     ["Still Air (Fan OFF)", "Fan LOW", "Fan HIGH"]
# )
# v = air_velocity_from_option(airflow_option)

# # Clothing insulation
# clothing_option = st.sidebar.selectbox(
#     "🧥 Clothing Level",
#     ["Light (T-shirt)", "Normal (Office Wear)", "Heavy (Jacket)"]
# )
# clo = clo_from_option(clothing_option)

# # Activity level
# activity_option = st.sidebar.selectbox(
#     "🏃 Activity Level",
#     ["Sitting", "Office Work", "Walking"]
# )
# met = met_from_option(activity_option)

# # Radiant temperature (auto or manual)
# radiant_mode = st.sidebar.radio(
#     "🔥 Radiant Temperature Mode",
#     ["Auto (same as air temp)", "Manual"]
# )

# if radiant_mode == "Auto (same as air temp)":
#     tr = ta
# else:
#     tr = st.sidebar.slider("Radiant Temperature (°C)", 18.0, 35.0, ta)

st.sidebar.header("🔧 Indoor Environment Controls")

# ---------------- Temperature ----------------
ta = st.sidebar.slider("🌡️ Air Temperature (°C)", 1.0, 45.0, 20.0)

# ---------------- Humidity ----------------
humidity_mode = st.sidebar.radio(
    "💧 Humidity Input Mode",
    ["Preset", "Manual"]
)

if humidity_mode == "Preset":
    humidity_option = st.sidebar.selectbox(
        "Humidity Level",
        ["Dry", "Comfortable", "Humid"]
    )
    rh = humidity_from_option(humidity_option)
else:
    rh = st.sidebar.slider("Relative Humidity (%)", 20.0, 90.0, 50.0)

# ---------------- Air Velocity ----------------
airflow_mode = st.sidebar.radio(
    "🌬️ Airflow Input Mode",
    ["Preset", "Manual"]
)

if airflow_mode == "Preset":
    airflow_option = st.sidebar.selectbox(
        "Airflow Condition",
        ["Still Air (Fan OFF)", "Fan LOW", "Fan HIGH"]
    )
    v = air_velocity_from_option(airflow_option)
else:
    v = st.sidebar.slider("Air Velocity (m/s)", 0.05, 0.60, 0.15)

# ---------------- Clothing ----------------
clothing_mode = st.sidebar.radio(
    "🧥 Clothing Input Mode",
    ["Preset", "Manual"]
)

if clothing_mode == "Preset":
    clothing_option = st.sidebar.selectbox(
        "Clothing Level",
        ["Light (T-shirt)", "Normal (Office Wear)", "Heavy (Jacket)"]
    )
    clo = clo_from_option(clothing_option)
else:
    clo = st.sidebar.slider("Clothing Insulation (clo)", 0.3, 1.5, 0.8)

# ---------------- Activity ----------------
activity_mode = st.sidebar.radio(
    "🏃 Activity Input Mode",
    ["Preset", "Manual"]
)

if activity_mode == "Preset":
    activity_option = st.sidebar.selectbox(
        "Activity Level",
        ["Sitting", "Office Work", "Walking"]
    )
    met = met_from_option(activity_option)
else:
    met = st.sidebar.slider("Metabolic Rate (met)", 1.0, 2.5, 1.2)

# ---------------- Radiant Temperature ----------------
radiant_mode = st.sidebar.radio(
    "🔥 Radiant Temperature Mode",
    ["Auto (same as air temp)", "Manual"]
)

if radiant_mode == "Auto (same as air temp)":
    tr = ta
else:
    tr = st.sidebar.slider("Radiant Temperature (°C)", 1.0, 45.0, ta)



# ---------- INPUT DATA ----------
input_data = pd.DataFrame([{
    "Air temperature (C)": ta,
    "Relative humidity (%)": rh,
    "Air velocity (m/s)": v,
    "Radiant temperature (C)": tr,
    "Clo": clo,
    "Met": met
}])

# ---------- MAIN PANEL ----------
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📥 Current Indoor Conditions")
    st.table(input_data)

with col2:
    st.subheader("🎯 Predicted Thermal Comfort")

    if st.button("🔍 Run Digital Twin Simulation"):
        prediction = model.predict(input_data)[0]

        if prediction == "Cold":
            st.warning("❄️ **COLD**\n\nOccupants may feel chilly. Consider reducing airflow or increasing temperature.")
        elif prediction == "Warm":
            st.error("🔥 **WARM**\n\nOccupants may feel uncomfortable. Consider increasing ventilation or reducing temperature.")
        else:
            st.success("✅ **NEUTRAL**\n\nThermal conditions are comfortable for most occupants.")

        st.markdown(
            f"""
            **Digital Twin Output:**  
            Based on the current indoor conditions, the AI model predicts the environment to be **{prediction}**.
            """
        )

# ---------- FOOTER ----------
st.divider()
st.caption(
    "Final Year Project | AI-Driven Indoor Thermal Comfort Prediction Using Digital Twin Concepts"
)
