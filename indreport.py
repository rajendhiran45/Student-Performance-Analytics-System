import pandas as pd
import streamlit as st
import datetime as dt
import report
import os

#strong path
BAS_DIR=os.path.dirname(__file__)
CSV_PATH=os.path.join(BAS_DIR,"stddata.csv")
data=pd.read_csv(CSV_PATH)
rf=pd.DataFrame(data)
rf.index=rf.index+1

#calling calc anf get_grade function from report module to get total,avg,status and grades
rf=report.calc(rf)
rf=report.get_grade(rf)

#individual students report
def indishow(rf):
    reg_no=st.number_input("ENTER REGISTER NUMBER:",step=1,format="%d")
    d_b=st.date_input("ENTER DATE OF BIRTH",min_value=dt.date(1990,12,31))
    db=d_b.strftime("%Y-%m-%d")

    student=rf[(rf["Register Number"]==reg_no)&(rf['Dob']==db)]
    if student.empty:
        st.warning("STUDENT REGISTER NUMBER OR DATE OF BIRTH IS INVALID!")
    else:
        indshow(student)

#display individual students report
def indshow(student):
    st.info("STUDENT RESULT")
    st.dataframe(student)
