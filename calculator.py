import streamlit as st
from PIL import Image

# ---------- MOBILE-FIRST CONFIG ----------
st.set_page_config(page_title="SIT AIML Calc", page_icon="🎓", layout="centered")

# ---------- MOBILE OPTIMIZED CSS ----------
st.markdown("""
<style>
    /* Prevent horizontal scrolling */
    .main { overflow-x: hidden; }
    
    /* Make buttons and inputs large for thumbs */
    .stButton>button {
        width: 100%;
        height: 55px; /* Large touch target */
        border-radius: 12px;
        font-size: 18px !important;
        font-weight: 700;
        background: #059669;
        margin-top: 10px;
    }
    
    /* Input field styling */
    .stNumberInput input {
        height: 45px !important;
        font-size: 16px !important;
    }

    /* Result Card */
    .mobile-result {
        background: #ffffff;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border: 2px solid #059669;
        margin: 20px 0;
    }

    /* Clean Header */
    .header-text {
        text-align: center;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
try:
    st.image("logo.png", width=120) # Center-aligned by default in 'centered' layout
except:
    st.markdown("<h3 style='text-align:center;'>🎓 SIT AIML</h3>", unsafe_allow_html=True)

st.markdown("""
    <div class='header-text'>
        <h2 style='margin-bottom:0;'>Grade Portal</h2>
        <p style='color:#64748b;'>Srinivas Institute of Technology</p>
    </div>
""", unsafe_allow_html=True)

# ---------- LOGIC ----------
def get_gp(m):
    if m >= 90: return 10
    if m >= 80: return 9
    if m >= 70: return 8
    if m >= 60: return 7
    if m >= 50: return 6
    if m >= 45: return 5
    if m >= 40: return 4
    return 0

sem_data = {
    "Sem 3": {"Maths":4, "DDCO":4, "OS":4, "DS":3, "DS Lab":1, "Java":3, "Social":1, "Excel":1},
    "Sem 4": {"Maths AI":4, "CN":4, "DBMS":4, "ML":3, "ML Lab":1, "Web":3, "Ethics":1},
    "Sem 5": {"Mining":4, "Deep L":4, "NLP":4, "AI Lab":3, "Big Data":3, "Soft Skills":1},
    # Add others as needed...
}

# ---------- TABS FOR MOBILE ----------
tab1, tab2 = st.tabs(["📊 SGPA", "📈 CGPA"])

with tab1:
    sel_sem = st.selectbox("Choose Semester", list(sem_data.keys()))
    subjects = sem_data[sel_sem]
    
    marks_entry = {}
    st.info("👇 Enter marks for each subject")
    
    # Single column layout for mobile scrolling
    for sub, cr in subjects.items():
        marks_entry[sub] = st.number_input(f"{sub} ({cr} Cr)", 0, 100, step=1, key=f"m_{sub}")

    if st.button("Calculate My SGPA"):
        total_p = sum(get_gp(m) * subjects[s] for s, m in marks_entry.items())
        total_c = sum(subjects.values())
        sgpa = total_p / total_c
        
        st.markdown(f"""
            <div class='mobile-result'>
                <p style='margin:0; color:#64748b;'>Your Result</p>
                <h1 style='margin:0; color:#059669;'>{sgpa:.2f}</h1>
            </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("#### Cumulative Average")
    cgpa_inputs = []
    # Using 2-column grid for CGPA to keep it compact but readable
    c1, c2 = st.columns(2)
    for i in range(1, 9):
        col = c1 if i % 2 != 0 else c2
        val = col.number_input(f"Sem {i}", 0.0, 10.0, step=0.01, key=f"c_{i}")
        if val > 0: cgpa_inputs.append(val)
        
    if st.button("Calculate Final CGPA"):
        if cgpa_inputs:
            res = sum(cgpa_inputs) / len(cgpa_inputs)
            st.balloons()
            st.markdown(f"""
                <div class='mobile-result' style='background:#1e293b; border-color:#10b981;'>
                    <p style='margin:0; color:#94a3b8;'>Final CGPA</p>
                    <h1 style='margin:0; color:#10b981;'>{res:.2f}</h1>
                </div>
            """, unsafe_allow_html=True)
