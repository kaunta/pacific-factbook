def generate() -> str:
    """
    Generate a random flag. Outputs SVG blob.

    """
    return """
        <svg width="300" height="200">
            <rect width="100%" height="100%" fill="blue"/>
            <circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" />
        </svg>
    """


if __name__ == "__main__":
    print("<h1>Test Flag Report</h1>")
    for _ in range(12):
        print(generate())
        print("<hr>")
