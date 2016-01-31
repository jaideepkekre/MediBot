# @author: @v0dro
# use: create a friendly interface for interacting with various things in the
# telegram API

import telegram


def create_keyboard(text_list, keyboard_type='column'):
    presentation_text = []

    if keyboard_type == 'column':
        for text in text_list:
            presentation_text.append([text])
    elif keyboard_type == 'custom':
        presentation_text = text_list
    else:
        raise ("Wrong input " + keyboard_type)

    return telegram.ReplyKeyboardMarkup(presentation_text, one_time_keyboard=True)


def tester():
    create_keyboard(['hello', 'my', 'dear'])


if __name__ == '__main__':
    tester()
