# Copyright (c) 2024 Otávio Biagioni
# License: MIT License
"""ENCODER/DECODER"""

print("ENTER YOUR PASSWORD")
key = input().upper().encode('ascii', 'replace').decode('ascii')
print("TYPE THE SECRET MSG")
print("JUST TYPE 'STOP' WHEN DONE")

while True:
    inp = input().upper().encode('ascii', 'replace').decode('ascii')
    if inp == "STOP":
        break
    out = ""
    j = 0
    for i in range(0, len(inp)):
        inp_char = inp[i:i + 1]
        if inp_char.isalpha():
            j += 1
            if j > len(key):
                j = 1
            key_pos = ord(key[j - 1:j]) - ord("A") + 1
            inp_pos = ord(inp_char) - ord("A") + 1
            if key_pos <= inp_pos:
                key_pos += 26
            out_pos = key_pos - inp_pos
            out += chr(out_pos + ord("A") - 1)
        else:
            out += inp_char
    print(out)
