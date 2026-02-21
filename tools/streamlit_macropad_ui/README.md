# Streamlit Macropad UI

**First time here?** This tool helps you set up your macropad without writing any code. You type what each key should say, and it creates the firmware file for you. No experience needed.

## What is this?

Your macropad has 3 buttons. Each button can type **3 different things** depending on how many times you tap it:
- **1 tap** → one phrase
- **2 taps** → a different phrase  
- **3 taps** → another phrase  

This web app lets you type in those 9 phrases, just pick your board version, and download a ready-to--use file. You then copy that file onto your macropad when you plug it into a computer .


---

## DISCLAIMER: You can access this web app by going to [my website](https://_____.streamlit.app) to configure your device instead of hosting it locally on your computer (more efficient and can use offline too).

---

## Step 1: Install (one-time setup)

You need **Python** on your computer. Don't have it? [Download Python](https://www.python.org/downloads/) (3.10 or newer) and make sure to check **"Add Python to PATH"** when installing.

Open a **terminal** on MacOS (or Command Prompt on Windows) and navigate to this project folder. Then run these commands one at a time:

```bash
# Create a virtual environment (a clean space for this apps dependencies)
python -m venv .venv

# Activate it —--------------- pick the line for your system:
source .venv/bin/activate          # Mac & Linux
# OR
.venv\Scripts\activate             # Windows

# Install the app
pip install -r tools/streamlit_macropad_ui/requirements.txt
```

If something errors, double check that you're in the repo root folder and that Python 3.10 or newer is installed.

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

A browser tab will open (usually http://localhost:8501). That's your configurator hosted locally on your computer (offline).
Another alternative is by going to [my website](https://www._____.streamlit.app) to configure online without hosting.

---

## Step 3: Use the app (tutorial)

### Main area — What each key types

You'll see 3 columns: **Key 1**, **Key 2**, **Key 3**. Each has 3 text boxes for:
- **1 tap** — what the key types when you tap it once
- **2 taps** — what it types when you tap twice quickly
- **3 taps** — what it types when you tap three times quickly

**Tip:** The example phrases (Hungry, Thirsty, Help, etc.) are just placeholders. Replace them with whatever you actually want your macropad to type.

### Sidebar — Board version/formatting

On the left, under **Hardware**:
- Pick **V1** or **V2** — this matches your physical macropad board. Not sure? Check your project docs or PCB.
- If you have **V2** and your board needs it, check **V2: drive GP29 low**. Most users can leave this unchecked.

### Sidebar — Timing (optional)

- **Tap window** — How long you have between taps before it counts as a new sequence. Default is 1 second. If taps feel ignored, try increasing it.
- **Poll delay** — Usually leave as it is.

### Preview

Scroll down to see how each phrase will look when it’s typed. This helps you spot typos before you deploy.

### Download and deploy

1. Click **Download code.py** — a file named `code.py` will save to your computer.
2. Plug in your macropad with USB.
3. Your computer should show a drive called **CIRCUITPY** (that’s your macropad’s storage).
4. Copy the downloaded `code.py` into the CIRCUITPY drive. Replace the old `code.py` if asked.
5. The macropad will restart and start using your new phrases.

**Troubleshooting:** If you don’t see CIRCUITPY, make sure CircuitPython is installed on your board and the cable supports data (not charge-only).

---

## Saving your settings

Click **Download config.json** in the sidebar to save your formatting . You can keep it as a backup or share it with someone else

---

## Quick reference

| Thing | What to do |
|-------|------------|
| Change what a key types | Edit the text boxes in the main area |
| Switch board version | Use the **Board version** radio in the sidebar |
| Get the firmware file | Click **Download code.py** |
| Put it on the macropad | Copy `code.py` onto the CIRCUITPY drive |




## License

MIT License

Copyright (c) 2026 Ted Tan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
