# -*- coding: utf-8 -*-
"""
Created on Thu May 21 22:27:22 2020

@author: kritik
@dice roll
"""
import random
play = "y"
while play == "y" or play == "yes":
    facenumber = random.randint(1, 6)# generating random no. from 1 to 6
    

    if facenumber == 1:#generating faces for facenumbers
        print("----------")
        print("|        |")
        print("|   O    |")
        print("|        |")
        print("----------")
    if facenumber == 2:
        print("----------")
        print("|   O    |")
        print("|        |")
        print("|   O    |")
        print("----------")
    if facenumber == 3:
        print("----------")
        print("|O       |")
        print("|   O    |")
        print("|      O |")
        print("----------")
    if facenumber == 4:
        print("----------")
        print("|O      O|")
        print("|        |")
        print("|O      O|")
        print("----------")
    if facenumber == 5:
        print("----------")
        print("|O      O|")
        print("|   O    |")
        print("|O      O|")
        print("----------")
    if facenumber == 6:
        print("----------")
        print("|O      O|")
        print("|O      O|")
        print("|O      O|")
        print("----------")
        
    play = input("Roll the dice again type yes/no or y/n:\t").lower()




    
        
        
        
        
        
        
