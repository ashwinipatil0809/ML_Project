import streamlit as st
import pandas as pd
import joblib

model = joblib.load("student_performace__exam_score_model.pkl")

st.title("Student Exam Score Prediction App")
st.write("Enter the details to predict the student's performance score.")


# User inputs
def user_input():
    age = st.number_input("Age", 18, 30)
    gender = st.selectbox("Gender", ["Male", "Female"])
    study_hours = st.number_input("Study Hours Per Day", 0.0, 10.0)
    social_media = st.number_input("Social Media Hours", 0.0, 10.0)
    netflix = st.number_input("Netflix Hours", 0.0, 10.0)
    part_time = st.selectbox("Part-time Job", ["Yes", "No"])
    attendance = st.number_input("Attendance %", 0.0, 100.0)
    sleep = st.number_input("Sleep Hours", 0.0, 12.0)
    diet = st.selectbox("Diet Quality", ["Poor", "Fair", "Good"])
    exercise = st.number_input("Exercise Frequency (per week)", 0, 7)
    parent_edu = st.selectbox("Parent Education Level", ["High School", "Bachelor", "Master"])
    internet = st.selectbox("Internet Quality", ["Poor", "Average", "Good"])
    extra = st.selectbox("Extracurricular Participation", ["Yes", "No"])
    mental = st.number_input("Mental Health Rating", 1, 10)

    data = pd.DataFrame({
        "age": [age],
        "gender": [gender],
        "study_hours_per_day": [study_hours],
        "social_media_hours": [social_media],
        "netflix_hours": [netflix],
        "part_time_job": [part_time],
        "attendance_percentage": [attendance],
        "sleep_hours": [sleep],
        "diet_quality": [diet],
        "exercise_frequency": [exercise],
        "parental_education_level": [parent_edu],
        "internet_quality": [internet],
        "extracurricular_participation": [extra],
        "mental_health_rating": [mental]
    })

    return data

input_df = user_input()

if st.button("Predict Exam Score"):
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Exam Score: {prediction:.2f}")
