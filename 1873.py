r = ["pedra tesoura", "pedra lagarto", "papel spock", "tesoura lagarto", "lagarto spock", "papel pedra", "spock pedra", "tesoura papel", "lagarto papel", "spock tesoura"]
out = []
n = int(input())
for _ in range(n):
    input_ = input()
    if input_[:input_.index(" ")] == input_[input_.index(" ") + 1:]:
        out.append ("empate") 
    elif input_ in r:
        out.append ("rajesh")
    else:
        out.append ("sheldon")
    
print (*out, sep='\n')
