a = int(input("panjang sisi 1: "))
b = int(input("panjang sisi 2: "))
c = int(input("panjang sisi 3: "))

if a == b == c:
    print("SAMA SISI")
elif a == b or b == c or a == c:
    print("SAMA KAKI")
else:
    print("SEMBARANG")