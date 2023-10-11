import speech_recognition as sr
import os
from pydub import AudioSegment

# AudioSegment.ffmpeg = '/home/pranshu1902/.cache/pip/wheels/8e/7a/69/cd6aeb83b126a7f04cbe7c9d929028dc52a6e7d525ff56003a'
# AudioSegment.ffprobe = "/path/to/ffprobe"


import moviepy.editor as mp
import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()

    # Load the MP3 audio file using pydub
    audio = AudioSegment.from_mp3("audio.mp3")

    # Export the audio as raw PCM data (16-bit signed little-endian, mono)
    audio = audio.set_channels(1)  # Convert to mono
    audio = audio.set_sample_width(2)  # 16-bit audio
    audio = audio.set_frame_rate(16000)  # 16 kHz sample rate (adjust as needed)

    # Export as raw audio data
    audio_data = audio.raw_data

    # Use the Google Web Speech API to convert audio to text
    try:
        text = recognizer.recognize_google(audio_data)
        print("Transcribed text:")
        print(text)
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")

#     # convert mp3 file to wav                                                       
#     # sound = AudioSegment.from_mp3(os.path.join('audio', 'audio.mp3'))
#     # sound.export("audio.wav", format="wav")

#     # # transcribe audio file                                                         
#     # AUDIO_FILE = "audio.wav"

#     # use the audio file as the audio source                                        
#     r = sr.Recognizer()
#     with sr.AudioFile(os.path.join('audio', 'audio.mp3')) as source:
#         audio = r.record(source)  # read the entire audio file     
#         text = r.recognize_google(audio)
#         return text

# import speech_recognition as sr

# Initialize the recognizer
    # recognizer = sr.Recognizer()

    # # Load the audio file (replace 'audio.mp3' with your file)
    # audio_file = os.path.join('audio', 'audio.mp3')

    # with sr.AudioFile(audio_file) as source:
    #     audio_data = recognizer.record(source)

    # # Use the Google Web Speech API to convert audio to text
    # try:
    #     text = recognizer.recognize_google(audio_data)
    #     print("Transcribed text:")
    #     print(text)
    # except sr.UnknownValueError:
    #     print("Google Web Speech API could not understand the audio")
    # except sr.RequestError as e:
    #     print(f"Could not request results from Google Web Speech API; {e}")


