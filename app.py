import streamlit as st
import joblib

from utils.weather import get_weather_from_dataset
from utils.feature_builder import build_features
from utils.pricing import calculate_price

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(
    page_title="Intelligent Surge Pricing System",
    layout="centered"
)

# ======================
# LOAD MODEL
# ======================
@st.cache_resource
def load_model():
    return joblib.load("surge_pricing_model.pkl")

model = load_model()

# ======================
# HEADER
# ======================
st.markdown(
    """
    <h2 style="text-align:center;">
    Intelligent Surge Pricing and Dynamic Fare Optimization
    </h2>
    <p style="text-align:center; color:gray;">
    ML-Driven Fare Estimation Engine
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ======================
# USER INPUT
# ======================
st.subheader("Trip Details")

col1, col2 = st.columns(2)

with col1:
    cab_type = st.selectbox(
        "Cab Type",
        ["Uber", "UberX", "UberXL", "Black", "Lyft", "Lyft XL"]
    )
    source = st.selectbox(
        "Pickup Location",
        ["Boston University", "Back Bay", "Fenway", "Financial District"]
    )

with col2:
    destination = st.selectbox(
        "Drop Location",
        ["Boston University", "Back Bay", "Fenway", "Financial District"]
    )
    distance = st.slider("Trip Distance (miles)", 1.0, 30.0, 6.0)

time_min = st.slider("Estimated Travel Time (minutes)", 5, 120, 25)

st.divider()

# ======================
# ACTION
# ======================
if st.button("Estimate Price", use_container_width=True):

    with st.spinner("Calculating optimal fare..."):

        # ✅ Get realistic weather from dataset
        weather = get_weather_from_dataset(source)

        # ✅ Build features (same as training)
        features = build_features(
            distance,
            cab_type,
            source,
            destination,
            weather
        )

        # ✅ Predict surge
        surge = model.predict(features)[0]

        # ✅ Calculate price
        low, high = calculate_price(distance, time_min, surge)

    st.subheader("Pricing Result")

    col_out1, col_out2 = st.columns(2)

    with col_out1:
        st.metric("Predicted Surge Multiplier", f"{surge:.2f}x")

    with col_out2:
        st.metric("Estimated Fare Range", f"₹{low} – ₹{high}")

    st.caption(
        "Fare estimation combines ML-based surge prediction with rule-based pricing."
    )
