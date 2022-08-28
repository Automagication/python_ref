#DECORATORS**
def lowercase_decorator(function):
    def wrapper():
        func=function()
        string_lowercase=func.lower()
        return string_lowercase
    return wrapper

@lowercase_decorator
def hello_world():
    return "Hello world"

print(hello_world())
