#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 00:44:10 2022

@author: olasubomi
"""

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

        #  print (show[])
       


 return course[0]