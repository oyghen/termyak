import termyak


def main():
    actual = termyak.__name__
    expected = "termyak"
    if actual == expected:
        print("smoke test passed")
    else:
        raise RuntimeError("smoke test failed")


if __name__ == "__main__":
    main()
