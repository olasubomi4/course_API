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



@app.get('/Recommend_Courses/{data}')

def predict_course(data:str):

            

     query = data

    # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
     course=[]
     df = pd.read_csv("https://storagesubomi.blob.core.windows.net/consolesubomi/udemy_courses.csv")
         #df.dropna(inplace=True)
     features = ['course_title','num_subscribers','num_reviews','subject','level']

     def combine_features(row):
         return row['course_title'] + " " + str(row['num_subscribers']) + " " + str(row['num_reviews']) + " " + row['subject'] + " " + str(row['level'])

     for feature in features:
         df[feature] = df[feature].fillna('')  # filling all NaNs with blank string

     df["combined_features"] = df.apply(combine_features,
                                             axis=1)  # applying combined_features() method over each rows of dataframe and storing the combined string in "combined_features" column

          # applying combined_features() method over each rows of dataframe and storing the combined string in "combined_features" column
     df.iloc[0].combined_features

     cv = CountVectorizer()  # creating new CountVectorizer() object
     count_matrix = cv.fit_transform(df["combined_features"])
     cosine_sim = cosine_similarity(count_matrix)

     def get_title_from_index(index):
         return df[df.index == index]["course_title"].values[0]

     def get_index_from_title(title):
       try:
             
                return df[df.course_title == title]["index"].values[0]
       except:
                return 
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
                                  course_id2=str(course_id)
                                  course.append({"course_id":course_id2})

            #  print (show[])
           
     else:
    
        course="invalid input";

    
     return course




# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__app__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload