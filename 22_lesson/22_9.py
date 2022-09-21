import wave, struct


def break_the_silence():
    source = wave.open("in10.wav", mode="rb")
    dest = wave.open("out9.wav", mode="wb")
    dest.setparams(source.getparams())
    ch = source.getnchannels()
    frames_count = source.getnframes() * ch
    data = struct.unpack("<" + str(frames_count) + "h", source.readframes(frames_count))
    newdata = list()
    for elem in data:
        if -5 <= elem <= 5:
            pass
        else:
            newdata.append(elem)
    newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)
    dest.writeframes(newframes)
    source.close()
    dest.close()


break_the_silence()
