"""Generate and print numbers from 33 to 50 (inclusive)."""


def generate_numbers(start: int = 33, end: int = 50) -> list[int]:
    """Return a list of integers from start to end (inclusive)."""
    return list(range(start, end + 1))


def main() -> None:
    numbers = generate_numbers()
    print(f"Numbers from 33 to 50:")
    for n in numbers:
        print(n)


if __name__ == "__main__":
    main()
