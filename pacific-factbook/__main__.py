from . import name, flag, coordinate

print("<h1>", name.generate(), "</h1>")
print("<figure>", flag.generate(), "</figure>")
print("<p>Location:")
pos = coordinate.generate()

if pos.latitude > 0:
    print(f"{pos.latitude:.2f}&deg; N,")
elif pos.latitude < 0:
    print(f"{-pos.latitude:.2f}&deg; S,")
else:
    print(f"{pos.latitude:.2f}&deg;,")

if pos.longitude > 0:
    print(f"{pos.longitude:.2f}&deg; E.")
elif pos.longitude < 0:
    print(f"{-pos.longitude:.2f}&deg; W.")
else:
    print(f"{pos.longitude:.2f}&deg;.")

print("</p>")
