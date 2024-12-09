import streamlit as st
from parse import split_content, parse_with_genai
from chapter import split_into_chapters, display_chapter
import docx, os
import google.generativeai as genai
st.title("AI Course Creator")

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

uploaded_file = st.file_uploader("Choose a .docx file", type="docx")

if uploaded_file is not None:
    try:
        doc = docx.Document(uploaded_file)
        chapters = split_into_chapters(doc)

        chapter_titles = [chapter["title"] for chapter in chapters]
        selected_chapter_title = st.selectbox("Select a chapter", chapter_titles)

        selected_chapter = next((chapter for chapter in chapters if chapter["title"] == selected_chapter_title), None)

        if selected_chapter:
            summary = selected_chapter["content"]

            if st.button("Generate Readings"):
                st.write("Generating...")
                summary_chunks = split_content(summary)
                result = parse_with_genai(summary_chunks, api_key,'readings')
                st.write(result)

            if st.button("Generate Assignments"):
                st.write("Generating...")
                summary_chunks = split_content(summary)
                result = parse_with_genai(summary_chunks, api_key, 'assignments')
                st.write(result)

            if st.button("Generate Case Study"):
                st.write("Generating...")
                summary_chunks = split_content(summary)
                result = parse_with_genai(summary_chunks, api_key, 'case-study')
                st.write(result)

            if st.button("Generate Practise Project Prompt"):
                st.write("Generating...")
                summary_chunks = split_content(summary)
                result = parse_with_genai(summary_chunks, api_key, 'project')
                st.write(result)

    except Exception as e:
        st.error(f"Error processing the file: {e}")