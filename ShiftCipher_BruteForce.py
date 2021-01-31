#Name: ShiftCipherv3
#Author: Mark Tullier
#Last Edited: 01/30/2021 10:01PM
#Desc: This program was developed for CIS491: Intro to Cryptography at CSU-Pueblo. 
#The user inputs a string that has been encrypted with a shift cipher, and the program does its best to
#pull the decrypted string with a distance calculation using frequency tables. 
#There are two tables used in the calculation: a model table of the English language, trained on 
#the first chapter of a book called "Ender's Game", and the frequency table of the shifted string (which is iterated over 25 times).
#The program accepts the two tables into a function where the difference of each pair of index values is squared, added to the total, 
#and finally returned after the square root of the total is found. Each of these distances is stored in a list that then has the index position 
#of the smallest value taken from it and compared against the index position of a list that holds all of the decrypted string possibilities. 
#The final result returned should, in theory, be the correct decryption, depending on how much text you've trained the model table on;
#the larger your sample size, the more accurate your results will be for the population. Granted, the program is quite hamfisted in the ways
#that it tackles each individual challenge associated with such an application; however, I'm just honestly glad it works :)

import math

#function that finds the distance between two frequency table
def freq_table_dist(a, b):
    #holds the value of the return float
    total = 0;
    
    #iterates through list and finds the difference between each element at index i
    for i in range(0, 26):
        #subtracts i in a from i in b, squares it, then adds it to the total
        total += pow(a[i] - b[i], 2)
    
    #squares the total and returns it
    return round(math.sqrt(total), 4)

#function that creates a frequency table for the passed string s
def rel_freq_table(s):
    #tables to be written to
    f_table, rf_table = [0] * 26, [0] * 26
    
    s = "".join([c.lower() for c in s if c.isalpha()])
    
    #iterates over the string s
    for c in s:
        #subtracts the value of the character from the value of 'a', 
        #then adds 1 to that position in the table
        f_table[ord(c) - ord('a')] += 1
    
    #builds out the relative frequency table from the original frequency table
    for i in range(0, 26):
        rf_table[i] = round(f_table[i]/sum(f_table), 3)
        
    #prints the frequency list for the specified string    
    return rf_table

#function that brute-forces the shift cipher
def brute_decrypt(s):
    #model frequency list of the English alphabet
    with open('longtext.txt', 'rt') as myfile:
        contents = myfile.read()
    
    model_lst = rel_freq_table(contents)
    
    s = "".join([c.lower() for c in s if c.isalpha()])
    
    #list for decrypted strings and distances
    decrypted_strings_lst, distance_lst = [""] * 26, [0] * 26
    
    #iterates over a range from 1 to 26
    for i in range(0, 26):
        #empty string to be written to
        decrypted_string = ""
        
        #iterates over the characters in the string
        for c in s:
            #if letters are uppercase then shifts them by i
            if(c.isupper()):
                decrypted_string += chr((ord(c) - i - ord('A')) % 26 + ord('A'))
            #else shift letters by i as if they were lowercase
            else:
                decrypted_string += chr((ord(c) - i - ord('a')) % 26 + ord('a'))
        
        #adds each decrypted string to the list to be pulled when compared        
        decrypted_strings_lst[i] = decrypted_string
        
        #creates a list of distances to compare against for the 
        distance_lst[i] = freq_table_dist(rel_freq_table(decrypted_strings_lst[i]), model_lst)
    
    #returns the string at the same index position as the shortest distance from distance_lst
    return decrypted_strings_lst[distance_lst.index(min(distance_lst))]

#calls the function with the string
s = input("Enter the string to be decrypted: ")

print("Decrypted String: " + brute_decrypt(s))