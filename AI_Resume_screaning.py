import os
import re
import docx
import nltk
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download("stopwords")
stopwords = set(nltk.corpus.stopwords.words("english"))


# Text extraction
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text


def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return " ".join([para.text for para in doc.paragraphs])


# Text cleaning
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    words = [w for w in text.split() if w not in stopwords]
    return " ".join(words)


# Load Resumes
resume_folder = "resumes/"
resumes = []
valid_filenames = []  # Track only matched resume filenames

if os.path.exists(resume_folder):
    for file in os.listdir(resume_folder):
        file_path = os.path.join(resume_folder, file)
        if file.endswith(".pdf"):
            resumes.append(clean_text(extract_text_from_pdf(file_path)))
            valid_filenames.append(file)
        elif file.endswith(".docx"):
            resumes.append(clean_text(extract_text_from_docx(file_path)))
            valid_filenames.append(file)

# Job description (Cleaned to match TF-IDF preprocessing)
job_description = "Looking for Data Analyst with skills in SQL, Python, Power BI, and Excel dashboards."
cleaned_jd = clean_text(job_description)

# TF-IDF vectorization & Scoring
if resumes:
    vectorizer = TfidfVectorizer()
    documents = resumes + [cleaned_jd]
    tfidf_matrix = vectorizer.fit_transform(documents)

    scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()

    # Ranking candidates using valid_filenames
    ranked_candidates = sorted(
        list(zip(valid_filenames, scores)), key=lambda x: x[1], reverse=True
    )

    # Display
    print("Candidate Ranking:")
    for candidate, score in ranked_candidates:
        print(f"{candidate}: {score * 100:.2f}% match")