#--------importing usefull libraries for this project ----------------
import csv
from fpdf import FPDF

# --------------Read data from CSV file--------------
names = []  #storing data into list 
marks = []

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header (name , marks) focus on the given data 
    for row in reader:
        names.append(row[0])
        marks.append(int(row[1]))

# ------------Data analysis--------------
total_students = len(marks)
average_marks = sum(marks) / total_students
highest_marks = max(marks)
lowest_marks = min(marks)

# ----------Create PDF-----------
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Student Performance Report", ln=True, align="C")

#---------showing data analysis ----------
pdf.ln(10)
pdf.set_font("Arial", "", 12)
pdf.cell(0, 10, f"Total Students: {total_students}", ln=True)
pdf.cell(0, 10, f"Average Marks: {average_marks:.2f}", ln=True)
pdf.cell(0, 10, f"Highest Marks: {highest_marks}", ln=True)
pdf.cell(0, 10, f"Lowest Marks: {lowest_marks}", ln=True)

#------creating the table ----------
pdf.ln(10)
pdf.set_font("Arial", "B", 12)
pdf.cell(60, 10, "Name", border=1)
pdf.cell(40, 10, "Marks", border=1, ln=True)

#------adding names ansd marks into the table -------------
pdf.set_font("Arial", "", 12)
for i in range(total_students):
    pdf.cell(60, 10, names[i], border=1)
    pdf.cell(60, 10, str(marks[i]), border=1, ln=True)

# ---------Save PDF--------
pdf.output("sample_report.pdf")

print("PDF report generated successfully!")