from random import choice


def generate() -> str:
    consonant = lambda: choice("bcdfghjklmnpqrstvwxyz")
    vowel = lambda: choice("aeiou")
    syllable = lambda: consonant() + vowel() + choice(("", "n"))
    return (syllable() + syllable()).capitalize()


if __name__ == "__main__":
    print("<h1>Test Name Report</h1>")
    for _ in range(20):
        print("<hr>")
        print(generate())
