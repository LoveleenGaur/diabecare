import streamlit as st
from groq import Groq

st.set_page_config(page_title="AI Assistant · DiabeCare", page_icon="💬", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Nunito', sans-serif; }
.chat-header {
    background: linear-gradient(135deg, #1a4a3a, #2d7a5f);
    color: white; padding: 1.5rem 2rem; border-radius: 16px; margin-bottom: 1.5rem;
}
.quick-btn-row { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 1rem; }
.disclaimer-box {
    background: #fff3cd; border-left: 4px solid #ffc107;
    padding: 0.8rem 1rem; border-radius: 8px; font-size: 0.85rem; margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="chat-header">
    <h2>💬 AI Health Assistant</h2>
    <p>Ask anything about diabetes, frozen shoulder, brain health, South Indian diet, exercises, or general wellness.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="disclaimer-box">
    ⚕️ <strong>Note:</strong> This AI provides health education only — not a substitute for your doctor.
    For emergencies, call 112 (India) or visit your nearest hospital immediately.
</div>
""", unsafe_allow_html=True)

# Groq client setup
def get_groq_client():
    api_key = st.session_state.get("groq_api_key") or st.secrets.get("GROQ_API_KEY", "")
    if not api_key:
        return None
    return Groq(api_key=api_key)

# Sidebar: API key input
with st.sidebar:
    st.markdown("### 🔑 Groq API Key")
    api_key_input = st.text_input(
        "Enter your Groq API Key",
        type="password",
        value=st.session_state.get("groq_api_key", ""),
        help="Get a free key at https://console.groq.com"
    )
    if api_key_input:
        st.session_state["groq_api_key"] = api_key_input
        st.success("✅ Key saved for this session")

    st.markdown("---")
    st.markdown("### ⚙️ Model")
    model = st.selectbox("Choose model", [
        "llama-3.3-70b-versatile",
        "llama-3.1-8b-instant",
        "mixtral-8x7b-32768",
        "gemma2-9b-it"
    ])

    st.markdown("---")
    st.markdown("### 🌡️ Response Style")
    temp = st.slider("Creativity", 0.1, 1.0, 0.6, 0.1)

    if st.button("🗑️ Clear Chat"):
        st.session_state["messages"] = []
        st.rerun()

    st.markdown("---")
    st.markdown("**Get free API key:**")
    st.markdown("[console.groq.com](https://console.groq.com)")

SYSTEM_PROMPT = """You are DiabeCare AI — a warm, compassionate, and knowledgeable health assistant helping a diabetic South Indian vegetarian patient who has:
- Type 2 Diabetes (possibly poorly controlled)
- Frozen Shoulder (Adhesive Capsulitis) — a very common diabetic complication
- Brain swelling (cerebral edema) found on MRI — this is serious

YOUR EXPERTISE COVERS:
1. **Diabetes management**: Blood sugar monitoring, HbA1c, medications, hypoglycemia/hyperglycemia recognition
2. **Frozen shoulder recovery**: 3 stages (freezing 6wk-9mo / frozen 4-6mo / thawing 6mo-2yr), physiotherapy, pendulum exercises, wall climbing exercises, towel stretches
3. **Brain/neurological health**: Warning signs of cerebral edema (severe headache, confusion, vision changes, drowsiness, vomiting, neck stiffness) — ALWAYS flag these as EMERGENCY
4. **South Indian vegetarian diet for diabetes**: Emphasize: 
   - Beneficial: Ragi (finger millet), foxtail millet, barnyard millet, kozhukattai (steamed rice dumplings), idli (small portions), sambar with drumstick/moringa, bitter gourd (pavakka/karela) dishes, fenugreek (methi/vendhayam), curry leaves, coconut oil in moderation, buttermilk (mor), turmeric, pepper rasam, horse gram (kollu) rasam, jackfruit seed curry, raw banana preparations
   - Avoid: White rice in large quantities, maida, sweets, fruit juices, fried snacks like murukku/chips, sweetened payasam
5. **Alternative/natural medicine**: Fenugreek seeds soaking, bitter gourd juice (small amounts), moringa leaves, curry leaves, yoga (sukhasana, vrikshasana modified for shoulder), pranayama (Anulom Vilom, Bhramari), meditation
6. **Exercises**: Pendulum swings, wall walking, towel stretch, cross-body stretch, doorway stretch — all modified for diabetics
7. **Do's and Don'ts**: Specific to diabetes + frozen shoulder + brain health
8. **Monitoring**: What to track daily/weekly
9. **Motivational stories**: Real-world examples of people recovering from diabetic complications

RESPONSE STYLE:
- Warm and encouraging — like a knowledgeable friend
- Use bullet points and clear sections
- Bold key terms
- Always mention when something requires a doctor visit
- For EMERGENCY symptoms (severe headache, confusion, loss of consciousness, very low blood sugar <70mg/dL, very high >400mg/dL): respond with 🚨 EMERGENCY — CALL 112 / GO TO ER IMMEDIATELY
- Sprinkle Tamil/Telugu/Kannada/Malayalam food names naturally (with English in brackets)
- End with one motivational sentence

Keep responses focused, practical, and under 400 words unless the topic truly requires more detail."""

# Quick topic buttons
st.markdown("**Quick questions:**")
quick_topics = [
    ("🚨 Danger signs", "What are the emergency warning signs I should never ignore as a diabetic with brain swelling?"),
    ("🧘 Shoulder exercises", "What are the best home exercises for frozen shoulder for a diabetic patient?"),
    ("🥗 Diet plan", "Give me a full day South Indian vegetarian meal plan that is good for diabetes and frozen shoulder recovery"),
    ("🌿 Natural remedies", "What natural/alternative medicines and herbs from South India help diabetes and frozen shoulder?"),
    ("📊 What to monitor", "What should I monitor daily as a diabetic patient with frozen shoulder and brain swelling?"),
    ("💪 Inspire me", "Share a real story of someone who recovered from diabetic complications and frozen shoulder"),
    ("💊 Medications", "What medications are used for frozen shoulder in diabetics and what should I watch out for?"),
    ("🧠 Brain health", "How do I protect my brain health as a diabetic? What lifestyle changes help?"),
]

cols = st.columns(4)
for i, (label, question) in enumerate(quick_topics):
    with cols[i % 4]:
        if st.button(label, key=f"quick_{i}", use_container_width=True):
            st.session_state.setdefault("messages", [])
            st.session_state["messages"].append({"role": "user", "content": question})
            st.session_state["trigger_response"] = True
            st.rerun()

st.markdown("---")

# Initialize chat
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"], avatar="🌿" if msg["role"] == "assistant" else "👤"):
        st.markdown(msg["content"])

# Auto-trigger from quick buttons
if st.session_state.get("trigger_response"):
    st.session_state["trigger_response"] = False
    client = get_groq_client()
    if not client:
        st.error("Please enter your Groq API key in the sidebar.")
    else:
        with st.chat_message("assistant", avatar="🌿"):
            with st.spinner("Thinking..."):
                try:
                    response = client.chat.completions.create(
                        model=model,
                        messages=[{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state["messages"],
                        temperature=temp,
                        max_tokens=1024,
                    )
                    reply = response.choices[0].message.content
                    st.markdown(reply)
                    st.session_state["messages"].append({"role": "assistant", "content": reply})
                except Exception as e:
                    st.error(f"Error: {e}")

# Chat input
if prompt := st.chat_input("Ask about diabetes, frozen shoulder, diet, exercises, brain health..."):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    client = get_groq_client()
    if not client:
        st.error("Please enter your Groq API key in the sidebar to start chatting.")
    else:
        with st.chat_message("assistant", avatar="🌿"):
            with st.spinner("Thinking..."):
                try:
                    response = client.chat.completions.create(
                        model=model,
                        messages=[{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state["messages"],
                        temperature=temp,
                        max_tokens=1024,
                    )
                    reply = response.choices[0].message.content
                    st.markdown(reply)
                    st.session_state["messages"].append({"role": "assistant", "content": reply})
                except Exception as e:
                    st.error(f"Error connecting to Groq: {e}")
