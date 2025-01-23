# Local Whisper

This script lets you do voice-to-text. It runs locally, it's free, and it's fast. You can get responses back in less than a second.

It's easy to use:
1. Click on a text field that you want to write in
2. Press hotkey to start (ctrl+shift+r)
3. Say stuff
4. Press hotkey again to stop

It's great for coding and writing! The average person speaks ~160 words per minute, so speaking is faster than typing unless you're a god-tier typist.

## How to run

```
pip install -r requirements.txt
python main.py
```

If you want, you can configure some variables in `main.py`. For example, by default it uses the tiny whisper model. You can use a bigger model to get more accuracy, but it'll be slower.
