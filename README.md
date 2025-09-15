# 🛡️ AI Resume Scraper & Matcher 🚀

An intelligent application that uses machine learning to score and match resumes against a job description.

---

### 🎥 Demo Video

Here is a quick demo of the application in action.


https://github.com/user-attachments/assets/e68eb3c5-4bcb-4645-92df-c657bc24908d




### ✨ Features

* **Semantic Matching**: Uses state-of-the-art NLP to accurately compare resume content with job requirements.
* **Bulk Analysis**: Process and score multiple resumes simultaneously against a single job description.
* **Detailed Skill Breakdown**: Shows which skills from the job description are present or missing from a resume.
* **File Compatibility**: Supports both PDF and DOCX resume formats.

---

### ⚙️ Technologies Used

* **Python**: The core programming language.
* **Streamlit**:  For building the interactive web application.
* **Sentence-Transformers**: For generating semantic embeddings.
* **scikit-learn**:  For cosine_similarity calculations.
* **PyPDF2 & python-docx**: For parsing text from resume files.
* **Spacy**: For extracting keywords and skills.
* **Pandas**: For handling and displaying the data in a clean tabular format.
* 
---

### 🚀 Getting Started

To run this application locally, follow these steps:

1.  **Clone the repository**:
    ```sh
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3.  **Run the Flask application**:
    ```sh
    gunicorn app:app
    ```
    The application will be accessible at `http://localhost:5000`.
