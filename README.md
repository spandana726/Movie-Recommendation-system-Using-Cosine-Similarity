
# 🎬 Movie Recommender System Using Machine Learning (Cosine Similarity)

Recommendation systems are revolutionizing how we consume content. With endless choices and limited time, intelligent systems that personalize suggestions help users make quick, meaningful decisions — whether it’s what movie to watch, what book to read, or which product to buy.

This project is a **Streamlit-powered web application** that recommends movies similar to a user's selected movie based on **cosine similarity**. It’s built using TMDB metadata and delivers fast, relevant suggestions through efficient NLP and ML techniques.

---

## What is a Recommendation System?

A **Recommendation System** suggests items (like movies, music, books) to users by analyzing their past behaviors, preferences, or demographic similarities with others. It works using **Artificial Intelligence** models that rely on content metadata and user interactions.

---

## 🔍 Types of Recommendation Systems

### 1️⃣ Content-Based Filtering

- Uses item features (e.g., genre, cast, keywords) to recommend similar content.
- Learns what a user likes and recommends similar items.
- Used by platforms like YouTube, Spotify.
- 🔺 Downside: May suffer from **over-specialization** (repetitive recommendations).

### 2️⃣ Collaborative Filtering

- Relies on user-item interactions (ratings, reviews).
- Finds clusters of users with similar preferences.
- Used by Netflix, Amazon.
- 🔺 Downside: Cold start problem for new users or new items.

### 3️⃣ Hybrid Systems

- Combine **Content-Based** and **Collaborative Filtering**.
- Aim to overcome limitations of both systems.
- Common in production-grade systems using deep embeddings, word2vec, etc.

---

## About This Project

This is a **movie recommendation web app** built using **Python**, **Streamlit**, and **Cosine Similarity**.

- Built on the [TMDB 5000 Movie Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)
- Returns top 5 similar movies based on user-selected movie
- Uses NLP techniques like TF-IDF and vector similarity
- Fully interactive UI via Streamlit

---

## Machine Learning Concept Used

### Cosine Similarity

- A metric to measure the **similarity between two vectors**.
- Returns value between **0 (completely different)** and **1 (completely similar)**.
- Used to compare the **vectorized representations of movies** based on metadata like genre, cast, keywords, etc.

🔗 [Learn More](https://www.learndatasci.com/glossary/cosine-similarity/)

---

## 💾 Dataset Used

- TMDb Movie Metadata:  
  📁 [`tmdb_5000_movies.csv`](https://www.kaggle.com/tmdb/tmdb-movie-metadata)

---

## How to Run the Project Locally

### Step 1: Clone the Repository

```bash
git clone https://github.com/spandana726/Movie-Recommendation-system-Using-Cosine-Similarity.git
cd Movie-Recommendation-system-Using-Cosine-Similarity
```

### Step 2: Create a Virtual Environment

```bash
conda create -n movie python=3.7.10 -y
conda activate movie
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Generate the Model

```bash
# Run the data analysis and vectorizer code to create similarity matrix
jupyter notebook "Movie Recommender System Data Analysis.ipynb"
```

### Step 5: Launch the App

```bash
streamlit run app.py
```

---

## Demo Outputs

### 👇 Screenshots of the Working Web App

| Select Movie | Recommendations | Visual UI |
|--------------|------------------|-----------|
| ![Screenshot 1](https://github.com/user-attachments/assets/49e8ebcf-1af9-4610-9306-10a0f6a90c8c) | ![Screenshot 2](https://github.com/user-attachments/assets/09a0ba42-f47a-4fcc-b040-a97bba97d830) | ![Screenshot 3](https://github.com/user-attachments/assets/588e08b9-95f3-43c8-b25c-88f5d558f08c) |

---

## 📁 Project Structure

```
├── app.py                              # Streamlit UI logic
├── Movie Recommender System Data Analysis.ipynb   # Model generation & analysis
├── similarity.pkl                      # Cosine similarity matrix
├── movies.pkl                          # Processed movie data
├── requirements.txt                   # Python dependencies
└── README.md                          # Project overview
```

---

## 👩‍💻 Author

**Spandana Gunaganti**  
📧 Email: 227r1a66f7@cmrtc.ac.in  
💼 GitHub: [@spandana726](https://github.com/spandana726)

## Future Improvements

- Add TMDb API integration for dynamic metadata updates
- Include hybrid filtering logic using user ratings
- Enhance UI with cover images, filters, and animations
- Deploy using Streamlit Cloud or Hugging Face Spaces
