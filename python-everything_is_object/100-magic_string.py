def magic_string():
    magic_string.counter = getattr(magic_string, 'counter', 0) + 1
    return ", ".join(["BestSchool"] * magic_string.counter)
