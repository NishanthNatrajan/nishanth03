import streamlit as st
import pandas as pd
st.title("Student Management System")
st.write("Welcome to the student management system app.")
if "student" not in st.session_state:
    st.session_state.student = pd.DataFrame(
        columns=["Name", "Age", "Marks"]
    )
name = st.text_input("Enter student name:")
age = st.number_input("Enter student age:", min_value=1, max_value=25)
marks = st.number_input("Enter student marks:", min_value=0, max_value=100)
if st.button("Add Student"):
    if name == "":
        st.error("Please enter student name")
    else:
        new_student = {
            "Name": name,
            "Age": age,
            "Marks": marks
        }

        st.session_state.student = pd.concat(
            [st.session_state.student, pd.DataFrame([new_student])],
            ignore_index=True
        )

        st.success(f"Student {name} added successfully!")
st.subheader("Student Records")
st.dataframe(st.session_state.student)
st.subheader("Delete Student")
delete_name = st.text_input("Enter student name to delete:")
if st.button("Delete Student"):
    if delete_name == "":
        st.error("Please enter name to delete")
    else:
        original_len = len(st.session_state.student)

        st.session_state.student = st.session_state.student[
            st.session_state.student["Name"] != delete_name
        ]

        if len(st.session_state.student) < original_len:
            st.success(f"Student {delete_name} deleted successfully!")
        else:
            st.warning("Student not found")