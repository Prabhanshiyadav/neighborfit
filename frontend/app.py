import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.main import run_backend

st.set_page_config(page_title="NeighborFit", page_icon="🏘️", layout="centered")

# Sidebar Info
with st.sidebar:
    st.image("frontend/assets/image1.png", width=240)
    st.title("📘 NeighborFit")
    st.markdown(
        """
        **NeighborFit** is a smart neighborhood matching assistant that helps users discover communities aligned with their unique lifestyle needs.

        Whether you're looking for a peaceful family-friendly area, a buzzing nightlife hub, or a balance of parks and safety, NeighborFit uses data-driven algorithms to recommend the best neighborhoods for you.

        **How It Works**
        - You rate your preferences: 🛡️ safety, 🎉 nightlife, 🏫 schools, 🌳 parks  
        - We analyze neighborhood data  
        - We recommend top 5 matches ranked by score

        **Why Use It?**  
        ✅ Data-based suggestions  
        ✅ No login needed  
        ✅ Open-source, beginner-friendly  
        ✅ Works offline with CSV  

        ---
        ### 📚 Resources
        - [🧠 Streamlit Docs](https://docs.streamlit.io/)
        - [📦 Project Source on GitHub](https://github.com/your-repo-link)
        """
    )

st.markdown("<h1 style='text-align: center;'>🏡 NeighborFit</h1>", unsafe_allow_html=True)
st.subheader("🔍 Match Your Lifestyle with the Perfect Neighborhood")

# Interactive Sliders
st.markdown("### Choose your preferences:")

safety = st.slider("🛡️ Safety", 1, 5, 4)
nightlife = st.slider("🎉 Nightlife", 1, 5, 3)
schools = st.slider("🏫 School Quality", 1, 5, 5)
parks = st.slider("🌳 Parks & Greenery", 1, 5, 4)

if st.button("🚀 Find My Ideal Neighborhoods"):
    user_input = {
        "safety": safety,
        "nightlife": nightlife,
        "schools": schools,
        "parks": parks
    }
    results = run_backend(user_input)

    st.markdown("### 🌟 Top Recommendations:")

    for name, score in results:
        st.success(f"🏘️ **{name}** — Score: `{score}`")
        st.progress(min(score, 100) / 100)
