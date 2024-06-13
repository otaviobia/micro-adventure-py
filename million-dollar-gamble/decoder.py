# Decodificador
TA = ord('A')
TZ = ord('Z')
KT = 0
print("ENTRE A MENSAGEM SECRETA")
print("DIGITE FIM PARA TERMINAR O PROGRAMA")
print()
M = input("MENSAGEM SECRETA ")

while M != "FIM":
	for I in range(len(M)):
		T = ord(M[I])
		if T < TA or T > TZ:
			print(chr(T), end = "")
			continue
		else:
			KT = KT + 1
			if KT > 26:
				KT = 1
			T = T - KT
			if T < TA:
				T = T + 26
			print(chr(T), end = "")
	print()
	KT = 0
	M = input("MENSAGEM SECRETA ")

print("*** FIM DA MENSAGEM ***")
quit()