import pickle
import streamlit as st
import requests
import os

session = requests.Session()
OMDB_API_KEY = "9436b3db"
manual_title_fixes = {
    "Aliens vs Predator: Requiem": "AVPR: Aliens vs Predator - Requiem"
}

def fetch_poster(title):
    title_query = manual_title_fixes.get(title, title)
    try:
        url = f"http://www.omdbapi.com/?t={requests.utils.quote(title_query)}&apikey={OMDB_API_KEY}"
        res = session.get(url, timeout=2)
        if res.status_code == 200:
            data = res.json()
            poster_url = data.get("Poster")
            if poster_url and poster_url != "N/A":
                return poster_url
    except:
        pass
    return "https://via.placeholder.com/500x750?text=No+Image"

def recommend(movie, movies, similarity):
    idx = movies[movies['title'] == movie].index[0]
    dist = sorted(enumerate(similarity[idx]), key=lambda x: x[1], reverse=True)
    names, posters = [], []
    for i, _ in dist[1:6]:
        t = movies.iloc[i].title
        names.append(t)
        posters.append(fetch_poster(t))
    return names, posters

def main():
    st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")
    st.header('🎬 Movie Recommender System Using Machine Learning')

    path = os.path.join(os.path.dirname(__file__), 'artifacts')
    try:
        movies = pickle.load(open(os.path.join(path, 'movie_list.pkl'), 'rb'))
        similarity = pickle.load(open(os.path.join(path, 'similarity.pkl'), 'rb'))
    except Exception as e:
        st.error(f"❌ Could not load artifacts: {e}")
        return

    selection = st.selectbox("🎥 Type or select a movie:", movies['title'].values)
    if st.button('🔍 Show Recommendations'):
        names, posters = recommend(selection, movies, similarity)
        cols = st.columns(5)
        for c, name, poster in zip(cols, names, posters):
            c.text(name)
            c.image(poster)

if __name__ == "__main__":
    main()
