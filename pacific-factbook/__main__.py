import random
from string import Template

from . import name, flag, coordinate

report_template = Template(
    """
<!doctype html>
<html>
<head>
    <meta charset="utf-8" />
    <title>$name</title>
</head>
<body>
    <header>
        <h1>$name</h1>
    </header>
    <figure>
        <figcaption>Flag of $name</figcaption>
        $flag_svg
    </figure>
    <figure>
        <figcaption>Map of $name</figcaption>
        $map_svg
    </figure>

    <section>
        <header>
            <h2>Geography</h2>
        </header>
        <dl>
        <dt>Location</dt>
            <dd>$location</dd>
        <dt>Geographic Coordinates</dt>
            <dd>$coordinates</dd>
        <dt>Coastline</dt>
            <dd>$coastline</dd>
        <dt>Climate</dt>
            <dd>$climate</dd>
        <dt>Natural Resources</dt>
            <dd>$natural_resources</dd>
        </dl>
    </section>

    <section>
        <header>
            <h2>People and Society</h2>
        </header>
        <dl>
        <dt>Population</dt>
            <dd>$population</dd>
        <dt>Nationality</dt>
            <dd>$nationality</dd>
        </dl>
    </section>

    <style>
    header {
        position: sticky;
        top: 0px;
        background: #ECE691;
        padding-left: 1ch;
    }
    body {
        font-family: sans-serif;
    }
    dt {
        margin-top: 1ch;
        font-weight: bold;
    }
    </style>
</body>
</html>
"""
)

pos = coordinate.generate()

coords = ""

if pos.latitude > 0:
    coords += f"{pos.latitude:.2f}&deg; N, "
elif pos.latitude < 0:
    coords += f"{-pos.latitude:.2f}&deg; S, "
else:
    coords += f"{pos.latitude:.2f}&deg;, "

if pos.longitude > 0:
    coords += f"{pos.longitude:.2f}&deg; E."
elif pos.longitude < 0:
    coords += f"{-pos.longitude:.2f}&deg; W."
else:
    coords += f"{pos.longitude:.2f}&deg;."

country_name = name.generate()

report_parameters = {
    "name": country_name,
    "flag_svg": flag.generate(),
    "map_svg": """
        <svg width="200" height="200" style="border: 1px solid black">
            <rect width="100%" height="100%" fill="#0ca4ff"/>
            <circle cx="100" cy="100" r="40" stroke="#E8D9C5" stroke-width="4" fill="#E8D9C5" />
        </svg>
    """,
    "location": "The Pacific ocean.",
    "coordinates": coords,
    "coastline": f"{random.randint(100, 1_000)} km",
    "climate": "Tropical; hot and humid; wet season May to November.",
    "natural_resources": random.choice(
        [
            "forests",
            "minerals (especially gold)",
            "marine products",
            "deep-seabed minerals",
        ]
    ).capitalize(),
    "population": format(random.randint(40000, 400_000), ","),
    "nationality": f"{country_name}ian",
}

print(report_template.safe_substitute(report_parameters))
