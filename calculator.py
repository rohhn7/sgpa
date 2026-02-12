import streamlit as st
import base64

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="SIT AIML Portal", page_icon="🎓", layout="centered")

# ---------- HELPER FOR LOGO ENCODING ----------
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return None

# ---------- THE FINAL CENTERED CSS ----------
st.markdown(f"""
<style>
    /* 1. APP BACKGROUND */
    .stApp {{
        background-color: #0e1117;
    }}
    
    /* 2. HEADER SECTION */
    .main-header {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        width: 100%;
        padding-top: 10px;
    }}

    .logo-img {{
        width: 110px;
        height: auto;
        margin-bottom: 12px;
    }}

    .college-title {{
        color: #ffffff !important; 
        margin: 0px;
        font-weight: 600;
        font-size: 1.3rem !important;
        white-space: nowrap;
        line-height: 1.2;
    }}

    .dept-title {{
        color: #10b981 !important; 
        font-weight: 500;
        font-size: 0.9rem;
        margin-top: 6px;
        margin-bottom: 15px;
        opacity: 0.85;
    }}

    /* 3. INPUT LABELS */
    label p {{
        color: #ffffff !important; 
        font-size: 0.95rem !important;
        font-weight: 400 !important; 
        letter-spacing: 0.4px;
        opacity: 0.9;
    }}

    /* 4. BUTTONS */
    .stButton>button {{
        width: 100%;
        height: 52px;
        background: #059669;
        border-radius: 12px;
        color: white;
        font-weight: 600;
        border: none;
        margin-top: 10px;
    }}

    /* 5. THE ABSOLUTE CENTER RESULT CARD FIX */
    .result-card {{
        background-color: #1e293b;
        border-radius: 15px;
        padding: 30px 10px;
        border: 1px solid #334155;
        margin-top: 25px;
        /* Force strict center alignment */
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        width: 100%;
    }}

    .result-label {{
        color: #94a3b8; 
        font-weight: bold; 
        font-size: 0.85rem;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin: 0 !important;
        padding: 0 !important;
        display: block;
    }}

    .result-value {{
        color: inherit;
        font-weight: 700;
        font-size: 4rem !important;
        margin: 0 !important;
        padding: 0 !important;
        line-height: 1.1 !important;
        display: block;
    }}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER SECTION ----------
logo_base64 = get_base64_of_bin_file("logo.png")
if logo_base64:
    st.markdown(f"""
        <div class="main-header">
            <img src="data:image/png;base64,{logo_base64}" class="logo-img">
            <div class="college-title">Srinivas Institute of Technology</div>
            <div class="dept-title">Artificial Intelligence & Machine Learning</div>
            <hr style="width: 100%; border-color: #334155; opacity: 0.2; margin: 5px 0 20px 0;">
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <div class="main-header">
            <h1 style="color:white; font-size: 2.5rem; margin:0;">🎓</h1>
            <div class="college-title">Srinivas Institute of Technology</div>
            <div class="dept-title">Artificial Intelligence & Machine Learning</div>
        </div>
    """, unsafe_allow_html=True)

# ---------- CURRICULUM DATA ----------
sem_subjects = {
    "3rd Semester": {
        "Mathematics for Computer Science (BCS301)": 4, "Digital Design & CO (BCS302)": 4,
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
                    <div class='result-label'>SGPA</div>
                    <div class='result-value' style='color:#10b981;'>{res_sgpa:.2f}</div>
                </div>
            """, unsafe_allow_html=True)

with tab2:
    cgpa_list = []
    for i in range(1, 9):
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
                    <div class='result-label'>CGPA</div>
                    <div class='result-value' style='color:white;'>{final_res:.2f}</div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("⚠️ Enter at least one Semester SGPA.")
