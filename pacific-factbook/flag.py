from fractions import Fraction
from random import choice


def generate() -> str:
    """
    Generate a random flag. Outputs SVG blob.

    """
    colors = set("red blue white green yellow black orange brown gray purple".split())
    color_background = choice(list(colors))
    color_shape = choice(list(colors - {color_background}))
    aspect_ratio = choice([Fraction("2/3"), Fraction("1/2")])
    height = 200
    width = height / aspect_ratio
    return f"""
        <svg width="{width}" height="{height}" style="border: 1px solid black">
            <rect width="100%" height="100%" fill="{color_background}"/>
            <circle cx="50" cy="50" r="40" stroke="black" stroke-width="4" fill="{color_shape}" />
        </svg>
    """


if __name__ == "__main__":
    print("<h1>Test Flag Report</h1>")
    for _ in range(12):
        print(generate())
        print("<hr>")
