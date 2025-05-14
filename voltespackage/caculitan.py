import pyjokes

def tell_joke():
    """Displays a random programming joke."""
    joke = pyjokes.get_joke()
    print("\nHere's a joke for you:")
    print(joke)