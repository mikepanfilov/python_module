import urwid

def has_digits(password):
  return any(symbol.isdigit() for symbol in password)

def has_letters(password):
  return any(symbol.isalpha() for symbol in password)

def has_upper_letters(password):
  return any(symbol.isupper() for symbol in password)

def has_lower_letters(password):
  return any(symbol.islower() for symbol in password)

def has_symbols(password):
  return any(not symbol.isalnum() for symbol in password)

def doesnt_consist_of_symbols(password):
  return not(all(not symbol.isalnum() for symbol in password))

def is_very_long(password):
  return len(password) > 12

def password_check(edit, new_edit_text, reply):
  score = 0
  functions = [has_digits, is_very_long, has_letters,   
              has_upper_letters, has_lower_letters, 
              has_symbols,    doesnt_consist_of_symbols]
  for func in functions:
    if func(new_edit_text):
      score += 2
  reply.set_text('Рейтинг этого пароля: %d' % score)

# спасибо большое за подсказки!!!!
def main():
  ask = urwid.Edit('Введите пароль: ')
  reply = urwid.Text('')
  menu = urwid.Pile([ask, reply])
  menu = urwid.Filler(menu, valign='top')
  urwid.connect_signal(ask, 'change', password_check, reply)
  urwid.MainLoop(menu).run()

if __name__ == "__main__":
  main()