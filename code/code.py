import time
import audioio
import board
import digitalio
 
button1 = digitalio.DigitalInOut(board.D0)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP
button2 = digitalio.DigitalInOut(board.D1)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP
leda = digitalio.DigitalInOut(board.D4)
ledb = digitalio.DigitalInOut(board.D5)
ledc = digitalio.DigitalInOut(board.D6)
ledd = digitalio.DigitalInOut(board.D7)
lede = digitalio.DigitalInOut(board.D8)
ledf = digitalio.DigitalInOut(board.D9)
ledg = digitalio.DigitalInOut(board.D10)
ledh = digitalio.DigitalInOut(board.D11)
ledi = digitalio.DigitalInOut(board.D12)
 
wave_file = open("helvetica.wav", "rb")
wave = audioio.WaveFile(wave_file)
audio = audioio.AudioOut(board.A0)

leda.direction = digitalio.Direction.OUTPUT
leda.value = False
ledb.direction = digitalio.Direction.OUTPUT
ledb.value = False
ledc.direction = digitalio.Direction.OUTPUT
ledc.value = False
ledd.direction = digitalio.Direction.OUTPUT
ledd.value = False
lede.direction = digitalio.Direction.OUTPUT
lede.value = False
ledf.direction = digitalio.Direction.OUTPUT
ledf.value = False
ledg.direction = digitalio.Direction.OUTPUT
ledg.value = False
ledh.direction = digitalio.Direction.OUTPUT
ledh.value = False
ledi.direction = digitalio.Direction.OUTPUT
ledi.value = False

speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.direction = digitalio.Direction.OUTPUT
speaker_enable.value = True


 
while True:
    audio.play(wave)
    while audio.playing:
        pass
    print("Waiting for button press to continue!")
    while button2.value:
        pass
    audio.resume()

    print("Done!")