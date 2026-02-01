import streamlit as st
import random
import time

# =========================
# CONFIGURATION
# =========================
PAGE_TITLE = "you will be my valentine!"
PAGE_ICON = "💖"
MAX_CLICKS = 14

# ------------------------------------------------------
# 📷 PASTE YOUR GIF LINKS HERE
# ------------------------------------------------------

MAIN_GIF = "https://media.tenor.com/wIx44jsp4DMAAAAi/kiss.gif" 

SUCCESS_GIF = "https://media.tenor.com/OrxXcqX25KcAAAAi/dudu-bubu-love-gif.gif"
# ------------------------------------------------------

NOTES = [
    "You are sure!",
    "This is our first valentine's day together",
    "I promise it will be happy",
    "Because you make me so happy",
    "And I wanted to make it special",
    "Almost there…",
    "asim",
    "bantot",
    "impakta",
    "wala nang bawian to!!",
    "wala ka nang magagawa",
    "its me your lovie dovie boyfriend",
    "i love you from my hypothalamus",
    "mwaaaaaaaaaaa mwaaaaaaaaaaa"
]

# =========================
# PAGE SETUP
# =========================
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="centered",
)

# =========================
# STATE MANAGEMENT
# =========================
if "yes_clicks" not in st.session_state:
    st.session_state.yes_clicks = 0

if "btn_top" not in st.session_state:
    st.session_state.btn_top = 50
    st.session_state.btn_left = 50

# =========================
# STYLING
# =========================
st.markdown("""
<style>
/* Gradient background */
body {
    background: radial-gradient(circle at center, #ffb6c1 40%, #8a2be2 70%, #00bfff 100%);
    font-family: 'Segoe UI', sans-serif;
    overflow: hidden;
    margin: 0;
}

/* Center card */
.card {
    background: rgba(255, 255, 255, 0.25);
    padding: 2.5rem;
    border-radius: 24px;
    text-align: center;
    max-width: 450px;
    margin: 5% auto;
    color: white;
    backdrop-filter: blur(10px);
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
}

/* --- UPDATED IMAGE STYLING FOR CENTERING --- */
.card-img {
    display: block;           /* Ensures it behaves like a block element */
    margin-left: auto;        /* Auto margin on left */
    margin-right: auto;       /* Auto margin on right centers it */
    margin-bottom: 20px;      /* Keep the bottom spacing */
    border-radius: 15px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    max-width: 100%;
}
/* ------------------------------------------- */

/* General Button Style */
div.stButton > button {
    border-radius: 50px;
    background-color: #ff69b4;
    color: white;
    font-weight: bold;
    border: 2px solid white;
    box-shadow: 0px 0px 15px rgba(255, 105, 180, 0.7);
    transition: all 0.5s ease;
}
</style>
""", unsafe_allow_html=True)

# =========================
# CARD UI
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)

# LOGIC: Show Main GIF while playing, Success GIF when done
if st.session_state.yes_clicks < MAX_CLICKS:
    # 1. THE MAIN GIF
    st.markdown(f"<img src='{MAIN_GIF}' class='card-img' width='250'>", unsafe_allow_html=True)
    st.markdown("<h1>❤️You will Be My Valentine!❤️</h1>", unsafe_allow_html=True)
    st.markdown("<h2>🎀First ever valentine's day together🎀</h2>", unsafe_allow_html=True)
    st.markdown(f"<h2>{NOTES[st.session_state.yes_clicks]}</h2>", unsafe_allow_html=True)

else:
    # 2. THE SUCCESS GIF
    st.balloons()
    st.markdown(f"<img src='{SUCCESS_GIF}' class='card-img' width='300'>", unsafe_allow_html=True)
    st.markdown("""
    <h1>🎉 IT’S A DATE 🎉</h1>
    <h2>💞 Thank you for saying YES 💞</h2>
    <h3>💙💜 I can’t wait to spend Valentine’s with you 💙💜</h3>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# FLOATING BUTTON LOGIC
# =========================
if st.session_state.yes_clicks < MAX_CLICKS:

    font_size = 22 + (st.session_state.yes_clicks * 2)
    padding_y = 12 + (st.session_state.yes_clicks * 2)
    padding_x = 24 + (st.session_state.yes_clicks * 4)

    top_pos = st.session_state.btn_top
    left_pos = st.session_state.btn_left

    pos_type = "relative" if st.session_state.yes_clicks == 0 else "fixed"

    st.markdown(f"""
    <style>
    div.stButton > button {{
        position: {pos_type} !important;
        top: {top_pos}% !important;
        left: {left_pos}% !important;
        font-size: {font_size}px !important;
        padding: {padding_y}px {padding_x}px !important;
        height: auto !important;
        width: auto !important;
        white-space: nowrap !important;
        z-index: 9999;
        transition: all 0.5s ease;
    }}
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        if st.button(f"YES ❤️", key="yes_button"):
            st.session_state.yes_clicks += 1
            st.session_state.btn_top = random.randint(10, 80)
            st.session_state.btn_left = random.randint(10, 80)
            st.rerun()
