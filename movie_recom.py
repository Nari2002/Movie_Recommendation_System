import streamlit as st
import pandas as pd
import pickle
import sklearn

def recom(movie):
    movie_index = movies_d[movies_d['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)),reverse=True ,key= lambda x:x[1])[1:6]
    
    recommend_movie=[]
 
    for i in movie_list:
        recommend_movie.append(movies_d.iloc[i[0]].title)
    
        
    return recommend_movie


def genress(movie):
    movie_index = movies_d[movies_d['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)),reverse=True ,key= lambda x:x[1])[1:6]
    
    geners=[]
    for i in movie_list:
        geners.append(movies_d.iloc[i[0]].genres)
    return geners

def website(movie):
    movie_index = movies_d[movies_d['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)),reverse=True ,key= lambda x:x[1])[1:6]
    
    webs=[]
    for i in movie_list:
        webs.append(movies_d.iloc[i[0]].tagline)
    return webs
    
    

movies_d = pickle.load(open("movies1.pkl",'rb'))
#movies=pd.DataFrame(movies_d)
def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://brocku.ca/brock-news/wp-content/uploads/2022/10/GettyImages-1336937059-1600x728.jpg?x70330");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack_url()

st.title("Movie Recommendation System")

option = st.selectbox("select a movie", movies_d['title'].values)



similarity=pickle.load(open("similarity.pkl",'rb'))



if st.button("Recommend a Movie"):
    recommendation = recom(option)
    recommandation = genress(option)
    recommandationn= website(option)
    mov=[]
    gen=[]
    websss=[]
    for i in recommendation:
        mov.append(i)
        
    for j in recommandation:
        gen.append(j)
    for k in recommandationn:
        websss.append(k)
    df = pd.DataFrame(list(zip(mov, gen,websss)),
               columns =['Movie Name', 'Genres','Tagline'])
    st.write(df)
        
  
 
      
