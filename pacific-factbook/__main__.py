from . import name, flag, coordinate

print("<h1>", name.generate(), "</h1>")
print("<figure>", flag.generate(), "</figure>")
print("<p>Location:")
pos = coordinate.generate()

if pos.latitude > 0:
    print(f"{pos.latitude}&deg; N,")
elif pos.latitude < 0:
    print(f"{-pos.latitude}&deg; S,")
else:
    print(f"{pos.latitude}&deg;,")

if pos.longitude > 0:
    print(f"{pos.longitude}&deg; E.")
elif pos.longitude < 0:
    print(f"{-pos.longitude}&deg; W.")
else:
    print(f"{pos.longitude}&deg;.")

print("</p>")
