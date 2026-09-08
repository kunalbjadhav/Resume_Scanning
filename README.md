# AI Resume Screening & Candidate Ranking System

An NLP-driven Applicant Tracking System (ATS) script built to parse, process, and evaluate candidate resumes against custom job descriptions using TF-IDF vectorization and Cosine Similarity.

---

## Key Features

- **Multi-Format Extraction:** Automatically extracts text from both `.pdf` and `.docx` candidate resumes.
- **NLP Text Normalization:** Lowers text case, removes special characters, and strips English stopwords using NLTK.
- **Automated Similarity Scoring:** Computes relative match percentages by comparing resume vector representations directly against job descriptions.
- **Index-Safe Processing:** Filters non-supported files in the working directory to prevent data offset and mismatching candidate scores.

---

## Project Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Nikhil-Portfolio/your-repo-name.git](https://github.com/Nikhil-Portfolio/your-repo-name.git)
   cd your-repo-name
