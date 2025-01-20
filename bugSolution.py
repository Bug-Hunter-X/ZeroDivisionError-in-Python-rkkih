def my_function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0  # or handle the error in another appropriate way

result = my_function(10, 0)
print(result) # Output: 0