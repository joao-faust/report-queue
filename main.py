from threading import Thread, Event
from termcolor import cprint

from app.Queue import Queue
from app.report.Report import Report
from app.menu.ReportMenu import ReportMenu
from menu_manager import show_menu
from report_manager import generate_report

report_queue = Queue[Report]()
thread_evt = Event()

try:
  Thread(target=generate_report, args=(thread_evt, report_queue,)).start()
  show_menu(ReportMenu(report_queue))
except BaseException as err:
  report_queue.clear()
  thread_evt.set()

  if not isinstance(err, KeyboardInterrupt):
    cprint('An unexpected error occurred:', 'red')
    cprint(err, 'light_red')
  elif str(err) != 'interrupt-with-option':
    print()
