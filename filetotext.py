import speech_recognition as sr

r = sr.Recognizer()
sample = sr.AudioFile('voicealphatest.wav')
with sample as source:
    audio = r.record(source)
type(audio)
print(r.recognize_google(audio))
