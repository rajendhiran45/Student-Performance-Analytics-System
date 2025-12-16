import pandas as pd
import streamlit as st
import os

#weak students
def showweakstd(rf):
    subjects = ['Tamil', 'English', 'Maths', 'Science', 'Social Science']
    rf['Average'] =rf[subjects].mean(axis=1)
    weakstd = rf[(rf['Status'] == 'FAIL') | (rf['Average'] <= 45)]
    weakstd=weakstd.sort_values(by='Average',ascending=False)
    weakstd = weakstd.reset_index(drop=True)
    weakstd.index = weakstd.index + 1
    
    #display
    st.title("WEAK STUDENTS")
    st.caption("Note: Only students with an average below 45 are shown as weak students.")
    st.dataframe(
        weakstd[['Register Number','Student Name','Section', 'Average']],
        hide_index=True,
        use_container_width=True
    )
