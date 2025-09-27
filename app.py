import streamlit as st
import json
from datetime import datetime


class Portfolio:
    def __init__(self):
        self.projects = self.load_data('data/projects.json')
        self.services = self.load_data('data/services.json')
        self.testimonials = self.load_data('data/testimonials.json')
        self.education = self.load_data('data/education.json')
        self.contact_info = self.load_data('data/contact_info.json')
        self.content = self.load_data('data/content.json')

    def load_data(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)

    def render_header(self):
        st.title(self.content['header']['title'])

    def _render_contact_details(self):
        st.header(self.content['get_in_touch']['title'])
        st.write(
            self.content['get_in_touch']['description']
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
        st.header(self.content['about']['header'])
        col1, col2 = st.columns([2, 1])
        with col1:
            st.write(self.content['about']['text'])
        with col2:
            st.image("assets\personal_photos\profile.png")

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

    def _render_projects_by_category(self, category):
        filtered_projects = [p for p in self.projects if p.get("Category") == category]

        for i in range(0, len(filtered_projects), 4):
            cols = st.columns(4)
            for j in range(4):
                if i + j < len(filtered_projects):
                    project = filtered_projects[i + j]
                    with cols[j]:
                        with st.container(border=True):
                            st.image(project["image"], use_container_width='always')
                            st.subheader(project["title"])
                            st.write(project["description"] if "description" in project else "")

                            # Tags
                            tech_tags = " ".join([f"`{tech}`" for tech in project["tech"]])
                            st.markdown(tech_tags)

                            # Buttons
                            if project["show_live_url"] != "#":
                                button_cols = st.columns(2)

                                # Show Live (only if url != "#")
                                with button_cols[0]:
                                    st.link_button(
                                        "Show Live",
                                        url=project["show_live_url"],
                                        use_container_width=True
                                    )

                                # Source
                                if project["Source_url"] != "#":
                                    with button_cols[1]:
                                        st.link_button(
                                            "Source",
                                            url=project["Source_url"],
                                            use_container_width=True
                                        )
                            elif project["Source_url"] != "#":
                                st.link_button(
                                    "Source",
                                    url=project["Source_url"],
                                    use_container_width=True
                                )

            st.markdown("---")

    def render_projects(self):
        st.header("My Projects")

        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["AI", "Automation", "Data Analysis", "Web Scraping", "ML & Data Science", "Deep Learning", "Websites"])

        with tab1:
            st.subheader("AI Projects")
            self._render_projects_by_category("ai")

        with tab2:
            st.subheader("Automation Projects")
            self._render_projects_by_category("automation")

        with tab3:
            st.subheader("EDA, Dashbords, Data Analysis, Data Cleaning and Data Visualization Projects")
            self._render_projects_by_category("data_analysis")

        with tab4:
            st.subheader("Web Scraping Projects")
            self._render_projects_by_category("web_scraping")

        with tab5:
            st.subheader("ML & Data Science Projects")
            self._render_projects_by_category("ml_data_science")

        with tab6:
            st.subheader("Deep Learning Projects")
            self._render_projects_by_category("deep_learning")

        with tab7:
            st.subheader("Websites")
            self._render_projects_by_category("websites")

    def render_skills(self):
        st.header(self.content['skills']['header'])
        categories = self.content['skills']['categories']
        col1, col2, col3 = st.columns(3)
        cols = [col1, col2, col3]
        for i, category in enumerate(categories):
            with cols[i]:
                st.subheader(category['title'])
                st.write("\n".join([f"- {item}" for item in category['items']]))

    def render_education(self):
        st.header("Education")

        tab1, tab2, tab3 = st.tabs(["University", "Professional Certificate", "Achievements"])

        with tab1:
            st.subheader("University")
            for edu in self.education['university']:
                with st.container(border=True):
                    col1, col2 = st.columns([1, 4])
                    with col1:
                        if edu['image']:
                            st.image(edu['image'], use_container_width='always')
                    with col2:
                        st.write(f"**{edu['name']}**")
                        st.write(edu['degree'])

        with tab2:
            st.subheader("Professional Certificate")
            for cert in self.education['Professional Certificate']:
                with st.container(border=True):
                    col1, col2 = st.columns([1, 4])
                    with col1:
                        if cert['image']:
                            st.image(cert['image'], use_container_width='always')
                    with col2:
                        st.markdown(f"**<a href='{cert['url']}' style='color: #ADD8E6;'>{cert['name']}</a>**", unsafe_allow_html=True)
                        st.markdown(f"<small>Issued by <strong>{cert['issuer']}</strong> in {cert['date']}</small>", unsafe_allow_html=True)
                        st.markdown(f"<small>{cert['hours']}</small>", unsafe_allow_html=True)

        with tab3:
            st.subheader("Achievements")
            for cert in self.education['achievements']:
                with st.container(border=True):
                    col1, col2 = st.columns([1, 4])
                    with col1:
                        if cert['image']:
                            st.image(cert['image'], use_container_width='always')
                    with col2:
                        st.markdown(f"**<a href='{cert['url']}' style='color: #ADD8E6;'>{cert['name']}</a>**", unsafe_allow_html=True)
                        st.markdown(f"<small>Issued by <strong>{cert['issuer']}</strong> in {cert['date']}</small>", unsafe_allow_html=True)
                        st.markdown(f"<small>{cert['hours']}</small>", unsafe_allow_html=True)
    
    def render_testimonials(self):
        st.header("Client Testimonials")
        for testimonial in self.testimonials:
            with st.container(border=True, width="stretch"):
                # Client name + position
                st.markdown(
                    f"### {testimonial['client_name']}  "
                    f"<span style='font-size:14px; color:gray;'>({testimonial.get('position', '')})</span>",
                    unsafe_allow_html=True
                )

                # Project name + rating in columns
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"**Project:** {testimonial['project_name']}")
                with col2:
                    st.markdown(f"**Rating:** {testimonial['rating']}")

                # Platform, Cost, Duration in columns
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown(f"**Platform:** {testimonial['location']}")
                with col2:
                    st.markdown(f"**Cost:** {testimonial['project_cost']}")
                with col3:
                    st.markdown(f"**Duration:** {testimonial['project_duration']}")

                # Testimonial message
                col1, col2, col3 = st.columns([1, 4, 1])
                with col2:
                    st.markdown(f"*\"{testimonial['message']}\"*")

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
