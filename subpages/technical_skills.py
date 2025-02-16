from streamlit_pills import pills
import json
import streamlit as st


# Add custom CSS to reset default font size and harmonize styles
st.markdown(
    """
    <style>
    /* Reset font sizes for a clean look */
    html, body, [class*="streamlit"] {
        font-size: 16px;
        font-family: 'Arial', sans-serif;
    }
    h1 {
        font-size: 28px !important;
        color: #4CAF50;
        margin-bottom: 10px;
    }
    h2 {
        font-size: 22px !important;
        color: #444;
        margin-bottom: 8px;
    }
    .stMarkdown {
        color: #333;
        line-height: 1.6;
        font-size: 16px;
        margin-top: 0;
    }
    .stRadio > div {
        flex-wrap: wrap;
    }
    /* Adjust column padding for cleaner alignment */
    .block-container {
        padding: 1rem 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Main function
def show_page():
    # Load technical skills data from the JSON file
    with open(r'data/technical_skills.json') as file:
        technical_skills = json.load(file)

    # Extract skill names and descriptions from the data
    skills = [skill["name"] for skill in technical_skills["skills"]]

    # Create a two-column layout (balanced width)
    left_column, right_column = st.columns([2, 3])

    with left_column:
        st.title("Technical Skills")
        # Use pills to allow users to select a category
        selected = pills("Select a skill", skills)

    with right_column:
        st.title("Skill Description")
        # Display the selected skill's description dynamically
        for skill in technical_skills["skills"]:
            if skill["name"] == selected:
                st.markdown(f"### {skill['name']}")
                st.markdown(skill["description"])
