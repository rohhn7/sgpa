import streamlit as st
from PIL import Image

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="SIT AIML Portal", page_icon="🎓", layout="centered")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
    /* Force Centering for Header & Logo */
    .stImage {
        display: flex;
        justify-content: center;
    }
    
    .header-container {
        text-align: center;
        margin-bottom: 20px;
    }
    
    /* Mobile Card Styling */
    .result-card {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        border-top: 6px solid #059669;
        margin: 20px 0;
    }

    /* Large Touch-Friendly Buttons */
    .stButton>button {
        width: 100%;
        height: 60px;
        border-radius: 12px;
        background: #059669;
        color: white;
        font-weight: 700;
        font-size: 1.1rem;
        border: none;
        margin-top: 10px;
    }

    /* Styling Inputs for readability */
    .stNumberInput label p {
        font-size: 1rem;
        font-weight: 600;
        color: #1e293b;
    }
</style>
""", unsafe_allow_html=True)

# ---------- CENTERED HEADER ----------
st.markdown("<div class='header-container'>", unsafe_allow_html=True)
try:
    # Use use_container_width=False with a specific width for centering
    st.image("logo.png", width=160)
except:
    st.markdown("### 🎓 SIT MANGALURU")

st.markdown("""
    <h2 style='margin-bottom:0;'>Srinivas Institute of Technology</h2>
    <p style='color:#64748b; font-size:1.1rem; font-weight:500;'>Dept. of Artificial Intelligence & Machine Learning</p>
    <hr style='border:0.5px solid #e2e8f0;'>
    </div>
""", unsafe_allow_html=True)

# ---------- DATA (ALL 8 SEMESTERS) ----------
sem_subjects = {
    "3rd Semester": {
        "Mathematics for Computer Science (BCS301)": 4,
        "Digital Design & Computer Organization (BCS302)": 4,
        "Operating Systems (BCS303)": 4,
        "Data Structures (BCS304)": 3,
        "Data Structures Laboratory (BCSL305)": 1,
        "Object Oriented Programming with Java (BCS306A)": 3,
        "Social Connectivity And Responsibility (BSCK307)": 1,
        "Data Analytics With Excel (BCS358A)": 1
    },
    "4th Semester": {
        "Mathematics for Artificial Intelligence (BCS401)": 4,
        "Computer Networks (BCS402)": 4,
        "Database Management Systems (BCS403)": 4,
        "Analysis & Design of Algorithms (BCS404)": 3,
        "Analysis & Design of Algorithms Lab (BCSL405)": 1,
        "Python Programming (BCS406A)": 3,
        "Constitution of India & Professional Ethics (BSCK407)": 1
    },
    "5th Semester": {
        "Data Mining & Data Warehousing (BCS501)": 4,
        "Deep Learning (BCS502)": 4,
        "Natural Language Processing (BCS503)": 4,
        "Artificial Intelligence Lab (BCSL504)": 3,
        "Big Data Analytics (BCS505A)": 3,
        "Soft Skills & Communication (BSCK506)": 1
    },
    "6th Semester": {
        "Computer Vision (BCS601)": 4,
        "Reinforcement Learning (BCS602)": 4,
        "Cloud Computing (BCS603)": 3,
        "AI Capstone Project Lab (BCSL604)": 3,
        "Entrepreneurship & Management (BSCK605)": 1
    },
    "7th Semester": {
        "Advanced Machine Learning (BCS701)": 4,
        "Robotics & AI (BCS702)": 4,
        "IoT & Smart Systems (BCS703)": 3,
        "AI System Design Lab (BCSL704)": 3
    },
    "8th Semester": {
        "Project Work Phase-2 (BCS801)": 6,
        "Internship / Professional Practice (BCS802)": 4,
        "Technical Seminar (BCS803)": 1
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
    
    st.markdown(f"**Enter Marks for {selected_sem}:**")
    marks_input = {}
    for sub, credit in current_subjects.items():
        marks_input[sub] = st.number_input(
            f"{sub} (Cr: {credit})", 
            min_value=0, max_value=100, value=None, step=1,
            key=f"sgpa_{sub}"
        )

    if st.button("Calculate SGPA"):
        if None in marks_input.values():
            st.error("❌ Please fill all marks.")
        else:
            total_p = sum(get_gp(m) * current_subjects[s] for s, m in marks_input.items())
            total_c = sum(current_subjects.values())
            res_sgpa = total_p / total_c
            
            st.markdown(f"""
                <div class='result-card'>
                    <p style='color:#64748b; font-weight:bold;'>{selected_sem.upper()} RESULT</p>
                    <h1 style='color:#059669; font-size:3.5rem; margin:0;'>{res_sgpa:.2f}</h1>
                </div>
            """, unsafe_allow_html=True)

with tab2:
    st.markdown("**Enter SGPA for each Semester:**")
    cgpa_list = []
    
    # Single column for CGPA as requested
    for i in range(1, 9):
        val = st.number_input(f"Semester {i} SGPA", 0.0, 10.0, step=0.01, value=None, key=f"cgpa_sem_{i}")
        if val is not None:
            cgpa_list.append(val)
            
    if st.button("Calculate Final CGPA"):
        if cgpa_list:
            final_res = sum(cgpa_list) / len(cgpa_list)
            st.balloons()
            st.markdown(f"""
                <div class='result-card' style='border-top-color:#1e293b;'>
                    <p style='color:#64748b; font-weight:bold;'>FINAL CUMULATIVE CGPA</p>
                    <h1 style='color:#1e293b; font-size:3.5rem; margin:0;'>{final_res:.2f}</h1>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("⚠️ Enter at least one Semester SGPA.")
