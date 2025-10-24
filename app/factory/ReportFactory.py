from ..report.PdfReport import PdfReport

class ReportFactory:
  @staticmethod
  def build(name: str, format: str):
    match format:
      case 'pdf':
        return PdfReport(name)
      case _:
        return None
