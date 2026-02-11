import streamlit as st
from PIL import Image

st.set_page_config(page_title="SIT AIML SGPA Calculator", layout="centered")

# ---------- LOGO ----------
try:
    logo = Image.open("logo.png")
    col1, col2, col3 = st.columns([1.2, 2, 5])
    with col2:
        st.image(logo, width=180)
except:
    st.warning("Logo file not found")

st.markdown("<h2 style='text-align: center;'>Srinivas Institute of Technology</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Artificial Intelligence & Machine Learning</h4>", unsafe_allow_html=True)

st.title("SGPA & CGPA Calculator")
st.subheader("3rd Semester - 2022 Scheme")

# ---------- SUBJECTS ----------
subjects = {
    "Mathematics for CS (BCS301)": 4,
    "Digital Design & CO (BCS302)": 4,
    "Operating Systems (BCS303)": 4,
    "Data Structures (BCS304)": 3,
    "Data Structures Lab (BCSL305)": 1,
    "OOP with Java (BCS306A)": 3,
    "Social Connectivity And Responsibility (BSCK307)": 1,
    "Data Analytics With Excel (BCS358A)": 1
}

st.markdown("### Enter Marks for SGPA")

marks_dict = {}

for subject, credit in subjects.items():
    marks = st.text_input(
        f"{subject} (Credits: {credit})",
        placeholder="Enter marks",
        key=subject
    )
    marks_dict[subject] = marks

# ---------- GRADE FUNCTION ----------
def calculate_grade_point(marks):
    if marks >= 90:
        return 10
    elif marks >= 80:
        return 9
    elif marks >= 70:
        return 8
    elif marks >= 60:
        return 7
    elif marks >= 50:
        return 6
    elif marks >= 40:
        return 4
    else:
        return 0

# ---------- SGPA CALCULATION ----------
if st.button("Calculate SGPA"):
    total_credits = 0
    total_points = 0
    all_filled = True

    for subject, credit in subjects.items():
        marks = marks_dict[subject]
        if marks == "" or marks is None:
            all_filled = False
            break
        try:
            marks = int(marks)
            if 0 <= marks <= 100:
                gp = calculate_grade_point(marks)
                total_credits += credit
                total_points += gp * credit
            else:
                st.warning(f"Marks for {subject} must be between 0 and 100")
                all_filled = False
                break
        except:
            st.warning(f"Please enter valid number for {subject}")
            all_filled = False
            break

    if all_filled and total_credits > 0:
        sgpa = total_points / total_credits
        st.success(f"Your SGPA is: {round(sgpa, 2)}")
    elif total_credits == 0:
        st.warning("Please enter marks to calculate SGPA.")

# ---------- CGPA SECTION (Simple Average) ----------
st.markdown("---")
st.subheader("CGPA Calculator (Simple Average)")

sgpa1 = st.text_input("Enter 1st Semester SGPA", placeholder="SGPA 1", key="cgpa1")
sgpa2 = st.text_input("Enter 2nd Semester SGPA", placeholder="SGPA 2", key="cgpa2")
sgpa3 = st.text_input("Enter 3rd Semester SGPA", placeholder="SGPA 3", key="cgpa3")

if st.button("Calculate CGPA"):
    sgpa_list = [sgpa1, sgpa2, sgpa3]
    
    if all(sgpa != "" for sgpa in sgpa_list):
        try:
            sgpa_list = [float(sgpa) for sgpa in sgpa_list]
            cgpa = sum(sgpa_list) / len(sgpa_list)
            st.success(f"Your CGPA after 3 semesters is: {round(cgpa, 2)}🎉")
        except:
            st.warning("Please enter valid SGPA values.")
    else:
        st.warning("Please enter all SGPA values.")




