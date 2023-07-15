#!/usr/bin/python3

def element_at(my_list, idx):
   #for i in range(len(my_list)):
   if idx < 0:
       return (None)
   if idx > len(my_list) - 1:
       return (None)
   return (my_list[idx])
