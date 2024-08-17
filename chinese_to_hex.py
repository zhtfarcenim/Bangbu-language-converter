def string_to_hex_binary(unicode_string):
    hex_binary_string = ""
    for char in unicode_string:
        unicode_code = ord(char)
        hex_binary_string += f"{unicode_code:04x} "
    return hex_binary_string.strip()
user_input = input()
hex_binary_result = string_to_hex_binary(user_input)
print( hex_binary_result)