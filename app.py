import os
import streamlit as st
import fitz

st.title("Doc2MCQ")
st.info("An app that generates Multiple choice QnA using on uploaded documentx")
uploaded_file = st.file_uploader("Please upload a file to continue",type=['pdf'])

# Check if file is uploaded
if uploaded_file:
    filename = uploaded_file.name
    st.write(filename+" uploaded successfully")
else:
    st.write('Please upload a file to continue')

def data_extraction(filename):
    pdf_text = ""
    cwd = os.getcwd()
    file_directory = os.path.join(cwd,filename)

    with open(file_directory,'wb') as pdfdata:
        pdfdata.write(uploaded_file.read())
    # st.write(file_directory)

    pdf_file = fitz.open(file_directory)
    for page in pdf_file.pages():
        pdf_text += page.get_text()

if uploaded_file:
    data_extraction(filename)
