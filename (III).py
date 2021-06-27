#print one message if the try block raises a NameError and another for other errors

try:
    a = 123
    if a==123:
        print(b)
        raise NameError("Name error")
    if a >0:
        raise ValueError("Value error")
except NameError as ne:
        print(ne)
except ValueError as ve:
    pritn(ve)
