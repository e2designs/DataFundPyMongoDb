audio = {
    "amp": "Linn",
    "preamp": "Luxman",
    "speakers": "Energy",
    "ic": "Crystal Ultra",
    "pc": "JPS",
    "power": "Equi-Tech",
    "sp": "Crystal Ultra",
    "cdp": "Nagra",
    "up": "Oppo",
}
dict_ls = [audio]
video = {"tv": "LG 65C7 OLED", "stp": "DISH", "HDMI": "DH Labs", "cable": "coax"}
print("list of dict elements;")
dict_ls.append(video)
for i, row in enumerate(dict_ls):
    print("row", i, ":")
    print(row)

# OUTPUT
"""
row 0 :
{'amp': 'Linn', 'preamp': 'Luxman', 'speakers': 'Energy', 'ic': 'Crystal Ultra', 'pc': 'JPS', 'power': 'Equi-Tech', 'sp': 'Crystal Ultra', 'cdp': 'Nagra', 'up': 'Oppo'}
row 1 :
{'tv': 'LG 65C7 OLED', 'stp': 'DISH', 'HDMI': 'DH Labs', 'cable': 'coax'}
"""
