# import streamlit as st
# import pandas as pd
# import pickle


# # recommend function
# def recommend(food):
#     food_index = foods[foods['name'] == food].index[0]
#     distances = similarity[food_index]
#     food_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:11]

#     recommended_food = []
#     recommended_food_posters = []
#     for i in food_list:
#         food = foods.iloc[i[0]]
#         recommended_food.append(food['name'])
#         recommended_food_posters.append(food['file'])
    
#     return recommended_food, recommended_food_posters

# # food list
# food_dict = pickle.load(open('notebook/food_dict.pkl', 'rb'))
# foods = pd.DataFrame(food_dict)

# similarity = pickle.load(open('notebook/similarity.pkl', 'rb'))

# st.title("Food Recommendation System")

# option = st.selectbox("Type or select from list", foods['name'].values)

# if st.button("Recommend"):
#     names, poster = recommend(option)

#     for name in names:
#             st.write(name)

#     st.write("")
#     st.write('\n\n-------------------------- Food with images -----------------------------\n\n')
#     st.write("")

#     for index, value in enumerate(names):
#             st.write(value)
#             st.image(poster[index])

# ----------------------------------------- Using Flask ----------------------------------

from flask import Flask, render_template, request

application = Flask(__name__)

app = application

#Route for home page
@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/recommend', methods = ['GET', 'POST'])
# def recommend_food():

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)
