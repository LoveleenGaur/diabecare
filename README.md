# 🌿 DiabeCare — AI Health Companion for Diabetic Patients

> *"Rooted in South Indian wisdom · Powered by modern AI"*

A comprehensive Streamlit app built with **Groq + LLaMA** to help diabetic patients — especially those dealing with **frozen shoulder**, **neurological complications**, and **blood sugar management**. Tailored for **South Indian vegetarian patients**.

---

## 🌟 Features

| Page | What It Offers |
|------|---------------|
| 💬 **AI Assistant** | 24/7 AI health chatbot (Groq-powered) with diabetes expertise |
| 🧘 **Exercises** | Frozen shoulder physio, yoga, pranayama, daily routines |
| 🥗 **Diet Guide** | South Indian diabetic meal plans, healing foods, recipes |
| ✅ **Do's & Don'ts** | Critical daily guidelines for diabetes + frozen shoulder + brain health |
| 📊 **Monitor** | What to track, target ranges, daily log with charts |
| 💪 **Inspiration** | Real recovery stories, daily affirmations, community wisdom |

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/diabecare.git
cd diabecare
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Get a FREE Groq API Key
- Visit [console.groq.com](https://console.groq.com)
- Sign up for free
- Create an API key
- It's completely free for personal use!

### 4. Set up your API key (two options)

**Option A: Via the app sidebar** (easiest)
Just paste your key in the sidebar when you open the app — no setup needed.

**Option B: Via secrets file** (for deployment)
```bash
mkdir -p .streamlit
echo 'GROQ_API_KEY = "your_key_here"' > .streamlit/secrets.toml
```

### 5. Run the app
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501` 🎉

---

## 📁 Project Structure

```
diabecare/
│
├── app.py                          # 🏠 Home / Landing page
│
├── pages/
│   ├── 1_💬_AI_Assistant.py        # AI chatbot (Groq + LLaMA)
│   ├── 2_🧘_Exercises.py           # Physio, yoga, pranayama
│   ├── 3_🥗_Diet_Guide.py          # South Indian diet & recipes
│   ├── 4_✅_Dos_and_Donts.py       # Guidelines & warning signs
│   ├── 5_📊_Monitor.py             # Tracking & daily log
│   └── 6_💪_Stories.py             # Inspiration & affirmations
│
├── .streamlit/
│   ├── config.toml                 # Theme configuration
│   └── secrets.toml                # API keys (create this yourself)
│
├── requirements.txt
└── README.md
```

---

## 🤖 AI Models Supported (via Groq — all FREE)

| Model | Speed | Best For |
|-------|-------|----------|
| `llama-3.3-70b-versatile` | Fast | Best quality, recommended |
| `llama-3.1-8b-instant` | Fastest | Quick answers |
| `mixtral-8x7b-32768` | Fast | Long conversations |
| `gemma2-9b-it` | Fast | Alternative option |

---

## 🧠 What the AI Knows

The AI assistant is specifically trained with knowledge about:

- **Diabetes management**: Blood sugar targets, HbA1c, medications, hypoglycemia/hyperglycemia
- **Frozen shoulder**: All 3 stages, physiotherapy exercises, steroid considerations for diabetics
- **Brain/neurological health**: Cerebral edema warning signs, neuropathy, when to go to ER
- **South Indian vegetarian diet**: Ragi, millets, horse gram (kollu), moringa, bitter gourd, traditional remedies
- **Herbs & Ayurveda**: Fenugreek, curry leaves, turmeric, amla — with science-backed explanations
- **Yoga & Pranayama**: Anulom Vilom, Bhramari, modified yoga for frozen shoulder
- **Emergency recognition**: Will clearly flag when symptoms require immediate medical attention

---

## 🥗 Diet Philosophy

This app follows a **South Indian therapeutic diet** approach:
- Emphasizes **millets** (ragi, thinai, kudiraivali) over white rice
- Champions **traditional ingredients**: kollu rasam, moringa sambar, bitter gourd, horse gram
- Provides **7-day meal plans** with authentic South Indian dishes adapted for diabetes
- Includes **healing recipes** like Kollu Rasam, Ragi Kanji, Golden Milk
- Uses Tamil/Telugu/Kannada names alongside English for authenticity

---

## 🧘 Exercise Program

### Frozen Shoulder Recovery
1. Pendulum (Codman's) Exercise
2. Wall Finger Walking
3. Towel Stretch (Internal Rotation)
4. Cross-Body Stretch
5. Doorway Stretch (External Rotation)

### Yoga (Modified for Frozen Shoulder)
- Vrikshasana (Tree Pose) — modified
- Sukhasana + Neck Rolls
- Marjaryasana (Cat-Cow)
- Shavasana (Deep Relaxation)
- Balasana (Child's Pose) — modified

### Pranayama
- Anulom Vilom (Alternate Nostril Breathing)
- Bhramari (Humming Bee Breath)
- Kapalbhati — slow version
- Surya Nadi

---

## 📊 Health Monitoring

Track all key diabetic health metrics:
- Fasting & post-meal blood sugar
- Blood pressure
- Weight
- Shoulder range of motion
- Neurological symptoms
- HbA1c, kidney function (reminders for lab tests)
- Daily log with trend charts

---

## ⚕️ Medical Disclaimer

> This application provides **health education and information only**. It is **not a substitute** for professional medical advice, diagnosis, or treatment. Always consult your doctor, physiotherapist, or specialist before:
> - Starting any new exercise routine
> - Changing medications
> - Beginning any herbal remedy
> - Making significant dietary changes
>
> **For emergencies: Call 112 (India) or go to your nearest hospital immediately.**

---

## 🚀 Deploy to Streamlit Cloud (Free)

1. Push this project to your GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "New app" → Select your repo → Set `app.py` as main file
4. Add your Groq API key under **Settings → Secrets**:
   ```
   GROQ_API_KEY = "your_key_here"
   ```
5. Click Deploy — your app is live! 🎉

---

## 💡 Contributing

Have a healing story? A better recipe? A more effective exercise?

Open a Pull Request or Issue — let's build this together for the diabetic community. 🌿

---

## 🙏 Dedication

*Built with love for every diabetic patient who wakes up every morning and chooses to fight — especially those dealing with the compounded challenges of frozen shoulder and neurological complications. You are stronger than your diagnosis.*

**Remember: You are not alone on this journey. 🌿**

---

## 📄 License

MIT License — Free to use, share, and build upon. If you help someone with it, that's all the credit we need.
