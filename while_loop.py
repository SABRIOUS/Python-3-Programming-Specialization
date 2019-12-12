Write a function called stop_at_four that iterates through a list of numbers. Using a while loop, append each number to a new list until the number 4 appears. The function should return the new list.

def stop_at_four(lisq):
    new_list = []
    count = 0

    while count < len(lisq):
        if lisq[count] != 4:
            new_list.append(lisq[count])
            count += 1
        else:
            break
    return new_list
