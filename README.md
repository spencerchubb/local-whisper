# Local Whisper

This script lets you do voice-to-text. It runs locally, it's free, and it's fast. You can get responses back in less than a second.

It's easy to use:
1. Click on a text field that you want to write in
2. Press the hotkey (ctrl+shift+r)
3. Say stuff

It's great for coding and writing! The average person speaks ~160 words per minute, so speaking is faster than typing unless you're a god-tier typist.

## How to setup

Download one of the llamafiles. I recommend [whisper-tiny.en.llamafile](https://huggingface.co/Mozilla/whisperfile/blob/main/whisper-tiny.en.llamafile) to get responses in less than a second.

Larger models are more accurate, but slower. You can also use a GPU, but it's a little more work to setup. See the llamafile docs for more info.

After downloading, run the llamafile server by simply running the file:

```
./whisper-tiny.en.llamafile
```

Then open a second terminal and run the python script:

```
pip install -r requirements.txt
python main.py
```
