L1  = int(input("Digite o tamanho do primeiro lado:"))
L2 = int(input("Digite o tamanho do segundo lado:"))
L3 = int(input("Digite o tamanho do terceiro lado:"))

soma_dos_Lados = L1 + L2
soma_dos_Lados2 = L2 + L3
soma_dos_Lados3 = L1 + L3


if soma_dos_Lados > L3 and soma_dos_Lados2 > L1 and soma_dos_Lados3 > L2:
    print("Ok!")

    if L1 == L2 and L1 == L3:
        print("Equilátero")
    elif L1 == L2 or L1 == L3 or L2 == L3:
        print("Isóceles")
    else:
        print("Escaleno")
else:
    print("Nao forma triangulo")