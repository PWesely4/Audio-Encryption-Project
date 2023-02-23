import wave
door_creek = wave.open("door_creak.wav", "rb")
door_creek_soundwave = door_creek.readframes(door_creek.getnframes())
#print(door_creek_soundwave)
list = [ord(i) for i in str(door_creek_soundwave)]
print(list)
