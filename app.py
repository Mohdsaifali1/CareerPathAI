import streamlit as st
import google.generativeai as genai

# Get API key from Streamlit secrets
api_key = st.secrets["GEMINI_API_KEY"]

# Configure Gemini
genai.configure(api_key=api_key)
import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY") 

# Configure Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit App
st.set_page_config(page_title="CareerPath AI", page_icon="🎓", layout="centered")

st.title("🎓 CareerPath AI")
st.subheader("Your Personalized Career & Skills Advisor")

# User Inputs
name = st.text_input("Enter your name")
education = st.selectbox("Education Level", ["High School", "Undergraduate", "Postgraduate", "Other"])
skills = st.text_area("List your current skills (comma separated)")
interests = st.text_area("What are your career interests? (e.g., Data Science, Web Development, AI, etc.)")

if st.button("Get Career Roadmap"):
    if not name or not skills:
        st.warning("⚠️ Please enter your name and skills before continuing.")
    else:
        with st.spinner("🔮 Analyzing your profile and preparing a career roadmap..."):
            prompt = f"""
            You are a career advisor AI. Based on the following details, generate a structured **career roadmap**:

            Name: {name}
            Education Level: {education}
            Current Skills: {skills}
            Interests: {interests}

            Please format the response like this:

            ### Recommended Career Paths
            - Path 1
            - Path 2

            ### Skills to Learn Next
            - Skill A
            - Skill B

            ### Suggested Entry-Level Roles
            - Role A
            - Role B

            ### Long-Term Opportunities
            - Role X
            - Role Y

            ### Timeline Roadmap
            **Year 1:** ...
            **Year 2-3:** ...
            **Year 4+:** ...
            """

            response = model.generate_content(prompt)

        # Show Results
        st.success(f"✨ Here’s your personalized career roadmap, {name}!")
        st.markdown("---")
        st.markdown(response.text)
