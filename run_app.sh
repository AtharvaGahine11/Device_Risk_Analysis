#!/bin/bash
# Convenient launcher for Device Risk Analysis Streamlit Application
cd "$(dirname "$0")"

if [ -f "./venv/bin/streamlit" ]; then
    echo "Starting Device Risk Analysis Dashboard..."
    open "http://localhost:8501"
    ./venv/bin/streamlit run app/app.py
else
    echo "Virtual environment not detected. Using system streamlit..."
    open "http://localhost:8501"
    streamlit run app/app.py
fi
