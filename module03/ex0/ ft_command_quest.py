import sys

def main() -> None:
    print("=== Player Score Analytics ===")
    print(f"Program name:{sys.argv[0]}")
    if len(sys.argv) > 1:
        print(f"Arguments received: {len(sys.argv) - 1}")
        i = 1
        for arg in sys.argv[1:]:
            print(f"Argument {i}: {arg}")
            i += 1
        print(f"Total arguments: {len(sys.argv)}")
    else:
        print("No arguments provided!")
        print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()