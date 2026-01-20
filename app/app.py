import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import os


# ------------------- Helper mappings -------------------
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


# ------------------- Load Model -------------------
import os
import joblib
from src.data_loader import load_raw_data
from src.preprocessing import preprocess_data
from src.model_training import train_models

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "thermal_comfort_model.pkl")

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()


st.set_page_config(
    page_title="Indoor Thermal Comfort Digital Twin",
    page_icon="🏢",
    layout="wide"
)

# ------------------- HEADER -------------------
st.markdown(
    """
    <h1 style='text-align:center;'>🏢 AI Driven Indoor Thermal Comfort Prediction Using Digital Twin Concept</h1>
    <p style='text-align:center; color:gray;'>
    AI-based system to simulate and predict occupant thermal comfort under varying indoor conditions
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ------------------- SIDEBAR -------------------
st.sidebar.title("⚙️ Environment Settings")
st.sidebar.caption("Human-friendly controls with manual override")

ta = st.sidebar.slider(
    "🌡️ Air Temperature (°C)",
    min_value=1.0,
    max_value=45.0,
    value=25.0,
    help="Indoor air temperature (1°C to 45°C)"
)

humidity_mode = st.sidebar.radio("💧 Humidity Mode", ["Preset", "Manual"])
rh = humidity_from_option(
    st.sidebar.selectbox("Humidity Level", ["Dry", "Comfortable", "Humid"])
) if humidity_mode == "Preset" else st.sidebar.slider("Humidity (%)", 20.0, 90.0, 50.0)

airflow_mode = st.sidebar.radio("🌬️ Airflow Mode", ["Preset", "Manual"])
v = air_velocity_from_option(
    st.sidebar.selectbox("Airflow Condition", ["Still Air (Fan OFF)", "Fan LOW", "Fan HIGH"])
) if airflow_mode == "Preset" else st.sidebar.slider("Air Velocity (m/s)", 0.05, 0.60, 0.15)

clothing_mode = st.sidebar.radio("🧥 Clothing Mode", ["Preset", "Manual"])
clo = clo_from_option(
    st.sidebar.selectbox("Clothing Level", ["Light (T-shirt)", "Normal (Office Wear)", "Heavy (Jacket)"])
) if clothing_mode == "Preset" else st.sidebar.slider("Clothing (clo)", 0.3, 1.5, 0.8)

activity_mode = st.sidebar.radio("🏃 Activity Mode", ["Preset", "Manual"])
met = met_from_option(
    st.sidebar.selectbox("Activity Level", ["Sitting", "Office Work", "Walking"])
) if activity_mode == "Preset" else st.sidebar.slider("Metabolic Rate (met)", 1.0, 2.5, 1.2)

radiant_mode = st.sidebar.radio("🔥 Radiant Temperature", ["Auto", "Manual"])
tr = ta if radiant_mode == "Auto" else st.sidebar.slider("Radiant Temp (°C)", 18.0, 35.0, ta)

# ------------------- INPUT DATA -------------------
input_df = pd.DataFrame([{
    "Air temperature (C)": ta,
    "Relative humidity (%)": rh,
    "Air velocity (m/s)": v,
    "Radiant temperature (C)": tr,
    "Clo": clo,
    "Met": met
}])

# baseline_conditions = pd.DataFrame([{
#     "Air temperature (C)": 25.0,
#     "Relative humidity (%)": 50.0,
#     "Air velocity (m/s)": 0.15,
#     "Radiant temperature (C)": 25.0,
#     "Clo": 0.8,
#     "Met": 1.2
# }])


# st.subheader("⚠️ System Checks & Warnings")

# warnings = []

# if ta > 32 and v < 0.15:
#     warnings.append("High temperature with low airflow may cause discomfort.")

# if rh > 70:
#     warnings.append("High humidity may cause sticky and uncomfortable conditions.")

# if clo > 1.0 and ta > 28:
#     warnings.append("Heavy clothing at high temperature may increase warmth.")

# if met > 1.6 and ta > 27:
#     warnings.append("High activity level may increase perceived warmth.")

# if warnings:
#     for w in warnings:
#         st.warning(w)
# else:
#     st.success("Indoor conditions are within generally acceptable comfort limits.")


# ------------------- MAIN CONTENT -------------------
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📥 Current Indoor Conditions")
    st.dataframe(input_df, use_container_width=True)

    st.info(
        "This represents the **virtual indoor environment** being simulated by the Digital Twin."
    )

with col2:
    st.subheader("🎯 Digital Twin Prediction")

    if st.button("🚀 Run Simulation", use_container_width=True):
        prediction = model.predict(input_df)[0]
        probabilities = model.predict_proba(input_df)[0]
        classes = model.classes_

        if prediction == "Cold":
            st.error("❄️ **COLD ENVIRONMENT**")
            st.caption("Recommendation: Increase temperature or reduce airflow.")
        elif prediction == "Warm":
            st.warning("🔥 **WARM ENVIRONMENT**")
            st.caption("Recommendation: Improve ventilation or reduce temperature.")
        else:
            st.success("✅ **COMFORTABLE (NEUTRAL)**")
            st.caption("Thermal conditions are suitable for most occupants.")

        st.markdown(
            f"""
            **Digital Twin Insight:**  
            Based on the current configuration, the predicted thermal comfort state is **{prediction}**.
            """
        )

        # st.subheader("🔁 Scenario Comparison")
 
        # baseline_pred = model.predict(baseline_conditions)[0]
        # current_pred = prediction

        # comparison_df = pd.DataFrame({
        #     "Scenario": ["Baseline (Comfortable)", "Current Input"],
        #     "Predicted Comfort": [baseline_pred, current_pred]
        #     })

        # st.table(comparison_df)

        # if baseline_pred != current_pred:
        #     st.info(
        #         f"Comfort changed from **{baseline_pred}** to **{current_pred}** "
        #         "due to modified indoor conditions."
        #     )
        # else:
        #     st.success("Comfort level remains unchanged compared to baseline.")


        st.subheader("🧠 Why this comfort level?")

        reasons = []

        if ta >= 28:
            reasons.append("Relatively high indoor air temperature.")
        elif ta <= 20:
            reasons.append("Low indoor air temperature.")

        if v >= 0.35:
            reasons.append("High air movement improves cooling effect.")
        elif v <= 0.12:
            reasons.append("Low air movement reduces cooling.")

        if clo >= 1.0:
            reasons.append("Higher clothing insulation traps body heat.")

        if met >= 1.4:
            reasons.append("Higher activity level increases metabolic heat.")

        if reasons:
            for r in reasons:
                st.write("•", r)
        else:
            st.write("• Indoor parameters are balanced for comfort.")


        st.subheader("🧠 Thermal Comfort Confidence")

        fig, ax = plt.subplots()

        colors = ["#4FC3F7", "#81C784", "#FF8A65"]  # Cold, Neutral, Warm

        ax.pie(
            probabilities,
            labels=classes,
            autopct="%1.1f%%",
            startangle=90,
            colors=colors,
            explode=[0.05 if cls == prediction else 0 for cls in classes]
            )

        ax.axis("equal")  # Makes it a perfect circle
        ax.set_title("Predicted Thermal Comfort Distribution")

        st.pyplot(fig)


# ------------------- FOOTER -------------------
st.divider()
st.caption(
    "Final Year Project | AI-Driven Indoor Thermal Comfort Prediction using Digital Twin Concepts"
)

