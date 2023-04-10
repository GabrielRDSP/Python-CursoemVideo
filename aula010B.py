n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
m = (n1 + n2)/2
if m >=8:
    print(f"Ta bom!!!")
else:
    print(f"Ta ruim...")
print(f"A média das suas notas é: {m:.1f}")