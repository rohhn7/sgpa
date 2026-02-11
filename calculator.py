import streamlit as st
from PIL import Image
from io import BytesIO
import base64

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="SIT AIML SGPA & CGPA Calculator", layout="centered")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
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
.stNumberInput>div>input {
    height: 35px;
    font-size: 16px;
}
.subject-label {
    font-weight: bold;
    margin-bottom: 3px;
    display: block;
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
    st.warning("Logo file not found. Make sure 'logo.png' is in the same folder as calculator.py")

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
    "3": {
        "Mathematics for CS (BCS301)":4, "Digital Design & CO (BCS302)":4,
        "Operating Systems (BCS303)":4, "Data Structures (BCS304)":3,
        "Data Structures Lab (BCSL305)":1, "OOP with Java (BCS306A)":3,
        "Social Connectivity And Responsibility (BSCK307)":1,
        "Data Analytics With Excel (BCS358A)":1
    },
    "4": {
        "Mathematics for AI (BCS401)":4, "Computer Networks (BCS402)":4,
        "Database Management (BCS403)":4, "Machine Learning Basics (BCS404)":3,
        "ML Lab (BCSL405)":1, "Web Programming (BCS406A)":3,
        "Professional Ethics (BSCK407)":1
    },
    "5": {
        "Data Mining (BCS501)":4, "Deep Learning (BCS502)":4,
        "NLP (BCS503)":4, "AI Lab (BCSL504)":3,
        "Big Data Analytics (BCS505A)":3, "Soft Skills (BSCK506)":1
    },
    "6": {
        "Computer Vision (BCS601)":4, "Reinforcement Learning (BCS602)":4,
        "Cloud Computing (BCS603)":3, "AI Project Lab (BCSL604)":3,
        "Entrepreneurship (BSCK605)":1
    },
    "7": {
        "Advanced ML (BCS701)":4, "Robotics AI (BCS702)":4,
        "IoT & AI (BCS703)":3, "AI Project Lab 2 (BCSL704)":3
    },
    "8": {
        "AI Thesis (BCS801)":6, "Internship Evaluation (BCS802)":4
    }
}

# ---------- SEMESTER DROPDOWN ----------
selected_sem = st.selectbox("Select Semester to calculate SGPA", options=["3","4","5","6","7","8"])
st.subheader(f"{selected_sem} Semester SGPA Calculator")

subjects = sem_subjects[selected_sem]

# ---------- SGPA INPUTS ----------
marks_dict = {}
for subject, credit in subjects.items():
    st.markdown(f'<span class="subject-label">{subject} (Credits:{credit})</span>', unsafe_allow_html=True)
    marks_dict[subject] = st.number_input("", min_value=1, max_value=100, step=1, format="%i", key=f"{selected_sem}_{subject}")

# ---------- CALCULATE SGPA ----------
semester_sgpas = {}
if st.button(f"Calculate SGPA for {selected_sem} Semester"):
    total_credits = 0
    total_points = 0
    all_filled = True
    for subject, credit in subjects.items():
        marks = marks_dict[subject]
        if marks < 1 or marks > 100:
            all_filled = False
            st.warning(f"⚠️ Enter valid marks for {subject} (1-100)")
            break
        gp = calculate_grade_point(marks)
        total_credits += credit
        total_points += gp * credit
    if all_filled and total_credits > 0:
        sgpa = total_points / total_credits
        semester_sgpas[selected_sem] = sgpa
        st.success(f"🎉 {selected_sem} Semester SGPA: {round(sgpa,2)}")

# ---------- CGPA INPUTS ----------
st.markdown("<hr>", unsafe_allow_html=True)
st.subheader("CGPA Calculator")

sgpa_inputs = {}
for sem in range(1,9):
    st.markdown(f'<span class="subject-label">{sem} Semester SGPA</span>', unsafe_allow_html=True)
    sgpa_inputs[sem] = st.number_input("", min_value=1.0, max_value=10.0, step=0.01, format="%.2f", key=f"manual_sgpa{sem}")

if st.button("Calculate Final CGPA"):
    sgpa_list = [sg for sg in sgpa_inputs.values() if sg >= 1]
    if sgpa_list:
        cgpa = sum(sgpa_list)/len(sgpa_list)
        st.success(f"🎉 Your final CGPA: {round(cgpa,2)}")
    else:
        st.warning("⚠️ Enter SGPA for at least one semester.")