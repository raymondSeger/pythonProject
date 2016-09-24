class ExampleClass:
    """A simple example class"""

    i = 12345

    def f(self):
        return 'hello world'

    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart



example_object = ExampleClass(3.0, -4.5)
print(example_object)

print(example_object.i)

example_object.f()