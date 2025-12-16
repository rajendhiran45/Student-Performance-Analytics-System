import streamlit as st
import report as ik
import pandas as pd
import indreport as irp
import subjectwise as subj
import addstudentdata as ads
import topperformers as topper
import weakstd
import classanalytics
import about
import os


BAS_DIR=os.path.dirname(__file__)
CSV_PATH=os.path.join(BAS_DIR,"stddata.csv")

EXPECTED_COLUMNS = [
    'Register Number', 'Dob', 'Student Name', 'Section',
    'Tamil', 'English', 'Maths', 'Science', 'Social Science'
]

#ensure csv has header or not
def ensure_csv_header(path):
    # Case 1: File does not exist → create with header
    if not os.path.exists(path):
        pd.DataFrame(columns=EXPECTED_COLUMNS).to_csv(path, index=False)
        return

    # Case 2: File exists but is completely empty (0 bytes)
    if os.path.getsize(path) == 0:
        pd.DataFrame(columns=EXPECTED_COLUMNS).to_csv(path, index=False)
        return

    # Case 3: File exists but no header
    try:
        df = pd.read_csv(path, nrows=1)

        if list(df.columns) != EXPECTED_COLUMNS:
            df_full = pd.read_csv(path, header=None)
            df_full.columns = EXPECTED_COLUMNS
            df_full.to_csv(path, index=False)

    except pd.errors.EmptyDataError:
        pd.DataFrame(columns=EXPECTED_COLUMNS).to_csv(path, index=False)

ensure_csv_header(CSV_PATH)


#loading data
def load_data():
    df = pd.read_csv(CSV_PATH)
    df = ik.calc(df)
    df = ik.get_grade(df)
    df['Dob'] = df['Dob'].astype(str)   # safety
    return df
    

def dashboardop():
    rf = load_data() 
    if len(rf) == 0:
        st.warning("⚠️ No student data available. Please add students first.")
    st.title('Student Performance Analytics System')
    menu = st.selectbox(
        "Select Option",
        [
        "All Students Report",
        "Individual Student Report",
        "Class Analytics",
        "Subject Wise Analysis",
        "Top Performers",
        "Weak Students",
        "Add Students Data",
        "About"
    ]
    )
    

    if menu == "All Students Report":
        ik.show(rf)

    elif menu == "Individual Student Report":
        irp.indishow(rf)
       
    elif menu == "Class Analytics":
       classanalytics.class_analytics(rf)

    elif menu == "Subject Wise Analysis":
        subj.subjectwiseanalyze(rf)

    elif menu == "Top Performers":
        topper.toppersmenu(rf)

    elif menu == "Weak Students":
        weakstd.showweakstd(rf)

    elif menu == "Add Students Data":
        ads.addstddata(rf)

    elif menu=="About":
        about.credits()

    
dashboardop()
