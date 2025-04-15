import streamlit as st
import urllib.parse

# Page configuration
st.set_page_config(page_title="Wedding of Anton and Peniel", layout="wide")

# Custom CSS for fixed background and scroll effects
st.markdown("""
    <style>
        body {
            background-image: url('A+P.jpg');
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            background-repeat: no-repeat;
            font-family: 'Helvetica', sans-serif;
        }

        .title-block {
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            color: white;
            font-size: 3em;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.7);
        }

        .content-block {
            background-color: rgba(255, 255, 255, 0.8);
            padding: 3rem;
            border-radius: 12px;
            max-width: 700px;
            margin: auto;
            margin-top: -80px;
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

# Title block that fills the screen
st.markdown('<div class="title-block">Wedding of Anton and Peniel</div>', unsafe_allow_html=True)

# Main content
st.markdown('<div class="content-block">', unsafe_allow_html=True)

st.markdown("""
### You're Invited 💒

Join us to celebrate our love and the beginning of a lifetime together.  

**📅 Date**: 22nd November  
**📍 Location**: St John's Anglican Church, Fremantle

**⏰ Time**: 10am 

We can't wait to share this beautiful moment with you.
""")

# RSVP Button Setup
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
