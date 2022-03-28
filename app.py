import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=103104b0c1097f8ad3a11f8add24e37d&language=en-US'.format(movie_id))
    data = response.json()
    return 'http://image.tmdb.org/t/p/w500/' + data['poster_path']



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movie_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)

        # fetch poster from api
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movie_posters

movie_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('movie recommender system')

select_movie_name = st.selectbox(
'select movie name?',
movies['title'].values)

if st.button('recommend'):
    names,posters = recommend(select_movie_name)

    col1,col2,col3,col4,col5 = st.beta_columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])