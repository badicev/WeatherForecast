import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox, and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="How many days do you want to forecast?")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} in {place}")

if place:
    # Get the temperature/sky data
    try:
        filtered_data = get_data(place, days)


        if option == "Temperature":
            temps = [dict["main"]["temp"] for dict in filtered_data]
            temps_10 = [i/10 for i in temps]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create a temperature plot
            figure = px.line(x=dates, y=temps_10, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)  # figure object(data visualization libraries: plotly and bokeh)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            #translating the data
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=110 )
    except KeyError:
        st.write("That place does not exist.")
