import struct

with open("/dev/input/js0", "rb") as f:
    while True:
        a = f.read(8)
        t, value, code, index = struct.unpack("<Ihbb", a) 
        print("t: {:10d} ms, value: {:6d}, code: {:1d}, index: {:1d}".format(t, value, code, index))
        # count -= 1