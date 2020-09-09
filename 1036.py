out = []

a, b, c = map(float, input().split())

try:
    delta = float((b**2 - 4*a*c)**0.5)
    out.append(f"R1 = {((-b + delta)/(2*a)):.5f}")
    out.append(f"R2 = {((-b - delta)/(2*a)):.5f}")

except:
    out.append("Impossivel calcular")

print (*out, sep='\n')