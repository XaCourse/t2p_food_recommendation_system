from flask import Flask,request,render_template
import numpy as np
import pandas as pd 

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

# @app.route('/predictdata',methods=['GET','POST'])
# def predict_datapoint():
#     if request.method=='GET':
#         return render_template('home.html')
#     else:
#         data=CustomData(
#             gender=request.form.get('gender'),
#             race_ethnicity=request.form.get('ethnicity'),
#             parental_level_of_education=request.form.get('parental_level_of_education'),
#             lunch=request.form.get('lunch'),
#             test_preparation_course=request.form.get('test_preparation_course'),
#             reading_score=float(request.form.get('writing_score')),
#             writing_score=float(request.form.get('reading_score'))

#         )
#         pred_df=data.get_data_as_data_frame()
#         print(pred_df)
#         print("Before Prediction")

#         predict_pipeline=PredictPipeline()
#         print("Mid Prediction")
#         results=predict_pipeline.predict(pred_df)
#         print("after Prediction")
#         return render_template('home.html',results=results[0])
    

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)        



# import streamlit as st
# import pandas as pd
# import pickle
# from flask import Flask, request, render_template


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

# application=st

# application.title("Food Recommendation System")

# option = application.selectbox("Type or select from list", foods['name'].values)

# if application.button("Recommend"):
#     names, poster = recommend(option)

#     for name in names:
#             application.write(name)

#     application.write("")
#     application.write('\n\n-------------------------- Food with images -----------------------------\n\n')
#     application.write("")

#     for index, value in enumerate(names):
#             application.write(value)
#             application.image(poster[index])


# application = Flask(__name__)
# app  = application

# if __name__=='__main__':
#     app.run(host='0.0.0.0')
