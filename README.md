# Circuitpython
## Installing Circuitpython
1. To install circuit python, first got to [here](https://circuitpython.org/board/waveshare_rp2040_zero/) and download the `.UF2` file.
2. Plug in the macropad to the computer
3. Hold the `boot` button and press the `reset` button. a drive named `RPI-RP2` should show up on your computer
4. Copy `.UF2` file downloaded to the drive. It should automatically reset and a `CIRCUITPY` drive should show up on your computer.

## Installing Dependencies
1. Go [here](https://circuitpython.org/libraries) to download `Bundle for Version 9.X`
2. Extract the folder
3. Copy the following files from `/lib` from the extracted folder to the `/lib` in `CIRCUITPY` folder from your macropad
    - `adafruit_debouncer.mpy`
    - `adafruit_hid` (the whole folder)
    - `adafruit_ticks.mpy`


## Uploading Code
1. Copy code from `firmware/circuitpython/code.py` in github to `code.py` in `CIRCUITPY`
2. Save
3. Code should auto-reload and you can press keys to test.

### Multi-tap text mode (this repo’s `code.py`)

The default `firmware/circuitpython/code.py` is set up as **multi-tap text output**:

- 3 keys × 1–3 taps (within 1 second) = **9 different text outputs**
- If you press 2 keys at once, **the first key pressed wins** and other keys are ignored until the tap sequence completes

To customize the 9 texts + optional formatting (prefix/suffix/newline), use the Streamlit UI at `tools/streamlit_macropad_ui/`.

**Note:** If using version 2 of the macropad, use `realCode_v2.py` instead of `code.py`.


# Links and Resources
[Circuit python docs](https://docs.circuitpython.org/en/latest/README.html)
[List of Keycodes](https://docs.circuitpython.org/projects/hid/en/latest/api.html#adafruit_hid.keycode.Keycode)
[Circuit python website](https://circuitpython.org/)
