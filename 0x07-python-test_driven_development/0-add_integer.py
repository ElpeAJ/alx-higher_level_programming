def add_integer(a, b=98):
    while True:
        try:
            # Attempt to cast a and b to integers if they are floats
            a = int(a) if isinstance(a, float) else a
            b = int(b) if isinstance(b, float) else b

        # Add a and b and return the result
        except (ValueError, TypeError):
            raise TypeError("a and b must be integers or floats")
        else:
            break
    return a + b
