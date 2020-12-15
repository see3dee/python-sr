import speech_recognition as sr

r = sr.Recognizer()
sample = sr.AudioFile('02_voice_test.wav')
with sample as source:
    audio = r.record(source)
print(type(audio))
print(r.recognize_google(audio))
