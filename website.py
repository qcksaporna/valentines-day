import streamlit as st

# =========================
# CONFIGURATION
# =========================
PAGE_TITLE = "Valentine’s Invitation"
PAGE_ICON = "❤️"
MAX_CLICKS = 4

NOTES = [
    "❤️ Are you really sure?",
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
    layout="centered"
)

# =========================
# STATE MANAGEMENT
# =========================
if "yes_clicks" not in st.session_state:
    st.session_state.yes_clicks = 0

# =========================
# STYLES (Cloud-Safe)
# =========================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #8B0000, #B22222);
    color: #fff;
    font-family: 'Segoe UI', sans-serif;
}

h1, h2, h3 {
    text-align: center;
    font-weight: 600;
}

.main-card {
    background: rgba(255, 255, 255, 0.12);
    padding: 2.5rem;
    border-radius: 24px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    margin-top: 3rem;
}

div.stButton > button {
    background: #ff3366;
    color: white;
    border: none;
    border-radius: 50px;
    transition: all 0.3s ease;
}

div.stButton > button:hover {
    background: #ff5c85;
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# =========================
# UI LAYOUT
# =========================
st.markdown("<div class='main-card'>", unsafe_allow_html=True)

st.markdown("<h1>❤️ Will You Be My Valentine?</h1>", unsafe_allow_html=True)
st.markdown("<h3>💖 💐 🧸 💌 💍</h3>", unsafe_allow_html=True)

# Show progressive note
if st.session_state.yes_clicks < MAX_CLICKS:
    st.markdown(
        f"<h2>{NOTES[st.session_state.yes_clicks]}</h2>",
        unsafe_allow_html=True
    )

# Dynamic button sizing
font_size = 22 + (st.session_state.yes_clicks * 14)
padding_y = 12 + (st.session_state.yes_clicks * 6)
padding_x = 40 + (st.session_state.yes_clicks * 16)

st.markdown(
    f"""
    <style>
    div.stButton > button {{
        font-size: {font_size}px;
        padding: {padding_y}px {padding_x}px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# INTERACTION LOGIC
# =========================
if st.session_state.yes_clicks < MAX_CLICKS:
    if st.button("YES ❤️"):
        st.session_state.yes_clicks += 1
else:
    st.balloons()
    st.markdown("""
    <h1>🎉 IT’S A DATE 🎉</h1>
    <h2>💞 Thank you for saying YES 💞</h2>
    <h3>🌹 I can’t wait to spend Valentine’s with you 🌹</h3>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
