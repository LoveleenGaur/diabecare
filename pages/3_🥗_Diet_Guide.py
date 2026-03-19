import streamlit as st

st.set_page_config(page_title="Diet Guide · DiabeCare", page_icon="🥗", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Nunito', sans-serif; }
.section-header {
    background: linear-gradient(135deg, #5a2d00, #a05010);
    color: white; padding: 1.5rem 2rem; border-radius: 16px; margin-bottom: 1.5rem;
}
.food-card {
    background: white; border-radius: 14px; padding: 1.2rem 1.4rem;
    border: 2px solid #f0e8d8; margin-bottom: 0.8rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}
.food-card h4 { color: #5a2d00; font-weight: 700; margin-bottom: 0.3rem; }
.food-card .gi-badge {
    display: inline-block; padding: 2px 10px; border-radius: 20px;
    font-size: 0.75rem; font-weight: 700; margin-bottom: 0.5rem;
}
.gi-low { background: #d4f7d4; color: #1a6a1a; }
.gi-medium { background: #fff3cd; color: #856404; }
.gi-high { background: #f8d7da; color: #842029; }
.meal-card {
    background: #fffaf4; border: 2px solid #f0e8d8; border-radius: 14px;
    padding: 1.2rem 1.4rem; margin-bottom: 1rem;
}
.herb-card {
    background: #f0faf0; border: 2px solid #c0e8c0; border-radius: 14px;
    padding: 1.2rem 1.4rem; margin-bottom: 0.8rem;
}
.herb-card h4 { color: #1a5a1a; font-weight: 700; }
.avoid-card {
    background: #fff0f0; border: 2px solid #f0c0c0; border-radius: 14px;
    padding: 1.2rem 1.4rem; margin-bottom: 0.8rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-header">
    <h2>🥗 South Indian Vegetarian Diet Guide for Diabetes</h2>
    <p>Healing foods from our own culture — backed by Ayurveda and modern nutrition science</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🌾 Healing Foods", "🍽️ Meal Plan", "🌿 Herbs & Remedies", "❌ Foods to Avoid", "🧪 Recipes"
])

# ─── TAB 1: HEALING FOODS ───
with tab1:
    st.markdown("### 🌾 Best Foods for Diabetic South Indians")
    st.info("**GI (Glycemic Index):** Low GI foods raise blood sugar slowly — perfect for diabetics. Always prefer Low GI options.")

    foods = [
        {
            "name": "Ragi (Finger Millet) / ராகி / రాగి",
            "gi": "Low (54)", "gi_class": "gi-low",
            "why": "Exceptionally high in calcium, iron & fibre. Slows glucose absorption dramatically. Great for frozen shoulder recovery as calcium strengthens bones and collagen.",
            "how": "Ragi idli, ragi mudde, ragi dosa, ragi kanji (porridge), ragi laddoo (jaggery-free)"
        },
        {
            "name": "Foxtail Millet (Thinai) / தினை / కొర్రలు",
            "gi": "Low (50)", "gi_class": "gi-low",
            "why": "Ancient South Indian grain — rich in B vitamins and magnesium. Magnesium improves insulin sensitivity. High fibre keeps you full longer.",
            "how": "Thinai pongal, thinai upma, thinai rice as substitute for white rice"
        },
        {
            "name": "Bitter Gourd (Pavakka/Karela) / பாவக்காய் / కాకరకాయ",
            "gi": "Very Low", "gi_class": "gi-low",
            "why": "Contains plant insulin (polypeptide-p) that mimics insulin. Multiple studies show it lowers blood sugar. Also anti-inflammatory — helps shoulder.",
            "how": "Pavakka thoran (Kerala stir-fry), karela curry, stuffed bitter gourd, 30ml fresh juice (morning, empty stomach — not more)"
        },
        {
            "name": "Drumstick / Moringa (Murungakkai) / முருங்கைக்காய்",
            "gi": "Very Low", "gi_class": "gi-low",
            "why": "Called 'miracle tree' — packed with vitamins, anti-inflammatory compounds, and isothiocyanates that lower blood sugar. Great for neurological health too.",
            "how": "Sambar with drumstick (must!), moringa leaf rice, moringa chutney, moringa powder in buttermilk"
        },
        {
            "name": "Fenugreek (Vendhayam/Methi) / வெந்தயம் / మెంతులు",
            "gi": "Very Low", "gi_class": "gi-low",
            "why": "Soluble fibre (galactomannan) slows carb absorption. Proven to lower fasting blood sugar and HbA1c. Also reduces inflammation in shoulder joint.",
            "how": "Soak 1 tsp seeds overnight, drink water + eat seeds on empty stomach. Methi dosa, vendhayam kuzhambu, methi thepla"
        },
        {
            "name": "Horse Gram (Kollu) / கொள்ளு / ఉలవలు",
            "gi": "Low (29)", "gi_class": "gi-low",
            "why": "One of lowest GI legumes. Rich in protein, iron and anti-diabetic compounds. Traditional Tamil medicine for diabetes.",
            "how": "Kollu rasam (amazing!), kollu sundal, kollu chutney, sprouted kollu salad"
        },
        {
            "name": "Curry Leaves (Karuvepillai) / கறிவேப்பிலை",
            "gi": "Very Low", "gi_class": "gi-low",
            "why": "Contains mahanimbine alkaloids that stimulate insulin secretion. Studies show regular consumption reduces fasting blood sugar. Do NOT discard them!",
            "how": "Eat the leaves in your curry — don't push them aside! Curry leaf chutney, curry leaf rice, curry leaf rasam"
        },
        {
            "name": "Raw Banana (Vazhakkai) / வாழைக்காய் / అరటిపండు",
            "gi": "Low (45)", "gi_class": "gi-low",
            "why": "High in resistant starch which is not digested — acts like fibre. Great substitute for potato. Rich in potassium (good for BP).",
            "how": "Vazhakkai poriyal, raw banana curry, steamed raw banana slices with curd"
        },
        {
            "name": "Buttermilk (Mor/Majjiga) / மோர் / మజ్జిగ",
            "gi": "Very Low", "gi_class": "gi-low",
            "why": "Probiotic-rich, cooling, excellent for gut health. Good gut bacteria improve insulin sensitivity. Great summer drink for diabetics.",
            "how": "Plain thin buttermilk with curry leaves + cumin + ginger. Mor kuzhambu. Avoid sweetened versions."
        },
        {
            "name": "Jackfruit Seeds (Palakkai Vithai) / பலாச்சுளை விதை",
            "gi": "Low", "gi_class": "gi-low",
            "why": "High protein, high fibre legume substitute. Rich in B vitamins. Emerging research on anti-diabetic properties.",
            "how": "Boiled jackfruit seeds with coconut chutney, jackfruit seed curry, dried and powdered as flour"
        },
        {
            "name": "Brown Rice / Red Rice (Sigappu Arisi) / சிகப்பு அரிசி",
            "gi": "Medium (55–65)", "gi_class": "gi-medium",
            "why": "Far better than white rice — retains bran layer with fibre, magnesium, and B vitamins. Always preferred over polished white rice.",
            "how": "Use as main rice. Combine with lots of sambar/rasam/dal to lower the overall GI of the meal."
        },
        {
            "name": "Turmeric (Manjal) / மஞ்சள் / పసుపు",
            "gi": "Negligible", "gi_class": "gi-low",
            "why": "Curcumin is powerfully anti-inflammatory — directly helps frozen shoulder and brain inflammation. Studies show it improves insulin sensitivity.",
            "how": "Golden milk (haldi doodh with warm milk — use plant milk), turmeric rice, add generously to all cooking. Black pepper increases absorption 2000%."
        },
    ]

    for food in foods:
        st.markdown(f"""
        <div class="food-card">
            <h4>{food['name']}</h4>
            <span class="gi-badge {food['gi_class']}">GI: {food['gi']}</span>
            <p><strong>Why it helps:</strong> {food['why']}</p>
            <p><strong>How to use:</strong> {food['how']}</p>
        </div>
        """, unsafe_allow_html=True)

# ─── TAB 2: MEAL PLAN ───
with tab2:
    st.markdown("### 🍽️ Sample 7-Day South Indian Diabetic Meal Plan")
    st.success("**Golden Rule:** Eat small portions every 3–4 hours. Never skip meals. Eat your largest meal at lunch, lightest at dinner.")

    days = {
        "Monday": {
            "early_morning": "Warm water + 1 tsp soaked fenugreek seeds (vendhayam)",
            "breakfast": "2 Ragi idli + sambar with drumstick + green chutney (no coconut excess)",
            "mid_morning": "1 small guava or 1 small orange",
            "lunch": "1 cup red rice + kollu rasam + bitter gourd curry (pavakka poriyal) + 1 cup curd",
            "evening": "Small cup of buttermilk (mor) + handful roasted horse gram (kollu)",
            "dinner": "2 small ragi dosa + sambar + raw banana curry"
        },
        "Tuesday": {
            "early_morning": "Warm water + 5 curry leaves (eat them)",
            "breakfast": "Foxtail millet upma (thinai upma) with vegetables + 1 boiled egg white optional",
            "mid_morning": "Cucumber slices with lemon",
            "lunch": "1 cup broken wheat (dalia) rice + sambar + beans poriyal + rasam",
            "evening": "Carrot + cucumber sticks with groundnut chutney",
            "dinner": "2 small idli + drumstick sambar + turmeric milk (before bed)"
        },
        "Wednesday": {
            "early_morning": "30ml fresh bitter gourd juice (karela juice) — only if tolerated",
            "breakfast": "Oats pongal (oats cooked like ven pongal with pepper-cumin) + coconut chutney (small)",
            "mid_morning": "A small pear or papaya",
            "lunch": "1 cup brown rice + dal (toor dal) + ridge gourd curry (peerkangai) + mor",
            "evening": "Sprouted green gram (sundal) — very healthy snack",
            "dinner": "Keerai kootu (spinach with lentils) + 2 small chapati (wheat)"
        },
        "Thursday": {
            "early_morning": "Warm coriander seed water (drink 1 glass — boil, cool, drink)",
            "breakfast": "Pesarattu (green moong dosa) — protein-rich, low GI + ginger chutney",
            "mid_morning": "1 small apple",
            "lunch": "Ragi mudde (2 small balls) + bisi bele bath (small portion) + mor",
            "evening": "Moringa leaf tea or curry leaf buttermilk",
            "dinner": "Vegetable sambar with lots of drumstick + 1 small portion rice"
        },
        "Friday": {
            "early_morning": "Warm water + 1 tsp soaked fenugreek + 2 soaked almonds",
            "breakfast": "Idli with sambar (2 idli only) + green chutney",
            "mid_morning": "Coconut water (small, unsweetened — excellent for brain health)",
            "lunch": "Jackfruit seed curry + red rice (small) + rasam + pappad (1 only)",
            "evening": "Roasted makhana (fox nuts) — anti-inflammatory",
            "dinner": "Vegetable dalia khichdi + curd"
        },
        "Saturday": {
            "early_morning": "Warm turmeric water (1/4 tsp turmeric + 1/4 tsp pepper in warm water)",
            "breakfast": "Barnyard millet (kudiraivali) pongal + chutney",
            "mid_morning": "Amla (Indian gooseberry) — 1–2 fresh or juice (no sugar)",
            "lunch": "Horse gram rasam rice + ash gourd (poosanikai) curry + mor",
            "evening": "Peanuts (small handful, roasted)",
            "dinner": "Wheat chapati (2) + dal + stir-fried greens"
        },
        "Sunday": {
            "early_morning": "Warm water + curry leaves (10 leaves, chew them)",
            "breakfast": "Ven pongal (small) made with millet + pepper-ghee — festival special with portion control!",
            "mid_morning": "Guava + 1 small pomegranate (pomegranate is excellent for brain)",
            "lunch": "Red rice + mixed vegetable sambar + raw banana poriyal + rasam + curd",
            "evening": "Buttermilk + handful of roasted chana dal (pottu kadalai)",
            "dinner": "Light — idli (1–2) + sambar or just kanji (congee) with vegetables"
        }
    }

    selected_day = st.selectbox("📅 View meal plan for:", list(days.keys()))
    day_plan = days[selected_day]

    meal_icons = {
        "early_morning": ("🌅", "Early Morning (5:30–6 AM)"),
        "breakfast": ("🍽️", "Breakfast (7:30–8 AM)"),
        "mid_morning": ("🍎", "Mid-Morning Snack (10–10:30 AM)"),
        "lunch": ("🍛", "Lunch (1–1:30 PM)"),
        "evening": ("🌿", "Evening Snack (4–5 PM)"),
        "dinner": ("🌙", "Dinner (7–7:30 PM)")
    }

    for key, (icon, label) in meal_icons.items():
        st.markdown(f"""
        <div class="meal-card">
            <strong>{icon} {label}</strong><br>
            {day_plan[key]}
        </div>
        """, unsafe_allow_html=True)

# ─── TAB 3: HERBS & REMEDIES ───
with tab3:
    st.markdown("### 🌿 Traditional South Indian Herbs & Natural Remedies")
    st.warning("Always consult your doctor before starting any herbal remedy — some interact with diabetes medications.")

    herbs = [
        {
            "name": "Fenugreek Seeds (Vendhayam) — The #1 Diabetic Herb",
            "what": "Soak 1 teaspoon in water overnight. Eat seeds and drink water first thing in morning on empty stomach.",
            "why": "Galactomannan fibre slows glucose absorption. Multiple clinical trials show 20–30% reduction in fasting blood sugar. Also reduces joint inflammation.",
            "tip": "Do this every single day. Takes 4–6 weeks to see results.",
            "safety": "Safe. May cause mild gas initially — start small."
        },
        {
            "name": "Bitter Gourd Juice (Karela/Pavakka) — Plant Insulin",
            "what": "Extract 30–50ml of fresh bitter gourd juice. Drink on empty stomach, 3–4 times a week.",
            "why": "Contains polypeptide-p, charantin, and vicine — all act like plant insulin. Traditional Siddha and Ayurvedic medicine for diabetes for centuries.",
            "tip": "Mix with 1/2 tsp lemon juice to make it more tolerable. Do NOT take more than 50ml — excess can cause hypoglycemia.",
            "safety": "Monitor blood sugar carefully — can lower it significantly."
        },
        {
            "name": "Curry Leaves (Karuvepillai) — Morning Ritual",
            "what": "Eat 10–15 fresh curry leaves on empty stomach every morning. Chew them thoroughly.",
            "why": "Mahanimbine compound stimulates insulin production. Also anti-oxidant, neuroprotective — great for brain health.",
            "tip": "If you can't eat them raw, make curry leaf chutney with no coconut or fry in a small amount of oil.",
            "safety": "Completely safe. Available in any South Indian kitchen."
        },
        {
            "name": "Moringa (Murungai) Leaves — Superfood for Brain & Blood Sugar",
            "what": "Add fresh leaves to dal, sambar, or make moringa leaf rice. Or use 1 tsp moringa powder in buttermilk daily.",
            "why": "Contains isothiocyanates that lower blood sugar. Rich in Vitamin C, iron, and antioxidants. Emerging evidence for neurological protection.",
            "tip": "Drumstick sambar daily is an easy way to get moringa in your diet.",
            "safety": "Very safe. Avoid moringa root and bark (these can be harmful)."
        },
        {
            "name": "Turmeric + Black Pepper (Manjal + Milagu) — Anti-Inflammation",
            "what": "Golden milk: warm milk + 1/4 tsp turmeric + pinch of black pepper + 1/4 tsp cinnamon. Drink before bed.",
            "why": "Curcumin is one of nature's most powerful anti-inflammatories. Black pepper (piperine) increases curcumin absorption by 2000%. Directly targets shoulder inflammation and brain inflammation.",
            "tip": "Use plant milk (almond/oat) if regular milk raises blood sugar. This is one of the best things you can do for your friend!",
            "safety": "Safe at culinary doses. High supplement doses — consult doctor."
        },
        {
            "name": "Coriander Seeds (Dhaniya) Water",
            "what": "Boil 2 tsp coriander seeds in 2 cups water. Reduce to 1 cup. Cool and drink morning.",
            "why": "Stimulates insulin secretion from pancreatic beta cells. Traditional Siddha remedy with modern research backing.",
            "tip": "You can add this to your morning routine alongside fenugreek water.",
            "safety": "Safe. May lower blood pressure — monitor if on BP medications."
        },
        {
            "name": "Amla (Indian Gooseberry / Nellikkai) — Vitamin C Powerhouse",
            "what": "1–2 fresh amla or 30ml amla juice (no sugar) daily.",
            "why": "Chromium in amla regulates carbohydrate metabolism. Powerful antioxidant. Protects brain cells from oxidative stress. Great for frozen shoulder's connective tissue repair.",
            "tip": "Fresh amla is best. If using dried, take powder with warm water. Excellent immunity booster too.",
            "safety": "Safe. Avoid if on blood thinners."
        },
        {
            "name": "Cinnamon (Pattai) — Blood Sugar Regulator",
            "what": "Add 1/2 tsp Ceylon cinnamon (not Cassia) to warm water or golden milk daily.",
            "why": "Improves insulin sensitivity and glucose uptake by cells. Studies show modest but consistent reduction in fasting blood sugar.",
            "tip": "Use Ceylon cinnamon (true cinnamon) — Cassia cinnamon in large amounts can harm liver.",
            "safety": "Safe in small culinary amounts. Supplement doses — consult doctor."
        },
    ]

    for herb in herbs:
        st.markdown(f"""
        <div class="herb-card">
            <h4>🌿 {herb['name']}</h4>
            <p><strong>How to use:</strong> {herb['what']}</p>
            <p><strong>Why it works:</strong> {herb['why']}</p>
            <p><strong>💡 Tip:</strong> {herb['tip']}</p>
            <p><strong>🛡️ Safety:</strong> {herb['safety']}</p>
        </div>
        """, unsafe_allow_html=True)

# ─── TAB 4: FOODS TO AVOID ───
with tab4:
    st.markdown("### ❌ Foods to Avoid — Strict List for Diabetics")
    st.error("These foods will spike your blood sugar rapidly and worsen inflammation in the shoulder and brain. Discipline here is medicine.")

    avoid_list = [
        ("White rice in large quantities", "Very High GI (72+)", "Switch to red rice, brown rice, or millets. If you must have white rice, reduce portion to 1/2 cup max and add lots of sambar/rasam."),
        ("Maida (All-Purpose Flour) products", "Very High GI (85)", "This means: parotta, white bread, naan, biscuits, cake, pastry, samosa, puri. Replace with whole wheat or millet alternatives."),
        ("Sweet tea & coffee", "High sugar load", "Switch to tea/coffee with no sugar or use stevia. A cup of sweet chai has 2–4 tsp sugar — that's huge."),
        ("Fruit juices (even fresh)", "Very High GI", "Whole fruit is OK (fibre slows absorption). Juice removes all fibre — it's liquid sugar. A glass of mango juice = 6 tsp sugar instantly."),
        ("South Indian sweets: Payasam, Halwa, Ladoo, Mysore Pak", "Extremely High GI", "Festival foods are the enemy. Have a tiny taste only if absolutely necessary. Make sugar-free versions with stevia/jaggery for yourself."),
        ("Fried snacks: Murukku, Chakli, Banana chips, Vadai", "High GI + High fat", "These cause a double spike — trans fats worsen insulin resistance AND blood sugar spikes. Replace with roasted horse gram, peanuts, or sprouted legumes."),
        ("Polished white sugar", "GI 65+", "Every teaspoon counts. Switch to small amounts of jaggery (slightly lower GI) or stevia."),
        ("White potato (Urulaikizhangu)", "High GI (78)", "Replace with raw banana, yam (chenai), or sweet potato (small amounts). Sweet potato is much lower GI."),
        ("Packaged breakfast cereals (cornflakes etc.)", "Very High GI (80+)", "These are marketed as healthy but are terrible for diabetics. Choose ragi/millet-based homemade alternatives."),
        ("Alcohol", "Dangerous for diabetics", "Interacts with diabetes medications, can cause dangerous hypoglycemia, and damages nerves (worsening neuropathy that contributes to frozen shoulder)."),
        ("Very salty foods (pappad in excess, pickles, salted snacks)", "High sodium", "Raises blood pressure — dangerous with brain swelling. A small amount of homemade pickle is OK."),
        ("Red meat, processed meat", "Not applicable (vegetarian)", "Already not an issue! Great advantage — vegetarian diet is naturally better for diabetes."),
    ]

    for food, gi, note in avoid_list:
        st.markdown(f"""
        <div class="avoid-card">
            <h4>❌ {food}</h4>
            <p><strong>Why:</strong> {gi}</p>
            <p><strong>What to do instead:</strong> {note}</p>
        </div>
        """, unsafe_allow_html=True)

# ─── TAB 5: RECIPES ───
with tab5:
    st.markdown("### 🧪 Healing Recipe Cards")

    recipes = {
        "Kollu Rasam (Horse Gram Soup)": {
            "desc": "A powerful anti-diabetic traditional Tamil soup — tastes amazing and works like medicine",
            "ingredients": [
                "1/2 cup horse gram (kollu) — soaked 8 hrs",
                "2 tomatoes", "10 curry leaves", "1 tsp cumin",
                "1 tsp pepper", "1/2 tsp turmeric", "Tamarind (small ball)",
                "Asafoetida (hing) — pinch", "Salt to taste", "Mustard seeds, curry leaves for tempering"
            ],
            "method": [
                "Pressure cook horse gram for 3–4 whistles. Collect the water (this is the medicine!)",
                "Boil tomatoes with tamarind water, turmeric, and salt",
                "Add the horse gram water (not the cooked gram themselves — save for chutney)",
                "Add cumin, pepper powder",
                "Temper with mustard, hing, curry leaves in 1/2 tsp oil",
                "Drink 1 cup before lunch daily"
            ],
            "benefit": "Lowest GI legume, extremely rich in iron and protein, traditional diabetic remedy"
        },
        "Ragi Kanji (Finger Millet Porridge)": {
            "desc": "Perfect breakfast — keeps you full for 4–5 hours without spiking blood sugar",
            "ingredients": [
                "3 tbsp ragi flour", "2 cups water",
                "1/4 tsp cumin powder", "Pinch of salt",
                "1/2 cup thin buttermilk (to add at end)",
                "Optional: curry leaves, green chilli"
            ],
            "method": [
                "Mix ragi flour with 1/2 cup cold water (no lumps)",
                "Bring remaining 1.5 cups water to boil",
                "Add ragi mixture slowly, stirring constantly",
                "Cook on low flame 5–7 minutes until thick",
                "Add salt, cumin",
                "Cool slightly, add buttermilk, mix well",
                "Temper curry leaves in drops of oil, add on top"
            ],
            "benefit": "Richest plant source of calcium — excellent for frozen shoulder bone and collagen repair"
        },
        "Anti-Inflammatory Golden Milk": {
            "desc": "Have every night before bed — fights shoulder inflammation while you sleep",
            "ingredients": [
                "1 cup warm milk (dairy or almond/oat milk)",
                "1/4 tsp turmeric powder",
                "1/4 tsp cinnamon (Ceylon)",
                "1 pinch black pepper (crucial — activates curcumin)",
                "1/4 tsp dried ginger (sukku)",
                "A few drops of stevia or tiny pinch of jaggery (optional)"
            ],
            "method": [
                "Warm milk (don't boil)",
                "Add all spices and whisk well",
                "Drink warm before bed",
                "Do this every single night"
            ],
            "benefit": "Curcumin + piperine combo is clinically proven to reduce inflammation in joints and brain"
        },
    }

    for recipe_name, recipe in recipes.items():
        with st.expander(f"🍲 {recipe_name}"):
            st.markdown(f"*{recipe['desc']}*")
            st.markdown(f"**🎯 Why this recipe:** {recipe['benefit']}")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**🛒 Ingredients:**")
                for item in recipe["ingredients"]:
                    st.markdown(f"- {item}")
            with col2:
                st.markdown("**👩‍🍳 Method:**")
                for i, step in enumerate(recipe["method"], 1):
                    st.markdown(f"**{i}.** {step}")
