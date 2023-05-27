import streamlit as st
import pandas as pd
import sklearn
import xgboost
import joblib

model=joblib.load("final_model.pkl")
inputs=joblib.load("columns.pkl")
def prediction(Airline, Source, Destination, Duration, Total_Stops,day_of_journey, month_of_journey, Weekday_of_Journey,Arrival_Time_day, Dep_Hour_time, Dep_Minute_time,Arrival_Hour_time, Arrival_Minute_time):
    test_df=pd.DataFrame(columns=inputs)
    test_df.at[0,"Airline"]=Airline
    test_df.at[0,"Source"]=Source
    test_df.at[0,"Destination"]=Destination
    test_df.at[0,"Duration"]=Duration
    test_df.at[0,"Total_Stops"]=Total_Stops
    test_df.at[0,"day_of_journey"]=day_of_journey
    test_df.at[0,"month_of_journey"]=month_of_journey
    test_df.at[0,"Weekday_of_Journey"]=Weekday_of_Journey
    test_df.at[0,"Arrival_Time_day"]=Arrival_Time_day
    test_df.at[0,"Dep_Hour_time"]=Dep_Hour_time
    test_df.at[0,"Dep_Minute_time"]=Dep_Minute_time
    test_df.at[0,"Arrival_Hour_time"]=Arrival_Hour_time
    test_df.at[0,"Arrival_Minute_time"]=Arrival_Minute_time
    result=model.predict(test_df)
    return result[0]
def main():
    Airline=st.selectbox("Airline",['Air India', 'Jet Airways', 'IndiGo', 'SpiceJet','Multiple carriers', 'GoAir', 'Vistara', 'Air Asia'])
    Source=st.selectbox("source",['Kolkata', 'Delhi', 'Banglore', 'Chennai', 'Mumbai'])
    Destination=st.selectbox("Destination",['Banglore', 'Cochin', 'New Delhi', 'Kolkata', 'Delhi', 'Hyderabad'])
    Duration=st.number_input("Duration time",75,2860)
    Total_Stops=st.slider("Number of stop through flight",1,4)
    day_of_journey=st.slider("Day of journey",1,30)
    month_of_journey=st.slider("Month of journey",3,6)
    Weekday_of_Journey=st.slider("Weekday of Journey",1,7)
    Dep_Hour_time=st.slider("Journey hour",0,23)
    Dep_Minute_time=st.slider("Journey minute",0,60,5)
    Arrival_Time_day=st.slider("Arrival Day",1,30)
    Arrival_Hour_time=st.slider("Arrival Hour",0,23)
    Arrival_Minute_time=st.slider("Arrival minute",0,60,5)
    if st.button("Predict"):
        result=prediction(Airline, Source, Destination, Duration, Total_Stops,day_of_journey, month_of_journey, Weekday_of_Journey,Arrival_Time_day, Dep_Hour_time, Dep_Minute_time,Arrival_Hour_time, Arrival_Minute_time)
        st.text(f"The price of journey is {result}")
if __name__=="__main__":
    main()
