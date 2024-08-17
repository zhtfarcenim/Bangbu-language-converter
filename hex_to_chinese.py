def hex_binary_to_string(hex_binary_string):
    hex_groups = hex_binary_string.split()
    unicode_string = ""
    for hex_group in hex_groups:
        unicode_code = int(hex_group, 16)
        unicode_string += chr(unicode_code)
    return unicode_string
hex_binary_result=input()
recovered_string = hex_binary_to_string(hex_binary_result)
print(recovered_string)