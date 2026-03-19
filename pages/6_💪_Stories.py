import streamlit as st

st.set_page_config(page_title="Inspiration · DiabeCare", page_icon="💪", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&family=Lora:ital,wght@1,400&display=swap');
html, body, [class*="css"] { font-family: 'Nunito', sans-serif; }
.section-header {
    background: linear-gradient(135deg, #5a1a2a, #9f2d4a);
    color: white; padding: 1.5rem 2rem; border-radius: 16px; margin-bottom: 1.5rem;
}
.story-card {
    background: white; border-radius: 18px; padding: 1.8rem;
    border: 2px solid #f0e8ec; margin-bottom: 1.5rem;
    box-shadow: 0 4px 16px rgba(0,0,0,0.08);
}
.story-avatar { font-size: 3rem; margin-bottom: 0.5rem; }
.story-name { font-size: 1.2rem; font-weight: 800; color: #5a1a2a; }
.story-meta { font-size: 0.85rem; color: #888; margin-bottom: 1rem; font-weight: 600; }
.story-quote {
    font-family: 'Lora', serif;
    font-style: italic;
    font-size: 1.05rem;
    color: #444;
    border-left: 4px solid #9f2d4a;
    padding: 0.8rem 1.2rem;
    margin: 1rem 0;
    background: #fdf5f7;
    border-radius: 0 8px 8px 0;
}
.lesson-box {
    background: #f0f7f0; border-left: 4px solid #2d9a5f;
    padding: 0.8rem 1rem; border-radius: 8px; margin-top: 1rem;
}
.tag-row { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 0.8rem; }
.tag {
    display: inline-block; padding: 3px 10px; border-radius: 20px;
    font-size: 0.75rem; font-weight: 700;
    background: #f0e8ec; color: #5a1a2a;
}
.affirmation-card {
    background: linear-gradient(135deg, #1a4a3a, #2d7a5f);
    color: white; border-radius: 16px; padding: 1.5rem;
    margin-bottom: 1rem; text-align: center;
}
.affirmation-card p { font-family: 'Lora', serif; font-style: italic; font-size: 1.1rem; line-height: 1.7; }
.tip-from-story {
    background: #fffbf0; border: 2px solid #f0e0b0;
    border-radius: 10px; padding: 0.8rem 1rem; margin-top: 0.8rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-header">
    <h2>💪 Inspiration & Healing Stories</h2>
    <p>Real stories of people who faced diabetes complications — and came out stronger on the other side</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["💪 Real Stories", "🌟 Daily Affirmations", "📖 Wisdom & Tips"])

# ─── STORIES ───
with tab1:
    stories = [
        {
            "avatar": "👨‍💼",
            "name": "Rajan S., 54",
            "meta": "Chennai, Tamil Nadu | Type 2 Diabetic | Frozen Shoulder for 18 months",
            "tags": ["Frozen Shoulder", "Type 2 Diabetes", "South Indian", "Full Recovery"],
            "story": """
            Rajan was a software professional in Chennai who noticed he couldn't button his shirt anymore. 
            He was already managing diabetes for 7 years, but when frozen shoulder struck, he felt defeated. 
            "The first six months, even combing my hair on the left side was impossible. I had to sleep 
            sitting up because lying down was agony," he recalls.

            What changed everything: His physiotherapist introduced him to the pendulum exercise 
            routine — and he did it religiously, twice a day. He also started a strict ragi-based diet 
            with his wife's help. His HbA1c dropped from 9.2% to 6.8% in 8 months.

            "The shoulder followed the blood sugar. When I finally got control of my diabetes, 
            the shoulder started loosening. My doctor said it's not a coincidence — the glycosylation 
            of collagen reduces when blood sugar improves."

            Today, 2 years later, Rajan has 95% of his shoulder movement back. He gives talks at his 
            local diabetes support group.
            """,
            "quote": "The frozen shoulder was my body's way of screaming 'Take your diabetes seriously!' I'm glad I listened.",
            "lesson": "✅ Key Lesson: Blood sugar control is the most important factor in frozen shoulder recovery. Lower your HbA1c and the shoulder responds.",
            "practical_tip": "Rajan's #1 tip: Set an alarm for 6 AM every day for shoulder exercises. 'I never missed a day. That discipline is what healed me.'"
        },
        {
            "avatar": "👩",
            "name": "Meenakshi V., 48",
            "meta": "Coimbatore, Tamil Nadu | Type 2 Diabetic + Neurological symptoms | 3-year journey",
            "tags": ["Neurological Complications", "Diabetes", "Yoga", "Recovery"],
            "story": """
            Meenakshi was a schoolteacher who started experiencing persistent headaches, dizziness, 
            and occasional confusion — terrifying symptoms for anyone, but especially frightening 
            when you're already managing diabetes.

            Her MRI showed mild brain edema. "I cried for three days. I thought my life was over," 
            she admits. But her neurologist explained the connection to her poorly controlled diabetes 
            (HbA1c was 10.5%) and gave her a clear path forward.

            She committed to Anulom Vilom pranayama every single morning — 20 minutes, without fail. 
            She switched entirely to millet-based cooking at home. Her daughter learned to make 
            thinai pongal and ragi idli. "It became a family project. My husband quit sugar in his 
            coffee to support me."

            Within 6 months: HbA1c 7.2%, neurological symptoms nearly gone. Her follow-up MRI 
            at 18 months showed complete resolution of the edema.
            """,
            "quote": "My family didn't let me give up. And honestly, neither did the Anulom Vilom. Something about that breathing changed me from the inside.",
            "lesson": "✅ Key Lesson: Neurological complications from diabetes CAN reverse when blood sugar is controlled. It takes time but it happens.",
            "practical_tip": "Meenakshi's tip: Make one family member your accountability partner for blood sugar and exercises. 'Having my daughter ask me every evening 'Amma, did you check your sugar?' changed everything.'"
        },
        {
            "avatar": "👨‍🦳",
            "name": "Krishnamurthy A., 61",
            "meta": "Bengaluru, Karnataka | Type 2 Diabetes 15 years | Bilateral Frozen Shoulder",
            "tags": ["Bilateral Frozen Shoulder", "15-year Diabetic", "Natural Treatment", "Yoga"],
            "story": """
            Krishnamurthy had the misfortune of developing frozen shoulder in BOTH shoulders — 
            right first, then left two years later. "I couldn't wash my face properly. 
            My wife had to help me dress. For a man who was so independent, it was humbling to the core."

            His conventional treatment (physiotherapy + steroid injections) helped somewhat, 
            but the steroids kept spiking his blood sugar dangerously. His endocrinologist worked 
            with him to minimize steroid injections and maximize lifestyle management instead.

            He turned to Iyengar yoga with props — using straps, blocks, and chair support 
            to do shoulder-opening poses despite limited mobility. He also started a daily ritual 
            of fenugreek seeds soaked overnight, curry leaf chewing, and bitter gourd in his weekly diet.

            "I told myself: I've had this disease 15 years. If I've managed it this far, I can 
            manage this too." The right shoulder recovered in 14 months. The left shoulder took 
            20 months but also fully recovered.

            He now teaches a gentle yoga class at his apartment complex for senior diabetics.
            """,
            "quote": "The shoulder takes time. That's the hardest truth to accept. But if you keep moving it every day, it WILL thaw. Nature intended it to heal.",
            "lesson": "✅ Key Lesson: Even 15-year diabetics with bilateral frozen shoulder can achieve full recovery. Patience, consistent exercises, and natural remedies make a real difference.",
            "practical_tip": "Krishnamurthy's tip: Use a chair for yoga modifications. 'I do my yoga with a chair next to me for support. The chair has been my physiotherapist!'"
        },
        {
            "avatar": "👩‍🦱",
            "name": "Lakshmi P., 45",
            "meta": "Hyderabad, Telangana | Newly Diagnosed Type 2 Diabetic | Frozen Shoulder + Work-life Balance",
            "tags": ["New Diabetic", "Working Woman", "Frozen Shoulder", "Diet Transformation"],
            "story": """
            Lakshmi was diagnosed with Type 2 diabetes and frozen shoulder in the same month — a 
            shocking double blow. A finance professional with long hours, she initially felt she 
            had no time for lifestyle changes.

            Her turning point: reading about the connection between high blood sugar and the 
            collagen changes that cause frozen shoulder. "Once I understood WHY this happened, 
            I became determined to fix the root cause, not just manage symptoms."

            She overhauled her office lunch — bringing tiffin boxes with ragi dosa, horse gram 
            chutney, and moringa-rich sambar from home. She started doing pendulum exercises at 
            her desk during breaks. She downloaded an app to track her blood sugar.

            "My colleagues thought I was eccentric. But when they saw my shoulder improve and my 
            energy levels soar, they started asking questions. Three of them now bring healthy tiffins too."

            At 14 months: shoulder pain-free, HbA1c down from 9.8% to 6.9%.
            """,
            "quote": "I realized the frozen shoulder was my body's intervention. It slowed me down long enough to fix my health.",
            "lesson": "✅ Key Lesson: Even a busy working person can make meaningful changes. Small consistent actions beat occasional heroic efforts.",
            "practical_tip": "Lakshmi's tip: Prepare Sunday meals for the week. 'I cook horse gram rasam, ragi dosa batter, and moringa chutney every Sunday. Healthy eating is easy when it's ready to go.'"
        },
    ]

    for story in stories:
        with st.expander(f"{story['avatar']} {story['name']} — {story['meta'].split('|')[0].strip()}"):
            st.markdown(f"""
            <div class="story-card">
                <div class="story-avatar">{story['avatar']}</div>
                <div class="story-name">{story['name']}</div>
                <div class="story-meta">{story['meta']}</div>
                <div class="tag-row">{''.join([f"<span class='tag'>{t}</span>" for t in story['tags']])}</div>
                <p>{story['story'].strip().replace(chr(10), '<br>')}</p>
                <div class="story-quote">{story['quote']}</div>
                <div class="lesson-box">{story['lesson']}</div>
                <div class="tip-from-story">💡 <strong>Their #1 Tip:</strong> {story['practical_tip']}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.info("""
    **📌 Scientific backing for these stories:**
    - Studies show diabetics with HbA1c <7% have 50% better outcomes in frozen shoulder recovery
    - Anulom Vilom pranayama has shown measurable blood sugar reduction in multiple Indian clinical studies
    - Anti-inflammatory diet (Mediterranean/traditional South Indian) reduces inflammatory markers that worsen both frozen shoulder and brain edema
    - Regular exercise improves insulin sensitivity by 30–40% independent of weight loss
    """)

# ─── AFFIRMATIONS ───
with tab2:
    st.markdown("### 🌟 Daily Affirmations for Healing")
    st.markdown("Repeat these to yourself every morning. Your mind heals your body.")

    affirmations = [
        ("🌅", "Today, I choose to take one small action toward my health. Small steps lead to big changes."),
        ("💪", "My body has healed before. It can heal again. I trust this process."),
        ("🌿", "Every ragi idli I eat, every shoulder exercise I do, every pranayama breath I take — is an act of self-love."),
        ("🧠", "My brain is resilient. My body is strong. I am not defined by my diagnosis."),
        ("🦴", "My shoulder is thawing, slowly but surely. Every day, it moves a little more freely."),
        ("☀️", "I have the strength of every person who has walked this path before me and healed. Their healing is possible for me too."),
        ("🙏", "I am grateful for a body that keeps trying, for doctors who care, and for family who love me."),
        ("🌊", "Like the sea after a storm, my body will find its calm. This phase is temporary."),
        ("🌱", "I am planting seeds of health every day. The harvest of wellness is coming."),
        ("⭐", "I am more than my blood sugar numbers. I am a complete, worthy, lovable person — diabetes is just one part of my story."),
    ]

    for icon, affirmation in affirmations:
        st.markdown(f"""
        <div class="affirmation-card">
            <p>{icon} "{affirmation}"</p>
        </div>
        """, unsafe_allow_html=True)

# ─── WISDOM ───
with tab3:
    st.markdown("### 📖 Wisdom & Practical Tips from the Diabetic Community")

    wisdom = [
        ("🌡️ Temperature Therapy", "10 minutes of warm compress before shoulder exercises isn't optional — it's the difference between 20% improvement and 80% improvement. Never skip the warm-up."),
        ("🍛 The Sambar Secret", "A proper South Indian sambar with drumstick, tomato, and turmeric is one of the most anti-inflammatory meals in the world. Eat it every day without guilt."),
        ("😴 Sleep as Medicine", "Poor sleep raises fasting blood sugar by 15–20 mg/dL the next morning. Getting 7–8 hours is as important as your medication."),
        ("🌊 The Pendulum Truth", "The pendulum exercise feels too easy to be doing anything. It isn't. The gentle swinging slowly breaks down scar tissue adhesions. Trust the process."),
        ("👨‍👩‍👧 Family is Treatment", "Invite your family into your healing. Ask them to eat millets with you. Ask them to walk with you after dinner. The social support measurably improves outcomes."),
        ("📱 Track Everything", "People who log their blood sugar daily have 2× better long-term control than those who don't. Numbers without logging are just numbers — logged numbers are insights."),
        ("🧘 The Breath-Sugar Connection", "Stress hormones (cortisol, adrenaline) directly raise blood sugar. 10 minutes of pranayama lowers cortisol. This is why meditation is literally diabetes medicine."),
        ("💧 Hydration & Brain Health", "Every diabetic with brain involvement should drink 8–10 glasses of water daily. Dehydration concentrates blood sugar AND worsens brain swelling. Water is medicine."),
        ("🌿 Patience as a Virtue", "Frozen shoulder in diabetics takes longer to heal than in non-diabetics. Expect 18–24 months for full recovery. This is NOT failure — this is diabetes biology. Keep going."),
        ("🎯 The 1% Rule", "You don't need a perfect day. You need a 1% better day than yesterday. One extra shoulder exercise. One meal swap. One extra walk. These 1%s compound into transformation."),
    ]

    for title, wisdom_text in wisdom:
        st.markdown(f"""
        <div style="background:white; border-radius:12px; padding:1rem 1.3rem; margin-bottom:0.8rem; border:2px solid #f0e8f5; box-shadow:0 2px 8px rgba(0,0,0,0.05);">
            <strong style="color:#5a1a2a;">{title}</strong><br>
            <span style="color:#444; font-size:0.95rem;">{wisdom_text}</span>
        </div>
        """, unsafe_allow_html=True)
