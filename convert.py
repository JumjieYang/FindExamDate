import tabula

pdf = tabula.read_pdf(
    "https://www.mcgill.ca/exams/files/exams/december_2019_final_exam_schedule_with_room_locationsd12.pdf",
    pages="all")
pdf.to_csv('exam.csv',encoding='utf-8')

