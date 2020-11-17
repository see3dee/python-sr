import pyttsx3
import speech_recognition as sr


# Create a recognizer instance, 'r'
r = sr.Recognizer()
# Tell SR that this is an audio file.
audio_sample = sr.AudioFile('voicetest1.wav')
# Feed that sample into the recognizer instance's 'record' method
with audio_sample as source:
    record = r.record(source)  # record is speech_recognition.AudioData object.

# Google Web Speech API reads the speech_recognition.AudioData object and returns Text.
audio_text = r.recognize_google(record)

# Create VS-engine instance
engine = pyttsx3.init()

# Provide google api output test to the engine.say method:
engine.say(audio_text)  # VS engine reads text
engine.runAndWait()

