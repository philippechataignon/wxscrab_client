#!/usr/bin/env python3

def play_pyaudio(seg):
    import pyaudio

    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(seg.sample_width),
                    channels=seg.channels,
                    rate=seg.frame_rate,
                    output=True)

    # Just in case there were any exceptions/interrupts, we release the resource
    # So as not to raise OSError: Device Unavailable should play() be used again
    try:
        # break audio into half-second chunks (to allows keyboard interrupts)
        for chunk in make_chunks(seg, 500):
            stream.write(chunk._data)
    finally:
        stream.stop_stream()
        stream.close()

        p.terminate()

def play_dsp(file):
    f = open(file, "rb")
    out = open("/dev/dsp", "wb")
    out.write(f.read())
    out.close()
    f.close()

# play_dsp("fin_tour.raw")
# play_dsp("debut.raw")
play_dsp("valid.raw")
