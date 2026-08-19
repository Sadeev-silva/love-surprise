"""
Streamlit wrapper for the Love Surprise experience.

The whole experience lives in index.html (a single self-contained file).
This script simply serves it inside Streamlit so the project can be
deployed free on Streamlit Community Cloud straight from GitHub.

If a music.mp3 file exists next to this script, it is embedded into the
page as a base64 data URI so the play button produces real audio.
(You must supply your own legally obtained audio file — none ships with
this project.)
"""

import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="A Little Surprise 💌",
    page_icon="💌",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit chrome so the experience fills the page.
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      iframe {border: none;}
    </style>
    """,
    unsafe_allow_html=True,
)

APP_DIR = Path(__file__).parent
html = (APP_DIR / "index.html").read_text(encoding="utf-8")

# Optional: embed music.mp3 if the user has added one to the repo.
music = APP_DIR / "music.mp3"
if music.exists():
    b64 = base64.b64encode(music.read_bytes()).decode()
    html = html.replace('src="music.mp3"', f'src="data:audio/mpeg;base64,{b64}"')

# Height of the embedded experience. Increase if content is clipped.
components.html(html, height=760, scrolling=False)
