#!/usr/bin/bash


apt install python3-pip python3-venv -y
python3 -m venv venv2
source venv2/bin/activate
pip install streamlit
streamlit run quizgame/testquiz_app.py
