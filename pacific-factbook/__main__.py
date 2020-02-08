import random

from . import name, flag, coordinate

country_name = name.generate()

print("<h1>", country_name, "</h1>")
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

print("<h1>People and Society</h1>")
print(
    "<dl><dt>population</dt><dd>",
    format(random.randint(40000, 400_000), ","),
    "</dd><dt>nationality</dt><dd>",
    f"{country_name}ian",
    "</dd></dl>",
)
