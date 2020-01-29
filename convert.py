import tabula

pdf = tabula.read_pdf(
    "https://mcgill.ca/exams/files/exams/april_2020_tentative_exam_schedule_1.pdf",
    pages="all")
pdf.to_csv('exam.csv',encoding='utf-8')

