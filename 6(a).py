#program to search for the position of an element in an array using sequential search 
def search(lst, key):
    for i in lst:
        if i == key:
            return lst.index(i)
            
input_lst = []
n = int(input("Enter no of elements : "))
print("Enter the elements")

for i in range(0, n):
    ele = int(input())
    input_lst.append(ele)
    
key = int(input("Enter the element to be searched : ")
pos = search(input_lst, key)
          
if pos == None:
    print("Element is not found")
else:
    print(f"Element is present at position {pos}")

