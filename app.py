import streamlit as st
import pandas as pd
from parser import get_text_from_file
from matcher import get_final_score

# --- Inject Custom CSS for Styling ---
st.markdown("""
<style>
/* Style for main headers (h1) and specific sections */
.section-header {
    background-color: #0068C9;
    color: #FAFAFA;
    padding: 15px;
    border-radius: 8px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# --- Page Title and Header ---
st.markdown('<div class="section-header"><h1>AI Resume Scraper & Matcher 🚀</h1></div>', unsafe_allow_html=True)
st.markdown("### Match multiple resumes to one job description")

# --- Input Section ---
col1, col2 = st.columns(2)

with col1:
    with st.container():
        st.subheader("Upload Resumes")
        uploaded_resumes = st.file_uploader(
            "Select Your Resumes (PDF or DOCX)", 
            type=["pdf", "docx"], 
            accept_multiple_files=True,
            help="You can upload multiple resumes at once."
        )

with col2:
    with st.container():
        st.subheader("Job Description")
        job_desc = st.text_area(
            "Paste the Job Description Here", 
            height=400,
            help="Paste the text of the job description you want to match against."
        )

# --- Analysis Button ---
if st.button("Analyze Matches"):
    if uploaded_resumes and job_desc:
        with st.spinner("Analyzing..."):
            results_data = []
            for resume in uploaded_resumes:
                resume_text = get_text_from_file(resume)
                score, matched_skills, required_skills = get_final_score(resume_text, job_desc)
                
                results_data.append({
                    "Resume Name": resume.name,
                    "Match Score": f"{score:.2f}%",
                    "Matched Skills": ", ".join(matched_skills),
                    "Missing Skills": ", ".join(set(required_skills) - set(matched_skills))
                })

            df_results = pd.DataFrame(results_data)
            st.success("Analysis Complete!")
            
            with st.container():
                st.markdown("---")
                # Apply the same header style to this heading
                st.markdown('<div class="section-header"><h3>Match Results Summary</h3></div>', unsafe_allow_html=True)
                st.dataframe(df_results, width='stretch')
            
            if not df_results.empty:
                st.markdown("---")
                with st.container():
                    # Apply the same header style to this heading
                    st.markdown('<div class="section-header"><h3>Top Candidate Breakdown</h3></div>', unsafe_allow_html=True)
                    top_candidate = df_results.iloc[df_results["Match Score"].str.rstrip('%').astype(float).idxmax()]
                    st.write(f"**Top Candidate:** {top_candidate['Resume Name']}")
                    st.metric(label="Overall Score", value=top_candidate["Match Score"])
                    
                    with st.expander("Show detailed skills"):
                        st.write(f"**Matched Skills:** {top_candidate['Matched Skills']}")
                        st.warning(f"**Missing Skills:** {top_candidate['Missing Skills']}")
                        
    else:
        st.error("Please upload at least one resume and paste a job description.")