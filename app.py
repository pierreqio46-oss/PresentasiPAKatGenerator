import streamlit as st
import os

from ai_engine import AIEngine
from quiz_engine import QuizGenerator
from image_engine import ImageGenerator
from ppt_generator import PPTGenerator
from pdf_generator import PDFGenerator
from file_reader import *

st.set_page_config(
    page_title=
    "AI Presentasi Guru",
    layout="wide"
)

st.title(
    "⛪ AI Presentasi Guru"
)

key=st.sidebar.text_input(
    "OpenAI API Key",
    type="password"
)

if key:

    ai=AIEngine(key)

    image=ImageGenerator(
        ai.client
    )

    quiz=QuizGenerator(
        ai.client
    )

    ppt=PPTGenerator(
        image
    )

    pdf=PDFGenerator()

uploaded=st.file_uploader(
    "Upload Modul",
    type=["docx","pdf"]
)

if uploaded and key:

    if st.button(
        "🚀 Buat Presentasi Interaktif"
    ):

        ext=os.path.splitext(
            uploaded.name
        )[1]

        if ext==".docx":

            text=read_docx(
                uploaded
            )

        else:

            text=read_pdf(
                uploaded
            )

        slides=ai.create_slides(
            text
        )

        quiz_result=(
            quiz.create_quiz(
                text
            )
        )

        ppt_file=(
            ppt.create(
                slides,
                quiz_result
            )
        )

        pdf_file=(
            pdf.create(
                slides
            )
        )

        st.success(
            "Selesai"
        )

        with open(
            ppt_file,
            "rb"
        ) as f:

            st.download_button(
                "Download PPT",
                f,
                "presentasi.pptx"
            )

        with open(
            pdf_file,
            "rb"
        ) as f:

            st.download_button(
                "Download PDF",
                f,
                "materi.pdf"
            )