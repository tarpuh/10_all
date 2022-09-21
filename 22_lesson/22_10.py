import wave, struct


def pitch_and_toss():
    source = wave.open("in10.wav", mode="rb")
    dest = wave.open("out10.wav", mode="wb")
    dest.setparams(source.getparams())
    ch = source.getnchannels()
    frames_count = source.getnframes() * ch
    data = struct.unpack("<" + str(frames_count) + "h", source.readframes(frames_count))
    newdata = data[2 * frames_count // 4: 3 * frames_count // 4:] + data[3 * frames_count // 4:] + data[
                                                                                                   :frames_count // 4] + data[
                                                                                                                         frames_count // 4:2 * frames_count // 4]
    newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)
    dest.writeframes(newframes)
    source.close()
    dest.close()


pitch_and_toss()
