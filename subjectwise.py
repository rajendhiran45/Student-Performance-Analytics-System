import pandas as pd
import streamlit as st
import os

#subject wise analyse
def subjectwiseanalyze(rf):
    subjects = ['Tamil', 'English', 'Maths', 'Science', 'Social Science']
    sub_data=[]
    for sub in subjects:
        avg=rf[sub].mean()
        pass_count=len(rf[rf[sub]>=35])
        fail_count=len(rf[rf[sub]<35])
        sub_data.append([sub,avg,pass_count,fail_count])

    subject_df=pd.DataFrame(sub_data,columns=['Subject','Average','Pass','Fail'],)
    st.dataframe(subject_df,hide_index=True,use_container_width=True)


