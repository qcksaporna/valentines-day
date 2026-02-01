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
    layout="wide",
)

# =========================
# STATE MANAGEMENT
# =========================
if "yes_clicks" not in st.session_state:
    st.session_state.yes_clicks = 0
if "x_pos" not in st.session_state:
    st.session_state.x_pos = 50
if "y_pos" not in st.session_state:
    st.session_state.y_pos = 50

# =========================
# STYLES (RESPONSIVE + AESTHETIC)
# =========================
st.markdown("""
<style>
/* Body background gradient */
body {
    background: linear-gradient(135deg, #ffb6c1, #00bfff, #8a2be2);
    font-family: 'Segoe UI', sans-serif;
    overflow: hidden;
    margin: 0;
}

/* Center card */
.card {
    background: rgba(255, 255, 255, 0.15);
    padding: 2rem;
    border-radius: 24px;
    text-align: center;
    max-width: 500px;
    margin: 5% auto;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}

/* Headings */
h1, h2 {
    color: white;
    margin-bottom: 0.5rem;
}

/* Floating YES button */
#yes-btn {
    position: absolute;
    cursor: pointer;
    border: none;
    border-radius: 50px;
    background: #ff69b4;
    color: white;
    font-weight: bold;
    font-size: 24px;
    padding: 15px 40px;
    transition: all 0.3s ease;
    box-shadow: 0 5px 20px rgba(0,0,0,0.2);
    z-index: 9999;
}

/* Hover effect */
#yes-btn:hover {
    background: #ff85c1;
    transform: scale(1.05);
}

/* Responsive YES button for small screens */
@media (max-width: 480px) {
    #yes-btn {
        font-size: 20px !important;
        padding: 12px 32px !important;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================
# CARD
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<h1>💖 Will You Be My Valentine?</h1>", unsafe_allow_html=True)
st.markdown("<h2>💖 💙 💜 💌 💍</h2>", unsafe_allow_html=True)

if st.session_state.yes_clicks < MAX_CLICKS:
    st.markdown(
        f"<h2>{NOTES[st.session_state.yes_clicks]}</h2>",
        unsafe_allow_html=True
    )
else:
    st.balloons()
    st.markdown("""
    <h1>🎉 IT’S A DATE 🎉</h1>
    <h2>💞 Thank you for saying YES 💞</h2>
    <h3>💖💙💜 I can’t wait to spend Valentine’s with you 💖💙💜</h3>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# FLOATING YES BUTTON
# =========================
if st.session_state.yes_clicks < MAX_CLICKS:
    # Random position for desktop/mobile (viewport width/height)
    st.session_state.x_pos = random.randint(10, 80)
    st.session_state.y_pos = random.randint(10, 80)
    font_size = 24 + (st.session_state.yes_clicks * 10)
    padding_y = 15 + st.session_state.yes_clicks * 5
    padding_x = 40 + st.session_state.yes_clicks * 10

    # Render the floating button
    st.markdown(f"""
    <button id='yes-btn' 
        style='left:{st.session_state.x_pos}vw; top:{st.session_state.y_pos}vh; font-size:{font_size}px; padding:{padding_y}px {padding_x}px;'
        onclick="window.streamlitYesClicked()">
        YES ❤️
    </button>

    <script>
    const btn = document.getElementById('yes-btn');
    btn.onclick = () => {{
        const streamlitEvent = new CustomEvent("streamlitYesClicked");
        window.dispatchEvent(streamlitEvent);
    }}
    </script>
    """, unsafe_allow_html=True)

# =========================
# STREAMLIT BUTTON CALLBACK
# =========================
# Capture clicks from floating YES
def increment_clicks():
    st.session_state.yes_clicks += 1

# Streamlit event listener hack
st.components.v1.html("""
<script>
window.streamlitYesClicked = () => {
    fetch("/_stcore/streamlitYesClicked");
}
</script>
""")
