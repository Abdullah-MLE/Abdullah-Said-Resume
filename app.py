import streamlit as st
import json
from datetime import datetime


class Portfolio:
    def __init__(self):
        self.projects = self.load_data('data/projects.json')
        self.services = self.load_data('data/services.json')
        self.testimonials = sorted(
            self.load_data('data/testimonials.json'),
            key=lambda x: datetime.fromisoformat(x['timestamp']),
            reverse=True
        )
        self.education = self.load_data('data/education.json')
        self.contact_info = self.load_data('data/contact_info.json')

    def load_data(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)

    def render_header(self):
        st.title("Abdullah Said Portfolio")

    def _render_contact_details(self):
        st.header("Get in Touch")
        st.write(
            "I'm always open to discussing new opportunities and "
            "interesting projects. Feel free to reach out!"
        )
        st.write(f'📧 Email: {self.contact_info["email"]}')
        st.write(f'📱 Phone: {self.contact_info["phone"]}')
        st.write(f'📍 Location: {self.contact_info["location"]}')

        st.subheader("Social Media")
        st.write(
            f'- [WhatsApp]({self.contact_info["whatsapp"]})\n'
            f'- [LinkedIn]({self.contact_info["LinkedIn"]})\n'
            f'- [GitHub]({self.contact_info["GitHub"]})\n'
            f'- [Twitter]({self.contact_info["Twitter"]})\n'
            f'- [Personal Website]({self.contact_info["Personal Website"]})\n'
        )

    def render_sidebar(self):
        with st.sidebar:
            self._render_contact_details()

    def render_tabs(self):
        tabs = st.tabs([
            "About", "Services", "Projects", "Testimonials", "Education",
            "Contact"
        ])

        with tabs[0]:
            self.render_about()

        with tabs[1]:
            self.render_services()

        with tabs[2]:
            self.render_projects()

        with tabs[3]:
            self.render_testimonials()

        with tabs[4]:
            self.render_education()

        with tabs[5]:
            self.render_contact()

    def render_about(self):
        st.header("About Me")
        col1, col2 = st.columns([2, 1])
        with col1:
            st.write("""
                Hello! I'm a passionate software developer with expertise in
                full-stack development and data analysis. I love creating
                innovative solutions that make a real impact.

                With 5+ years of experience in the tech industry, I've
                worked on various projects ranging from web applications to
                machine learning models. I'm always eager to learn new
                technologies and take on challenging projects.

                When I'm not coding, you can find me exploring new
                technologies, contributing to open-source projects, or
                enjoying outdoor activities.
            """)
        with col2:
            st.image("assets/profile.png")

        st.write("---")
        self.render_skills()

    def render_services(self):
        st.header("My Services")
        for i in range(0, len(self.services), 4):
            cols = st.columns(4)
            for j in range(4):
                if i + j < len(self.services):
                    service = self.services[i + j]
                    with cols[j]:
                        with st.container(border=True):
                            st.image(
                                service["image"], use_container_width='always'
                            )
                            st.subheader(service["title"])
                            st.write(service["description"])
                            button_cols = st.columns(2)
                            with button_cols[0]:
                                if st.button("Show More",
                                             key=f"show_more_{i+j}",
                                             use_container_width=True):
                                    page = f"pages/service_{service['page']}"
                                    st.switch_page(page)
                            with button_cols[1]:
                                st.link_button(
                                    "Order Now",
                                    url=self.contact_info["whatsapp"],
                                    use_container_width=True
                                )
            st.markdown("---")

    def render_projects(self):
        st.header("My Projects")
        for i in range(0, len(self.projects), 4):
            cols = st.columns(4)
            for j in range(4):
                if i + j < len(self.projects):
                    project = self.projects[i + j]
                    with cols[j]:
                        with st.container(border=True):
                            st.image(project["image"],
                                     use_container_width='always')
                            st.subheader(project["title"])
                            st.write(project["description"])
                            tech_tags = " ".join(
                                [f"`{tech}`" for tech in project["tech"]]
                            )
                            st.markdown(tech_tags)
                            button_cols = st.columns(2)
                            with button_cols[0]:
                                st.link_button(
                                    "Show Live",
                                    url=project["show_live_url"],
                                    use_container_width=True
                                )
                            with button_cols[1]:
                                st.link_button(
                                    "GitHub",
                                    url=project["github_url"],
                                    use_container_width=True
                                )
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

        st.subheader("University")
        for edu in self.education['university']:
            st.markdown(f'''
                <a href="{edu['url']}" style="text-decoration: none; color: inherit;">
                    <h4 style="margin-bottom: 0;">{edu['name']}</h4>
                </a>
                ''',
                unsafe_allow_html=True
            )
            st.write(f"**{edu['degree']}**")


        st.write("---")

        st.subheader("Professional Certifications")
        for cert in self.education['professional_certifications']:
            st.markdown(f'''
                <a href="{cert['url']}" style="text-decoration: none; color: inherit;">
                    <h4 style="margin-bottom: 0;">{cert['name']}</h4>
                </a>
                <small>Issued by <strong>{cert['issuer']}</strong> in {cert['date']}</small>
                ''',
                unsafe_allow_html=True
            )

        st.write("---")

        st.subheader("Other Certificates")
        for cert in self.education['other_certificates']:
            st.markdown(f'''
                <a href="{cert['url']}" style="text-decoration: none; color: inherit;">
                    <h4 style="margin-bottom: 0;">{cert['name']}</h4>
                </a>
                <small>Issued by <strong>{cert['issuer']}</strong> in {cert['date']}</small>
                ''',
                unsafe_allow_html=True
            )

    def render_testimonials(self):
        st.header("Client Testimonials")
        for testimonial in self.testimonials:
            with st.container(border=True):
                st.subheader(testimonial["client_name"])
                st.markdown(
                    f"**{testimonial['project_name']}**     "
                    f"{testimonial['rating']}"
                )

                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.write(f"**Platform:** {testimonial['location']}")
                with col2:
                    st.write(f"**Cost:** {testimonial['project_cost']}")
                with col3:
                    st.write(
                        f"**Duration:** {testimonial['project_duration']}"
                    )
                with col4:
                    st.link_button("View Testimonial", testimonial["link"])
            st.markdown("---")

    def render_contact(self):
        self._render_contact_details()
        st.subheader("Hire me on freelance platforms")
        freelance_links = ""
        for platform, url in self.contact_info["freelance_platforms"].items():
            freelance_links += f"- [{platform}]({url})\n"
        st.write(freelance_links)

    def run(self):
        self.render_sidebar()
        self.render_header()
        self.render_tabs()


def main():
    st.set_page_config(
        page_title="My Portfolio",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    st.markdown("""
        <style>
            [data-testid="stSidebarNav"] {
                display: none;
            }
        </style>
    """, unsafe_allow_html=True)

    portfolio = Portfolio()

    portfolio.run()


if __name__ == "__main__":
    main()
