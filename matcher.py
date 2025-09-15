from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import spacy

# Load a pre-trained sentence embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')
# Load the spaCy model for Named Entity Recognition (NER)
nlp = spacy.load("en_core_web_sm")

def extract_skills_from_jd(job_desc_text):
    """
    A simple function to extract skills from a job description using a predefined list.
    """
    skills_list = ["Python", "SQL", "Flask", "React", "AWS", "Machine Learning", "Data Analysis", "Communication"]
    found_skills = [skill for skill in skills_list if skill.lower() in job_desc_text.lower()]
    return set(found_skills)

def get_final_score(resume_text, job_desc_text):
    """
    Combines semantic match with a simple skills match for a final score.
    """
    # Create embeddings for both documents to get semantic similarity
    embeddings = model.encode([resume_text, job_desc_text])
    semantic_score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0] * 100

    # Extract skills from both documents
    jd_skills = extract_skills_from_jd(job_desc_text)
    
    # Simple skills extraction from resume (can be improved)
    resume_skills_found = set()
    for skill in jd_skills:
        if skill.lower() in resume_text.lower():
            resume_skills_found.add(skill)
    
    skill_match_percentage = (len(resume_skills_found) / len(jd_skills)) * 100 if jd_skills else 0
    
    # Weighted average for a more comprehensive final score
    final_score = (semantic_score * 0.7) + (skill_match_percentage * 0.3)
    
    return final_score, list(resume_skills_found), list(jd_skills)