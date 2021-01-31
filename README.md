# ShiftCipher_BruteForce
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
