import streamlit as st


st.title("BMI Calculator")

weight = st.number_input("Enter a Weight in kg:")
height = st.number_input("Enter a height in cm:")
final_height = height ** 2

if st.button("BMI Calculator"):
    bmi = weight / final_height
    st.success(f"bmi calculator:{bmi:.2f}")

    if bmi < 18.5:

     st.warning("you are underWeight")
    elif 18.5 <= bmi < 24.9:
     st.info("you are a normal weight")
    elif 25 <= bmi < 29.9:
     st.warning("you are over weight")
    else:
     st.error("you are obessed")
    

