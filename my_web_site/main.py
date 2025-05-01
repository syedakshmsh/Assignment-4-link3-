import streamlit as st

st.set_page_config(page_title="My python Website",page_icon="#",layout="centered")
st.title("My WEBSITE")



st.sidebar.title("CODE_WITH_SHAJIYA")
page = st.sidebar.radio("Go To",["Home","About","Contact"])


if page == "Home":
    st.header("Home page")
    st.write("This is a simple homepage built with python ")
    name = st.text_input("Whats your name")
    if name:
        st.success(f"Hello {name}! Thankyou for Visiting")

elif page == "About":
    st.header("About")
    st.write("this website is built entirly using python and streamlit")
    about = st.text_input("Something About  for You")
    if about:
        st.success(f"Hello {about}! Thankyou for Visiting")

elif page == "Contact":
    st.header("Contact us ")
    email  = st.text_input("your email")
    message = st.text_input("your message")
    if st.button("submit"):
       st.success("Thankew for recived your message")
