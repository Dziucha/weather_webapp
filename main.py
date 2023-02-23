import streamlit as st

st.set_page_config(layout="centered")

st.header("Weather Forecast for the Next Days")

place = st.text_input("Place:")
days = st.slider("Forecast Days:", 1, 5, step=1)
data_to_view = st.selectbox("Select data to view:", ("Temperature", "Sky"))

info = ""
if place != "":
    if days == 1:
        info = st.subheader(f"{data_to_view} for the "
                            f"next {days} day in {place}")
    else:
        info = st.subheader(f"{data_to_view} for the "
                            f"next {days} days in {place}")
