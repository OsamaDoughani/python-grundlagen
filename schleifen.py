preise = [4.50, 12.99, 3.20, 8.00]
summe = 0

for preis in preise:
    print(f"Preis: {preis:.2f} Euro")
    summe = summe + preis

print(f"Gesamt: {summe:.2f} Euro")