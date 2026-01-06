📊 Automated Student Report Generator (CSV → PDF)

A Python automation project that reads student data from a CSV file, performs basic data analysis, and generates a formatted PDF report automatically. This project demonstrates file handling, data processing, and PDF generation using Python.

🚀 Features

📂 Reads student data from a CSV file

📈 Performs data analysis:

Total number of students

Average marks

Highest marks

Lowest marks

📄 Automatically generates a professional PDF report

📋 Displays student details in a tabular format

⚡ Reduces manual reporting effort

🛠️ Technologies Used

Programming Language: Python

Libraries:

csv – reading structured data

fpdf – PDF report generation

📂 Project Structure
Automated-Report-Generator/
│
├── data.csv
├── report_generator.py
├── sample_report.pdf
└── README.md

▶️ How to Run the Project
Step 1: Install Required Library
pip install fpdf

Step 2: Prepare CSV File

Ensure data.csv is in the following format:

name,marks
Alice,85
Bob,78
Charlie,92

Step 3: Run the Script
python report_generator.py

📄 Output

A PDF file named sample_report.pdf will be generated

The PDF contains:

Student performance summary

Marks analysis

Tabular student data