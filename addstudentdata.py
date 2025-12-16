import pandas as pd
import streamlit as st
import datetime as dt
import os

#strongpath
BAS_DIR=os.path.dirname(__file__)
CSV_PATH=os.path.join(BAS_DIR,"stddata.csv")


def addstddata(rf):
    data = pd.read_csv(CSV_PATH)

    #getting students details
    st.title("STUDENTS DETAILS")
    reg=st.number_input("ENTER STUDENT REGISTER NUMBER",step=1,format="%d")
    do_b=st.date_input("ENTER STUDENT DATE OF BIRTH",min_value=dt.date(1990,12,31))
    dobb=do_b.strftime("%Y-%m-%d")
    student_name=st.text_input("ENTER STUDENT NAME").title()
    secction=st.text_input("SECTION").upper()
    #getting students mark details
    st.title("STUDENTS MARK FOR EACH SUBJECT")
    tm=st.number_input("ENTER TAMIL MARK",step=1,format="%d",min_value=0,max_value=100)
    eng=st.number_input("ENTER ENGLISH MARK",step=1,format="%d",min_value=0,max_value=100)
    mt=st.number_input("ENTER MATHS MARK",step=1,format="%d",min_value=0,max_value=100)
    sci=st.number_input("ENTER SCIENCE MARK",step=1,format="%d",min_value=0,max_value=100)
    ss=st.number_input("ENTER SOCIAL SCIENCE MARK",step=1,format="%d",min_value=0,max_value=100)

    #to avoid duplicate register number
    if reg in data['Register Number'].values:
        st.error("Register number already exists!")
        return


    if st.button("UPDATE"):
        #avoiding any section is not filled
        if not student_name or not secction:
            st.warning("⚠️Please fill all student details!")

        else:
            new_student={

                'Register Number': reg,
                'Dob': dobb,
                'Student Name': student_name,
                'Section': secction,
                'Tamil': tm,
                'English': eng,
                'Maths': mt,
                'Science': sci,
                'Social Science': ss
                }
            
            columns = [
                'Register Number','Dob','Student Name','Section',
                'Tamil','English','Maths','Science','Social Science'
            ]

            new_data=pd.DataFrame([new_student],columns=columns)

            #appenidng new data into csv file
            new_data.to_csv(CSV_PATH,mode='a',header=False,index=False,lineterminator='\n')
            st.success("SUCCESFULLY UPDATED!")