def test_function():
    def inner_function():
        return "Inside test_function"

    return inner_function()


print(test_function())
#inner_function()
