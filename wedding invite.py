import streamlit as st
import urllib.parse

# Page configuration
st.set_page_config(page_title="Wedding of Anton and Peniel", layout="wide")

# Load background image and fonts
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');

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
            flex-direction: column;
            justify-content: center;
            align-items: flex-start;
            color: white;
            padding-left: 10vw;
            padding-right: 10vw;
            text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.7);
        }

        .title-line-1 {
            font-size: 4em;
            margin: 0;
            font-family: 'Great Vibes', cursive;
            align-self: flex-start;
        }

        .title-line-2 {
            font-size: 5em;
            margin: 0;
            font-family: 'Great Vibes', cursive;
            align-self: flex-end;
        }

        .content-block {
            background-color: rgba(255, 255, 255, 0.85);
            padding: 3rem;
            border-radius: 12px;
            max-width: 700px;
            margin: auto;
            margin-top: -80px;
            font-size: 1.2rem;
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
st.markdown('''
<div class="title-block">
    <h1 class="title-line-1">Wedding of</h1>
    <h1 class="title-line-2">Anton and Peniel</h1>
</div>
''', unsafe_allow_html=True)

# Content block
st.markdown('<div class="content-block">', unsafe_allow_html=True)

st.markdown("""
### You're Invited 💒

Join us to celebrate our love and the beginning of a lifetime together.  

**📅 Date**: 22nd November  
**📍 Location**: St John's Anglican Church, Fremantle  
**⏰ Time**: 10am  

We can't wait to share this beautiful moment with you.
""")

# RSVP setup
rsvp_subject = urllib.parse.quote("Wedding RSVP")
rsvp_body = urllib.parse.quote("Hi Anton and Peniel,\n\nI would love to RSVP to your wedding!\n\n[Your Message Here]")
mailto_link = f"mailto:anton.haruk@gmail.com?subject={rsvp_subject}&body={rsvp_body}"

# RSVP button
st.markdown(f'''
<div class="rsvp-button">
    <a href="{mailto_link}" target="_blank">📩 RSVP via Email</a>
</div>
''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
