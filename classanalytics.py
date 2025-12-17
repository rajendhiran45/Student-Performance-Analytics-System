import pandas as pd
import streamlit as st
import altair as alt
import os

#class analytics
def class_analytics(rf):
    st.title("CLASS ANALYTICS")
    st.caption('CHOOSE CLASS WHICH IS TO BE ANALYZE')

    subjects = ['Tamil', 'English', 'Maths', 'Science', 'Social Science']

    select_class=st.selectbox("Select Class",sorted(rf['Section'].unique()))

    #calculating subject average
    class_df=rf[rf['Section']==select_class]
    class_df['Average']=class_df[subjects].mean(axis=1)

    #calculating total students 
    total_std=len(class_df)

    
     #calculating class average
    class_avg=class_df['Average'].mean()
    pass_count = len(class_df[class_df['Status'] == 'PASS'])
    fail_count = len(class_df[class_df['Status'] == 'FAIL'])


    #DISPLAY
    col1,col2,col3,col4=st.columns(4)
    col1.metric("Total Students",total_std)
    col2.metric("Class Average",f"{class_avg:.2f}")
    col3.metric("Pass Count",pass_count)
    col4.metric("Fail Count",fail_count)

    st.subheader("SUBJECT WISE AVERAGE")
    
    subject_avg = class_df[subjects].mean().reset_index()
    subject_avg.columns = ['Subject', 'Average']

    
    subject_avg['Subject'] = pd.Categorical(
        subject_avg['Subject'],
        categories=subjects,
        ordered=True
    )

    #plotting chart for each subject
    chart = alt.Chart(subject_avg).mark_bar().encode(
        x=alt.X('Subject:N', sort=subjects, title="Subject"),
        y=alt.Y('Average:Q', title="Average Marks"),
        tooltip=['Subject', 'Average']
    )

    st.subheader("Subject-wise Average")
    st.altair_chart(chart, use_container_width=True)

    #display
    st.subheader("Class Topper")
    topper = class_df.loc[class_df['Average'].idxmax()]

    st.success(f"Topper: {topper['Student Name']} ({topper['Average']:.2f})")
