#Python 3.4
n = eval(input())

la, lb = map(int, input().split())

sa, sb = map(int, input().split())

if n >= la and n <= lb and n >= sa and n <= sb:
    print("possivel")
else:
    print("impossivel")