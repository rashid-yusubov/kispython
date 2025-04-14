def main(fields):
    result = 0
    field_specs = {
        'N1': {'start_bit': 0, 'size': 3},
        'N2': {'start_bit': 3, 'size': 6},
        'N3': {'start_bit': 9, 'size': 9},
        'N5': {'start_bit': 27, 'size': 10}
    }
    for name, value in fields:
        if name in field_specs:
            start_bit = field_specs[name]['start_bit']
            size = field_specs[name]['size']
            mask = (1 << size) - 1
            masked_value = value & mask
            result |= (masked_value << start_bit)
    return str(result)
