#!/usr/bin/python3
import hidden_4  # type: ignore

if __name__ == "__main__":
    for name in sorted(dir(hidden_4)):
        if "__" not in name:
            print(name)
