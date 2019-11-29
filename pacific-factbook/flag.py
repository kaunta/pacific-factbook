from fractions import Fraction
from random import choice


def generate() -> str:
    """
    Generate a random flag. Outputs SVG blob.

    """
    aspect_ratio = choice([Fraction("2/3"), Fraction("1/2")])
    height = 200
    width = height / aspect_ratio
    return f"""
        <svg width="{width}" height="{height}">
            <rect width="100%" height="100%" fill="blue"/>
            <circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" />
        </svg>
    """


if __name__ == "__main__":
    print("<h1>Test Flag Report</h1>")
    for _ in range(12):
        print(generate())
        print("<hr>")
