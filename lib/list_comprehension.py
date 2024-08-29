#!/usr/bin/env python3

def return_evens(num_list):
    evens = []
    for n in num_list:
        if n % 2 == 0:
            evens.append(n)  
    return evens 
return_evens([1, 2, 3, 4, 5, 6, 7, 8, 9])


def make_exclamation(sentence_list):
    s= []
    for sentence in sentence_list:
        if len(sentence_list) > 0:
            s.append(sentence + '!')
    return s
make_exclamation(["Hello", "I'm doing great", "Python is fun"])