from uuid import uuid4
from .Report import Report

class ReportManager:
  def __init__(self, outdir: str):
    self.__outdir = outdir

  def generate(self, report: Report):
    filename = str(uuid4()).replace('-', '')
    filepath = f'{self.__outdir}/{filename}'
    filepath_with_ext = report.generate(filepath)
    return filepath_with_ext
