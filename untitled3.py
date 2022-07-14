#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 08:37:26 2022

@author: olasubomi
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 15:13:01 2022

@author: olasubomi
"""
# 1. Library imports
import uvicorn
from fastapi import FastAPI
import pickle
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# 2. Create the app object
app = FastAPI()

pickle_in = open("udem.pkl","rb")
count_matrix=pickle.load(pickle_in)

pickle_in = open("df.pkl","rb")
df=pickle.load(pickle_in)
@app.get('/')

def index():

    return {'message': 'Hello, World'}


# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/Recommend movies/{data}')

def predict_banknote(data:str):

            

    query ='Learn Photoshop Actions - Save time with repetitive tasks'
  
   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    course = []
    
    cosine_sim = cosine_similarity(count_matrix)

    def get_title_from_index(index):
        return df[df.index == index]["course_title"].values[0]

    def get_index_from_title(title):
        return df[df.course_title == title]["index"].values[0]
    def get_course_id_from_index(index):
                                return df[df.index == index]["course_id"].values[0]
   
    selected_course=query
    course_index = get_index_from_title(selected_course)
    similar_course = list(enumerate(cosine_sim[
                                             course_index]))  # accessing the row corresponding to given movie to find all the similarity scores for that movie and then enumerating over it
    sorted_similar_course = sorted(similar_course, key=lambda x: x[1], reverse=True)[1:]
    sort_size = len(sorted_similar_course)
    if sort_size > 10:
                             print("Top 10 similar courses to " +  selected_course + " are:\n")
                             for element in sorted_similar_course[:10]:
                                 courses = (get_title_from_index(element[0]))
                                 course_id=(get_course_id_from_index(element[0]))
                                 course.append(course_id)

  
    return course

   
   




# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__app__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload