import streamlit as st

st.set_page_config(page_title="Exercises · DiabeCare", page_icon="🧘", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Nunito', sans-serif; }
.section-header {
    background: linear-gradient(135deg, #2d4a7a, #4a6fa5);
    color: white; padding: 1.5rem 2rem; border-radius: 16px; margin-bottom: 1.5rem;
}
.exercise-card {
    background: white; border-radius: 14px; padding: 1.4rem;
    border: 2px solid #e8eef5; margin-bottom: 1rem;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}
.exercise-card h4 { color: #2d4a7a; font-size: 1.05rem; font-weight: 700; }
.exercise-card .sets { 
    display: inline-block; background: #e8f0fb; color: #2d4a7a;
    padding: 2px 10px; border-radius: 20px; font-size: 0.82rem; font-weight: 700;
    margin: 6px 0 10px;
}
.step-num {
    background: #2d4a7a; color: white; width: 24px; height: 24px;
    border-radius: 50%; display: inline-flex; align-items: center; justify-content: center;
    font-size: 0.8rem; font-weight: 700; margin-right: 8px; flex-shrink: 0;
}
.tip-box {
    background: #f0f7e6; border-left: 4px solid #4a9e3a;
    padding: 0.8rem 1rem; border-radius: 8px; font-size: 0.88rem; margin-top: 0.6rem;
}
.warning-box {
    background: #fff3cd; border-left: 4px solid #ffc107;
    padding: 0.8rem 1rem; border-radius: 8px; font-size: 0.88rem; margin-bottom: 1rem;
}
.yoga-card {
    background: #faf5ff; border: 2px solid #e0d0f5; border-radius: 14px;
    padding: 1.2rem; margin-bottom: 1rem;
}
.yoga-card h4 { color: #5a2d82; font-weight: 700; }
.pranayama-card {
    background: #f0faf5; border: 2px solid #b0e0cc; border-radius: 14px;
    padding: 1.2rem; margin-bottom: 1rem;
}
.pranayama-card h4 { color: #1a6a4a; font-weight: 700; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-header">
    <h2>🧘 Exercises & Physical Therapy</h2>
    <p>Safe, evidence-based exercises for frozen shoulder recovery, diabetes management & brain health — for South Indian patients</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="warning-box">
    ⚠️ <strong>Important:</strong> Always check your blood sugar <em>before</em> exercising. Don't exercise if blood sugar is below 100 mg/dL or above 300 mg/dL. Stop immediately if you feel dizzy, chest pain, or severe pain.
    <strong>Get your doctor's approval before starting any new exercise routine.</strong>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["🦴 Frozen Shoulder", "🧘 Yoga & Stretching", "🌬️ Pranayama", "🚶 Daily Activity"])

# ─── TAB 1: FROZEN SHOULDER ───
with tab1:
    st.markdown("### 🦴 Frozen Shoulder Exercises")
    st.info("**Stage matters!** If you are in the *Freezing stage* (very painful), focus only on pendulum and gentle ROM. In *Frozen* stage, add more stretches. In *Thawing*, add strengthening.")

    exercises = [
        {
            "name": "🔵 Pendulum Exercise (Codman's Exercise)",
            "sets": "3 sets × 10 circles each direction, 2× daily",
            "good_for": "All stages — especially freezing stage",
            "steps": [
                "Lean forward, rest your good arm on a table or chair back",
                "Let your affected arm hang loosely downward",
                "Gently swing the arm in small circles — clockwise 10 times",
                "Then counterclockwise 10 times",
                "Also swing forward-back and side-to-side",
                "Use gravity, not muscle force — let it dangle naturally"
            ],
            "tip": "Do this first thing in morning after a warm compress. The warmth loosens the joint capsule.",
            "avoid": "Don't force the range. Pain > 3/10 means stop."
        },
        {
            "name": "🟢 Wall Finger Walking (Ladder Stretch)",
            "sets": "2 sets × 10 reps, 2× daily",
            "good_for": "Frozen and Thawing stages",
            "steps": [
                "Stand facing a wall, about arm's length away",
                "Place your fingertips on the wall at waist height",
                "Walk your fingers slowly upward as far as comfortable",
                "Mark today's highest point with a small sticky note",
                "Hold at the top for 5 seconds, then walk back down",
                "Try to go 1 cm higher each week — track your progress!"
            ],
            "tip": "Mark your progress on the wall with a pencil — watching yourself improve each week is deeply motivating.",
            "avoid": "Don't shrug your shoulder — keep it down and relaxed."
        },
        {
            "name": "🟡 Towel Stretch (Internal Rotation)",
            "sets": "3 holds × 30 seconds, 2× daily",
            "good_for": "Frozen and Thawing stages",
            "steps": [
                "Hold a towel or dhoti behind your back — good arm on top",
                "Good arm gently pulls the towel upward",
                "This moves the affected arm behind your back (internal rotation)",
                "Hold for 30 seconds at a gentle stretch",
                "Release slowly, rest 30 seconds, repeat"
            ],
            "tip": "A long kitchen towel or old dupatta works perfectly.",
            "avoid": "Stop if you feel sharp pain — stretch should be a gentle pull, not pain."
        },
        {
            "name": "🔴 Cross-Body Stretch",
            "sets": "3 holds × 30 seconds, 2× daily",
            "good_for": "All stages for pain relief",
            "steps": [
                "Sit or stand upright",
                "Use your good arm to lift the affected arm at the elbow",
                "Gently bring it across your chest toward the opposite shoulder",
                "Hold for 30 seconds — feel a gentle stretch in the back of shoulder",
                "Release and repeat"
            ],
            "tip": "Apply a warm compress for 10 minutes before this exercise — it significantly improves how far you can stretch.",
            "avoid": "Never jerk or force the movement."
        },
        {
            "name": "🟣 Doorway Stretch (External Rotation)",
            "sets": "3 holds × 30 seconds, 1× daily",
            "good_for": "Thawing stage — restoring external rotation",
            "steps": [
                "Stand in a doorway",
                "Place your affected arm on the door frame, elbow at 90°",
                "Gently lean your body forward through the doorway",
                "You'll feel a stretch at the front of your shoulder",
                "Hold 30 seconds, step back, rest, repeat"
            ],
            "tip": "This is the exercise that finally restores the ability to put on a shirt! Very rewarding to feel progress here.",
            "avoid": "Skip this in the freezing stage — too much pain."
        },
    ]

    for ex in exercises:
        with st.expander(f"{ex['name']}  |  🎯 {ex['good_for']}", expanded=False):
            st.markdown(f"<span class='sets'>⏱️ {ex['sets']}</span>", unsafe_allow_html=True)
            st.markdown("**Steps:**")
            for i, step in enumerate(ex["steps"], 1):
                st.markdown(f"**{i}.** {step}")
            st.markdown(f"""<div class='tip-box'>💡 <strong>Pro Tip:</strong> {ex['tip']}</div>""", unsafe_allow_html=True)
            if ex.get("avoid"):
                st.markdown(f"""<div class='warning-box'>🚫 <strong>Avoid:</strong> {ex['avoid']}</div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🌡️ Heat & Cold Therapy")
    col1, col2 = st.columns(2)
    with col1:
        st.success("""
**✅ Warm Compress (BEFORE exercises)**
- Use a warm towel or heating pad
- Apply for 10–15 minutes before exercise
- Loosens the joint capsule
- Helps reduce stiffness
- Temperature: comfortably warm, not hot
        """)
    with col2:
        st.info("""
**🧊 Ice Pack (AFTER exercises)**
- Apply after exercise if inflamed/swollen
- 10 minutes max
- Wrap in cloth — never directly on skin
- Reduces post-exercise inflammation
- Diabetics: check skin frequently (reduced sensation)
        """)

# ─── TAB 2: YOGA ───
with tab2:
    st.markdown("### 🧘 Yoga Poses (Modified for Diabetics with Frozen Shoulder)")
    st.info("These are modified, gentle versions safe for frozen shoulder. Hold each pose gently — never force your range of motion.")

    yoga_poses = [
        {
            "name": "🌳 Vrikshasana (Tree Pose) — Modified",
            "benefit": "Balance, focus, blood sugar regulation",
            "how": "Stand near a wall for support. Place one foot on the inner calf (not knee). Bring hands only to heart center (Anjali mudra) — do NOT raise arms overhead if frozen shoulder is in freezing stage. Hold 30 sec each side.",
            "modification": "Keep affected arm at your side or lightly resting on the wall.",
            "diabetes_benefit": "Improves proprioception (balance often affected in diabetics due to neuropathy)"
        },
        {
            "name": "😊 Sukhasana (Easy Pose) + Neck Rolls",
            "benefit": "Stress relief, circulation, shoulder tension",
            "how": "Sit cross-legged on a folded blanket (use a chair if floor sitting is difficult). Close eyes. Slowly roll neck in gentle circles — 5 times each direction. Breathe deeply.",
            "modification": "Chair version is equally effective.",
            "diabetes_benefit": "Reduces cortisol (stress hormone that raises blood sugar)"
        },
        {
            "name": "🐱 Marjaryasana (Cat-Cow Pose)",
            "benefit": "Spine mobility, shoulder warm-up, circulation",
            "how": "On hands and knees. Inhale: arch back downward, lift head (cow). Exhale: round spine upward, tuck chin (cat). 10 slow rounds. Move only through comfortable range.",
            "modification": "If wrists hurt (diabetic arthropathy), do on fists or use yoga blocks.",
            "diabetes_benefit": "Massages abdominal organs including pancreas; improves insulin sensitivity"
        },
        {
            "name": "🧘 Shavasana (Corpse Pose)",
            "benefit": "Deep relaxation, stress & blood sugar reduction",
            "how": "Lie flat on your back. Arms slightly away from body, palms up (or affected arm resting comfortably by your side). Close eyes. Focus only on your breath for 10–15 minutes.",
            "modification": "Place a thin pillow under the affected shoulder if needed.",
            "diabetes_benefit": "Activates parasympathetic system — lowers blood sugar and blood pressure naturally"
        },
        {
            "name": "🙇 Balasana (Child's Pose) — Modified",
            "benefit": "Gentle shoulder stretch, relaxation",
            "how": "Kneel, sit back on heels. Slowly lower forehead toward the mat. Extend only the good arm forward — keep affected arm alongside your body. Hold 30–60 sec.",
            "modification": "Only extend the unaffected arm. Never force the shoulder forward.",
            "diabetes_benefit": "Calms nervous system, reduces anxiety which spikes blood sugar"
        },
    ]

    for pose in yoga_poses:
        st.markdown(f"""
        <div class="yoga-card">
            <h4>{pose['name']}</h4>
            <p><strong>🎯 Benefit:</strong> {pose['benefit']}</p>
            <p><strong>📋 How to do:</strong> {pose['how']}</p>
            <p><strong>🔄 Modification:</strong> {pose['modification']}</p>
            <p style="color:#4a9e3a;"><strong>🩺 Diabetes benefit:</strong> {pose['diabetes_benefit']}</p>
        </div>
        """, unsafe_allow_html=True)

# ─── TAB 3: PRANAYAMA ───
with tab3:
    st.markdown("### 🌬️ Pranayama (Breathing Exercises)")
    st.success("**Pranayama is one of the most powerful tools for diabetes.** Studies show regular pranayama reduces blood sugar, lowers cortisol, improves circulation, and even helps frozen shoulder by reducing systemic inflammation. Do these every morning on an empty stomach.")

    pranayamas = [
        {
            "name": "🌀 Anulom Vilom (Alternate Nostril Breathing)",
            "duration": "10–15 minutes daily",
            "how": [
                "Sit comfortably (Sukhasana or on a chair)",
                "Right hand: Ring finger closes left nostril, thumb closes right nostril",
                "Close right nostril with thumb. Inhale slowly through LEFT nostril (4 counts)",
                "Close both nostrils. Hold breath (4 counts) — skip holding if you have brain swelling",
                "Open right nostril. Exhale slowly through RIGHT nostril (8 counts)",
                "Inhale through RIGHT nostril (4 counts)",
                "Hold both (4 counts). Exhale through LEFT nostril (8 counts)",
                "This completes one round. Do 10–15 rounds."
            ],
            "benefit": "Balances nervous system, reduces blood sugar, lowers BP, improves oxygenation to brain",
            "caution": "If you have brain swelling/cerebral edema — SKIP the breath retention (kumbhaka). Just inhale and exhale without holding."
        },
        {
            "name": "🐝 Bhramari (Humming Bee Breath)",
            "duration": "5–10 minutes daily",
            "how": [
                "Sit comfortably. Close your eyes.",
                "Place index fingers gently on the tragus (the small flap of the ear)",
                "Take a slow deep breath in",
                "As you exhale, make a smooth humming sound like a bee: 'Mmmmmm'",
                "Feel the vibration in your head and chest",
                "Do 7–10 rounds slowly"
            ],
            "benefit": "Reduces headaches, calms anxiety, lowers blood pressure, very soothing for neurological symptoms",
            "caution": "Excellent for brain swelling patients — the vibration is therapeutic and calming."
        },
        {
            "name": "🔥 Kapalbhati (Skull-Shining Breath) — Modified",
            "duration": "3–5 minutes (start slow)",
            "how": [
                "Sit comfortably with straight spine",
                "Take a normal inhale",
                "Exhale sharply through the nose — pull the navel inward",
                "The inhale happens passively on its own",
                "Do slow rhythmic pumps — 1 per second (NOT the fast version)",
                "Start with 30 pumps, rest, do 2 more rounds"
            ],
            "benefit": "Stimulates pancreas, improves insulin sensitivity, energizes body, improves metabolism",
            "caution": "⚠️ Do the SLOW version only. Avoid if you have very high BP or active brain swelling/headache. Consult your neurologist first."
        },
        {
            "name": "☀️ Surya Nadi (Right Nostril Breathing)",
            "duration": "5 minutes in morning",
            "how": [
                "Close the left nostril with your ring finger",
                "Breathe in and out ONLY through the right nostril",
                "Slow, deep breaths — 4 counts in, 8 counts out",
                "Do for 5 minutes in the morning"
            ],
            "benefit": "Activates sympathetic system, warms the body, energizes — good for morning sluggishness in diabetics",
            "caution": "Don't do in evening — can disturb sleep."
        },
    ]

    for p in pranayamas:
        with st.expander(f"{p['name']}  |  ⏱️ {p['duration']}"):
            st.markdown(f"**🎯 Benefit:** {p['benefit']}")
            st.markdown("**📋 Steps:**")
            for i, step in enumerate(p["how"], 1):
                st.markdown(f"**{i}.** {step}")
            if "caution" in p:
                caution_color = "warning-box" if "⚠️" in p["caution"] else "tip-box"
                st.markdown(f"<div class='{caution_color}'>⚕️ <strong>Note:</strong> {p['caution']}</div>", unsafe_allow_html=True)

# ─── TAB 4: DAILY ACTIVITY ───
with tab4:
    st.markdown("### 🚶 Daily Activity & Walking Plan")

    st.markdown("""
    Walking is the **single best exercise** for Type 2 diabetics. It lowers blood sugar immediately after meals.
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 📅 Weekly Walking Plan")
        plan = {
            "Week 1–2": "10 min walk after lunch & dinner (20 min/day)",
            "Week 3–4": "15 min walk after each meal (45 min/day)",
            "Week 5–8": "20–30 min brisk walk in morning + 10 min after dinner",
            "Month 3+": "45–60 min total daily — mix of walking + shoulder exercises",
        }
        for week, target in plan.items():
            st.markdown(f"**{week}:** {target}")

        st.markdown("---")
        st.markdown("#### ✅ Walking Rules for Diabetics")
        st.markdown("""
- ✅ Check blood sugar before walking
- ✅ Walk 30 min after meals (best time for blood sugar control)
- ✅ Wear proper diabetic footwear — check feet daily
- ✅ Carry glucose tablets in case of hypoglycemia
- ✅ Walk with a companion when possible
- ❌ Never walk on an empty stomach
- ❌ Never walk barefoot
        """)

    with col2:
        st.markdown("#### 🌅 Ideal Daily Routine")
        routine = [
            ("5:30 AM", "Wake up, drink warm water with fenugreek seeds (soaked overnight)"),
            ("6:00 AM", "Pranayama — Anulom Vilom + Bhramari (20 min)"),
            ("6:30 AM", "Frozen shoulder exercises (pendulum + wall walking)"),
            ("7:30 AM", "Breakfast — Ragi idli / Oats upma / Foxtail millet pongal"),
            ("8:00 AM", "Morning medications with breakfast"),
            ("10:00 AM", "Short 10 min walk"),
            ("1:00 PM", "Lunch — see diet guide"),
            ("1:30 PM", "15 min post-lunch walk (most important!)"),
            ("4:00 PM", "Evening snack — buttermilk / small handful of roasted horse gram"),
            ("5:00 PM", "Yoga + shoulder stretches (20 min)"),
            ("7:30 PM", "Dinner — early, light"),
            ("8:00 PM", "Evening walk (15 min)"),
            ("9:00 PM", "Blood sugar check, medications"),
            ("9:30 PM", "Shavasana / Meditation (10 min) before bed"),
            ("10:00 PM", "Sleep — 7–8 hrs is essential for blood sugar regulation"),
        ]
        for time, activity in routine:
            st.markdown(f"**{time}** — {activity}")

    st.markdown("---")
    st.markdown("### 🚫 Exercises to AVOID with Frozen Shoulder")
    st.error("""
- ❌ Overhead pressing or lifting heavy weights
- ❌ Push-ups (especially early stages)
- ❌ Swimming (until late thawing stage — rotation can injure capsule)
- ❌ Throwing motions
- ❌ Sleeping on the affected shoulder
- ❌ Carrying heavy bags on the affected side
- ❌ Any exercise that causes pain > 3/10
    """)
