import streamlit as st
import pandas as pd
import pickle
import requests

def fetchFoodDetails(foodId):
    response = requests.get("https://webapi.tastes2plate.com/app/product-details?id={}".format(foodId))
    data = response.json()
    return data['result'][0]['file'][0]['location']

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

st.title("Food Recommendation System")

option = st.selectbox("Type or select from list", foods['name'].values)

if st.button("Recommend"):
    names, poster = recommend(option)

    for name in names:
            st.write(name)

    st.write("")
    st.write('\n\n-------------------------- Food with images -----------------------------\n\n')
    st.write("")

    for index, value in enumerate(names):
            st.write(value)
            st.image(poster[index])

    # with st.container():
    #     col1, col2, col3, col4, col5 = st.columns(5)
    #     with col1:
    #        st.text(names[0])
    #        st.image(poster[0])
            
    #     with col2:
    #         st.text(names[1])
    #         st.image(poster[0])
            
        # with col3:
        #     st.text(names[2])
        #     st.image(poster[2])
            
        # with col4:
        #     st.text(names[3])
        #     st.image(poster[3])
            
        # with col5:
        #     st.text(names[4])
        #     st.image(poster[4])

            
    # with st.container():
    #     col1, col2, col3, col4, col5 = st.columns(5)
    #     with col1:
    #         st.text(names[5])
    #         st.image(poster[5])
            
    #     with col2:
    #         st.text(names[6])
    #         st.image(poster[6])
            
    #     with col3:
    #         st.text(names[7])
    #         st.image(poster[7])
            
    #     with col4:
    #         st.text(names[8])
    #         st.image(poster[8])
            
    #     with col5:
    #         st.text(names[9])
    #         st.image(poster[9])