# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 19:40:35 2020

@author: rhitc
"""

import streamlit as st
from datetime import datetime,date,time
import datetime
import pickle
import pandas as pd

st.write("""
    # Flight Fare Prediction Application
    This app predicts the fare of flights. Select parameters from the sidebar.
    """)
    
st.header('User Input Parameters')

dep_date = st.sidebar.date_input('Departure date',min_value=datetime.date(2020,9,21))
journey_day = int(dep_date.day)
journey_month = int(dep_date.month)
#st.write(journey_day,journey_month)

dep_time=st.sidebar.slider('Departure time',time(00,00),time(23,59))
dep_hour=int(dep_time.hour)
dep_min=int(dep_time.minute)
#st.write("You're scheduled for:", dep_time)

arr_time=st.sidebar.slider('Arrival time',dep_time,time(23,59))
Arrival_hour=int(arr_time.hour)
Arrival_min=int(arr_time.minute)
#st.write("You will arrive at:", arr_time)

# Duration
duration_hour = abs(Arrival_hour - dep_hour)
duration_min = abs(Arrival_min - dep_min)
duration=time(duration_hour,duration_min)
#st.write(duration,duration_hour,duration_min)

# Total Stops
Total_Stops = st.sidebar.radio('Number of stops', (0,1,2,3,4))
#st.write(Total_Stops)

#Airline type
airline = st.sidebar.selectbox(
'Which Airlines do you prefer',
('Jet Airways','IndiGo','Air India','Multiple carriers','SpiceJet','Vistara','GoAir'
 'Multiple carriers Premium economy','Jet Airways Business','Vistara Premium economy','Trujet',
 'Air Asia'))
#st.write('You selected:', airline)

#Source
Source=st.sidebar.selectbox('Source',(
    'Chennai','Delhi','Kolkata','Mumbai','Banglore'
    ))
#st.write('You selected:', Source)

#Destination
destination=st.sidebar.selectbox('Destination',(
    'Cochin','Delhi','Kolkata','Banglore','New Delhi'
    ))
#st.write('You selected:', destination)

###########################################################
if(airline=='Jet Airways'):
    Jet_Airways = 1
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0 

elif (airline=='IndiGo'):
    Jet_Airways = 0
    IndiGo = 1
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0 

elif (airline=='Air India'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 1
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0 
    
elif (airline=='Multiple carriers'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 1
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0 
    
elif (airline=='SpiceJet'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 1
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0 
    
elif (airline=='Vistara'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 1
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0

elif (airline=='GoAir'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 1
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0

elif (airline=='Multiple carriers Premium economy'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 1
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0

elif (airline=='Jet Airways Business'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 1
    Vistara_Premium_economy = 0
    Trujet = 0

elif (airline=='Vistara Premium economy'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 1
    Trujet = 0
    
elif (airline=='Trujet'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 1

else:
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0

#Source
# Banglore = 0 (not in column)
if (Source == 'Delhi'):
    s_Delhi = 1
    s_Kolkata = 0
    s_Mumbai = 0
    s_Chennai = 0

elif (Source == 'Kolkata'):
    s_Delhi = 0
    s_Kolkata = 1
    s_Mumbai = 0
    s_Chennai = 0

elif (Source == 'Mumbai'):
    s_Delhi = 0
    s_Kolkata = 0
    s_Mumbai = 1
    s_Chennai = 0

elif (Source == 'Chennai'):
    s_Delhi = 0
    s_Kolkata = 0
    s_Mumbai = 0
    s_Chennai = 1

else:
    s_Delhi = 0
    s_Kolkata = 0
    s_Mumbai = 0
    s_Chennai = 0



#Destination
# Banglore = 0 (not in column)
if (destination == 'Cochin'):
    d_Cochin = 1
    d_Delhi = 0
    d_New_Delhi = 0
    d_Hyderabad = 0
    d_Kolkata = 0

elif (Source == 'Delhi'):
    d_Cochin = 0
    d_Delhi = 1
    d_New_Delhi = 0
    d_Hyderabad = 0
    d_Kolkata = 0

elif (Source == 'New_Delhi'):
    d_Cochin = 0
    d_Delhi = 0
    d_New_Delhi = 1
    d_Hyderabad = 0
    d_Kolkata = 0

elif (Source == 'Hyderabad'):
    d_Cochin = 0
    d_Delhi = 0
    d_New_Delhi = 0
    d_Hyderabad = 1
    d_Kolkata = 0

elif (Source == 'Kolkata'):
    d_Cochin = 0
    d_Delhi = 0
    d_New_Delhi = 0
    d_Hyderabad = 0
    d_Kolkata = 1

else:
    d_Cochin = 0
    d_Delhi = 0
    d_New_Delhi = 0
    d_Hyderabad = 0
    d_Kolkata = 0


model = pickle.load(open("flight_rf.pkl", "rb"))

dic={'Departure Date':dep_date,
     'Departure Time':dep_time,
     'Arrival Time':arr_time,
     'Duration':duration,
     'No. of stops':Total_Stops,
     'Airline':airline,
     'Source':Source,
     'Destination':destination
     }

df=pd.DataFrame(dic,index=[0])
st.dataframe(df)



#Prediction
fare=model.predict([[
    Total_Stops,
    journey_day,
    journey_month,
    dep_hour,
    dep_min,
    Arrival_hour,
    Arrival_min,
    duration_hour,
    duration_min,
    Air_India,
    GoAir,
    IndiGo,
    Jet_Airways,
    Jet_Airways_Business,
    Multiple_carriers,
    Multiple_carriers_Premium_economy,
    SpiceJet,
    Trujet,
    Vistara,
    Vistara_Premium_economy,
    s_Chennai,
    s_Delhi,
    s_Kolkata,
    s_Mumbai,
    d_Cochin,
    d_Delhi,
    d_Hyderabad,
    d_Kolkata,
    d_New_Delhi  
    ]])

fare=round(fare[0],2)
st.write("""
         ## The expected fare is Rs.""",fare)
         
st.balloons()