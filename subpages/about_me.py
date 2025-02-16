import streamlit as st

# Add custom CSS for styling
st.markdown(
    """
    <style>
        /* Style the content of the left column */
        .left-column {
            font-family: Arial, sans-serif;
            font-size: 16px;
            line-height: 1.6;
            color: #333333;
            text-align: justify;
        }

        /* Style the content of the right column */
        .right-column {
            background-color: #e6f7ff;
            border-radius: 10px;
            padding: 20px;
        }

        /* Style the header */
        .title {
            font-family: Arial, sans-serif;
            font-size: 36px;
            font-weight: bold;
            color: #1f4e79;
        }

        /* Add padding around the image */
        img {
            border-radius: 10px;
            margin-bottom: 20px;
        }

    </style>
    """,
    unsafe_allow_html=True
)


def show_page():
    # Title section with custom CSS class
    st.markdown("<h1 class='title'>About Me</h1>", unsafe_allow_html=True)
    st.write("Hongmei, a passionate Machine Learning and AI engineer.")

    # Adjust column widths
    left_column, right_column = st.columns([3, 1])

    # Left Column Content
    with left_column:
        st.markdown(
            """
            <div class="left-column">
                Hello! I'm Hongmei Jian Roy, and I'm absolutely passionate about artificial intelligence. 
                The ever-evolving field of AI captivates me, not just as a career path but as a fascinating journey 
                into the future. Witnessing AI transform industries, enhance everyday life, and solve complex problems 
                is a constant source of inspiration.
                <br><br>
                My skillset spans various areas, including machine learning, natural language processing, and computer vision. 
                Proficient in programming languages such as Python and Java, I also have hands-on experience with frameworks 
                like TensorFlow and PyTorch. Whether developing intelligent algorithms or fine-tuning models, I thrive on 
                tackling challenging projects and pushing the boundaries of what's possible with AI. I'm a lifelong learner, 
                with a curious mind, a love for tech, and a relentless drive to broaden my horizons and fuel my creativity.
                <br><br>
                Beyond the world of tech, I have a few hobbies that keep my life balanced and exciting. I enjoy walking in 
                the mountains and by lakes, as it provides a refreshing break from the screen and a chance to connect with nature. 
                Listening to music and dancing with the flow are integral parts of my life. My interests also extend to fashion, 
                Eastern medicine, and ancient philosophy, which I find endlessly fascinating.
                <br><br>
                Feel free to reach out if you'd like to chat more about AI, share insights, or even recommend a good book or hiking trail!
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Right Column Content
    with right_column:
        st.markdown(
            """
            <div class="right-column">
                <!-- This space can be used for styling -->
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.image(r"images/jane.jpg", use_column_width=True)


