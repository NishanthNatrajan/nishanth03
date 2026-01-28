import streamlit as st 
st.title("student management system")
import streamlit as st
import pandas as pd

st.title("Student Management System")

# Session state la data store pannrom
if "students" not in st.session_state:
    st.session_state.students = pd.DataFrame(columns=["Roll No", "Name", "Department", "Mark"])

st.header("Add Student")

roll = st.text_input("Enter Roll Number")
name = st.text_input("Enter Name")
dept = st.selectbox("Select Department", ["CSE", "ECE", "EEE", "MECH", "IT"])
mark = st.number_input("Enter Mark", min_value=0, max_value=100)

if st.button("Add Student"):
    if roll and name:
        new_data = pd.DataFrame([[roll, name, dept, mark]],
                                columns=["Roll No", "Name", "Department", "Mark"])
        st.session_state.students = pd.concat([st.session_state.students, new_data], ignore_index=True)
        st.success("Student Added Successfully")
    else:
        st.error("Please fill all details")

st.header("Student List")

st.dataframe(st.session_state.students)

st.header("Delete Student")

delete_roll = st.text_input("Enter Roll Number to Delete")

if st.button("Delete"):
    if delete_roll in st.session_state.students["Roll No"].values:
        st.session_state.students = st.session_state.students[
            st.session_state.students["Roll No"] != delete_roll
        ]
        st.success("Student Deleted Successfully")
    else:
        st.warning("Roll Number Not Found")