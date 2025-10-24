from threading import Event
from random import randint
from termcolor import cprint
from uuid import uuid4

from app.Queue import Queue
from app.report.Report import Report

def generate_report(queue: Queue[Report], outdir: str, thread_evt: Event):
  while not thread_evt.is_set():
    if queue.has_values():
      thread_evt.wait(randint(30, 60))

      report = queue.get_first()

      if not report:
        continue

      filename = str(uuid4()).replace('-', '')
      filepath = report.generate(f'{outdir}/{filename}')
      queue.dequeue()

      name = report.get_name()
      cprint(f'\nThe report "{name}" have been generated at "{filepath}".', 'cyan')

      next_report = queue.get_first()

      if not next_report:
        continue

      new_name = next_report.get_name()
      cprint(f'The generation of the report "{new_name}" have been started.', 'cyan')
