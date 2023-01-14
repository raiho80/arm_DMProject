import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from apyori import apriori
from sklearn import preprocessing
import streamlit as st

# streamlit containers
header = st.container()
output = st.container()

# streamlit body
with header:
    st.title("Apriori Algorithm")
    st.text("This application performs Association Rule Mining on the items carried to laundry and generate rules based on them.")

with st.sidebar:
    st.header("Parameters to manipulate")

    supp_slider = st.slider(
        "Minimum support", min_value=0.0, max_value=0.055, value=0.035)

    conf_slider = st.slider(
        "Minimum confidence", min_value=0.0, max_value=0.5, value=0.2)

    lift_slider = st.slider(
        "Minimum lift", min_value=0, max_value=5, value=3)

    length_slider = st.slider(
        "Minimum length", min_value=0, max_value=5, value=2)

    
df_arm = pd.read_csv('dataset_master.csv')
df_arm=df_arm.drop(["Date", "Time", "Race", "Gender", "Body_Size", "Age_Range", "With_Kids",
                    "Washer_No", "Dryer_No", "Spectacles","TimeSpent_minutes",
                    "latitude", "longitude", "buyDrinks", "TotalSpent_RM", "Num_of_Baskets",
                    "Temp_celsius", "Weather", "Wind_kmph", "Humidity_percent", "Laundry_count", "Hour"], axis=1)
df_arm['Basket_colour'] = df_arm['Basket_colour'] +'_basket'
df_arm['Shirt_Colour'] = df_arm['Shirt_Colour'] +'_shirt'
df_arm['Pants_Colour'] = df_arm['Pants_Colour'] +'_pants'
#df_arm

records = []

for i in range (0, df_arm.shape[0]):
    records.append([str(df_arm.values[i,j]) for j in range(0,df_arm.shape[1])])

records = []

for i in range (0, df_arm.shape[0]):
    records.append([str(df_arm.values[i,j]) for j in range(0,df_arm.shape[1])])

association_rules = apriori(records,min_support=supp_slider,
                           min_confidence=conf_slider,
                           min_lift=lift_slider, min_length=length_slider)
association_results = list(association_rules)
len(association_results)

cnt =0

with output:
    st.header("Output")
    st.text("The following are the rules created based on ARM.")
    for item in association_results:
        cnt += 1
        # first index of the inner list
        # Contains base item and add item
        pair = item[0] 
        items = [x for x in pair]
        a = "(Rule " + str(cnt) + ") " + items[0] + " -> " + items[1]

        #second index of the inner list
        b = "Support: " + str(round(item[1],3))

        #third index of the list located at 0th
        #of the third index of the inner list

        c = "Confidence: " + str(round(item[2][0][2],4))
        d = "Lift: " + str(round(item[2][0][3],4))
        e = "====================================="
        
        st.write(a)
        st.write(b)
        st.write(c)
        st.write(d)
        st.write(e)
