def generate() -> str:
    return "kirau"


if __name__ == "__main__":
    print("<h1>Test Name Report</h1>")
    for _ in range(20):
        print("<hr>")
        print(generate())
