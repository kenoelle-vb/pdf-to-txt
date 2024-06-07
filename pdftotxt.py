import streamlit as st
import PyPDF2

import tempfile
uploaded_file = st.file_uploader("File upload", type="pdf")
if uploaded_file:
        temp_dir = tempfile.mkdtemp()
        path = os.path.join(temp_dir, uploaded_file.name)
        with open(path, "wb") as f:
                f.write(uploaded_file.getvalue())
