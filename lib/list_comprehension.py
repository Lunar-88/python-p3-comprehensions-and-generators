
#!/usr/bin/env python3

def return_evens(num_list):
    # return a list of only even numbers from num_list
    return [num for num in num_list if num % 2 == 0]


def make_exclamation(sentence_list):
    # return a new list with "!" added to the end of each string
    return [sentence + "!" for sentence in sentence_list]
