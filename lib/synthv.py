import board
import audiocore
import audiobusio
import time

# setup PINs and i2s Audio
g_BCLK = board.GP3
y_LRC = board.GP4
o_DIN = board.GP2
i2s = audiobusio.I2SOut(g_BCLK, y_LRC, o_DIN)
# setup sounds (wav files)
snd_1_de = open("/sound/1wav_de.wav", "rb")                             # 0.63
snd_2_de = open("/sound/2wav_de.wav", "rb")                             # 0.56
snd_3_de = open("/sound/3wav_de.wav", "rb")                             # 0.49
# setup WaveFile objects (the actual objects to play)
wav_1_de = audiocore.WaveFile(snd_1_de)
wav_2_de = audiocore.WaveFile(snd_2_de)
wav_3_de = audiocore.WaveFile(snd_3_de)
# setup duration for each WaveFile
dur_1_de = 0.63
dur_2_de = 0.56
dur_3_de = 0.49
# setup variables for soundplay
samplename = "1_de"
duration = dur_1_de
samplewav = wav_1_de
swait = 0.1     # short waiting time (s)
lwait = 0.5     # long waiting time (s)
message = ["1", "2", "3"]

# define function for playing a sample
def plsamp():
    global samplename, duration, samplewav, i2s, swait, lwait
    print(samplename + ":" + str(duration))
    i2s.play(samplewav)
    time.sleep(duration)
    time.sleep(swait)

# define function for speaking the whole message from RAM
def spkmsg():
    global samplename, duration, samplewav, i2s, swait, lwait, message
    for c in range(3):
        letter = message[c]
        if letter == "1":
            samplename = "1_de"
            duration = dur_1_de
            samplewav = wav_1_de
            plsamp()
        if letter == "2":
            samplename = "2_de"
            duration = dur_2_de
            samplewav = wav_2_de
            plsamp()
        if letter == "3":
            samplename = "3_de"
            duration = dur_3_de
            samplewav = wav_3_de
            plsamp()
    time.sleep(lwait)
    print("finished spkmsg")
