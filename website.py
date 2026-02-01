import streamlit as st
import random

# =========================
# CONFIGURATION
# =========================
PAGE_TITLE = "you will be my valentine!"
PAGE_ICON = "💖"
MAX_CLICKS = 10

NOTES = [
    "You are sure!",
    "This is our first valentine's day together",
    "I promise it will be happy",
    "Because you make me so happy",
    "And I wanted to make it special",
    "Almost there…",
    "asim",
     "bantot",
    "wala nang bawian to!!",
    "i love you from my hypothalamus" 
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
# STATE
# =========================
if "yes_clicks" not in st.session_state:
    st.session_state.yes_clicks = 0

# =========================
# STYLING
# =========================
st.markdown("""
<style>
/* Gradient background: pink center, violet & blue sides */
body {
    background: radial-gradient(circle at center, #ffb6c1 40%, #8a2be2 70%, #00bfff 100%);
    font-family: 'Segoe UI', sans-serif;
    overflow-x: hidden;
    overflow-y: auto;
    margin: 0;
}

/* Center card */
.card {
    background: rgba(255, 255, 255, 0.15);
    padding: 2.5rem;
    border-radius: 24px;
    text-align: center;
    max-width: 450px;
    margin: 8% auto;
    color: white;
}

/* Headings */
h1, h2 {
    margin: 0.5rem 0;
}

/* YES button */
div.stButton > button {
    border-radius: 50px;
    background-color: #ff69b4;
    color: white;
    font-weight: bold;
    transition: all 0.3s ease;
}

div.stButton > button:hover {
    background-color: #ff85c1;
    transform: scale(1.05);
}

/* Mobile responsiveness */
@media (max-width: 480px) {
    div.stButton > button {
        font-size: 20px !important;
        padding: 12px 32px !important;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================
# CARD UI
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<h1>💖 Will You Be My Valentine?</h1>", unsafe_allow_html=True)
st.markdown("<h2>💖 💙 💜 💌 💍</h2>", unsafe_allow_html=True)

if st.session_state.yes_clicks < MAX_CLICKS:
    st.markdown(f"<h2>{NOTES[st.session_state.yes_clicks]}</h2>", unsafe_allow_html=True)
else:
    st.balloons()
    st.markdown("""
    <h1>🎉 IT’S A DATE 🎉</h1>
    <h2>💞 Thank you for saying YES 💞</h2>
    <h3>💖💙💜 I can’t wait to spend Valentine’s with you 💖💙💜</h3>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
# =========================
# YES BUTTON (CENTERED)
# =========================
if st.session_state.yes_clicks < MAX_CLICKS:
    font_size = 22 + st.session_state.yes_clicks * 10
    padding_y = 12 + st.session_state.yes_clicks * 5
    padding_x = 32 + st.session_state.yes_clicks * 10

    # Centered button
    st.markdown("<div style='display:flex; justify-content:center; margin-top:2rem;'>", unsafe_allow_html=True)
    # Only ONE real button, no extra hidden buttons
    if st.button(f"YES ❤️", key="yes_button"):
        st.session_state.yes_clicks += 1
    st.markdown("</div>", unsafe_allow_html=True)


