## This is the text editor interface. 
## Anything you type or change here will be seen by the other person in real time.

# Input: lists of numbers
# Output: a list of numbers that appear in every input list

# I: [[1, 4, 8, 9, -1], [2, 4, -6]]
# O: [4]

# I: [[], []]
# O: None



def in_every_list(numbers):
    
    length_of_numbers = len(numbers)
    
    num_list_index = {}
    
    num_to_print = []
    
    for index, num_list in enumerate(numbers):
        for num in num_list:
            if num in num_list_index.keys():
                num_list_index[num].add(index)
                
            else:
                num_list_index[num] = set([index])
                
    for num, list_index in num_list_index.items():
        print "num", num
        print "list_index", list_index
        if len(list_index) == length_of_numbers:
            num_to_print.append(num)

    return num_to_print
            
numbers = [[1, -4, 8, -9, 1], [2, -4, 6, -9], [-9, -4, 0, 0, 0]]

print in_every_list(numbers)
            
        
    