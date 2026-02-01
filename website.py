import streamlit as st
import random

# =========================
# CONFIGURATION
# =========================
PAGE_TITLE = "Valentine’s Invitation"
PAGE_ICON = "❤️"
MAX_CLICKS = 4

NOTES = [
    "❤️ Are you sure?",
    "🌹 I promise it will be special",
    "💌 Almost there…",
    "💍 No turning back now"
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
    st.session_state.x_pos = 50
if "y_pos" not in st.session_state:
    st.session_state.y_pos = 50

# =========================
# STYLES
# =========================
st.markdown("""
<style>
body {
    background: linear-gradient(160deg, #ff4d6d, #ff99aa);
    font-family: 'Segoe UI', sans-serif;
    overflow: hidden;
}
.card {
    background: rgba(255, 255, 255, 0.1);
    padding: 2rem;
    border-radius: 24px;
    text-align: center;
    max-width: 600px;
    margin: 5% auto;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}
h1, h2 {
    color: white;
}
#yes-btn {
    position: absolute;
    cursor: pointer;
    border: none;
    border-radius: 50px;
    background: #ff3366;
    color: white;
    font-size: 24px;
    padding: 15px 40px;
    transition: all 0.3s ease;
}
#yes-btn:hover {
    background: #ff5c85;
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# =========================
# CARD
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<h1>❤️ Will You Be My Valentine?</h1>", unsafe_allow_html=True)
st.markdown("<h2>💖 🧸 💐 💌 💍</h2>", unsafe_allow_html=True)

if st.session_state.yes_clicks < MAX_CLICKS:
    st.markdown(f"<h2>{NOTES[st.session_state.yes_clicks]}</h2>", unsafe_allow_html=True)
else:
    st.balloons()
    st.markdown("""
    <h1>🎉 IT’S A DATE 🎉</h1>
    <h2>💞 Thank you for saying YES 💞</h2>
    <h3>🌹 I can’t wait to spend Valentine’s with you 🌹</h3>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# YES BUTTON LOGIC (Floating)
# =========================
# Move button randomly each click
if st.session_state.yes_clicks < MAX_CLICKS:
    st.session_state.x_pos = random.randint(10, 80)
    st.session_state.y_pos = random.randint(10, 80)
    font_size = 24 + (st.session_state.yes_clicks * 10)
    st.markdown(f"""
        <button id='yes-btn' 
            style='left:{st.session_state.x_pos}vw; top:{st.session_state.y_pos}vh; font-size:{font_size}px;'
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
# CALLBACK FOR STREAMLIT BUTTON (Hacky but works)
# =========================
# Because Streamlit doesn't directly capture JS clicks,
# we need user to actually click a Streamlit button too
if st.button("Click YES here too to register ❤️"):
    st.session_state.yes_clicks += 1
