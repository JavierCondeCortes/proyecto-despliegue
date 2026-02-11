import os

a = int(os.getenv("VAR_A",0))
b = int(os.getenv("VAR_B",0))

print(f"Suma: {a+b}")