import time
from pynput.keyboard import Key, Controller
from mss.darwin import MSS as mss

locations = [999, 799, 599, 399, 199, 0]
tree_color = (160, 115, 61)

def capture_screenshot():
    with mss() as sct:
        bbox = (1069, 142, 1070, 642)
        return sct.grab(bbox)

keyboard = Controller()
time.sleep(5)

render_time = 0.17
keystroke_time = 0.024

def fell_tree(key):
    keyboard.press(key)
    time.sleep(keystroke_time)
    keyboard.press(key)
    keyboard.release(key)

while True:
    time.sleep(render_time)
    img = capture_screenshot()
    loc_colors = [img.pixels[loc][0] for loc in locations]

    for col in loc_colors:
        if not (col == tree_color):
            fell_tree(Key.right)
        else:
            fell_tree(Key.left)
