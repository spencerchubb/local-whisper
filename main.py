import sounddevice as sd
import scipy.io.wavfile as wav
import numpy as np
import requests
import tempfile
import time
import pyautogui
import keyboard

SAMPLE_RATE = 44100
def record_audio(channels=2):
    audio_data = sd.rec(
        int(SAMPLE_RATE * 60), # Record up to 1 minut
        samplerate=SAMPLE_RATE,
        channels=channels,
        blocking=False,
    )
    return audio_data

recording = False
audio_data = None
def start_or_stop():
    global recording
    global audio_data
    recording = not recording

    if recording:
        audio_data = record_audio()
        print("Recording...")
    else:
        print("Stopping...")
        sd.stop()
        
        start_time = time.time()
        non_zero = np.any(np.abs(audio_data) > 0.001, axis=1) # Use threshold
        if not np.any(non_zero):
            print("No audio data to process")
            return
        last_idx = np.where(non_zero)[0][-1]
        trimmed_audio = audio_data[:last_idx + 1]
        
        # Create a temporary file
        with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as temp_file:
            temp_path = temp_file.name
            wav.write(temp_path, SAMPLE_RATE, trimmed_audio)
        
        try:
            with open(temp_path, 'rb') as audio_file:
                files = {'file': ('recording.wav', audio_file, 'audio/wav')}
                data = {
                    'temperature': '0.0',
                    'temperature_inc': '0.2',
                    'response_format': 'json',
                }
                
                response = requests.post('http://127.0.0.1:8080/inference', files=files,data=data)
                response = response.json()
                text = response['text']

                # Remove newlines so it doesn't hit 'Enter' prematurely
                text = text.replace('\n', ' ')

                # idk why it has this but it's annoying
                text = text.replace('[BLANK_AUDIO]', '')

                # For good measure
                text = text.strip()
                

                print("Transcription:", text)
                pyautogui.write(text)
        except Exception as e:
            print(f"Error making API request: {str(e)}")
        print('Time:', time.time() - start_time)


def main():
    hotkey = 'ctrl+shift+r'
    print(f"Press {hotkey} to start and stop recording")

    # Hot key to start listening (e.g., Press F2 to start)
    keyboard.add_hotkey(hotkey, start_or_stop)

    # Keep the program running
    keyboard.wait()
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nRecording cancelled.")
        sd.stop()
