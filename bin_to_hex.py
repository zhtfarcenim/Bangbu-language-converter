def bin_to_hex(bin_str):
    bin_parts = bin_str.split()
    hex_str = ""
    for bin_part in bin_parts:
        decimal_value = int(bin_part, 2)
        hex_str += format(decimal_value, '02X') + " "
    return hex_str.strip()
bin_str = input()
hex_str = bin_to_hex(bin_str)
print(hex_str)