import streamlit as st
from PIL import Image
import base64

# Page configuration
st.set_page_config(
    page_title="Abdullah Said - AI & Data Science Engineer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main {
        padding: 0px 20px;
    }
    .stApp {
        background-color: #0e1117;
    }
    .hero-section {
        text-align: center;
        padding: 50px 0;
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        border-radius: 20px;
        margin-bottom: 50px;
    }
    .profile-img {
        width: 200px;
        height: 200px;
        border-radius: 50%;
        border: 5px solid white;
        margin-bottom: 20px;
    }
    .social-links {
        display: flex;
        justify-content: center;
        gap: 30px;
        margin: 20px 0;
    }
    .social-links a {
        color: white;
        font-size: 18px;
        text-decoration: none;
        padding: 10px 20px;
        background: rgba(255,255,255,0.1);
        border-radius: 10px;
        transition: all 0.3s;
    }
    .social-links a:hover {
        background: rgba(255,255,255,0.2);
        transform: translateY(-3px);
    }
    .section-header {
        color: #3498db;
        border-bottom: 3px solid #3498db;
        padding-bottom: 10px;
        margin-bottom: 30px;
    }
    .skill-tag {
        display: inline-block;
        background: #2c3e50;
        color: white;
        padding: 8px 15px;
        margin: 5px;
        border-radius: 20px;
        font-size: 14px;
    }
    .project-card {
        background: #1a1a2e;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
        border: 1px solid #333;
        transition: all 0.3s;
    }
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    .experience-item {
        background: #16213e;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        border-left: 4px solid #3498db;
    }
    .cert-link {
        color: #3498db;
        text-decoration: none;
        margin-right: 15px;
        display: inline-block;
        padding: 5px 10px;
        background: rgba(52, 152, 219, 0.1);
        border-radius: 5px;
        transition: all 0.3s;
    }
    .cert-link:hover {
        background: rgba(52, 152, 219, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# Load profile image
try:
    image = Image.open('personal photo.png')
    
    # Convert image to base64
    import io
    img_buffer = io.BytesIO()
    image.save(img_buffer, format='PNG')
    img_str = base64.b64encode(img_buffer.getvalue()).decode()
    
    # Hero Section with Profile
    st.markdown(f"""
    <div class="hero-section">
        <img src="data:image/png;base64,{img_str}" class="profile-img">
        <h1 style="color: white; font-size: 48px; margin-bottom: 10px;">Abdullah Said</h1>
        <h2 style="color: #ecf0f1; font-size: 28px; font-weight: 300;">AI & Data Science Engineer</h2>
        <p style="color: #bdc3c7; font-size: 18px; max-width: 800px; margin: 20px auto;">
            Results-driven AI & Data Science Engineer with hands-on experience in developing, 
            deploying, and optimizing machine learning and deep learning models.
        </p>
        <div class="social-links">
            <a href="https://github.com/yourusername" target="_blank">GitHub</a>
            <a href="https://linkedin.com/in/abdullah-said-mle" target="_blank">LinkedIn</a>
            <a href="mailto:abdullahsaid814@gmail.com">Email</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
except:
    # Fallback hero section without image
    st.markdown("""
    <div class="hero-section">
        <h1 style="color: white; font-size: 48px; margin-bottom: 10px;">Abdullah Said</h1>
        <h2 style="color: #ecf0f1; font-size: 28px; font-weight: 300;">AI & Data Science Engineer</h2>
        <p style="color: #bdc3c7; font-size: 18px; max-width: 800px; margin: 20px auto;">
            Results-driven AI & Data Science Engineer with hands-on experience in developing, 
            deploying, and optimizing machine learning and deep learning models.
        </p>
        <div class="social-links">
            <a href="https://github.com/yourusername" target="_blank">GitHub</a>
            <a href="https://linkedin.com/in/abdullah-said-mle" target="_blank">LinkedIn</a>
            <a href="mailto:abdullahsaid814@gmail.com">Email</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Contact Information
col1, col2, col3 = st.columns(3)
with col1:
    st.info("Phone: +201020965984")
with col2:
    st.info("Email: abdullahsaid814@gmail.com")
with col3:
    st.info("Location: Cairo, Egypt")

# About Section
st.markdown("<h2 class='section-header'>About Me</h2>", unsafe_allow_html=True)
st.write("""
A passionate AI & Data Science Engineer with expertise in developing and deploying machine learning solutions. 
Skilled in applying artificial intelligence algorithms to solve real-world problems, with practical expertise 
in data analysis, visualization, and building end-to-end applications. Strong background in machine learning 
pipelines, RAG-based systems, and data-driven decision-making. Currently pursuing a Bachelor's degree in 
Artificial Intelligence at Banha University (Class of 2026).
""")

# Key Competencies
st.markdown("<h2 class='section-header'>Key Competencies</h2>", unsafe_allow_html=True)
skills = [
    "Machine Learning", "Deep Learning", "Data Analysis", "Data Visualization",
    "Data Cleaning", "Model Deployment", "SQL & Databases", "Power BI",
    "FastAPI", "Streamlit", "RAG Systems", "LlamaIndex", "Web Scraping",
    "Problem Solving", "Research Projects", "Team Collaboration"
]

skills_html = "".join([f"<span class='skill-tag'>{skill}</span>" for skill in skills])
st.markdown(f"<div style='margin: 20px 0;'>{skills_html}</div>", unsafe_allow_html=True)

# Professional Experience
st.markdown("<h2 class='section-header'>Professional Experience</h2>", unsafe_allow_html=True)

experiences = [
    {
        "title": "Practical Projects",
        "company": "Faculty of Computers & Artificial Intelligence | Banha University",
        "description": [
            "Implemented artificial intelligence algorithms from scratch to solve real-world problems",
            "Conducted applied projects using Weka 3 - Data Mining with Open Source Machine Learning",
            "Gained solid knowledge of machine learning algorithms and introduction to deep learning"
        ]
    },
    {
        "title": "AI Trainee",
        "company": "NTI (National Telecommunication Institute)",
        "description": [
            "Applied all major machine learning algorithms on real datasets",
            "Developed introductory deep learning models for classification and regression problems"
        ]
    },
    {
        "title": "AI Intern",
        "company": "Namesoft Company",
        "description": [
            "Built multiple practical AI projects including RAG (Retrieval-Augmented Generation) system",
            "Developed Neural Network from scratch",
            "Implemented Llama Index integration project",
            "Created Dynamic Routing for LLMs project"
        ]
    }
]

for exp in experiences:
    st.markdown(f"""
    <div class='experience-item'>
        <h3 style='color: #3498db; margin-bottom: 5px;'>{exp['title']}</h3>
        <p style='color: #95a5a6; margin-bottom: 10px;'>{exp['company']}</p>
    </div>
    """, unsafe_allow_html=True)
    for desc in exp['description']:
        st.write(f"• {desc}")
    st.write("")

# Projects Section
st.markdown("<h2 class='section-header'>Projects</h2>", unsafe_allow_html=True)

# Project data with placeholder GitHub links
projects = [
    {
        "name": "Football Data Visualization Dashboard",
        "description": "Advanced football data analytics dashboard built with Streamlit for comprehensive statistical analysis and visualization",
        "github": "https://github.com/yourusername/football-dashboard"
    },
    {
        "name": "Mini-RAG Project",
        "description": "Lightweight retrieval-augmented generation system implementing efficient document retrieval and response generation",
        "github": "https://github.com/yourusername/mini-rag"
    },
    {
        "name": "Stock Revenue Analysis Dashboard",
        "description": "Comprehensive stock market analysis tool with historical data visualization and trend analysis built with Python and Streamlit",
        "github": "https://github.com/yourusername/stock-analysis"
    },
    {
        "name": "Real-Estate Data Cleanse",
        "description": "Data cleaning pipeline for real estate datasets, implementing advanced preprocessing and validation techniques",
        "github": "https://github.com/yourusername/realestate-cleanse"
    },
    {
        "name": "Web Scraping Automation",
        "description": "Automated data extraction and structuring system for various web sources using modern scraping techniques",
        "github": "https://github.com/yourusername/web-scraper"
    },
    {
        "name": "Power BI Interactive Dashboards",
        "description": "Collection of interactive business intelligence dashboards created for data-driven decision making",
        "github": "https://github.com/yourusername/powerbi-dashboards"
    },
    {
        "name": "FastAPI ML Services",
        "description": "RESTful API services for machine learning model deployment and real-time inference",
        "github": "https://github.com/yourusername/fastapi-ml"
    }
]

# Display projects in a grid
col1, col2 = st.columns(2)
for i, project in enumerate(projects):
    with col1 if i % 2 == 0 else col2:
        st.markdown(f"""
        <div class='project-card'>
            <h3 style='color: #3498db;'>{project['name']}</h3>
            <p style='color: #bdc3c7; margin: 10px 0;'>{project['description']}</p>
            <a href='{project['github']}' target='_blank' style='color: #3498db; text-decoration: none;'>
                View on GitHub →
            </a>
        </div>
        """, unsafe_allow_html=True)

# Education Section
st.markdown("<h2 class='section-header'>Education</h2>", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    <div class='experience-item'>
        <h3 style='color: #3498db;'>Bachelor's Degree in Artificial Intelligence</h3>
        <p style='color: #95a5a6;'>Banha University - Faculty of Computers & Artificial Intelligence</p>
        <p style='color: #bdc3c7;'>Expected Graduation: 2026</p>
    </div>
    """, unsafe_allow_html=True)

# Certifications and Links
st.markdown("<h2 class='section-header'>Certifications & Learning</h2>", unsafe_allow_html=True)

st.markdown("### Professional Certifications - Coursera")
certifications = [
    {"name": "Data Analysis Specialization", "link": "https://coursera.org/certificate/data-analysis"},
    {"name": "Database Management", "link": "https://coursera.org/certificate/databases"},
    {"name": "Machine Learning", "link": "https://coursera.org/certificate/machine-learning"},
    {"name": "Deep Learning Specialization", "link": "https://coursera.org/certificate/deep-learning"},
    {"name": "Data Science Professional Certificate", "link": "https://coursera.org/certificate/data-science"}
]

cert_html = ""
for cert in certifications:
    cert_html += f"<a href='{cert['link']}' target='_blank' class='cert-link'>{cert['name']}</a>"
st.markdown(f"<div style='margin: 20px 0;'>{cert_html}</div>", unsafe_allow_html=True)

# Footer with additional links
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 20px 0;'>
    <h3 style='color: #3498db; margin-bottom: 20px;'>Connect With Me</h3>
    <div class='social-links' style='justify-content: center;'>
        <a href='https://github.com/yourusername' target='_blank'>GitHub Profile</a>
        <a href='https://linkedin.com/in/abdullah-said-mle' target='_blank'>LinkedIn</a>
        <a href='https://coursera.org/user/yourusername' target='_blank'>Coursera Profile</a>
        <a href='https://www.bu.edu.eg/en' target='_blank'>Banha University</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Add a professional footer
st.markdown("""
<div style='text-align: center; color: #7f8c8d; padding: 30px 0;'>
    <p>© 2024 Abdullah Said. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)