import wave, struct


def chip_and_dale(number):
    source = wave.open("in10.wav", mode="rb")
    dest = wave.open("out8.wav", mode="wb")
    dest.setparams(source.getparams())
    ch = source.getnchannels()
    frames_count = source.getnframes() * ch
    data = struct.unpack("<" + str(frames_count) + "h", source.readframes(frames_count))
    newdata = data[::number]
    newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)
    dest.writeframes(newframes)
    source.close()
    dest.close()


chip_and_dale(2)
