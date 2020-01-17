#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for i in range(length):
        #print(f'index: {index}')
        #print(f'weight at index: {weights[index]}')
        weight_index = weights[i]
        #check for None value
        check = hash_table_retrieve(ht,  limit - weight_index)
        # print(f"weight check {check}")
        if check is None:
            #print(weight_index)
            hash_table_insert(ht, weight_index, i)
            # print(f' index: {i} weight: {weight}')
        else:
            result = (i, check)
            return result


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

my_weights = [4, 6, 10, 15, 16]
print(get_indices_of_item_weights(my_weights, 5, 21))