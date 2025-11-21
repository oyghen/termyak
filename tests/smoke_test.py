import termyak


def main():
    result = termyak.__name__
    expected = "termyak"
    if result == expected:
        print("smoke test passed")
    else:
        raise RuntimeError("smoke test failed")


if __name__ == "__main__":
    main()
