#!/usr/bin/python3

def element_at(my_list, idx):
    lenList = len(my_list)
    if idx > lenList and idx < 0:
        return None
    
    return my_list[idx]