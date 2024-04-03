# Copyright (c) 2024 Otávio Biagioni
# License: MIT License
"""QWERTYCODE"""

mixed_alphabet = "QAZWSXEDCRFVTGBYHNUJMIKOLP"
regular_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("TYPE 'STOP' TO END PROGRAM\n")

while True:
    print("INPUT MESSAGE")
    in_string = input().upper()
    if in_string == "STOP":
      break
    out_string = ""
    for i in range(0, len(in_string)):
      in_char_i = in_string[i:i+1]
      if (in_char_i.isalpha()):
        for j in range(0, len(regular_alphabet)):
          if in_char_i == mixed_alphabet[j: j+1]:
            out_string += regular_alphabet[j: j+1]
      else:
        out_string += in_char_i
    print (out_string)