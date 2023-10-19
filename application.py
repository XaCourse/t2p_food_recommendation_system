import streamlit as st
import pandas as pd
import pickle


# recommend function
def recommend(food):
    food_index = foods[foods['name'] == food].index[0]
    distances = similarity[food_index]
    food_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:11]

    recommended_food = []
    recommended_food_posters = []
    for i in food_list:
        food = foods.iloc[i[0]]
        recommended_food.append(food['name'])
        recommended_food_posters.append(food['file'])
    
    return recommended_food, recommended_food_posters

# food list
food_dict = pickle.load(open('notebook/food_dict.pkl', 'rb'))
foods = pd.DataFrame(food_dict)

similarity = pickle.load(open('notebook/similarity.pkl', 'rb'))

application=st

application.title("Food Recommendation System")

option = application.selectbox("Type or select from list", foods['name'].values)

if application.button("Recommend"):
    names, poster = recommend(option)

    for name in names:
            application.write(name)

    application.write("")
    application.write('\n\n-------------------------- Food with images -----------------------------\n\n')
    application.write("")

    for index, value in enumerate(names):
            application.write(value)
            application.image(poster[index])




