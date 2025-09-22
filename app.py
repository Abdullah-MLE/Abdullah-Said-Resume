import streamlit as st
from data.testimonials import testimonials
from data.projects import projects
from data.services import services

# =============================================================================
# PORTFOLIO CLASS
# =============================================================================
class Portfolio:
    """Simple portfolio website class"""

    def __init__(self):
        """Initialize portfolio"""
        self.projects = projects
        self.services = services

        self.achievements = [
            "Achievement 1: Lorem ipsum dolor sit amet.",
            "Achievement 2: Consectetur adipiscing elit.",
            "Achievement 3: Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        ]

        self.testimonials = sorted(testimonials, key=lambda x: x['timestamp'], reverse=True)

    def render_header(self):
        """Render simple header"""
        st.title("Abdullah Said Portfolio")

    def render_tabs(self):
        """Render main tabs"""
        tabs = st.tabs(["About", "Services", "Projects", "Skills", "Education", "Achievements", "Testimonials"])

        with tabs[0]:
            self.render_about()

        with tabs[1]:
            self.render_services()

        with tabs[2]:
            self.render_projects()

        with tabs[3]:
            self.render_skills()

        with tabs[4]:
            self.render_education()

        with tabs[5]:
            self.render_achievements()

        with tabs[6]:
            self.render_testimonials()

    def render_about(self):
        """Render about section"""
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
            # To display your photo, create an 'assets' folder in your project root
            # and place an image file named 'profile.png' inside it.
            st.image("assets/profile.png", width=350, )
            
        st.markdown("---")
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
        """Render services grid"""
        st.header("My Services")

        # Create grid layout - 4 columns per row
        for i in range(0, len(self.services), 4):
            cols = st.columns(4)

            for j in range(4):
                if i + j < len(self.services):
                    service = self.services[i + j]

                    with cols[j]:
                        # Service card
                        with st.container():
                            st.image(service["image"], use_column_width=True)
                            st.subheader(service["title"])
                            st.write(service["description"])

                        st.markdown("---")

    def render_projects(self):
        """Render projects grid"""
        st.header("My Projects")

        # Create grid layout - 4 columns per row
        for i in range(0, len(self.projects), 4):
            cols = st.columns(4)

            for j in range(4):
                if i + j < len(self.projects):
                    project = self.projects[i + j]

                    with cols[j]:
                        # Project card
                        with st.container():
                            st.image(project["image"], use_column_width=True)
                            st.subheader(project["title"])
                            st.write(project["description"])
                            
                            # Tech stack
                            tech_tags = " ".join([f"`{tech}`" for tech in project["tech"]])
                            st.markdown(tech_tags)
                            
                            # View project button
                            if st.button(
                                "View Project",
                                key=f"btn_{i+j}",
                                use_container_width=True
                            ):
                                st.switch_page(f"Projects/{project['page']}.py")

                        st.markdown("---")

    def render_skills(self):
        """Render skills section"""
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
        """Render education section"""
        st.header("Education & Certifications")

        st.subheader(
            "Banha University – Faculty of Computers & Artificial Intelligence"
        )
        st.write("**Bachelor’s Degree in Artificial Intelligence**, Class of 2026")

        st.markdown("---")

        st.subheader("Professional Certifications – Coursera (Selected)")
        st.write("""
        - Data Analysis
        - Databases
        - Machine Learning
        - Deep Learning
        - Data Science
        """)

    def render_achievements(self):
        """Render achievements section"""
        st.header("My Achievements")
        for achievement in self.achievements:
            st.markdown(f"- {achievement}")

    def render_testimonials(self):
        """Render testimonials section"""
        st.header("Client Testimonials")

        # Create grid layout - 3 columns per row
        for i in range(0, len(self.testimonials), 3):
            cols = st.columns(3)

            for j in range(3):
                if i + j < len(self.testimonials):
                    testimonial = self.testimonials[i + j]

                    with cols[j]:
                        # Testimonial card
                        with st.container():
                            col1, col2 = st.columns([3, 1])
                            with col1:
                                st.subheader(testimonial["client_name"])
                            with col2:
                                st.write(testimonial["rating"])
                            
                            st.write(f"**Location:** {testimonial['location']}")
                            st.write(f"**Project:** {testimonial['project_name']}")
                            st.write(f"**Cost:** {testimonial['project_cost']}")
                            st.write(f"**Duration:** {testimonial['project_duration']}")
                            if st.button("View Rating", key=f"view_rating_{i+j}", use_container_width=True):
                                # Define action for the button, e.g., switch page or show modal
                                pass

                        st.markdown("---")

    def run(self):
        """Main method to run the app"""
        self.render_header()
        self.render_tabs()


# =============================================================================
# MAIN APPLICATION
# =============================================================================
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
        </style>
    '''
    st.markdown(hide_img_fs, unsafe_allow_html=True)

    portfolio.run()


# =============================================================================
# RUN
# =============================================================================
if __name__ == "__main__":
    main()
