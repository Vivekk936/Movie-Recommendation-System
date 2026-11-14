# Movie Recommendation System

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NLTK](https://img.shields.io/badge/NLTK-NLP-blue?style=for-the-badge)](https://www.nltk.org/)

An interactive **Content-Based Movie Recommendation System** built using Natural Language Processing (NLP) techniques and deployed as a responsive web app with **Streamlit**.

The system analyzes movie metadata (genres, keywords, cast, crew, and overviews) to suggest the top 5 most similar movies based on cosine similarity.

---

##  Features

- **Content-Based Filtering**: Suggests movies similar to a user-selected title by calculating vector cosine similarity across rich metadata tags.
- **NLP Text Processing**: Utilizes text stemming (via NLTK) and vectorization with `CountVectorizer` to generate a 5,000-dimensional bag-of-words space.
- **Fast Similarity Lookups**: Uses precomputed and compressed similarity matrices with `joblib` for instantaneous recommendation retrieval.
- **Interactive UI**: Simple and intuitive dropdown selection powered by Streamlit.

---

##  How It Works

```
TMDB 5000 Dataset (Movies + Credits)
         │
         ▼
Data Preprocessing & Feature Extraction
(Overview + Genres + Keywords + Top Cast + Director)
         │
         ▼
Tag Generation & Stemming (NLTK)
         │
         ▼
Vectorization (CountVectorizer, 5000 features)
         │
         ▼
Cosine Similarity Matrix Calculation
         │
         ▼
Streamlit Web Interface (app.py) ──► Top 5 Movie Recommendations
```

1. **Data Source**: Built using the TMDB 5,000 Movies & Credits dataset.
2. **Metadata Merging**: Combines movie overviews, genres, keywords, top cast members, and directors into unified text tags.
3. **Stemming & Stopwords**: Cleans and normalizes tokens (e.g., `"loving"` and `"loved"` are stemmed to `"love"`).
4. **Vectorization**: Transforms metadata into 5,000 top feature vectors using `sklearn.feature_extraction.text.CountVectorizer`.
5. **Cosine Similarity**: Calculates pairwise similarity scores between all movies.
6. **Recommendation Engine**: Looks up the target movie's vector, ranks the nearest neighbors, and outputs the top 5 matches.

---

##  Project Structure

```bash
Movies-Recommendation-System/
├── app.py                 # Streamlit web application
├── movie.pickle           # Serialized movie DataFrame (titles and metadata)
├── similarity.joblib      # Compressed cosine similarity matrix
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

---

## Getting Started

### Prerequisites

Ensure you have **Python 3.8+** installed on your system.

### 1. Clone the Repository

```bash
git clone https://github.com/Vivekk936/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

### 2. Set Up a Virtual Environment (Optional but Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

After running the command, your default browser will automatically open the app at `http://localhost:8501`.

---

##  Built With

- **[Python](https://www.python.org/)** - Programming Language
- **[Streamlit](https://streamlit.io/)** - Web Framework for ML apps
- **[Scikit-learn](https://scikit-learn.org/)** - Vectorization & Cosine Similarity
- **[NLTK](https://www.nltk.org/)** - Natural Language Toolkit (Stemming)
- **[Pandas](https://pandas.pydata.org/)** - Data Manipulation & Analysis
- **[Joblib](https://joblib.readthedocs.io/)** / **Pickle** - Model & Data Serialization

---

##  Future Enhancements

- [ ] Fetch and display movie posters using the TMDB API.
- [ ] Add movie ratings, release dates, and trailer links.
- [ ] Implement collaborative filtering or hybrid recommendation algorithms.
- [ ] Add genre and release year filtering options.

---

##  License

This project is open-source and available under the [MIT License](LICENSE).
