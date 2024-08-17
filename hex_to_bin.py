def hex_to_bin(hex_str):
    return format(int(hex_str, 16), '04b')
def convert_hex_to_bin_spaced(hex_str):
    hex_numbers = hex_str.split()
    binary_str = ' '.join(hex_to_bin(num) for num in hex_numbers)
    return binary_str
hex_str = input()
binary_str = convert_hex_to_bin_spaced(hex_str)
print(binary_str)