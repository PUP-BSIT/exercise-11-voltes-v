import pyjokes

def joke_generator():
    joke = pyjokes.get_joke()
    print('Here is a joke for you:', joke)
    print("\n")