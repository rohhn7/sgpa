import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="SIT AIML SGPA & CGPA Calculator", layout="centered")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
/* 1. Basic UI Styling */
body { background-color: #f5f7fa; color: #1c1c1c; }
h2 { color: #1b4f72; }
h4 { color: #e67e22; }
.stButton>button {
    background-color: #1abc9c;
    color: white;
    height: 40px;
    width: 100%;
    border-radius:10px;
    font-size: 16px;
}

/* 2. COMPLETELY HIDE THE "CALCULATING..." BAR & SPINNER */
/* This prevents the "Calculating..." message from appearing for both SGPA and CGPA */
[data-testid="stStatusWidget"], 
.stStatusWidget, 
div[class*="stStatusWidget"],
div[data-testid="stHeader"] {
    display: none !important;
    visibility: hidden !important;
    height: 0px !important;
}

/* 3. Input field styling */
.stNumberInput>div>div>input {
    height: 35px;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# ---------- LOGO ----------
try:
    logo = Image.open("logo.png")
    buffered = BytesIO()
    logo.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    st.markdown(
        f"<div style='text-align:center; margin-top:10px; margin-bottom:20px;'>"
        f"<img src='data:image/png;base64,{img_str}' width='180'/></div>",
        unsafe_allow_html=True
    )
except:
    pass

# ---------- TITLE ----------
st.markdown("<h2 style='text-align: center;font-size:29px;'>Srinivas Institute of Technology</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;font-size:20px;'>Artificial Intelligence & Machine Learning</h4>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# ---------- GRADE FUNCTION ----------
def calculate_grade_point(marks):
    if marks >= 90: return 10
    elif marks >= 80: return 9
    elif marks >= 70: return 8
    elif marks >= 60: return 7
    elif marks >= 50: return 6
    elif marks >= 40: return 4
    else: return 0

# ---------- SUBJECTS PER SEM ----------
sem_subjects = {
    "3": {"Mathematics for CS (BCS301)":4, "Digital Design & CO (BCS302)":4, "Operating Systems (BCS303)":4, "Data Structures (BCS304)":3, "Data Structures Lab (BCSL305)":1, "OOP with Java (BCS306A)":3, "Social Connectivity And Responsibility (BSCK307)":1, "Data Analytics With Excel (BCS358A)":1},
    "4": {"Mathematics for AI (BCS401)":4, "Computer Networks (BCS402)":4, "Database Management (BCS403)":4, "Machine Learning Basics (BCS404)":3, "ML Lab (BCSL405)":1, "Web Programming (BCS406A)":3, "Professional Ethics (BSCK407)":1},
    "5": {"Data Mining (BCS501)":4, "Deep Learning (BCS502)":4, "NLP (BCS503)":4, "AI Lab (BCSL504)":3, "Big Data Analytics (BCS505A)":3, "Soft Skills (BSCK506)":1},
    "6": {"Computer Vision (BCS601)":4, "Reinforcement Learning (BCS602)":4, "Cloud Computing (BCS603)":3, "AI Project Lab (BCSL604)":3, "Entrepreneurship (BSCK605)":1},
    "7": {"Advanced ML (BCS701)":4, "Robotics AI (BCS702)":4, "IoT & AI (BCS703)":3, "AI Project Lab 2 (BCSL704)":3},
    "8": {"AI Thesis (BCS801)":6, "Internship Evaluation (BCS802)":4}
}

# ---------- SGPA CALCULATOR ----------
selected_sem = st.selectbox("Select Semester", options=["3","4","5","6","7","8"])
subjects = sem_subjects[selected_sem]
marks_dict = {}

for sub, crd in subjects.items():
    marks_dict[sub] = st.number_input(f"{sub} (Cr: {crd})", 0, 100, value=None, key=f"sgpa_{selected_sem}_{sub}")

if st.button(f"Calculate SGPA for Sem {selected_sem}"):
    if None not in marks_dict.values():
        pts = sum(calculate_grade_point(m) * subjects[s] for s, m in marks_dict.items())
        total_c = sum(subjects.values())
        st.success(f"🎉 Semester {selected_sem} SGPA: {round(pts/total_c, 2)}")
    else:
        st.warning("⚠️ Please fill all marks.")

# ---------- CGPA CALCULATOR ----------
st.markdown("<hr>", unsafe_allow_html=True)
st.subheader("CGPA Calculator")
cgpa_inputs = [st.number_input(f"Sem {i} SGPA", 0.0, 10.0, value=None, key=f"cgpa_{i}") for i in range(1, 9)]

if st.button("Calculate Final CGPA"):
    valid_sgpas = [v for v in cgpa_inputs if v is not None]
    if valid_sgpas:
        final_val = sum(valid_sgpas) / len(valid_sgpas)
        st.success(f"🎉 Your final CGPA: {round(final_val, 2)}")
    else:
        st.warning("⚠️ Enter at least one SGPA.")
