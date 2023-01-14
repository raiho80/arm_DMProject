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
    st.text("This application performs Association Rule Mining.")

with st.sidebar:
    st.header("Parameters to manipulate")

    num_generations = st.slider(
        "Number of generations", min_value=10, max_value=100, value=50, step=10)

    population_size = st.slider(
        "Population size", min_value=10, max_value=200, value=70, step=10)

    random_sel = st.slider(
        "Random selection", min_value=0.0, max_value=0.1, value=0.05)

    mutation_prob = st.slider(
        "Mutation probability", min_value=0.0, max_value=0.1, value=0.01)

    crossover_k = st.slider(
        "Crossover points", min_value=1, max_value=3, value=1, step=1)
    
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

association_rules = apriori(records,min_support=0.035,
                           min_confidence=0.2,
                           min_lift=3, min_length=2)
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
