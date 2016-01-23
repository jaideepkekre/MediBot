# @author: @v0dro
# use: create a friendly interface for interacting with various things in the
# telegram API

import telegram

def create_keyboard(text_list, orientation='column'):
  presentation_text = []

  if orientation == 'column':
    for text in text_list:
      presentation_text.append([text])
  elif orientation == 'custom':
    presentation_text.append(text_list)
  else:
    raise("Wrong input " + orientation)

  return telegram.ReplyKeyboardMarkup(presentation_text, one_time_keyboard=True)


def tester():
  create_keyboard(['hello', 'my', 'dear'])

if __name__ == '__main__':
  tester()
