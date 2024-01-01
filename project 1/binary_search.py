# input [1,2,3,4,5,6,7,8,9,10]
# target = 3 
# a function that takes a list and target parameter
# multiple varibales: middle,start, end, steps
# recursion or while loop 
# increase the steps each time a split is done
# conditions to if target is < or > and discard other part of list 
# or conditions to track target position 

def binary_search(list,element):
    middle = 0
    start = 0  # begin of current loop
    end = len(list)
    steps = 0

    while(start <= end):
        print(f"Step: {steps} list: ", list[start:end+1])

        steps = steps + 1
        middle = (start + end) // 2

        if element == list[middle]:
            return middle
        
        if element < list[middle]:
            end = middle -1

            # [1,2,3,4,5] element = 2 => 
        else:
            start = middle +  1
            # updating the start of the list so that it discards other 

    return -1

mylist = [1,2,3,4,5,6,7,8,9]
target = 5

result = binary_search(mylist,target)

if result != -1:
    print(f"Element {target} is found at index {result}")
else:
    print("Element not found ! ")