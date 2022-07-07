from fpdf import FPDF
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()
pdf.set_font("Arial", size=20)
pdf.cell(200, 10, txt="Welcome to Maths!", ln=1, align="L")
pdf.output("example.pdf")
