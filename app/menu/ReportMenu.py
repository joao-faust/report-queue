from termcolor import cprint, colored

from .Menu import Menu
from ..report.Report import Report
from ..factory.ReportFactory import ReportFactory

class ReportMenu(Menu[Report]):
  def __init__(self, queue):
    super().__init__(queue)

  def show_options(self):
    print('0 - Exit')
    print('1 - Generate report')
    print('2 - Display queue of reports')

  def add_item(self):
    while True:
      name = input('Type the report name: ')
      if name == '':
        cprint('The name must be provided.', 'red')
      else:
        break

    while True:
      format = input('Provide the report format (only pdf): ')
      report = ReportFactory.build(name, format)
      if format == '':
        cprint('The format must be provided.', 'red')
      elif not report:
        cprint('The provided format is not accepted.', 'red')
      else:
        break

    self._queue.enqueue(report)
    cprint(f'The report "{name}" have been added to the end of the queue.', 'green')

  def display_items(self):
    for i, report in enumerate(self._queue.get_values()):
      if i == 0:
        print(f'#1 - {report.get_name()} {colored('(generating)', 'cyan')}')
      else:
        print(f'#{i+1} - {report.get_name()}')
