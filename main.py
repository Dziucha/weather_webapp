import streamlit as st
import plotly.express as px

st.set_page_config(layout="centered")

st.header("Weather Forecast for the Next Days")

place = st.text_input("Place:")
days = st.slider("Forecast Days:", 1, 5, step=1,
                 help="Select a number of days to forecast.")
data_to_view = st.selectbox("Select data to view:", ("Temperature", "Sky"))

info = ""
if place != "":
    if days == 1:
        info = st.subheader(f"{data_to_view} for the "
                            f"next {days} day in {place}")
    else:
        info = st.subheader(f"{data_to_view} for the "
                            f"next {days} days in {place}")


def get_data(days_local):
    dates_local = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temperatures_local = [10, 11, 15]
    temperatures_local = [days_local * i for i in temperatures_local]
    return dates_local, temperatures_local


dates, temperatures = get_data(days)
figure = px.line(x=dates, y=temperatures,
                 labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
