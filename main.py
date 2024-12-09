import streamlit as st
from parse import split_content, parse_with_genai
import google.generativeai as genai
st.title("AI Course Creator")
summary = st.text_area("Write the Summary")
if summary:
    if st.button("Generate Readings"):
        st.write("Generating...")
        summary_chunks = split_content(summary)
        result = parse_with_genai(summary_chunks, 'readings')
        st.write(result)
        # user_input = st.text_input("Continue the chat with further instructions or feedback:")
        # if user_input:
        #     response = genai.GenerativeModel("gemini-1.5-flash").generate_content(user_input)
        #     st.write(response.text)
    if st.button("Generate Assignments"):
        st.write("Generating...")
        summary_chunks = split_content(summary)
        result = parse_with_genai(summary_chunks, 'assignments')
        st.write(result)
    if st.button("Generate Practise Project Prompt"):
        st.write("Generating...")
        summary_chunks = split_content(summary)
        result = parse_with_genai(summary_chunks, 'project')
        st.write(result)