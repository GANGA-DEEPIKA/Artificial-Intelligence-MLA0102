x, y = 0, 0
print(f"[{x}/5, {y}/3]")

x = 5
print(f"[{x}/5, {y}/3]")

t = min(x, 3 - y); x -= t; y += t
print(f"[{x}/5, {y}/3]")

y = 0
print(f"[{x}/5, {y}/3]")

t = min(x, 3 - y); x -= t; y += t
print(f"[{x}/5, {y}/3]")

x = 5
print(f"[{x}/5, {y}/3]")

t = min(x, 3 - y); x -= t; y += t
print(f"[{x}/5, {y}/3]")
