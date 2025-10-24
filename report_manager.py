from threading import Event
from time import sleep
from random import randint
from termcolor import cprint

from app.Queue import Queue
from app.report.Report import Report
from app.report.ReportManager import ReportManager

manager = ReportManager('./output')

def generate_report(thread_evt: Event, queue: Queue[Report]):
  while not thread_evt.is_set():
    if queue.has_values():
      thread_evt.wait(randint(30, 60))

      report = queue.get_first()

      if not report:
        continue

      filepath = manager.generate(report)
      queue.dequeue()

      name = report.get_name()
      cprint(f'\nThe report "{name}" have been generated at "{filepath}".', 'cyan')

      next_report = queue.get_first()

      if not next_report:
        continue

      new_name = next_report.get_name()
      cprint(f'The generation of the report "{new_name}" have been started.', 'cyan')
