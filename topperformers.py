import pandas as pd
import streamlit as st
import os


subjects = ['Tamil', 'English', 'Maths', 'Science', 'Social Science']

#overall top performers
def overalltop(rf):
    rf['Average'] =rf[subjects].mean(axis=1)
    toppers=rf[rf['Average']>=80]
    toppers=toppers.sort_values(by='Average',ascending=False)
    toppers = toppers.reset_index(drop=True)
    toppers.index = toppers.index + 1
    toppers['Rank'] = range(1, len(toppers)+1)

    st.title("TOP PERFORMERS")
    st.caption("Note: Only students with an average above 80 are shown as top performers.")
    st.dataframe(
        toppers[['Rank','Register Number','Student Name','Section','Average']],
        hide_index=True,
        use_container_width=True
    )

#subject wise top performers
def subwisetop(rf):
    st.title("TOP PERFORMERS")
    st.caption("Note: Only students with an average above 80 are shown as top performers.")
    subjects = ['Tamil', 'English', 'Maths', 'Science', 'Social Science']
    topper_data=[]
    
    for sub in subjects:
        topper=rf[sub].idxmax()
        topper_name=rf.loc[topper,'Student Name']
        topper_reg=rf.loc[topper,'Register Number']
        topper_mark=rf.loc[topper,sub]
        topper_data.append([sub,topper_reg,topper_name,topper_mark])

    topperfin=pd.DataFrame(topper_data,columns=["Subject Name","Register Number","Student Name","Mark"])
    st.dataframe(topperfin,hide_index=True,use_container_width=True)

#top 3 performers
def topthree(rf):
    rf['Average'] =rf[subjects].mean(axis=1)
    st.header('TOP 3 PERFORMERS')
    top3=rf.sort_values(by="Average",ascending=False).head(3)  #sorting the avg in descending order
    top3=top3.reset_index(drop=True)    #reseting the index
    #top3.index=top3.index+1         #set the index to 1
    #top3['Rank']=top3.index        #assigning index as rank
   
   #medal instead of numbers
    medals = ["🥇 Gold", "🥈 Silver", "🥉 Bronze"]
    top3["Medal"] = medals[:len(top3)]

    st.dataframe(top3[['Medal','Register Number','Student Name','Section','Average',]],hide_index=True,use_container_width=True)


#display
def toppersmenu(rf):
    topperip=st.selectbox("Select Topper Type",["Top 3 Performers","Overall Toppers","Subject Wise Toppers"])
        
    if topperip=="Overall Toppers":
        overalltop(rf)
    elif topperip=="Subject Wise Toppers":
        subwisetop(rf)
    else:
        topthree(rf)