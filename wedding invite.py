import streamlit as st
import urllib.parse

# Page configuration
st.set_page_config(page_title="Wedding of Anton and Peniel", layout="wide")

# Custom CSS with cursive font and background setup
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');

        html, body, .stApp {
            height: 100%;
            margin: 0;
            font-family: 'Helvetica', sans-serif;
        }

        .stApp {
            background-image: url("https://files.catbox.moe/mkqxur.jpg");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            background-repeat: no-repeat;
        }

        .title-block {
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            color: white;
            font-size: 3em;
            text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.7);
            font-family: 'Great Vibes', cursive;
        }

        .title-line1 {
            align-self: flex-start;
            margin-left: 15%;
        }

        .title-line2 {
            align-self: flex-end;
            margin-right: 15%;
        }

        .content-block {
            background-color: rgba(255, 255, 255, 0);
            padding: 3rem;
            max-width: 700px;
            margin: auto;
            margin-top: -100px;
            color: white;
            font-size: 1.2rem;
            text-align: center;
            text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.8);
        }

        .rsvp-button a {
            background-color: #f63366;
            color: white;
            padding: 0.75rem 2rem;
            border-radius: 30px;
            text-decoration: none;
            font-weight: bold;
            display: inline-block;
            margin-top: 1.5rem;
        }

        .rsvp-button a:hover {
            background-color: #d61c4e;
        }
    </style>
""", unsafe_allow_html=True)

# Title block
st.markdown("""
    <div class="title-block">
        <div class="title-line1">Wedding of</div>
        <div class="title-line2">Anton & Peniel</div>
    </div>
""", unsafe_allow_html=True)

# Main content block
st.markdown('<div class="content-block">', unsafe_allow_html=True)

st.markdown("""
### You're Invited 💒

Join us to celebrate our love and the beginning of a lifetime together.  

**📅 Date**: 22nd November  
**📍 Location**: St John's Anglican Church, Fremantle  
**⏰ Time**: 10am  

We can't wait to share this beautiful moment with you.
""")

# RSVP mailto link
rsvp_subject = urllib.parse.quote("Wedding RSVP")
rsvp_body = urllib.parse.quote("Hi Anton and Peniel,\n\nI would love to RSVP to your wedding!\n\n[Your Message Here]")
mailto_link = f"mailto:anton.haruk@gmail.com?subject={rsvp_subject}&body={rsvp_body}"

# RSVP Button
st.markdown(f'''
<div class="rsvp-button">
    <a href="{mailto_link}" target="_blank">📩 RSVP via Email</a>
</div>
''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
