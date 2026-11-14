import streamlit as st
import pickle
import joblib
st.title('Movie Recommendation System')
with open('movie.pickle','rb') as movies:
    movie=pickle.load(movies)
movies=movie['title'].values
similarities=joblib.load('similarity.joblib')
def recommend(name_movie):
    movie_index=movie[movie['title']==name_movie].index[0]
    recommendations=similarities[movie_index]
    movie_list=sorted(enumerate(recommendations),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    
    for i in movie_list:
        recommended_movies.append(movie.iloc[i[0]].title)
    return recommended_movies
name_movie=st.selectbox('Enter the Movie Name',movies)
if st.button('Recommend'):
    p=recommend(name_movie)
    st.write('The recommend movies are:\n')
    for i in p:
        st.write(i.title())