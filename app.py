"""
SunSafe AI v2.0
Professional Streamlit Dashboard
"""

import streamlit as st
from graph import run_agent

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="SunSafe AI",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

.main{
    padding-top:1rem;
}

.block-container{
    padding-top:1rem;
}

div[data-testid="metric-container"]{
    background:#f8f9fa;
    border:1px solid #e6e6e6;
    border-radius:12px;
    padding:15px;
}

h1{
    color:#ff9800;
}

.footer{
    text-align:center;
    color:gray;
    font-size:14px;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.title("☀ SunSafe AI")

    st.markdown("---")

    st.subheader("About")

    st.write(
        """
AI-powered Vitamin D recommendation system
built using:

- LangGraph
- Gemini
- Open-Meteo
- Rule Engine
- Streamlit
"""
    )

    st.markdown("---")

    st.subheader("Workflow")

    st.markdown("""
👤 User Profile

⬇

🌦 Weather API

⬇

⚠ Risk Assessment

⬇

⭐ Recommendation Engine

⬇

🤖 Gemini Explanation
""")

    st.markdown("---")

    st.subheader("Technology")

    st.write("Python")
    st.write("LangGraph")
    st.write("Gemini")
    st.write("Streamlit")

    st.markdown("---")

    st.caption("Version 2.0")

# ==========================================================
# HEADER
# ==========================================================

st.title("☀ SunSafe AI")

st.caption(
    "AI-powered Vitamin D Exposure Recommendation System"
)

st.divider()

# ==========================================================
# USER PROFILE
# ==========================================================

st.header("👤 User Profile")

skin_options = {
    "Type I - Very Fair": 1,
    "Type II - Fair": 2,
    "Type III - Medium": 3,
    "Type IV - Olive": 4,
    "Type V - Brown": 5,
    "Type VI - Dark Brown / Black": 6
}

body_options = {
    "Face Only (~10%)": 10,
    "Face + Arms (~25%)": 25,
    "Face + Arms + Legs (~50%)": 50,
    "Almost Full Body (~80%)": 80
}

left, right = st.columns(2)

with left:

    city = st.text_input(
        "📍 City",
        placeholder="Example: Kanpur"
    )

    selected_skin = st.selectbox(
        "🧑 Skin Type",
        list(skin_options.keys())
    )

with right:

    age = st.number_input(
        "🎂 Age",
        min_value=1,
        max_value=120,
        value=25
    )

    selected_body = st.selectbox(
        "🩳 Body Area Exposed",
        list(body_options.keys())
    )

skin = skin_options[selected_skin]
body = body_options[selected_body]

st.divider()

generate = st.button(
    "☀ Generate Recommendation",
    use_container_width=True,
    type="primary"
)




# ==========================================================
# RUN AI AGENT
# ==========================================================

if generate:

    if city.strip() == "":

        st.error("⚠ Please enter your city.")

        st.stop()

    with st.spinner(
        "🤖 Analyzing weather, calculating recommendation and generating AI explanation..."
    ):

        result = run_agent(
            city,
            skin,
            body,
            age
        )

    st.success("✅ Recommendation Generated Successfully!")

    st.divider()

    # ==========================================================
    # WEATHER SUMMARY
    # ==========================================================

    st.header("🌦 Today's Weather")

    weather1, weather2, weather3 = st.columns(3)

    with weather1:

        st.metric(
            "📍 Location",
            f"{result['city']}, {result['country']}"
        )

        st.metric(
            "🌡 Temperature",
            f"{result['temperature']} °C"
        )

    with weather2:

        st.metric(
            "☀ UV Index",
            result["uv_index"]
        )

        st.metric(
            "💊 Vitamin D Opportunity",
            result["vitamin_d_score"]
        )

    with weather3:

        if result["uv_index"] < 2:
            uv_status = "Very Low"

        elif result["uv_index"] < 5:
            uv_status = "Moderate"

        elif result["uv_index"] < 8:
            uv_status = "High"

        else:
            uv_status = "Very High"

        st.metric(
            "📈 UV Status",
            uv_status
        )

        st.metric(
            "⭐ Recommendation Score",
            f"{result['best_score']}/100"
        )

    st.progress(result["best_score"] / 100)

    st.divider()

    # ==========================================================
    # RISK ANALYSIS
    # ==========================================================

    st.header("⚠ Risk Assessment")

    risk1, risk2 = st.columns(2)

    with risk1:

        heat = result["heatstroke_risk"]

        if heat == "LOW":
            st.success("🟢 Heatstroke Risk : LOW")

        elif heat == "MODERATE":
            st.warning("🟡 Heatstroke Risk : MODERATE")

        else:
            st.error("🔴 Heatstroke Risk : HIGH")

    with risk2:

        burn = result["sunburn_risk"]

        if burn == "LOW":
            st.success("🟢 Sunburn Risk : LOW")

        elif burn == "MODERATE":
            st.warning("🟡 Sunburn Risk : MODERATE")

        else:
            st.error("🔴 Sunburn Risk : HIGH")

    st.divider()

    # ==========================================================
    # RECOMMENDATION CARD
    # ==========================================================

    st.header("⭐ Today's Recommendation")

    rec1, rec2 = st.columns(2)

    with rec1:

        st.metric(
            "🕘 Best Exposure Window",
            result["best_time"]
        )

        st.metric(
            "⏱ Recommended Duration",
            f"{result['recommended_duration']} minutes"
        )

    with rec2:

        st.metric(
            "💊 Vitamin D Rating",
            result["vitamin_d_score"]
        )

        st.metric(
            "🎯 Recommendation Score",
            f"{result['best_score']}/100"
        )

    st.success(
        f"🌞 Recommended exposure window:\n\n **{result['best_time']}**"
    )

    st.divider()
    
    # ==========================================================
    # EXPLAINABLE AI (RULE ENGINE)
    # ==========================================================

    st.header("🧠 Why this recommendation?")

    reasons = []

    # UV
    if 3 <= result["uv_index"] <= 6:
        reasons.append(
            "✅ UV Index is in the ideal range for Vitamin D production."
        )
    elif result["uv_index"] < 3:
        reasons.append(
            "⚠ UV Index is low, so a longer exposure duration is recommended."
        )
    else:
        reasons.append(
            "⚠ UV Index is high, therefore exposure duration has been reduced."
        )

    # Heatstroke
    if result["heatstroke_risk"] == "LOW":
        reasons.append(
            "✅ Heatstroke risk is low."
        )
    elif result["heatstroke_risk"] == "MODERATE":
        reasons.append(
            "🟡 Moderate heatstroke risk detected."
        )
    else:
        reasons.append(
            "🔴 High heatstroke risk detected. Limit exposure."
        )

    # Sunburn
    if result["sunburn_risk"] == "LOW":
        reasons.append(
            "✅ Sunburn risk is low."
        )
    elif result["sunburn_risk"] == "MODERATE":
        reasons.append(
            "🟡 Moderate sunburn risk detected."
        )
    else:
        reasons.append(
            "🔴 High sunburn risk detected."
        )

    # Body Area
    if body == 10:
        reasons.append(
            "👤 Only a small body area is exposed, increasing required duration."
        )
    elif body == 25:
        reasons.append(
            "🧍 Moderate body exposure slightly increases duration."
        )
    elif body == 50:
        reasons.append(
            "✅ Good body exposure provides balanced Vitamin D production."
        )
    else:
        reasons.append(
            "🌞 Large body exposure allows shorter recommended duration."
        )

    # Recommendation Score
    reasons.append(
        f"⭐ Overall Recommendation Score: {result['best_score']}/100"
    )

    for item in reasons:
        st.write(item)

    st.divider()

    # ==========================================================
    # GEMINI AI EXPLANATION
    # ==========================================================

    st.header("🤖 AI Explanation")

    with st.expander(
        "Click to view Gemini explanation",
        expanded=True
    ):
        st.write(result["explanation"])

    st.divider()

    # ==========================================================
    # SAFETY TIPS
    # ==========================================================

    st.header("🩺 General Safety Tips")

    st.info("""
• Stay hydrated before and after sun exposure.

• Wear sunglasses if outdoors for longer durations.

• Stop exposure immediately if you feel dizzy or excessively hot.

• Use sunscreen if remaining outdoors after the recommended duration.

• People with medical conditions or photosensitive disorders should consult a healthcare professional.
""")

    st.divider()

    # ==========================================================
    # DISCLAIMER
    # ==========================================================

    st.warning(
        """
This application provides general wellness guidance for Vitamin D exposure.

It is **NOT** medical advice.

Recommendations are generated using:
- Open-Meteo Weather API
- Rule-based Recommendation Engine
- Google Gemini AI for explanation

Always consult a healthcare professional for personalized medical advice.
"""
    )

# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.markdown(
    """
<div class="footer">

☀ <b>SunSafe AI v2.0</b><br>

Built using LangGraph • Gemini • Open-Meteo • Streamlit

Made with ❤️ as an AI Engineering Portfolio Project

</div>
""",
unsafe_allow_html=True
)