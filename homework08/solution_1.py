def main(fields):
    result = 0
    for name, value in fields:
        if name == 'N1':
            result |= (value & 0b111) << 0
        elif name == 'N2':
            result |= (value & 0b111111) << 3
        elif name == 'N3':
            result |= (value & 0b111111111) << 9
        elif name == 'N5':
            result |= (value & 0b1111111111) << 27
    return str(result)
