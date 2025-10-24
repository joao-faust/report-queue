from termcolor import cprint
from app.menu.Menu import Menu

def show_menu(menu: Menu):
  menu.show_options()

  methods = menu.get_methods()

  while True:
    try:
      option = input('Inform an option: ')

      if not option.isdigit():
        cprint('The option must be a digit.', 'red')
        continue

      if option == '0':
        raise KeyboardInterrupt('interrupt-with-option')

      if option not in methods:
        cprint('The provided option is invalid.', 'red')
        continue

      methods[option]()
    except ValueError as err:
      cprint(err, 'red')
