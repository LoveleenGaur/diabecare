import streamlit as st

st.set_page_config(page_title="Do's & Don'ts · DiabeCare", page_icon="✅", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Nunito', sans-serif; }
.section-header {
    background: linear-gradient(135deg, #1a3a5a, #2d6a9f);
    color: white; padding: 1.5rem 2rem; border-radius: 16px; margin-bottom: 1.5rem;
}
.do-card {
    background: #f0faf4; border-left: 5px solid #2d9a5f;
    border-radius: 10px; padding: 1rem 1.2rem; margin-bottom: 0.7rem;
}
.dont-card {
    background: #fff0f0; border-left: 5px solid #d9534f;
    border-radius: 10px; padding: 1rem 1.2rem; margin-bottom: 0.7rem;
}
.tip-card {
    background: #fff8e6; border-left: 5px solid #f0a500;
    border-radius: 10px; padding: 1rem 1.2rem; margin-bottom: 0.7rem;
}
.category-badge {
    display: inline-block; padding: 3px 12px; border-radius: 20px;
    font-size: 0.75rem; font-weight: 700; margin-bottom: 0.5rem;
    background: #dde8f5; color: #1a3a5a;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-header">
    <h2>✅ Do's & Don'ts</h2>
    <p>Critical guidelines for managing diabetes, frozen shoulder & brain health together</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["✅ Do's", "❌ Don'ts", "⚠️ Warning Signs"])

categories = ["🩸 Blood Sugar", "🦴 Frozen Shoulder", "🧠 Brain Health", "💊 Medications", "🍽️ Diet", "🧘 Lifestyle"]

# ─── DO'S ───
with tab1:
    st.markdown("### ✅ Essential Do's — Follow These Every Day")

    dos = [
        ("🩸 Blood Sugar", "Check blood sugar at least twice daily — fasting (morning) and 2 hours after lunch. Keep a log book or use an app."),
        ("🩸 Blood Sugar", "Know your target numbers: Fasting: 80–130 mg/dL | Post-meal (2hr): <180 mg/dL | HbA1c: <7%"),
        ("🩸 Blood Sugar", "Always carry fast-acting sugar (4–5 glucose tablets or 1/2 cup fruit juice) in case blood sugar drops (hypoglycemia)"),
        ("🩸 Blood Sugar", "Get HbA1c tested every 3 months — this is the most important indicator of diabetes control"),
        ("🦴 Frozen Shoulder", "Do your shoulder exercises every single day — even when it hurts mildly. Consistency is the cure."),
        ("🦴 Frozen Shoulder", "Apply a warm compress for 10 minutes before every exercise session"),
        ("🦴 Frozen Shoulder", "Sleep on your back or good side — place a pillow under the affected arm for support"),
        ("🦴 Frozen Shoulder", "Track your progress: measure how high you can walk your fingers up the wall each week"),
        ("🦴 Frozen Shoulder", "See a physiotherapist at least once to learn proper technique — then do exercises at home"),
        ("🧠 Brain Health", "Report ANY new neurological symptoms to your doctor immediately: severe headache, confusion, vision changes, numbness"),
        ("🧠 Brain Health", "Keep blood sugar well-controlled — this is the #1 brain protector for diabetics"),
        ("🧠 Brain Health", "Sleep 7–8 hours every night — brain repairs and clears waste products (including inflammatory ones) during sleep"),
        ("🧠 Brain Health", "Stay mentally active: read, solve puzzles, have conversations — neuroplasticity fights damage"),
        ("🧠 Brain Health", "Stay well hydrated — dehydration worsens brain swelling. Drink 8–10 glasses of water daily"),
        ("💊 Medications", "Take all medications at the same time every day — set phone alarms if needed"),
        ("💊 Medications", "Tell your doctor EVERY supplement and herb you take — many interact with diabetes drugs"),
        ("💊 Medications", "If your doctor prescribes a steroid injection for frozen shoulder — monitor blood sugar extra closely for 3–5 days after (steroids raise blood sugar significantly)"),
        ("🍽️ Diet", "Eat small meals every 3–4 hours — never go more than 5 hours without food"),
        ("🍽️ Diet", "Eat dinner by 7:30 PM — late dinners worsen fasting blood sugar next morning"),
        ("🍽️ Diet", "Eat protein at every meal — dal, legumes, curd, paneer — slows glucose absorption"),
        ("🧘 Lifestyle", "Walk 15–30 minutes after every meal — this is the single most effective blood sugar reducer"),
        ("🧘 Lifestyle", "Practice Anulom Vilom pranayama daily — proven to reduce blood sugar and inflammation"),
        ("🧘 Lifestyle", "Join a diabetes support group (in-person or online) — social support improves health outcomes significantly"),
    ]

    selected_cat = st.multiselect("Filter by category:", categories, default=categories)
    for cat, item in dos:
        if cat in selected_cat:
            st.markdown(f"""
            <div class="do-card">
                <span class="category-badge">{cat}</span><br>
                ✅ {item}
            </div>
            """, unsafe_allow_html=True)

# ─── DON'TS ───
with tab2:
    st.markdown("### ❌ Critical Don'ts — Avoid These")

    donts = [
        ("🩸 Blood Sugar", "NEVER skip insulin or diabetes medications without doctor's advice — even if blood sugar seems normal"),
        ("🩸 Blood Sugar", "Never stop checking blood sugar just because you 'feel fine' — diabetes is often asymptomatic until it's severe"),
        ("🩸 Blood Sugar", "Never manage blood sugar extremes (<70 or >400 mg/dL) at home alone — call your doctor"),
        ("🦴 Frozen Shoulder", "Never use a sling or completely stop moving the shoulder — immobility is what causes worsening frozen shoulder"),
        ("🦴 Frozen Shoulder", "Never do aggressive manipulation or 'crack' the shoulder yourself or let a non-specialist manipulate it forcefully"),
        ("🦴 Frozen Shoulder", "Never exercise through sharp pain (>4/10) — mild discomfort is normal, sharp pain means stop"),
        ("🦴 Frozen Shoulder", "Never sleep on the affected shoulder"),
        ("🦴 Frozen Shoulder", "Don't carry heavy bags, a laptop bag, or groceries on the affected side"),
        ("🧠 Brain Health", "NEVER ignore a sudden severe headache, confusion, or vision changes — go to ER immediately"),
        ("🧠 Brain Health", "Don't let blood sugar go very high for days — chronic hyperglycemia damages brain blood vessels"),
        ("🧠 Brain Health", "Avoid alcohol completely — it interacts with medications AND worsens brain health"),
        ("🧠 Brain Health", "Don't stay isolated or depressed — chronic stress and depression worsen both blood sugar and brain inflammation"),
        ("💊 Medications", "Never take NSAIDs (like Ibuprofen) regularly without doctor guidance — they affect kidney function in diabetics"),
        ("💊 Medications", "Don't start or stop any medication without telling your doctor"),
        ("💊 Medications", "Never take someone else's diabetes medication"),
        ("🍽️ Diet", "Never skip breakfast — it sets blood sugar control for the whole day"),
        ("🍽️ Diet", "Don't eat large amounts of food in one sitting — split into smaller frequent meals"),
        ("🍽️ Diet", "Never drink fruit juice as a 'healthy' substitute — it spikes blood sugar like soda"),
        ("🧘 Lifestyle", "Don't smoke — smoking doubles cardiovascular risk in diabetics and worsens nerve damage"),
        ("🧘 Lifestyle", "Don't exercise if blood sugar is below 100 mg/dL or above 300 mg/dL — dangerous"),
        ("🧘 Lifestyle", "Don't walk barefoot — diabetic neuropathy means foot injuries often go unnoticed and can escalate to serious infections"),
    ]

    selected_cat2 = st.multiselect("Filter by category:", categories, default=categories, key="dont_filter")
    for cat, item in donts:
        if cat in selected_cat2:
            st.markdown(f"""
            <div class="dont-card">
                <span class="category-badge">{cat}</span><br>
                ❌ {item}
            </div>
            """, unsafe_allow_html=True)

# ─── WARNING SIGNS ───
with tab3:
    st.markdown("### ⚠️ Warning Signs — Know When to Act NOW")

    st.error("""
    ### 🚨 CALL 112 OR GO TO ER IMMEDIATELY IF:

    **Brain/Neurological:**
    - Sudden severe headache (worst headache of life)
    - Sudden confusion, disorientation, or inability to speak
    - Vision changes: double vision, sudden blurring, or loss of vision
    - Seizures (convulsions / fits)
    - Loss of consciousness or difficulty waking up
    - Sudden weakness or numbness on one side of body
    - Neck stiffness with headache and fever
    - Vomiting with headache and drowsiness

    **Blood Sugar Emergencies:**
    - Blood sugar below 54 mg/dL (severe hypoglycemia) with confusion
    - Blood sugar above 400 mg/dL with vomiting, deep breathing, fruity-smelling breath (DKA)
    - Loss of consciousness or not responding

    **Heart:**
    - Chest pain, tightness, or pressure
    - Severe breathlessness
    - Arm/jaw pain with sweating
    """)

    st.warning("""
    ### ⚠️ Call your doctor within 24 hours if:
    - Shoulder pain becomes suddenly much worse
    - New arm weakness or numbness
    - Blood sugar consistently above 300 mg/dL for 2+ days
    - Foot wound that is not healing
    - Fever above 38.5°C with any diabetic complication
    - Any fall or injury to the frozen shoulder
    - Unusual drowsiness, not feeling 'right'
    - New severe headache (not the worst ever, but new and persistent)
    """)

    st.success("""
    ### 📋 Schedule a routine appointment if:
    - HbA1c is overdue (>3 months since last test)
    - Shoulder range of motion is not improving after 6 weeks of exercises
    - Follow-up MRI not scheduled yet for brain swelling
    - Foot numbness or tingling has increased
    - Weight changes of >3 kg unexpectedly
    - New medication side effects
    """)
