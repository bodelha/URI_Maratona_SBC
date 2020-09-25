while True:
    try:
        input_ = input().split("\n")
        for pair in input_:
            [a, b] = list(map(int, pair.split()))
            a, b = int(bin(a).replace("0b", "")), int(bin(b).replace("0b", ""))
            c = int ("0b"+(str(a+b)).replace("2", "0"),2)
            print(c)
    except EOFError:
        break