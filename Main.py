import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import time
import DataManipulation

st.title(":blue[**our bil481 project**]")

option = st.selectbox('please choose the country for flight information:', ('america', 'turkey', 'france'))

st.write('you selected:', option)


def assign_data():
    longitudes = DataManipulation.get_longitudes()
    latitudes = DataManipulation.get_latitudes()
    return longitudes, latitudes


@st.cache_data(ttl=10)
def assign_aircraft_list():
    aircraft_list = DataManipulation.get_aircrafts()
    return aircraft_list


longitude, latitude = assign_data()

# Create scatter plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(longitude, latitude, marker='o', color='blue')
ax.set_xlabel('Boylam')
ax.set_ylabel('Enlem')
ax.set_title('Uçakların Konumu')
ax.grid(True)

# Show MatPlotLib Figure on Streamlit
st.pyplot(fig)

# Empty container to draw the first map on
map_container = st.empty()

while True:
    aircraft_list = assign_aircraft_list()
    df = pd.DataFrame(aircraft_list)

    # Repaint the map
    with map_container:
        st.map(df)

    time.sleep(5)  # 10 second wait
