def shift(x, n):
    codA = ord(x)
    if 65 <= ord(x) <= 90:
        codA = (codA - ord('A') + n) % 26 + ord('A')
        carac_shiftat = chr(codA)
    if 97 <= codA <= 122:
        codA = (codA - ord('a') + n) % 26 + ord('a')
        carac_shiftat = chr(codA)
    return carac_shiftat
    
def shiftare_sir(sir, m):
    L = []
    for x in sir:
        if 65 <= ord(x) <= 90 or 97 <= ord(x) <= 122:
            L.append(shift(x, m))
        else:
            L.append(x)
    sir_shiftat = "".join(L)
    return sir_shiftat

def main():
    # citeste string, si cu cat vrei sa il shiftezi 
    sir = str(input("sirul pe care vr sa-l shiftez: "))
    m = int(input("nr de caractere cu care vr sa-l shiftez: "))
    # print la string shiftat 
    print(shiftare_sir(sir,m))

if __name__ == "__main__":
    main()
