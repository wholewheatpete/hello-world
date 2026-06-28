import argparse


def greet(name: str = "World") -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Print a greeting.")
    parser.add_argument("--name", default="World", help="Name to greet")
    args = parser.parse_args()
    print(greet(args.name))
