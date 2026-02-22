# Circuitpython setup
## Installing Circuitpython to your macropad (for brand new Raspberry Pi pico W):
1. To install circuit python, first got to [here](https://circuitpython.org/board/waveshare_rp2040_zero/) and download the `.UF2` file.
2. Plug in the macropad to the computer
3. Hold the `boot` button and press the `reset` button. a drive named `RPI-RP2` should show up on your computer
4. Copy `.UF2` file downloaded to the drive. It should automatically reset and a `CIRCUITPY` drive should show up on your computer.

## Installing Dependencies:
1. Go [here](https://circuitpython.org/libraries) to download `Bundle for Version 9.X`
2. Extract the folder
3. Copy the following files from `/lib` from the extracted folder to the `/lib` in `CIRCUITPY` folder from your macropad
    - `adafruit_debouncer.mpy`
    - `adafruit_hid` (the whole folder)
    - `adafruit_ticks.mpy`


## Uploading Code:
1. Copy/download code from the streamlit website as `code.py` into the macropad's drive called: `CIRCUITPY`
2. Then save
3. Then the code should auto-reload and you can press keys to test it out AFTER you eject the drive from your computer.

### Multi-tap text mode (this folder's `code.py`):

The default `firmware/circuitpython/code.py` is set up as **multi-tap text output**:

- 3 keys × 1–3 taps (within 1 second) = **9 different text outputs**
- If you press 2 keys at once, **the first key pressed wins** and other keys are ignored until the tap sequence completes

To customize the 9 texts + optional formatting (prefix/suffix/newline), use the Streamlit UI at the path: `tools/streamlit_macropad_ui/`.


# Links and Resources
[Circuit python docs](https://docs.circuitpython.org/en/latest/README.html)
[List of Keycodes](https://docs.circuitpython.org/projects/hid/en/latest/api.html#adafruit_hid.keycode.Keycode)
[Circuit python website](https://circuitpython.org/)



# For operating the board formatter:
## What is this?

Your macropad has 3 buttons. Each button can type **3 different text/sentences** depending on how many times you tap it:
- **1 tap** → one phrase
- **2 taps** → a different phrase  
- **3 taps** → another phrase  

This web app lets you type in those 9 phrases, just pick your board version, and download a ready to use file. You then replace that file onto your macropad when you plug it into a computer in the drive CIRCUITPY .

---

## Step 1: Install the environment for hosting locally (one-time setup)

You need **Python** on your computer. Don't have it? [Download Python](https://www.python.org/downloads/) (3.10 or newer) and make sure to check **"Add Python to PATH"** when installing.

Open a **terminal** on MacOS (or command Prompt on Windows) and navigate to this project folder. Then run these commands one at a time:

```bash
# Create a virtual environment (a clean space for this apps dependencies)
python -m venv .venv

# Activate it —--------------- pick the line for your system ------------------------------------------:
source .venv/bin/activate          # Mac & Linux
# OR
.venv\Scripts\activate             # Windows

# Install the app
pip install -r tools/streamlit_macropad_ui/requirements.txt
```

If something errors, double check that you're in the repo root folder and that Python version 3.10 or newer is installed.

---

## Step 2: Run the app

Each time you want to use the tool:

```bash
# Activate the virtual environment first (same as the one above)
source .venv/bin/activate          # Mac & Linux
.venv\Scripts\activate             # Windows

# Start/run the app
streamlit run tools/streamlit_macropad_ui/app.py
```

A browser tab will open (usually http://localhost:8501 (this is your link for your local-hosted website)). That's your configurator hosted locally on your computer (offline).

---

## Step 3: Use the app (tutorial)

### Main area — What each key types

You'll see 3 columns: **Key 1**, **Key 2**, **Key 3**. Each has 3 text boxes for:
- **1 tap** — what the key types when you tap it once
- **2 taps** — what it types when you tap twice quickly
- **3 taps** — what it types when you tap three times quickly

**Tip:** The example phrases (Hungry, Thirsty, Help, etc.) are just the default  placeholders. You can replace them with whatever you want your macropad to type if you want!

### Sidebar — Board version/formatting (Technical setup, IF your macropad works already, dont touch

On the left, under **Hardware**:
- Pick **V1** or **V2** — this matches your physical macropad board. Not sure? Check your project docs or PCB.
- If you have **V2** and your board needs it, check **V2: drive GP29 low**. You can just leave this unchecked as my board is not in this version.

### Sidebar — Timing (optional)

- **Tap window** — How long you have between taps before it counts as a new sequence. The default is 1 second. If the taps are ignored when pressed, increase the time by another 0.5 secs
- **Poll delay** — Usually leave as it is.

### Preview

Scroll down to the second table to see how each phrase will look when it’s typed out. This helps you spot typos or other issues before you upload your code into the circuitpython drive.

### Download and deploy

1. Click **Download code.py** — a file named `code.py` will save to your computer. (If you have one already in your computer, just replace that one already in your computer)
2. Plug in your macropad with USB.
3. Your computer should show a drive called **CIRCUITPY** (that’s your macropad’s storage drive).
4. Copy the downloaded `code.py` into the CIRCUITPY drive. Replace the old `code.py` if asked.
5. The macropad will restart and start using your new phrases/words.

**Troubleshooting:** If you don’t see CIRCUITPY in your computer's drive, make sure CircuitPython is installed on your board and the cable supports data (not charge-only, else it cant transfer data).

---

## Saving your settings

Click **Download config.json** in the sidebar to save your formatting . You can keep it as a backup or share it with someone else. Then import into the CIRCUITPY drive.
