import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse = True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

similarity = pickle.load(open('similarity.pkl', 'rb'))

movies_list = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_list)
st.title('Movie Recommendation System')


selected_movie_name = st.selectbox(
    "Choose Movies",
    movies['title'].values,
    index=None
)
st.write("You selected:", selected_movie_name)
if st.button("Recommend Movie"):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)