import streamlit as st
import random

# =========================
# CONFIGURATION
# =========================
PAGE_TITLE = "Valentine’s Invitation"
PAGE_ICON = "💖"
MAX_CLICKS = 4

NOTES = [
    "💖 Are you sure?",
    "💙 I promise it will be special",
    "💜 Almost there…",
    "💌 No turning back now"
]

# =========================
# PAGE SETUP
# =========================
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="wide"
)

# =========================
# STATE MANAGEMENT
# =========================
if "yes_clicks" not in st.session_state:
    st.session_state.yes_clicks = 0
if "x_pos" not in st.session_state:
    st.session_state.x_pos = 0
if "y_pos" not in st.session_state:
    st.session_state.y_pos = 0

# =========================
# CARD STYLING
# =========================
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #ffb6c1, #00bfff, #8a2be2);
    font-family: 'Segoe UI', sans-serif;
}
.card {
    background: rgba(255, 255, 255, 0.15);
    padding: 2rem;
    border-radius: 24px;
    text-align: center;
    max-width: 500px;
    margin: 5% auto;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    color: white;
}
h1, h2 {
    margin: 0.5rem 0;
}
div.stButton > button {
    border-radius: 50px;
    background-color: #ff69b4;
    color: white;
    font-weight: bold;
    transition: all 0.3s ease;
    box-shadow: 0 5px 20px rgba(0,0,0,0.2);
}
div.stButton > button:hover {
    background-color: #ff85c1;
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# =========================
# UI CARD
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
# FLOATING YES BUTTON (CLICKABLE)
# =========================
if st.session_state.yes_clicks < MAX_CLICKS:
    # Randomize position each render
    st.session_state.x_pos = random.randint(0, 70)
    st.session_state.y_pos = random.randint(0, 70)

    # Button grows with clicks
    font_size = 22 + st.session_state.yes_clicks * 10
    padding_y = 12 + st.session_state.yes_clicks * 5
    padding_x = 32 + st.session_state.yes_clicks * 10

    # Render the clickable Streamlit button in a container
    button_html = f"""
    <div style='position:absolute; left:{st.session_state.x_pos}vw; top:{st.session_state.y_pos}vh;'>
        <form method="post">
            <button type="submit" style="
                font-size:{font_size}px; 
                padding:{padding_y}px {padding_x}px;">
                YES ❤️
            </button>
        </form>
    </div>
    """
    st.markdown(button_html, unsafe_allow_html=True)

    # Use Streamlit’s st.button with unique key to capture click
    if st.button("💖", key="hidden_button"):
        st.session_state.yes_clicks += 1
