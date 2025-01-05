def function_with_uncommon_error(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a  #Handle b=0 case to prevent ZeroDivisionError
    else:
        return a / b

result = function_with_uncommon_error(10, 0)
print(result) # Output: 10
result2 = function_with_uncommon_error(10, 2)
print(result2) # Output: 5.0