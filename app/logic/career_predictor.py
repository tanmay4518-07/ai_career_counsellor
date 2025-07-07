import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_career_data():
    # Assumes run.py is executed from the root
    file_path = os.path.join("data", "careers.json")
    with open(file_path, "r") as file:
        return json.load(file)

def predict_career(user_input):
    careers = load_career_data()
    career_titles = list(careers.keys())
    descriptions = [careers[title]["description"] for title in career_titles]

    all_texts = [user_input] + descriptions

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    best_index = similarities.argmax()
    best_career = career_titles[best_index]

    return {
        "career": best_career,
        "description": careers[best_career]["description"],
        "skills": careers[best_career]["skills"],
        "resources": careers[best_career]["resources"]
    }
