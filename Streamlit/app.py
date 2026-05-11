import streamlit as st

st.title("Login Form")


email = st.text_input("Email")
ps = st.text_input("password",type = "password")
cps = st.text_input("Confirm Password",type = "password")

resume = st.file_uploader("Upload your Resume",type=["pdf","docx"])
age = st.number_input("Age",min_value =18,max_value =60)
photo = st.file_uploader("Upload your Photo",type = ["jpg", "jpeg", "png"])
video = st.file_uploader("Upload your Video",type=["mp4"])

submitted = st.button("Submit")



if submitted:
    if not email or not ps or not cps:
        st.error("Please fill all required fields")

    elif ps == cps:
        st.success("Logined Succesfully!...")

        if resume:
            st.write("Resume uploaded:", resume.name)
            
        if photo:
            st.write("Photo uploaded:", photo.name)
            st.image(photo)

        if video:
            st.write("Video uploaded:", video.name)
            st.video(video)

    else:
        st.error("Wrong Credentials ")
    