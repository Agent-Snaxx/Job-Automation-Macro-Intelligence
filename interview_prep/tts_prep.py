import pyttsx3
from pathlib import Path

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 160)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Option 1: Load external script file (recommended)
SCRIPT_FILE = Path("sample_script.txt")
if SCRIPT_FILE.exists():
    audio_script = SCRIPT_FILE.read_text(encoding="utf-8")
else:
    # Option 2: Inline script (replace text between triple quotes)
    audio_script = """
    Welcome to the Eric Wilson Token Life Cycle — ETH Edition.
    ...
    Loop restarting in 3... 2... 1...
    """

# Save the audio file
engine.save_to_file(audio_script, 'defi_loop.mp3')
engine.runAndWait()
print("MP3 audio created successfully: defi_loop.mp3")
