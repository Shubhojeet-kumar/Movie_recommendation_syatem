import streamlit as st
import pickle
import pandas as pd

# Load data
similarity = pickle.load(open('similarity.pkl', 'rb'))
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


# -------------------- UI --------------------
st.set_page_config(page_title="🎬 Movie Recommendation System", page_icon="🎥", layout="wide")

# Custom CSS
st.markdown("""
    <style>
        .title {
            font-size:50px !important;
            color:#FF4B4B;
            text-align:center;
            font-weight: bold;
        }
        .recommend-card {
            background-color: #262730;
            padding: 10px;
            border-radius: 12px;
            margin: 10px;
            color: white;
            text-align: center;
            font-size: 16px;
            font-weight: 600;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.4);
            height: 320px; /* 🔥 Fixed height for equal box size */
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .movie-title {
            margin-top: 8px;
            font-size: 16px;
            font-weight: 600;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">🎬 Movie Recommendation System</p>', unsafe_allow_html=True)

# Dummy poster (local file in same folder as app.py)
dummy_poster = "unnamed.png"

# Select movie
selected_movie = st.selectbox(
    '🔍 Search for a Movie:',
    movies['title'].values,
    index=0
)

if st.button('🚀 Recommend'):
    recommendations = recommend(selected_movie)
    
    st.subheader("✨ Recommended Movies for You:")
    
    # Display recommendations in columns (like movie cards)
    cols = st.columns(5)
    for idx, movie in enumerate(recommendations):
        with cols[idx]:
            #st.markdown('<div class="recommend-card">', unsafe_allow_html=True)
            
            st.markdown(f"<div class='movie-title'>🎥 {movie}</div>", unsafe_allow_html=True)
            st.image(dummy_poster, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
