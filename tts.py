import torch
import sounddevice as sd
import time

language = 'ru'
model_id = 'ru_v3'
sample_rate = 48000
speaker = 'kseniya' # aidar, baya, kseniya, xenia, random
put_accent = True
put_yoo = True
device = torch.device('cpu')

model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                          model='silero_tts',
                          language=language,
                          speaker=model_id)
model.to(device)

def va_speaker(what: str):
    audio = model.apply_tts(text=what+"..",
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yoo)
    sd.play(audio, sample_rate * 1.05)
    time.sleep((len(audio) / sample_rate) + 0.5)
    sd.wait()
    sd.stop()