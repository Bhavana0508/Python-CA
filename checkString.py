def check(string):
    lc_count = 0
    d_count = 0
    c_count = 0
    for i in string:
        if i>= '0' and i <= '9':
             d_count += 1
        elif i.islower():
             lc_count += 1
        elif i.upper():
             c_count += 1
        else:
             pass
    return d_count, lc_count, c_count
     
input_str = input("Enter a string : ")
d_count, lc_count, c_count = check(input_str)
print(f"No of digits = {d_count}")
print(f"No of Capital Case letters = {c_count}")
print(f"No of small case letters = {lc_count}")
