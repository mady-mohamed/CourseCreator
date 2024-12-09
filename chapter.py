import streamlit as st
import docx
import re

def split_into_chapters(doc):
    full_text = "\n".join([p.text for p in doc.paragraphs])
    chapter_texts = re.split(r"(Chapter:\s.*?)(?=\nChapter:|\Z)", full_text, flags=re.DOTALL | re.MULTILINE)
    chapters = []
    for i in range(1, len(chapter_texts), 2):  # Iterate through chapter matches
        chapter_text = chapter_texts[i].strip()
        chapters.append({"title": chapter_text.splitlines()[0].replace("Chapter:","").strip(), "content": "\n".join(chapter_text.splitlines()[1:])}) # Extract title and content

    return chapters




def display_chapter(chapter):
    st.header(chapter["title"])
    st.write(chapter["content"])

uploaded_file = st.file_uploader("Choose a .docx file", type="docx")

if uploaded_file is not None:
    try:
        doc = docx.Document(uploaded_file)
        chapters = split_into_chapters(doc)


        chapter_titles = [chapter["title"] for chapter in chapters]
        selected_chapter_title = st.selectbox("Select a chapter", chapter_titles)


        selected_chapter = next((chapter for chapter in chapters if chapter["title"] == selected_chapter_title), None)

        if selected_chapter:
            display_chapter(selected_chapter)

    except Exception as e:
        st.error(f"Error processing the file: {e}")