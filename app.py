import streamlit as st

st.set_page_config(
    page_title="DiabeCare — Your Healing Companion",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&family=Lora:ital,wght@0,400;0,600;1,400&display=swap');

html, body, [class*="css"] { font-family: 'Nunito', sans-serif; }

.main-hero {
    background: linear-gradient(135deg, #1a4a3a 0%, #2d7a5f 50%, #4a9e7a 100%);
    color: white;
    padding: 3rem 2rem;
    border-radius: 20px;
    margin-bottom: 2rem;
    text-align: center;
}
.main-hero h1 { font-size: 2.8rem; font-weight: 800; margin-bottom: 0.5rem; }
.main-hero p { font-size: 1.15rem; opacity: 0.9; }

.feature-card {
    background: white;
    border-radius: 16px;
    padding: 1.5rem;
    text-align: center;
    border: 2px solid #e8f5f0;
    transition: all 0.2s;
    height: 100%;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
}
.feature-card:hover { border-color: #2d7a5f; transform: translateY(-2px); }
.feature-icon { font-size: 2.5rem; margin-bottom: 0.8rem; }
.feature-card h3 { color: #1a4a3a; font-size: 1.05rem; font-weight: 700; }
.feature-card p { color: #666; font-size: 0.88rem; margin-top: 0.4rem; }

.info-banner {
    background: #fff8e6;
    border-left: 4px solid #f0a500;
    padding: 1rem 1.5rem;
    border-radius: 8px;
    margin: 1rem 0;
}
</style>
""", unsafe_allow_html=True)

# Hero section
st.markdown("""
<div class="main-hero">
    <h1>🌿 DiabeCare</h1>
    <p>Your AI-powered healing companion for diabetes, frozen shoulder & neurological wellness</p>
    <p style="font-size:0.95rem; opacity:0.8; margin-top:0.5rem;">Rooted in South Indian wisdom · Powered by modern AI</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="info-banner">
    ⚕️ <strong>Medical Disclaimer:</strong> This app provides educational health information only.
    Always consult your doctor, physiotherapist, or specialist before starting any new treatment, diet, or exercise.
</div>
""", unsafe_allow_html=True)

# Feature cards
st.markdown("## 🗺️ What would you like to explore today?")
st.markdown("Use the **sidebar** to navigate, or click a section below to get started.")
st.markdown("")

cols = st.columns(3)

features = [
    ("💬", "AI Health Assistant", "Chat with our AI about your symptoms, concerns, and questions — available 24/7", "pages/1_💬_AI_Assistant.py"),
    ("🧘", "Exercises & Physio", "Guided exercises for frozen shoulder recovery, yoga, and gentle movement", "pages/2_🧘_Exercises.py"),
    ("🥗", "South Indian Diet", "Healing recipes and meal plans tailored for diabetic South Indian vegetarians", "pages/3_🥗_Diet_Guide.py"),
    ("✅", "Do's & Don'ts", "Critical dos and don'ts for diabetes, frozen shoulder, and brain health", "pages/4_✅_Dos_and_Donts.py"),
    ("📊", "What to Monitor", "Track blood sugar, shoulder mobility, neuro symptoms and more", "pages/5_📊_Monitor.py"),
    ("💪", "Inspiration Stories", "Real stories of people who healed and thrived despite diabetes complications", "pages/6_💪_Stories.py"),
]

for i, (icon, title, desc, _) in enumerate(features):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="feature-card">
            <div class="feature-icon">{icon}</div>
            <h3>{title}</h3>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align:center; color:#999; font-size:0.85rem;">
    Built with ❤️ for diabetic warriors · DiabeCare uses Groq + LLaMA for fast AI responses<br>
    <strong style="color:#2d7a5f">Remember: You are stronger than your diagnosis. 🌿</strong>
</div>
""", unsafe_allow_html=True)
