import streamlit as st
import pandas as pd
import os

#calculating total,avg,status
def calc(rf):
    
    subjects = ['Tamil', 'English', 'Maths', 'Science', 'Social Science']
    rf.index = rf.index + 1
    rf['Total'] = rf[subjects].sum(axis=1)
    rf['Average'] =rf[subjects].mean(axis=1)
    rf['Status'] = rf[subjects].apply(lambda row: 'FAIL' if (row < 35).any() else 'PASS',axis=1)
    return rf

#calculating grades 
def get_grade(rf):  
    def grade(avg):
        if avg >= 90:
            return 'O'
        elif avg >= 75:
            return 'A+'
        elif avg >= 60:
            return 'A'
        elif avg >= 50:
            return 'B'
        elif avg>=35 and avg<=49:
            return 'C'
        else:
            return 'F'

    rf['Grade'] = rf['Average'].apply(grade)
    return rf

#display
def show(rf):
    st.info("ALL STUDENTS RESULT")
    st.caption('The Grade Creteria:avg>=90:O , avg>=75:A+ , avg>=60:A, avg>=50:B, avg>35 and<=49:C, avg<=35:F')
    rf_sorted = rf.sort_values(by=['Section','Student Name'],ascending=[True, True])
    allstdreport=rf_sorted[['Register Number','Student Name', 'Section', 'Total', 'Average', 'Status', 'Grade']]
    st.dataframe(allstdreport,hide_index=True,use_container_width=True)



    