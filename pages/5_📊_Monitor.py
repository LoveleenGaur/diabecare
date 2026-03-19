import streamlit as st
import pandas as pd
from datetime import date, timedelta
import json

st.set_page_config(page_title="Monitor · DiabeCare", page_icon="📊", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Nunito', sans-serif; }
.section-header {
    background: linear-gradient(135deg, #3a1a5a, #6a2d9f);
    color: white; padding: 1.5rem 2rem; border-radius: 16px; margin-bottom: 1.5rem;
}
.monitor-card {
    background: white; border-radius: 14px; padding: 1.2rem 1.4rem;
    border: 2px solid #ede8f5; margin-bottom: 1rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
.monitor-card h4 { color: #3a1a5a; font-weight: 700; }
.freq-badge {
    display: inline-block; padding: 2px 10px; border-radius: 20px;
    font-size: 0.75rem; font-weight: 700; margin-bottom: 0.5rem;
}
.daily { background: #fde8e3; color: #8a2510; }
.weekly { background: #e8f5e3; color: #1a5a10; }
.monthly { background: #e8eef8; color: #1a3a8a; }
.target-box {
    background: #f8f5ff; border: 1px solid #d8c8f5;
    border-radius: 8px; padding: 0.7rem 1rem; margin-top: 0.5rem;
    font-size: 0.88rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-header">
    <h2>📊 What to Monitor</h2>
    <p>Track these key health markers to stay in control and catch problems early</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["📋 Monitoring Guide", "📝 Daily Log"])

# ─── MONITORING GUIDE ───
with tab1:
    st.markdown("### 📋 Complete Monitoring Checklist")

    monitors = [
        {
            "name": "🩸 Fasting Blood Sugar",
            "freq": "Daily", "freq_class": "daily",
            "when": "Every morning before eating or drinking anything (except water)",
            "target": "80–130 mg/dL (ideal: <100 mg/dL)",
            "action": "Above 180 consistently → call doctor. Above 300 → go to ER.",
            "why": "The most important daily indicator. Shows how well insulin/medications are working overnight."
        },
        {
            "name": "🩸 Post-Meal Blood Sugar (PP)",
            "freq": "Daily", "freq_class": "daily",
            "when": "Exactly 2 hours after starting your largest meal (lunch or dinner)",
            "target": "Below 180 mg/dL (ideal: <140 mg/dL)",
            "action": "Consistently above 200 → adjust meal composition, increase post-meal walk",
            "why": "Post-meal spikes damage blood vessels. This reading shows the impact of your food choices."
        },
        {
            "name": "🦴 Shoulder Range of Motion",
            "freq": "Weekly", "freq_class": "weekly",
            "when": "Every Sunday morning, after warm compress and 5 minutes of pendulum exercise",
            "target": "Improvement of 1–2 cm per week in wall finger walking test",
            "action": "No improvement for 4+ weeks → physiotherapist visit needed",
            "why": "Tracking progress keeps you motivated and helps catch a plateau early."
        },
        {
            "name": "💉 HbA1c (Glycated Hemoglobin)",
            "freq": "Every 3 months", "freq_class": "monthly",
            "when": "Blood test at lab — doesn't require fasting",
            "target": "Below 7% (below 6.5% is ideal, below 8% is acceptable)",
            "action": "Above 8% consistently → intensify medication/diet with doctor",
            "why": "Shows your average blood sugar for the past 3 months. The gold standard of diabetes control."
        },
        {
            "name": "⚖️ Body Weight",
            "freq": "Weekly", "freq_class": "weekly",
            "when": "Every Monday morning, same time, same clothes, before eating",
            "target": "Gradual loss of 0.5–1 kg/month if overweight. Stable if normal weight.",
            "action": "Unexplained weight loss (>3 kg/month) or gain → inform doctor",
            "why": "Even 5–10% weight loss dramatically improves blood sugar control and reduces frozen shoulder inflammation."
        },
        {
            "name": "🧠 Neurological Symptoms Journal",
            "freq": "Daily", "freq_class": "daily",
            "when": "Every evening — 2 minutes to note any symptoms",
            "target": "No new or worsening symptoms",
            "action": "ANY sudden new symptom → call doctor immediately",
            "why": "With brain swelling, changes can be subtle. Writing daily helps spot patterns.",
            "track": ["Headache (location, intensity 1–10)", "Dizziness or balance issues", "Vision changes", "Confusion or memory lapses", "Neck stiffness", "Mood changes", "Sleep quality"]
        },
        {
            "name": "🦶 Foot Inspection",
            "freq": "Daily", "freq_class": "daily",
            "when": "Every night before bed — use a mirror for the sole if needed",
            "target": "No cuts, blisters, redness, swelling, or discolouration",
            "action": "Any wound that doesn't heal in 3 days → see doctor immediately",
            "why": "Diabetic foot is one of the most preventable serious complications. Neuropathy means you may not feel foot injuries."
        },
        {
            "name": "🫀 Blood Pressure",
            "freq": "3× weekly", "freq_class": "weekly",
            "when": "Sit quietly for 5 minutes before measuring. Morning is best.",
            "target": "Below 130/80 mmHg",
            "action": "Above 160/100 → call doctor. For brain swelling patients: keep it strictly controlled.",
            "why": "High BP dramatically worsens both diabetes complications and brain swelling."
        },
        {
            "name": "🔬 Kidney Function (Creatinine, eGFR)",
            "freq": "Every 6 months", "freq_class": "monthly",
            "when": "Blood + urine test at lab",
            "target": "Creatinine: 0.6–1.2 mg/dL | eGFR: >60",
            "action": "Declining eGFR → doctor review of medications (some diabetes drugs are harmful for kidneys)",
            "why": "Diabetes is the leading cause of kidney disease. Early detection = prevention."
        },
        {
            "name": "👁️ Eye Exam (Diabetic Retinopathy)",
            "freq": "Yearly", "freq_class": "monthly",
            "when": "Annual dilated eye exam with ophthalmologist",
            "target": "No retinopathy, or stable monitored retinopathy",
            "action": "Any vision changes before annual exam → see eye doctor sooner",
            "why": "Diabetes damages eye blood vessels silently. Caught early, progression can be stopped."
        },
    ]

    for m in monitors:
        freq_badge = f"<span class='freq-badge {m['freq_class']}'>{m['freq']}</span>"
        tracking = ""
        if "track" in m:
            track_list = "".join([f"<li>{t}</li>" for t in m["track"]])
            tracking = f"<strong>Track these specifically:</strong><ul>{track_list}</ul>"

        st.markdown(f"""
        <div class="monitor-card">
            <h4>{m['name']}</h4>
            {freq_badge}
            <p><strong>⏰ When:</strong> {m['when']}</p>
            <div class="target-box">
                🎯 <strong>Target:</strong> {m['target']}<br>
                🚦 <strong>Action needed if:</strong> {m['action']}
            </div>
            <p style="margin-top:0.5rem; font-size:0.88rem; color:#555;"><em>Why this matters: {m['why']}</em></p>
            {tracking}
        </div>
        """, unsafe_allow_html=True)

# ─── DAILY LOG ───
with tab2:
    st.markdown("### 📝 Daily Health Log")
    st.info("Track your key readings below. Your entries are saved for this session.")

    if "logs" not in st.session_state:
        st.session_state["logs"] = []

    with st.form("daily_log"):
        log_date = st.date_input("Date", value=date.today())
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**🩸 Blood Sugar (mg/dL)**")
            bs_fasting = st.number_input("Fasting (morning)", min_value=0, max_value=600, value=0, step=1)
            bs_pp = st.number_input("Post-meal (2hr after lunch)", min_value=0, max_value=600, value=0, step=1)
            bs_evening = st.number_input("Evening reading", min_value=0, max_value=600, value=0, step=1)

            st.markdown("**⚖️ Weight & BP**")
            weight = st.number_input("Weight (kg)", min_value=0.0, max_value=200.0, value=0.0, step=0.1)
            bp_sys = st.number_input("BP Systolic (top number)", min_value=0, max_value=300, value=0)
            bp_dia = st.number_input("BP Diastolic (bottom number)", min_value=0, max_value=200, value=0)

        with col2:
            st.markdown("**🦴 Shoulder**")
            shoulder_pain = st.slider("Shoulder pain (0=none, 10=worst)", 0, 10, 0)
            shoulder_rom = st.text_input("Wall walking height reached (cm or mark)", placeholder="e.g. 120cm or Elbow level")
            did_exercises = st.checkbox("✅ Did shoulder exercises today")

            st.markdown("**🧠 Neurological Symptoms**")
            headache = st.slider("Headache intensity (0=none)", 0, 10, 0)
            neuro_symptoms = st.multiselect("Any symptoms today:", [
                "Dizziness", "Vision changes", "Confusion", "Neck stiffness",
                "Nausea", "Balance issues", "Memory lapses", "Numbness"
            ])

            st.markdown("**🧘 Lifestyle**")
            exercise_done = st.checkbox("✅ Did walking/exercise today")
            pranayama = st.checkbox("✅ Did pranayama today")
            sleep_hours = st.slider("Hours slept last night", 0, 12, 7)
            mood = st.select_slider("Overall mood today", options=["😔 Low", "😐 Neutral", "🙂 Good", "😊 Great"])

        notes = st.text_area("📝 Additional notes / symptoms", placeholder="Anything unusual today...")

        submitted = st.form_submit_button("💾 Save Today's Log", use_container_width=True)

        if submitted:
            entry = {
                "date": str(log_date),
                "fasting_bs": bs_fasting,
                "pp_bs": bs_pp,
                "evening_bs": bs_evening,
                "weight": weight,
                "bp": f"{bp_sys}/{bp_dia}",
                "shoulder_pain": shoulder_pain,
                "shoulder_rom": shoulder_rom,
                "did_exercises": did_exercises,
                "headache": headache,
                "neuro_symptoms": neuro_symptoms,
                "exercise": exercise_done,
                "pranayama": pranayama,
                "sleep": sleep_hours,
                "mood": mood,
                "notes": notes
            }
            st.session_state["logs"].append(entry)

            # Show alerts
            alerts = []
            if bs_fasting > 180: alerts.append("🚨 Fasting blood sugar is very high — call your doctor")
            if bs_fasting > 0 and bs_fasting < 70: alerts.append("🚨 Blood sugar is LOW — eat glucose immediately")
            if headache >= 7: alerts.append("🚨 Severe headache — seek medical attention today")
            if neuro_symptoms: alerts.append(f"⚠️ Neurological symptoms noted: {', '.join(neuro_symptoms)} — inform your doctor if new or worsening")
            if bp_sys > 160: alerts.append("⚠️ Blood pressure is high — contact your doctor")

            if alerts:
                for alert in alerts:
                    st.error(alert)
            else:
                st.success("✅ Log saved! Keep up the great work tracking your health.")

    # Show log history
    if st.session_state["logs"]:
        st.markdown("---")
        st.markdown("### 📈 Recent Log History")
        df = pd.DataFrame(st.session_state["logs"])
        st.dataframe(df, use_container_width=True)

        if len(st.session_state["logs"]) >= 2:
            st.markdown("#### Blood Sugar Trend")
            bs_data = df[df["fasting_bs"] > 0][["date", "fasting_bs", "pp_bs"]].set_index("date")
            st.line_chart(bs_data)
