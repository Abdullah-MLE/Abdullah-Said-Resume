import streamlit as st
from data.testimonials import testimonials
from data.projects import projects
from data.services import services
from data.certifications import certifications

class Portfolio:
    def __init__(self):
        self.projects = projects
        self.services = services
        self.achievements = [
            "Achievement 1: Lorem ipsum dolor sit amet.",
            "Achievement 2: Consectetur adipiscing elit.",
            "Achievement 3: Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        ]
        self.testimonials = sorted(testimonials, key=lambda x: x['timestamp'], reverse=True)
        self.certifications = certifications

    def render_header(self):
        st.title("Abdullah Said Portfolio")

    def render_tabs(self):
        tabs = st.tabs(["About", "Services", "Projects", "Testimonials", "Achievements", "Contact Me", "Education"])

        with tabs[0]:
            self.render_about()

        with tabs[1]:
            self.render_services()

        with tabs[2]:
            self.render_projects()

        with tabs[3]:
            self.render_testimonials()

        with tabs[4]:
            self.render_achievements()

        with tabs[5]:
            self.render_contact_me()
            
        with tabs[6]:
            self.render_education()

    def render_about(self):
        st.header("About Me")
        col1, col2 = st.columns([2, 1])
        with col1:
            st.write("""
            Hello! I'm a passionate software developer with expertise in full-stack development 
            and data analysis. I love creating innovative solutions that make a real impact.
            
            With 5+ years of experience in the tech industry, I've worked on various projects 
            ranging from web applications to machine learning models. I'm always eager to learn 
            new technologies and take on challenging projects.
            
            When I'm not coding, you can find me exploring new technologies, contributing to 
            open-source projects, or enjoying outdoor activities.
            """)
        with col2:
            st.image("assets/profile.png", width=350)
        
        st.markdown("---")
        self.render_skills()

    def render_contact_me(self):
        st.header("Contact Me")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Get in Touch")
            st.write("""
            I'm always open to discussing new opportunities and interesting projects.
            Feel free to reach out!
            
            📧 Email: abdullahsaid814@gmail.com
            
            📱 Phone: +20 010 2069 5984
            
            📍 Location: Ciro, Egypt
            """)
        with col2:
            st.subheader("Social Media")
            st.write("""
            🔗 [LinkedIn](https://linkedin.com)
            
            💻 [GitHub](https://github.com)
            
            🐦 [Twitter](https://twitter.com)
            
            🌐 [Personal Website](https://example.com)
            """)

    def render_services(self):
        st.header("My Services")
        for i in range(0, len(self.services), 4):
            cols = st.columns(4)
            for j in range(4):
                if i + j < len(self.services):
                    service = self.services[i + j]
                    with cols[j]:
                        with st.container():
                            st.image(service["image"], use_container_width=True)
                            st.subheader(service["title"])
                            st.write(service["description"])
                            if st.button("Show More", key=f"show_more_{i+j}", use_container_width=True):
                                st.switch_page(f"services/{service['page']}.py")
                            st.link_button("Order Now", "#contact-me", use_container_width=True)
                        st.markdown("---")

    def render_projects(self):
        st.header("My Projects")
        for i in range(0, len(self.projects), 4):
            cols = st.columns(4)
            for j in range(4):
                if i + j < len(self.projects):
                    project = self.projects[i + j]
                    with cols[j]:
                        with st.container():
                            st.image(project["image"], use_container_width=True)
                            st.subheader(project["title"])
                            st.write(project["description"])
                            tech_tags = " ".join([f"`{tech}`" for tech in project["tech"]])
                            st.markdown(tech_tags)
                            if st.button("View Project", key=f"btn_{i+j}", use_container_width=True):
                                st.switch_page(f"Projects/{project['page']}.py")
                        st.markdown("---")

    def render_skills(self):
        st.header("Key Competencies")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("AI & Machine Learning")
            st.write("""
            - Machine Learning
            - Deep Learning
            - Model Deployment
            - RAG Systems
            - LlamaIndex
            """)
        with col2:
            st.subheader("Data & Analytics")
            st.write("""
            - Data Analysis
            - Data Visualization
            - Data Cleaning
            - SQL & Databases
            - Power BI
            - Web Scraping
            """)
        with col3:
            st.subheader("Development & Professional")
            st.write("""
            - FastAPI / Streamlit
            - Problem Solving
            - Research Projects
            - Team Collaboration
            """)

    def render_education(self):
        st.header("Education")
        st.subheader("Banha University – Faculty of Computers & Artificial Intelligence")
        st.write("**Bachelor’s Degree in Artificial Intelligence**, Class of 2026")
        st.link_button("Visit University Website", "https://fci.bu.edu.eg/")

    def render_achievements(self):
        st.header("My Achievements")
        for achievement in self.achievements:
            st.markdown(f"- {achievement}")
        
        st.markdown("---")
        st.subheader("Professional Certifications")
        for cert in self.certifications:
            st.markdown(f"- [{cert['name']}]({cert['url']})")

    def render_testimonials(self):
        st.header("Client Testimonials")
        for testimonial in self.testimonials:
            with st.container():
                st.subheader(testimonial["client_name"])
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown(f"**{testimonial['project_name']}**")
                with col2:
                    st.write(testimonial["rating"])

                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.write(f"**Platform:** {testimonial['location']}")
                with col2:
                    st.write(f"**Cost:** {testimonial['project_cost']}")
                with col3:
                    st.write(f"**Duration:** {testimonial['project_duration']}")
                with col4:
                    st.link_button("View Testimonial", testimonial["link"])
                st.markdown("---")

    def run(self):
        self.render_header()
        self.render_tabs()

def main():
    st.set_page_config(
        page_title="My Portfolio", 
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    portfolio = Portfolio()
    hide_img_fs = '''
        <style>
        button[title="View fullscreen"]{
            visibility: hidden;}
        div[data-testid="stHorizontalBlock"] div[data-testid="stVerticalBlock"] {
            height: 450px;
        }
        div[data-testid="stHorizontalBlock"] div[data-testid="stVerticalBlock"] img {
            object-fit: cover;
            height: 200px;
        }
        </style>
    '''
    st.markdown(hide_img_fs, unsafe_allow_html=True)
    portfolio.run()

if __name__ == "__main__":
    main()
