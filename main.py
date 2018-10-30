try:
    from google_speech import Speech
except RuntimeError as re:
    print(re)
import clipboard
from pynput import keyboard
from pynput.keyboard import Key, Controller
from googletrans import Translator

control = False
lang = "pt-BR"
key_controller = Controller()


def speech(text, lang="pt"):
    try:
        translate = Translator()
        t_text = translate.translate(text, dest='pt').text
        speech = Speech(t_text, lang)
        sox_effects = ("speed", "1")
        speech.play(sox_effects)
    except AttributeError as ae:
        print(ae)


def do_copy():
    try:
        key_controller.press(Key.ctrl_l)
        key_controller.press('c')
        key_controller.release('c')
        return True
    except Exception as ex:
        print(ex)
        return False


def on_press(key):
    global control
    global lang
    if key == Key.ctrl_l:
        control = True
    if control and key == Key.space:
        if do_copy():
            text = clipboard.paste()
            speech(text)


def on_release(key):
    global control
    if key == Key.ctrl_l:
        control = False


with keyboard.Listener(on_press=on_press,
                       on_release=on_release) as listener:
    listener.join()