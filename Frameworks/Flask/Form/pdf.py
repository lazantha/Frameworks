from reportlab.pdfgen import canvas
from io import BytesIO

class Pdf:
	def genPdf(self,first_name,last_name,department,email,start_date,pic):

		buffer=BytesIO()
		pdf=canvas.Canvas(buffer)
		pdf.drawString(100,700,'first name: '+first_name)
		pdf.drawString(100,700,'last name: '+last_name)
		pdf.drawString(100,700,'department: '+department)
		pdf.drawString(100,700,'email: '+email)
		pdf.drawString(100,700,'Start Date: '+str(start_date))
		pdf.drawImage(pic, 0, 0, 50, 50)
		pdf.save()
		pdf_string=buffer.getvalue()
		return pdf_string
		buffer.close()


