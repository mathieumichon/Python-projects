#!/usr/bin/python3

# === HEADER ===
# serial: 21/10/2020|01
# description: Visual progressbar when browsing an array
# project: None
# members: 
# - MICHON Mathieu (michon@et.intechinfo.fr)
# ==============

# easy-use module for escape sequences
from esc_seq import esc_seq
# without stoping the program on purpose 
# we won't be able to see the progressbar moving 
from time import sleep

# we generate an empty array of 40 None elements
# we don't need to put any values in, we won't make use of the elements
empty_array     = [None] * 40
# we set a max lenght for the progressbar when printed
progressbar_len = int(30)

# browse the array
for index in range(len(empty_array)):
    # we calculate the progress statement according to the index of the array
    progress = round((index * progressbar_len) / len(empty_array))
 
    # === instructions ===
    # empty_array[index] = 5
    # etc..
    # ====================

    # we have no instructions
    # we wait instead so we can see the bar progressing
    sleep(0.1)

    # we print the progress bar
    print("|", end='')
    for step in range(progressbar_len):
        # we give the result a margin of error (+ 2)
        # due to the unpredictable value given by the round() function
        if step <= (progress + 2):
            print(f"{esc_seq.b_white} {esc_seq.reset_all}", end='')
        else:
            print(f"{esc_seq.reset_all} ", end='')
    print("|\r", end='')
# finally, we jump the line
print('')
