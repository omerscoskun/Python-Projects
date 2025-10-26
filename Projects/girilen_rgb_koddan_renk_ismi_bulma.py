# region Imports

import json 

# endregion

# region Definitions

def rgb_to_hexCode(x, y, z):
    return "#{:02X}{:02X}{:02X}".format(x, y, z)

def hex_to_colorName(hex_code):

    color_map = {}
    file_path = "C:\\Users\\ASUS\\Desktop\\python_calismalari\\.resources\\2. Projeler\\Vector Spaces Similarity\\colors.txt"

    with open(file_path, "r") as file:
        for line in file:
                clean_line = line.strip().strip(',')
                if clean_line:
                    code, name = json.loads(clean_line)
                    color_map[code] = name

    lookup_key = hex_code.lstrip('#')

    return color_map.get(lookup_key, "Unknown Color")

# endregion

print("rgb renk kodu gir:")
r_input = input("R: ")
g_input = input("G: ")
b_input = input("B: ")

hex_code = rgb_to_hexCode(int(r_input), int(g_input), int(b_input))
color_name = hex_to_colorName(hex_code)

print("Hex Kodu:", hex_code)
print("Renk İsmi:", color_name)

