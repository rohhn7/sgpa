import streamlit as st
from PIL import Image

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="SIT AIML Portal", page_icon="🎓", layout="centered")

# ---------- THE "AGGRESSIVE CENTER" CSS ----------
st.markdown("""
<style>
    /* 1. FORCE LOGO TO ABSOLUTE CENTER */
    /* Targets the div that contains the image */
    [data-testid="stHorizontalBlock"] {
        align-items: center;
    }
    
    [data-testid="stImage"] {
        display: flex;
        justify-content: center;
        margin-left: auto;
        margin-right: auto;
        width: 100% !important;
    }

    [data-testid="stImage"] > img {
        margin-left: auto;
        margin-right: auto;
    }

    /* 2. CENTER THE TEXT HEADER */
    .centered-header {
        text-align: center;
        width: 100%;
        margin-bottom: 20px;
    }

    /* 3. VISIBILITY FIX: LABELS BOLD & WHITE */
    label p {
        color: #FFFFFF !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        margin-bottom: 8px !important;
    }

    /* 4. BUTTON & CARD STYLING */
    .stButton>button {
        width: 100%;
        height: 55px;
        border-radius: 12px;
        background: #059669;
        color: white;
        font-weight: bold;
        font-size: 1.1rem;
        border: none;
    }

    .result-card {
        background-color: #1e293b;
        border-radius: 15px;
        padding: 25px;
        text-align: center;
        border: 2px solid #059669;
        margin-top: 25px;
    }
</style>
""", unsafe_allow_html=True)

# ---------- HEADER (CENTERED) ----------
# We use a column layout to help force the image to take up the full center width
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image("logo.png", width=160)
    except:
        st.markdown("<h2 style='text-align:center;'>🎓 SIT</h2>", unsafe_allow_html=True)

st.markdown("<div class='centered-header'>", unsafe_allow_html=True)
st.markdown("<h2 style='color: white; margin-top: 10px; margin-bottom: 0;'>Srinivas Institute of Technology</h2>", unsafe_allow_html=True)
st.markdown("<p style='color: #10b981; font-weight: 800; font-size: 1.2rem; margin-top: 5px;'>Artificial Intelligence & Machine Learning</p>", unsafe_allow_html=True)
st.markdown("<hr style='border-color: #334155;'>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ---------- CURRICULUM DATA ----------
sem_subjects = {
    "3rd Semester": {
        "Mathematics for Computer Science (BCS301)": 4, "Digital Design & Computer Organization (BCS302)": 4,
        "Operating Systems (BCS303)": 4, "Data Structures (BCS304)": 3, "Data Structures Lab (BCSL305)": 1,
        "OOP with Java (BCS306A)": 3, "Social Connectivity (BSCK307)": 1, "Data Analytics (BCS358A)": 1
    },
    "4th Semester": {
        "Mathematics for AI (BCS401)": 4, "Computer Networks (BCS402)": 4, "DBMS (BCS403)": 4,
        "Algorithms (BCS404)": 3, "Algorithms Lab (BCSL405)": 1, "Python (BCS406A)": 3, "Ethics (BSCK407)": 1
    },
    "5th Semester": {
        "Data Mining (BCS501)": 4, "Deep Learning (BCS502)": 4, "NLP (BCS503)": 4,
        "AI Lab (BCSL504)": 3, "Big Data (BCS505A)": 3, "Soft Skills (BSCK506)": 1
    },
    "6th Semester": {
        "Computer Vision (BCS601)": 4, "RL (BCS602)": 4, "Cloud (BCS603)": 3, "AI Project (BCSL604)": 3, "Entrepreneurship (BSCK605)": 1
    },
    "7th Semester": {
        "Advanced ML (BCS701)": 4, "Robotics (BCS702)": 4, "IoT (BCS703)": 3, "Design Lab (BCSL704)": 3
    },
    "8th Semester": {
        "Project Work (BCS801)": 6, "Internship (BCS802)": 4, "Seminar (BCS803)": 1
    }
}

def get_gp(marks):
    if marks >= 90: return 10
    elif marks >= 80: return 9
    elif marks >= 70: return 8
    elif marks >= 60: return 7
    elif marks >= 50: return 6
    elif marks >= 45: return 5
    elif marks >= 40: return 4
    else: return 0

# ---------- UI TABS ----------
tab1, tab2 = st.tabs(["📊 SGPA Calculator", "📈 CGPA Calculator"])

with tab1:
    selected_sem = st.selectbox("Select Your Semester", list(sem_subjects.keys()))
    current_subjects = sem_subjects[selected_sem]
    
    marks_input = {}
    for sub, credit in current_subjects.items():
        # Added 'placeholder' as requested
        marks_input[sub] = st.number_input(
            f"{sub} (Cr: {credit})", 
            min_value=0, max_value=100, value=None, step=1,
            placeholder="Enter the marks",
            key=f"sgpa_in_{sub}"
        )

    if st.button("Calculate SGPA"):
        if None in marks_input.values():
            st.error("⚠️ Please fill in all subject marks.")
        else:
            total_p = sum(get_gp(m) * current_subjects[s] for s, m in marks_input.items())
            total_c = sum(current_subjects.values())
            res_sgpa = total_p / total_c
            
            st.markdown(f"""
                <div class='result-card'>
                    <p style='color:#94a3b8; font-weight:bold;'>SEMESTER RESULT</p>
                    <h1 style='color:#10b981; font-size:4rem; margin:0;'>{res_sgpa:.2f}</h1>
                </div>
            """, unsafe_allow_html=True)

with tab2:
    st.markdown("<p style='color: white; font-weight: bold;'>Enter SGPA for each Semester:</p>", unsafe_allow_html=True)
    cgpa_list = []
    
    for i in range(1, 9):
        # Added 'placeholder' as requested
        val = st.number_input(
            f"Semester {i} SGPA", 
            min_value=0.0, max_value=10.0, value=None, step=0.01,
            placeholder="0.00",
            key=f"cgpa_sem_in_{i}"
        )
        if val is not None:
            cgpa_list.append(val)
            
    if st.button("Calculate Final CGPA"):
        if cgpa_list:
            final_res = sum(cgpa_list) / len(cgpa_list)
            st.balloons()
            st.markdown(f"""
                <div class='result-card' style='border-color:white;'>
                    <p style='color:#94a3b8; font-weight:bold;'>FINAL CGPA</p>
                    <h1 style='color:white; font-size:4rem; margin:0;'>{final_res:.2f}</h1>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("⚠️ Enter at least one Semester SGPA.")
