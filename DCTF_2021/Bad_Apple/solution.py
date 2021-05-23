from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from pydub import AudioSegment
import numpy as np
from PIL import Image
import wave
import pylab


def make_wav():
    ffmpeg_extract_subclip("Bad_Apple.mp4", 91, 104, targetname="Сut_Bad_Apple.mp4")
    audio = AudioFileClip("Сut_Bad_Apple.mp4")
    audio.write_audiofile("Bad_Apple.mp3")
    audio_mp3 = AudioSegment.from_mp3("Bad_Apple.mp3")
    audio_mp3.export("Bad_Apple.wav", format="wav")


def get_wav_info(wav_file):
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames, 'int16')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate


def make_contrast():
    image = Image.open('spectrogram.png').convert("L")
    arr = np.asarray(image)
    pylab.imshow(arr, cmap=pylab.cm.binary)
    pylab.savefig('spectrogram.png')
    pylab.show()


def make_spectrogram():
    sound_info, frame_rate = get_wav_info("Bad_Apple.wav")
    pylab.figure(num=None, figsize=(30, 40))
    pylab.subplot(111)
    pylab.title('spectrogram of %r' % "Bad_Apple.wav")
    pylab.specgram(sound_info, Fs=frame_rate, detrend='linear')
    pylab.gray()
    pylab.savefig('spectrogram.png')


make_wav()
make_spectrogram()
make_contrast()
