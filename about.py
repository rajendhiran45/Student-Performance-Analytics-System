import streamlit as st

def credits():                                                     #credits
    st.markdown(
        """
        <h2 style='text-align:center;'>ℹ About This Project</h2>
        <hr>
        """,
        unsafe_allow_html=True
    )

    st.write(
        """
        *Student Performance Analytics System* is a data-driven application 
        designed to analyze and visualize academic performance of students.
        """
    )

    st.subheader("👨‍💻 Developer")
    st.write("*Rajendhiran*")

    st.subheader("🛠 Tech Stack")
    st.write("- Python")
    st.write("- Pandas")
    st.write("- Streamlit")
    st.write("- CSV-based Data Storage")

    st.subheader("🔗 Connect with me")
    
    st.link_button("LINKEDIN","www.linkedin.com/in/rajendhiran"
    )
    st.caption(
        "This project was developed as part of a hands-on learning initiative to build real-world data applications.")