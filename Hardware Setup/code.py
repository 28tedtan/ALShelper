import board
import usb_hid
from adafruit_debouncer import Debouncer
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import digitalio
import time

#
# Multi-tap text macropad (3 keys x 3 tap-counts = 9 outputs)
# v1 board: GP27 = Key1, GP26 = Key2, GP15 = Key3
#
# - Tap a key 1/2/3 times within TAP_WINDOW_S -> sends different text.
# - Keys are fully independent; first key pressed within a sequence wins.
#

# ----- Hardware pins (v1 board) -----
PIN_LIST = [board.GP27, board.GP26, board.GP15]

# ----- Timing -----
TAP_WINDOW_S = 1.0
POLL_S = 0.005

# ----- Text outputs [key_index][tap_count - 1] -----
TEXTS = [
    ["Hungry ",   "Thirsty ",   "Itch "    ],  # Key 1 (GP27): 1-tap / 2-tap / 3-tap
    ["Choking ",  "Bathroom ",  "Painful " ],  # Key 2 (GP26): 1-tap / 2-tap / 3-tap
    ["Help ",     "Adjust me ", "Cold/Hot "],  # Key 3 (GP15): 1-tap / 2-tap / 3-tap
]

# ----- Formatting -----
PREFIX = ""
SUFFIX = ""
ADD_NEWLINE = False


def format_text(s):
    out = PREFIX + s + SUFFIX
    if ADD_NEWLINE:
        out += "\n"
    return out


# ----- Hardware setup -----
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

pins = []
for p in PIN_LIST:
    io = digitalio.DigitalInOut(p)
    io.direction = digitalio.Direction.INPUT
    io.pull = digitalio.Pull.UP
    pins.append(io)

switches = [Debouncer(p) for p in pins]

# ----- State -----
active_key = None        # index of the key currently being tapped (0/1/2)
tap_count = 0            # how many taps recorded so far
last_tap_time = 0.0      # monotonic time of the most recent press
waiting_for_release = False  # True while we are waiting for the active key to come back up

# ----- Main loop -----
while True:
    now = time.monotonic()

    for sw in switches:
        sw.update()

    if active_key is None:
        # No active sequence — watch all keys for a new press
        for idx in range(len(switches)):
            if switches[idx].fell:
                active_key = idx
                tap_count = 1
                last_tap_time = now
                waiting_for_release = True
                break  # ignore any simultaneous presses; first wins

    else:
        sw = switches[active_key]

        # Track press/release of the active key
        if waiting_for_release:
            if sw.rose:
                waiting_for_release = False  # key is back up; another tap is possible
        else:
            if sw.fell:
                # Another tap on the same key
                tap_count += 1
                if tap_count > 3:
                    tap_count = 3  # clamp to max
                last_tap_time = now
                waiting_for_release = True

        # Commit when the tap window expires and the key is up
        if (not waiting_for_release) and (now - last_tap_time) >= TAP_WINDOW_S:
            text = TEXTS[active_key][tap_count - 1]
            layout.write(format_text(text))
            # Reset state
            active_key = None
            tap_count = 0
            last_tap_time = 0.0
            waiting_for_release = False

    time.sleep(POLL_S)
