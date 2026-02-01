import streamlit as st

st.set_page_config(page_title="💖 Valentine’s Invite 💖", page_icon="💘")

st.write("✅ App started")

if "clicks" not in st.session_state:
    st.session_state.clicks = 0

notes = [
    "💗 Are you sure?",
    "🥰 I promise it will be fun!",
    "🌹 Just one more YES!",
    "💍 You’re stuck with me now 😘"
]

st.markdown("""
<style>
.stApp {
    background-color: #ffe6f2;
}
div.stButton > button {
    font-size: calc(20px + var(--grow, 0px));
    padding: 12px 36px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>💘 Will you be my Valentine? 💘</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;'>💖 💕 🌸 🧸 💐 💞</h2>", unsafe_allow_html=True)

if st.session_state.clicks < 4:
    st.markdown(
        f"<h3 style='text-align:center;'>{notes[st.session_state.clicks]}</h3>",
        unsafe_allow_html=True
    )

st.markdown(
    f"""
    <style>
    div.stButton > button {{
        font-size: {20 + st.session_state.clicks * 15}px;
        padding: {10 + st.session_state.clicks*5}px {30 + st.session_state.clicks*10}px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

if st.button("YES 💖"):
    st.session_state.clicks += 1

if st.session_state.clicks >= 4:
    st.balloons()
    st.markdown("""
    <h1 style='text-align:center;'>🎉 YAYYYYY!!! 🎉</h1>
    <h2 style='text-align:center;'>💞 It’s a DATE! 💞</h2>
    <h3 style='text-align:center;'>🌹 I can’t wait to spend Valentine’s with you 🌹</h3>
    """, unsafe_allow_html=True)
