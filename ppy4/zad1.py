import math


def panel_calc(length, width, panel_length, panel_width, packet_size):
    length = length * 1.1
    width = width * 1.1
    columns = math.ceil(length / panel_length)
    rows = math.ceil(width / panel_width)
    return math.ceil((columns * rows) / packet_size)


print("Potrzeba: ", panel_calc(4, 4, 0.20, 1, 10))
