x = 42
y = 3.14
z = "hello"
flag = True
nothing = None
my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
my_dict = {"key": "value"}
my_set = {7, 8, 9}

def my_func():
    pass

print("name | value | type")
print("-" * 40)
print(f"x | {x} | {type(x).__name__}")
print(f"y | {y} | {type(y).__name__}")
print(f"z | {z} | {type(z).__name__}")
print(f"flag | {flag} | {type(flag).__name__}")
print(f"nothing | {nothing} | {type(nothing).__name__}")
print(f"my_list | {my_list} | {type(my_list).__name__}")
print(f"my_tuple | {my_tuple} | {type(my_tuple).__name__}")
print(f"my_dict | {my_dict} | {type(my_dict).__name__}")
print(f"my_set | {my_set} | {type(my_set).__name__}")
print(f"my_func | {my_func} | {type(my_func).__name__}")
