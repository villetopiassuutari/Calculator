def add(luku:int, syote:str):
    return luku+syote
def sub(luku:int, syote:str):
    return luku-syote
def mul(luku:int, syote:str):
    return luku*syote
def div(luku:int, syote:str):
    return luku/syote
luku = 0

print(f"Luku on {luku}.")
while True:

    op = input("Anna operaatio (tyhjä lopettaa): ")
    if op == "":
        print("Kiitos ja moi!")
        break
    fc = op[0]
    syote = int(op[1:len(op)])
    
    if fc != "+,-,*,/":
        print("Operaatio puuttui")
    if fc == "+":
        luku = add(luku, syote)
    if fc == "-":
        luku = sub(luku, syote)
    if fc == "*":
        luku = mul(luku, syote)
    if fc == "/":
       luku = div(luku, syote)


    print(f"Luku on {luku}.")