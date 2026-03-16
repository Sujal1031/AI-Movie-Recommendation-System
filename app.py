import streamlit as st
import pickle
import pandas as pd

def recommended(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]

    recommended_movies = []
    for i in movies_list:
        movie_id=i[0]
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


movies_dict = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movies = pd.DataFrame(movies_dict)

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    "Select the movie",
    movies['title'].values
)

if st.button("Recommend"):
    recommendations = recommended(selected_movie_name)
    for i in recommendations:
        st.write(i)