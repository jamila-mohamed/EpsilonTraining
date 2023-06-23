import streamlit as st
import pandas as pd
import joblib
from datetime import time
from datetime import datetime
import datetime
from st_pages import Page, show_pages
import os

inputs_file_path = os.path.join(os.path.dirname(__file__), "Inputs.pkl")
Inputs = joblib.load(inputs_file_path)

model_file_path = os.path.join(os.path.dirname(__file__), "Model.pkl")
Model = joblib.load(model_file_path)

def prediction(Airline, Source, Destination, Total_Stops, Additional_Info, Departure, Arrival, Date_of_Journey, Date_of_Arrival):
    test_df = pd.DataFrame(columns=Inputs)
    if Airline != 'Air Asia':
        test_df.at[0,f"Airline_{Airline}"] = 1
    if Source != 'Banglore':
        test_df.at[0,f"Source_{Source}"] = 1
    if Destination != 'Delhi':
        test_df.at[0,f"Destination_{Destination}"] = 1
    if Additional_Info != '1 Long layover':
        test_df.at[0,f"Additional_Info_{Additional_Info}"] = 1
    test_df.at[0,"Total_Stops"] = Total_Stops
    test_df.at[0,"Departure"] = Departure
    test_df.at[0,"Arrival"] = Arrival
    test_df.at[0,"Date_of_Journey"] = Date_of_Journey
    test_df.at[0,"Date_of_Arrival"] = Date_of_Arrival
    #st.dataframe(test_df)
    result = Model.predict(test_df)[0]
    return result

def main():
    
    show_pages([
    Page("Airfare/about.py", "About", "ℹ️"),
    Page("Airfare/flight_app.py", "Home", "🏠"),
    ])
    
    st.set_page_config(page_title="SkySpy")
    
    st.markdown(
    """
    <style>
        body {
            background-color: #A6B6D1;
        }
    </style>
    """,
    unsafe_allow_html=True,
    )
    
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://i.postimg.cc/3N1V8nYd/airplane.jpg");
             background-attachment: fixed;
             background-size: 100% 100%;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    
    st.markdown("<h2 style='text-align: center; font-style: italic; color: #2e4a7a;'>Your Ultimate Guide to Smarter Airfares!</h2>", unsafe_allow_html=True)
    st.markdown("---")
    st.write("")
    
    st.markdown("<div style='text-align: center;'><span style='font-size: 21px;'>Which </span><span style='color: blue; font-style: italic; font-size: 21px;'>airline</span><span style='font-size: 21px;'> will take you to your destination?</span></div>", unsafe_allow_html=True)
    Airline = st.selectbox("Airline" , ['Air Asia', 'Air India', 'GoAir', 'IndiGo', 'Jet Airways', 'Multiple carriers', 'SpiceJet', 'Trujet', 'Vistara'], label_visibility= 'collapsed')
    
    st.markdown("<div style='text-align: center;'><span style='font-size: 22px;'><span style='color: blue; font-style: italic;'>Where</span> will your journey begin?</span></div>", unsafe_allow_html=True)
    Source = st.selectbox("Source" , ['Banglore', 'Chennai', 'Kolkata', 'Mumbai', 'New Delhi'], label_visibility= 'collapsed')
    
    st.markdown("<div style='text-align: center;'><span style='font-size: 21px;'><span style='color: blue; font-style: italic;'>Where</span> will your journey take you?</span></div>", unsafe_allow_html=True)
    Destination = st.selectbox("Destination" , ['Cochin', 'Delhi', 'Hyderabad', 'Kolkata', 'New Delhi'], label_visibility= 'collapsed')
    
    st.markdown("<div style='text-align: center;'><span style='font-size: 21px;'>How many <span style='color: blue; font-style: italic; font-size: 21px;'>stops</span> do you prefer on your journey?</span></div>", unsafe_allow_html=True)
    Total_Stops = st.selectbox("Total Stops" , [0, 1, 2, 3, 4], label_visibility= 'collapsed')
    
    st.markdown("<div style='text-align: center;'><span style='font-size: 21px;'>Do you have any <span style='color: blue; font-style: italic; font-size: 21px;'>specific preferences</span> for your flight?</span></div>", unsafe_allow_html=True)
    Additional_Info = st.selectbox("Additional Info", ['1 Long layover', '1 Short layover', '2 Long layover', 'Business class', 'Change airports', 'In-flight meal not included', 'No check-in baggage included', 'No info', 'Red-eye flight'], label_visibility= 'collapsed')
    
    st.markdown("<div style='text-align: center;'><span style='font-size: 21px;'><span style='color: blue; font-style: italic;'>When</span> do you want to start your journey?</span></div>", unsafe_allow_html=True)
    date_of_journey = st.date_input('Date of journey', value=datetime.datetime.now(), label_visibility= 'collapsed')
    date_of_journey_ts = int(datetime.datetime(date_of_journey.year, date_of_journey.month, date_of_journey.day).timestamp())

    st.markdown("<div style='text-align: center;'><span style='font-size: 21px;'><span style='color: blue; font-style: italic;'>When</span> do you want to reach your destination?</span></div>", unsafe_allow_html=True)
    date_of_arrival = st.date_input('Date of arrival', value=datetime.datetime.now(), label_visibility= 'collapsed')
    date_of_arrival_ts = int(datetime.datetime(date_of_arrival.year, date_of_arrival.month, date_of_arrival.day).timestamp())
    
    st.markdown("<div style='text-align: center;'><span style='font-size: 21px;'>When do you want to <span style='color: blue; font-style: italic; font-size: 21px;'>take off</span>?</span></div>", unsafe_allow_html=True)
    departure_time = st.time_input('Departure time', value=time(12, 0), label_visibility= 'collapsed')
    departure_seconds = departure_time.hour * 3600 + departure_time.minute * 60 + departure_time.second

    st.markdown("<div style='text-align: center;'><span style='font-size: 21px;'>When do you want to <span style='color: blue; font-style: italic; font-size: 21px;'>land</span>?</span></div>", unsafe_allow_html=True)
    arrival_time = st.time_input('Arrival time', value=time(12, 0), label_visibility= 'collapsed')
    arrival_seconds = arrival_time.hour * 3600 + arrival_time.minute * 60 + arrival_time.second
    
    style = "<style>.row-widget.stButton {text-align: center; color: #2e4a7a}</style>"
    st.markdown(style, unsafe_allow_html=True)

    if st.button("Price me up! 💲"):
        result = prediction(Airline, Source, Destination, Total_Stops, Additional_Info, departure_seconds, arrival_seconds, date_of_journey_ts, date_of_arrival_ts)
        st.write("<div style='text-align: center;'><h5 style='color: #D0312D;'>Based on our analysis, the ticket price for this flight should run about ₹{}.</h5></div>".format(round(result)), unsafe_allow_html=True)

if __name__ == '__main__':
    main()