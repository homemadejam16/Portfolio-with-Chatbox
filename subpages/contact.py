import streamlit as st


def show_page():
    st.header(":mailbox: Welcome to Contact With Me!")

    # HTML contact form with customized inline styles for alignment and resizing
    contact_form = """
    <form action="https://formsubmit.co/86806d01587674667580d00061ad9f49" method="POST" style="width: 100%;">
        <div style="display: flex; gap: 16px;">
            <input type="text" name="name" placeholder="Your name" required style="flex: 1; padding: 10px; font-size: 14px; border-radius: 5px; border: 1px solid #ccc;">
            <input type="email" name="email" placeholder="Your email" required style="flex: 1; padding: 10px; font-size: 14px; border-radius: 5px; border: 1px solid #ccc;">
        </div>
        <textarea name="message" placeholder="Your message here" style="width: 100%; margin-top: 16px; padding: 10px; font-size: 14px; border-radius: 5px; border: 1px solid #ccc;" rows="5"></textarea>
        <button type="submit" style="margin-top: 16px; padding: 10px 20px; background-color: #1f4e79; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 14px;">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    # Use Local CSS File (Optional, if additional styling is needed)
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css(r"style/style.css")
