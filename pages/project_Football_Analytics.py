import streamlit as st


# =============================================================================
# PROJECT PAGE - FOOTBALL ANALYTICS
# =============================================================================
def render_project_page():
    """Render the football analytics project page"""

    # Image URLs
    HERO_IMG = "https://via.placeholder.com/1200x600/0055FF/FFFFFF?text=Football+Analytics+Dashboard"
    DASHBOARD_IMG = "https://via.placeholder.com/1000x600/1E88E5/FFFFFF?text=Main+Dashboard"
    ANALYSIS_IMG = "https://via.placeholder.com/1000x600/43A047/FFFFFF?text=Match+Analysis"
    PLAYER_IMG = "https://via.placeholder.com/1000x600/E53935/FFFFFF?text=Player+Statistics"
    REPORT_IMG = "https://via.placeholder.com/1000x600/FB8C00/FFFFFF?text=Report+Generation"

    # Back button
    if st.button("← Back to Portfolio"):
        st.switch_page("app.py")

    # Project header
    st.title("Football Analytics Dashboard")
    st.markdown("---")

    # Hero image
    st.image(
        HERO_IMG,
        use_container_width=True,
        caption="Football Analytics Dashboard - Main Interface"
    )

    # Project overview
    st.header("Project Overview")
    st.write("""
    The Football Analytics Dashboard is a comprehensive platform designed to provide 
    in-depth analysis of football matches, player performance, and team statistics. 
    This project leverages advanced data visualization techniques to present complex 
    football data in an intuitive and actionable format.
    """)

    # Key features
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Key Features")
        st.write("""
        - **Real-time Match Analysis**: Live tracking of match statistics and events
        - **Player Performance Metrics**: Detailed individual player analytics
        - **Team Comparison Tools**: Head-to-head team performance analysis
        - **Historical Data Trends**: Season-by-season performance tracking
        - **Predictive Analytics**: Match outcome predictions using ML models
        - **Custom Reports**: Generate detailed PDF reports for matches
        """)

    with col2:
        st.subheader("Technical Stack")
        st.write("""
        - **Frontend**: Streamlit for interactive web interface
        - **Backend**: Python with FastAPI for data processing
        - **Database**: PostgreSQL for storing match data
        - **Data Processing**: Pandas and NumPy for analysis
        - **Visualization**: Plotly and Matplotlib for charts
        - **Machine Learning**: Scikit-learn for predictions
        """)

    st.markdown("---")

    # Screenshots section
    st.header("Screenshots")

    # Create tabs for different views
    tabs = st.tabs(["Dashboard", "Match Analysis", "Player Stats", "Reports"])

    with tabs[0]:
        st.image(
            DASHBOARD_IMG,
            caption="Main Dashboard View",
            use_column_width=True
        )

    with tabs[1]:
        st.image(
            ANALYSIS_IMG,
            caption="Detailed Match Analysis",
            use_column_width=True
        )

    with tabs[2]:
        st.image(
            PLAYER_IMG,
            caption="Individual Player Statistics",
            use_column_width=True
        )

    with tabs[3]:
        st.image(
            REPORT_IMG,
            caption="Custom Report Generation",
            use_column_width=True
        )

    st.markdown("---")

    # Challenges and solutions
    st.header("Challenges & Solutions")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Challenges Faced")
        st.write("""
        1. **Data Quality**: Inconsistent data formats from different sources
        2. **Performance**: Processing large datasets in real-time
        3. **UI/UX**: Making complex data accessible to non-technical users
        4. **Accuracy**: Ensuring prediction models maintain high accuracy
        """)

    with col2:
        st.subheader("Solutions Implemented")
        st.write("""
        1. **Data Pipeline**: Built robust ETL pipeline for data standardization
        2. **Caching**: Implemented smart caching strategies for faster loading
        3. **Interactive Design**: Created intuitive filters and visualizations
        4. **Model Optimization**: Regular model retraining with new data
        """)

    st.markdown("---")

    # Results and impact
    st.header("Results & Impact")

    metrics_col1, metrics_col2, metrics_col3, metrics_col4 = st.columns(4)

    with metrics_col1:
        st.metric("Active Users", "2,500+", "↑ 45%")

    with metrics_col2:
        st.metric("Matches Analyzed", "10,000+", "↑ 120%")

    with metrics_col3:
        st.metric("Prediction Accuracy", "87%", "↑ 12%")

    with metrics_col4:
        st.metric("Reports Generated", "5,000+", "↑ 80%")

    st.write("""
    The Football Analytics Dashboard has revolutionized how coaches, analysts, and fans 
    interact with football data. By providing real-time insights and predictive analytics, 
    the platform has helped teams make data-driven decisions that have improved their 
    performance on the field.
    """)

    st.markdown("---")

    # Links section
    st.header("Links & Resources")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🔗 [Live Demo](https://example.com)")
        st.write("Try the live version of the dashboard")

    with col2:
        st.markdown("### 💻 [GitHub Repository](https://github.com)")
        st.write("View the source code and contribute")

    with col3:
        st.markdown("### 📄 [Documentation](https://docs.example.com)")
        st.write("Detailed technical documentation")


# =============================================================================
# MAIN
# =============================================================================
def main():
    st.set_page_config(
        page_title="Football Analytics - Project",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    render_project_page()


if __name__ == "__main__":
    main()
