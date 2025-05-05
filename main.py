import streamlit as st
import pandas as pd
from ANOMLY import main as anomaly_main
from COMPARE import main as compare_main
from solar import main as solar_main
from wind import main as wind_main
from cost import main as cost_main
from SAVINPLAN import main as saving_main


st.title("Energy Analysis Dashboard Suite")

# --- App Selection ---
app_choice = st.sidebar.selectbox(
    "Select Analysis:",
    [
        "Power Anomaly Detection",
        "Power Forecasting",
        "Solar Analysis",
        "Wind Analysis",
        "Cost Calculator",
        "Energy Saving Plans",
    ],
)

# --- Run the selected app ---
if app_choice == "Power Anomaly Detection":
    st.header("Power Anomaly Detection")
    uploaded_file = st.file_uploader("Upload Anomaly Data (Excel)", type=["xlsx"])
    if uploaded_file is not None:
        try:
            data = pd.read_excel(uploaded_file)
            anomaly_main(data)  # Pass the loaded data to the anomaly script
        except Exception as e:
            st.error(f"Error processing file: {e}")
    else:
        st.info("Please upload the Anomaly data Excel file.")

elif app_choice == "Power Forecasting":
    st.header("Power Forecasting")
    uploaded_file = st.file_uploader("Upload Forecasting Data (Excel)", type=["xlsx"])
    if uploaded_file is not None:
        try:
            data = pd.read_excel(uploaded_file)
            compare_main(data)  # Pass the loaded data to the compare script
        except Exception as e:
            st.error(f"Error processing file: {e}")
    else:
        st.info("Please upload the Forecasting data Excel file.")

elif app_choice == "Solar Analysis":
    st.header("Solar Analysis")
    uploaded_file = st.file_uploader("Upload Solar Data (Excel)", type=["xlsx"])
    if uploaded_file is not None:
        try:
            data = pd.read_excel(uploaded_file)
            solar_main(data)  # Pass the loaded data to the solar script
        except Exception as e:
            st.error(f"Error processing file: {e}")
    else:
        st.info("Please upload the Solar data Excel file.")

elif app_choice == "Wind Analysis":
    st.header("Wind Analysis")
    uploaded_file = st.file_uploader("Upload Wind Data (Excel)", type=["xlsx"])
    if uploaded_file is not None:
        try:
            data = pd.read_excel(uploaded_file)
            wind_main(data)  # Pass the loaded data to the wind script
        except Exception as e:
            st.error(f"Error processing file: {e}")
    else:
        st.info("Please upload the Wind data Excel file.")

elif app_choice == "Cost Calculator":
    st.header("Cost Calculator")
    cost_main()
elif app_choice == "Energy Saving Plans":
    st.header("Energy Saving Plans")
    saving_main()
