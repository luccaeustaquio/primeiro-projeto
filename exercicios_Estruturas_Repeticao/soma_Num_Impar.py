total = 0
for atual in range(3,100,3):
    if atual % 2 == 1 :
        print(atual)
        total += atual


print(f"Soma total: {total}")
