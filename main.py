import streamlit as st
import plotly.express as px
from backend import get_data

st.set_page_config(layout="centered")

st.header("Weather Forecast for the Next Days")

place = st.text_input("Place:")
days = st.slider("Forecast Days:", 1, 5, step=1,
                 help="Select a number of days to forecast.")
type_of_data = st.selectbox("Select data to view:", ("Temperature", "Sky"))

info = ""
if place != "":
    if days == 1:
        info = st.subheader(f"{type_of_data} for the "
                            f"next {days} day in {place.capitalize()}")
    else:
        info = st.subheader(f"{type_of_data} for the "
                            f"next {days} days in {place.capitalize()}")

if place:
    filtered_data = get_data(place, days)

    if type_of_data == "Temperature":
        dates = [dict["dt_txt"] for dict in filtered_data]
        temperatures = [data_set["main"]["temp"] for data_set in filtered_data]
        figure = px.line(x=dates, y=temperatures,
                         labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)
    if type_of_data == "Sky":
        filtered_data = [data_set["weather"][0]["main"] for data_set in filtered_data]
        st.image()