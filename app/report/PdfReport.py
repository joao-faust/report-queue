from fpdf import FPDF
from .Report import Report

class PdfReport(Report):
  def __init__(self, name):
    super().__init__(name)

  def generate(self, filepath: str):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', size=12)
    pdf.cell(200, 10, txt=f'{self._name}')

    filepath_with_ext = f'{filepath}.pdf'
    pdf.output(filepath_with_ext)

    return filepath_with_ext
