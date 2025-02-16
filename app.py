import streamlit as st
from streamlit_option_menu import option_menu
import importlib
import sqlite3


# Page configuration
st.set_page_config(
    page_title="Hongmei's Portfolio",
    page_icon="desktop_computer",
    layout="wide",
    initial_sidebar_state="auto",
)

# Add custom CSS for sidebar width and length
st.markdown(
    """
    <style>
        /* Adjust the sidebar width and length */
        [data-testid="stSidebar"] {
            width: 300px; /* Width of the sidebar */
            height: 100%; /* Full height */
        }

        /* Sidebar container styling */
        .css-1d391kg { 
            padding: 0;
        }

        /* Sidebar content alignment */
        [data-testid="stSidebar"] .css-1d391kg {  
            background-color: #48AAAD; /* Harmonized custom background color */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar menu
with st.sidebar:
    choose = option_menu(
        "Hongmei Jian Roy",
        [
            "Chatbot",
            "About Me",
            "Experience",
            "Technical Skills",
            "Education",
            "Certifications",
            "Projects",
            "Contact",
        ],
        icons=[
            "robot",
            "person fill",
            "clock history",
            "tools",
            "book half",
            "clipboard",
            "trophy fill",
            "envelope",
        ],
        menu_icon="mortarboard",
        default_index=0,
        styles={
            "container": {
                "padding": "5px",  # Padding around the menu container
                "background-color": "#48AAAD",  # Sidebar background color
                "width": "300px",  # Sidebar width
            },
            "icon": {
                "color": "#FFD700",  # Golden icon color
                "font-size": "24px",  # Slightly larger icon size
            },
            "nav-link": {
                "font-size": "18px",  # Larger font size for better readability
                "text-align": "left",
                "margin": "5px",  # Adequate spacing between menu items
                "color": "#FFFFFF",  # White text for better visibility
                "--hover-color": "#2E3A46",  # Slightly darker hover background
            },
            "nav-link-selected": {
                "background-color": "#A41117",  # Highlighted background
                "color": "#FFD700",  # Golden text color for selected link
                "font-size": "18px",  # Same font size for consistency
            },
        },
    )

    # Social media links
    st.markdown(
        """
        <div style='text-align: center; padding: 10px;'>
            <a href='https://www.linkedin.com/in/hongmei-jian-roy-ab35471b0' target='_blank' 
               style='display: inline-block; background-color: #48AAAD; border-radius: 50%; padding: 10px; margin: 5px;'>
                <img src='https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png' 
                width='30' style='margin: 0;'>
            </a>
            <a href='https://github.com/homemadejam16' target='_blank' 
               style='display: inline-block; background-color: #48AAAD; border-radius: 50%; padding: 10px; margin: 5px;'>
                <img src='https://upload.wikimedia.org/wikipedia/commons/2/24/Github_logo_svg.svg' 
                width='30' style='margin: 0;'>
            </a>
            <a href='mailto:homemadejam16@gmail.com' target='_blank' 
               style='display: inline-block; background-color: #48AAAD; border-radius: 50%; padding: 10px; margin: 5px;'>
                <img src='https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png' 
                width='30' style='margin: 0;'>
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Map selection to modules
pages = {
    "Chatbot": "subpages.home",
    "About Me": "subpages.about_me",
    "Experience": "subpages.experience",
    "Technical Skills": "subpages.technical_skills",
    "Education": "subpages.education",
    "Certifications": "subpages.certifications",
    "Projects": "subpages.projects",
    "Contact": "subpages.contact",
}

# Dynamically load and display the selected page
page_module = pages.get(choose)
if page_module:
    module = importlib.import_module(page_module)
    module.show_page()