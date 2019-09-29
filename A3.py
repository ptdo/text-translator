#Rachel Do

import os
import sys


path = input("Enter file name:  ") #Enter file name under format: "filename.txt"

'''Morse code dictopnary'''
#International Morse Code from https://www.123rf.com/photo_84079200_stock-vector-international-morse-code-.html
morse_dict = {
          "A" : ".-",
          "B" : "-...",
          "C" : "-.-.",
          "D" : "-..",
          "E" : ".",
          "F" : "..-.",
          "G" : "--.",
          "H" : "....",
          "I" : "..",
          "J" : ".---",
          "K" : "-.-",
          "L" : ".-..",
          "M" : "--",
          "N" : "-.",
          "O" : "---",
          "P" : ".--.",
          "Q" : "--.-",
          "R" : ".-.",
          "S" : "...",
          "T" : "-",
          "U" : "..-",
          "V" : "...-",
          "W" : ".--",
          "X" : "-..-",
          "Y" : "-.--",
          "Z" : "--..",
          " " : "",
          "\n": ".-.-",
          "1" : ".----",
          "2" : "..---",
          "3" : "...--",
          "4" : "....-",
          "5" : ".....",
          "6" : "-....",
          "7" : "--...",
          "8" : "---..",
          "9" : "----.",
          "0" : "-----",
          "." : ".-.-.-",
          "," : "--..--",
          ":" : "---...",
          "?" : "..--..",
          "'" : ".----.",
          "-" : "-....-",
          "/" : "-..-.",
          "@" : ".--.-.",
          "=" : "-...-",
          "(" : "-.--.",
          ")" : "-.--.- ",
          "_" : "..--.-",
          ";" : "-.-.-.",
          "&" : ".-...",
          "$" : "...-..-",
          "!" : "-.-.--",
          "+" : ".-.-."
     }
morse_lower = {
     "a" : ".-",
     "b" : "-...",
     "c" : "-.-.",
     "d" : "-..",
     "e" : ".",
     "f" : "..-.",
     "g" : "--.",
     "h" : "....",
     "i" : "..",
     "j" : ".---",
     "k" : "-.-",
     "l" : ".-..",
     "m" : "--",
     "n" : "-.",
     "o" : "---",
     "p" : ".--.",
     "q" : "--.-",
     "r" : ".-.",
     "s" : "...",
     "t" : "-",
     "u" : "..-",
     "v" : "...-",
     "w" : ".--",
     "x" : "-..-",
     "y" : "-.--",
     "z" : "--.."
     }
morse_reverse=dict((v,k) for (k,v) in morse_dict.items())
''' Baudot Dictionary'''
#Baudot-Murray code ITA2 from: https://www.boxentriq.com/code-breaking/baudot-code
baudot_upper = {
     "Figures" : "11011",
     "Letters" : "11111",
     " " : "00100",
     "Del" : "11000",
     "\n" : "00010",
     "CR" : "01000",
     "A" : "00011",
     "B" : "11001",
     "C" : "01110",
     "D" : "01001",
     "E" : "00001",
     "F" : "01101",
     "G" : "11010",
     "H" : "10100",
     "I" : "00110",
     "J" : "01011",
     "K" : "01111",
     "L" : "10010",
     "M" : "11100",
     "N" : "01100",
     "O" : "11000",
     "P" : "10110",
     "Q" : "10111",
     "R" : "01010",
     "S" : "00101",
     "T" : "10000",
     "U" : "00111",
     "V" : "11110",
     "W" : "10011",
     "X" : "11101",
     "Y" : "10101",
     "Z" : "10001"
     }
baudot_lower = {
     "a" : "00011",
     "b" : "11001",
     "c" : "01110",
     "d" : "01001",
     "e" : "00001",
     "f" : "01101",
     "g" : "11010",
     "h" : "10100",
     "i" : "00110",
     "j" : "01011",
     "k" : "01111",
     "l" : "10010",
     "m" : "11100",
     "n" : "01100",
     "o" : "11000",
     "p" : "10110",
     "q" : "10111",
     "r" : "01010",
     "s" : "00101",
     "t" : "10000",
     "u" : "00111",
     "v" : "11110",
     "w" : "10011",
     "x" : "11101",
     "y" : "10101",
     "z" : "10001"
     }
baudot_fig = {
     "3" : "00001",
     "\n" : "00010",
     "-" : "00011",
     " " : "00100",
     "'" : "00101",
     "8" : "00110",
     "7" : "00111",
     "CR" : "01000",
     "4" : "01010",
     "," : "01100",
     "!" : "01101",
     ":" : "01110",
     "(" : "01111",
     "5" : "10000",
     "+" : "10001",
     ")" : "10010",
     "2" : "10011",
     "$" : "10100",
     "6" : "10101",
     "0" : "10110",
     "1" : "10111",
     "9" : "11000",
     "?" : "11001",
     "&" : "11010",
     "Figures" : "11011",
     "." : "11100",
     "/" : "11101",
     ";" : "11110",
     "Letters" : "11111"
     }

baudot_upper_reverse = dict((v,k) for (k,v) in baudot_upper.items())
baudot_fig_reverse = dict((v,k) for (k,v) in baudot_fig.items())
''' File input function, allows you to put a file in for reading and converting.'''
def fileInput():
     file = open(path,'r')
     input_text = file.read()
     return input_text

input_text = fileInput()

def utf8_to_morse(input_text):
     morse_text = ""
     for x in input_text:
          if (x in morse_dict):
               morse_text += morse_dict[x] + " "
          elif (x in morse_lower):
               morse_text+=morse_lower[x] + " "
          else:
               morse_text +="???" + " "
     return morse_text

def utf8_to_baudot(input_text):         
     baudot_text = ""
     letter = 0 #To keep track of letters
     fig = 0 #To keep track of numbers
     for x in input_text:
          if (x in baudot_upper):
               if (letter > 0):
                    baudot_text+= baudot_upper[x] + " "
               else:
                    baudot_text+="11111" + " "
                    baudot_text+= baudot_upper[x] + " "
                    letter+=1
                    fig = 0
          elif (x in baudot_lower):
               if (letter > 0):
                    baudot_text+= baudot_lower[x] + " "
               else:
                    baudot_text+="11111" + " "
                    baudot_text+=baudot_lower[x] + " " 
                    letter+=1
                    fig = 0
          elif (x in baudot_fig):
               if(fig > 0):
                    baudot_text+= baudot_fig[x] + " "
               else:
                    baudot_text += "11011" + " "
                    baudot_text += baudot_fig[x] + " "
                    fig+=1
                    letter = 0
          else:
               baudot_text += "???"
     return baudot_text

def morse_to_utf8(input_text):
     split_text = input_text.split(' ')
     utf8_text = ""
     for x in split_text:
         if x in morse_reverse:
            utf8_text += morse_reverse[x]
         else:
            utf8_text += '???'
     return utf8_text

def baudot_to_utf8(input_text):
     baudot_text = ""
     input_text = input_text.split()
     letter = False
     fig = False
     for x in input_text:
          if (x == "11111"):
               letter = True
               fig = False
          elif (x == "11011"):
               letter = False
               fig = True
          else:
               if (letter == True):
                    if (x in baudot_upper_reverse):
                         baudot_text += baudot_upper_reverse[x]
                    else:
                         baudot_text += "???"
               elif (fig == True):
                    if (x in baudot_fig_reverse):
                         baudot_text += baudot_fig_reverse[x]
                    else:
                         baudot_text += "???"
               else:
                    baudot_text += "???"
     return baudot_text

def baudot_to_utf32():
     utf32_text = baudot_to_utf8(input_text)
     return utf32_text

def morse_to_baudot():
     data = morse_to_utf8(input_text)
     morse_text = utf8_to_baudot(data)
     return morse_text

def morse_to_utf32():
     data = morse_to_utf8(input_text)
     return data

def baudot_to_morse():
     data = baudot_to_utf8(input_text)
     morse_text = utf8_to_morse(data)
     return morse_text

def utf32_to_morse():
     data = utf32_to_utf8()
     morse_text = utf8_to_morse(data)
     return morse_text

def utf32_to_baudot():
     data = utf32_to_utf8()
     baudot_text = utf8_to_baudot(data)
     return baudot_text

def utf8_to_utf32():
     file = open(path, 'r', encoding= 'utf-8')
     input_text = file.read()
     return input_text

def utf32_to_utf8():
    file = open(path, 'r', encoding= 'utf-32')
    input_text = file.read()
    return input_text
''' Menu function for switching between different kinds of encodings.'''
def menu():
     print("--------------Menu-------------")
     print("1. UTF-8 to Morse Code")
     print("2. UTF-8 to Baudot Code")
     print("3. UTF-8 to UTF-32")
     print("4. Morse Code to UTF-8")
     print("5. Morse Code to Baudot Code")
     print("6. Morse Code to UTF-32")
     print("7. Baudot Code to UTF-8")
     print("8. Baudot Code to Morse Code")
     print("9. Baudot Code to UTF-32")
     print("10. UTF-32 to UTF-8")
     print("11. UTF-32 to Morse Code")
     print("12. UTF-32 to Baudot Code")
     print("13. Exit")
     print("--------------------------------")
     option = input("Choose your translator:  ")
     if (option == '1'):
          output_text = utf8_to_morse(input_text) 
          output_file = open('u8Morse.txt','w+') 
          output_file.write(output_text)
          output_file.close()
          print("File created: u8Morse.txt")
          cont = input("Do you want to continue? Y/N\n")
          if (cont == 'Y'):
               menu()
          else:
               sys.exit(0)
     elif (option == '2'):
          output_text = utf8_to_baudot(input_text)
          output_file = open('u8Baudot.txt','w+') 
          output_file.write(output_text)
          output_file.close()
          print("File created: u8Baudot.txt")
          cont = input("Do you want to continue? Y/N\n")
          if (cont == 'Y'):
               menu()
          else:
               sys.exit(0)   
     elif (option == '3'):
          output_file = open('utf8_to_utf32.txt','w+', encoding = 'utf-32')
          output_file.write(input_text)
          output_file.close()
          print("File created: utf8_to_utf32.txt")
          cont = input("Do you want to continue? Y/N\n")
          if (cont == 'Y'):
               menu()
          else:
               sys.exit(0)
     elif (option == '4'):
          output_text = morse_to_utf8(input_text) 
          output_file = open('morseU8.txt','w+') 
          output_file.write(output_text)
          output_file.close()
          print("File created: morseU8.txt")
          cont = input("Do you want to continue? Y/N\n")
          if (cont == 'Y'):
               menu()
          else:
               sys.exit(0)
     elif (option == '5'):
          output_text = morse_to_baudot() 
          output_file = open('morseBaudot.txt','w+') 
          output_file.write(output_text)
          output_file.close()
          print("File created: morseBaudot.txt")
          cont = input("Do you want to continue? Y/N\n")
          if (cont == 'Y'):
               menu()
          else:
               sys.exit(0)
     elif (option == '6'):
          output_text = morse_to_utf32() 
          output_file = open('morseU32.txt','w+',encoding="utf-32") 
          output_file.write(output_text)
          output_file.close()
          print("File created: morseU32.txt")
          cont = input("Do you want to continue? Y/N\n")
          if (cont == 'Y'):
               menu()
          else:
               sys.exit(0)
     elif (option == '7'):
          output_text = baudot_to_utf8(input_text) 
          output_file = open('baudotU8.txt','w+') 
          output_file.write(output_text)
          output_file.close()
          print("File created: baudotU8.txt")
          cont = input("Do you want to continue? Y/N\n")
          if (cont == 'Y'):
               menu()
          else:
               sys.exit(0)
     elif (option == '8'):
          output_text = baudot_to_morse() 
          output_file = open('baudotMorse.txt','w+',encoding="utf-8")
          output_file.write(output_text)
          output_file.close()
          print("File created: baudotMorse.txt")
          cont = input("Do you want to continue? Y/N\n")
          if (cont == 'Y'):
               menu()
          else:
               sys.exit(0)
     elif (option == '9'):
          output_text = baudot_to_utf32() 
          output_file = open('baudotU32.txt','w+',encoding="utf-32") 
          output_file.write(output_text)
          output_file.close()
          print("File created: baudotU32.txt")
          cont = input("Do you want to continue? Y/N\n")
          if (cont == 'Y'):
               menu()
          else:
               sys.exit(0)
     elif (option == '10'):
          data = utf32_to_utf8()
          output_file = open('utf32_to_utf8.txt','w+', encoding = 'utf-8')
          output_file.write(data)
          output_file.close()
          print("File created: utf32_to_utf8.txt")
          cont = input("Do you want to continue? Y/N\n")
          if (cont == 'Y'):
               menu()
          else:
               sys.exit(0)
     elif(option == '11'):
          output_text = utf32_to_morse() 
          output_file = open('u32Morse.txt','w+') 
          output_file.write(output_text)
          output_file.close()
          print("File created: u32Morse.txt")
          cont = input("Do you want to continue? Y/N\n")
          if (cont == 'Y'):
               menu()
          else:
               sys.exit(0)
     elif (option == '12'):
          output_text = utf32_to_baudot() 
          output_file = open('u32Baudot.txt','w+') 
          output_file.write(output_text)
          output_file.close()
          print("File created: u32Baudot.txt")
          cont = input("Do you want to continue? Y/N\n")
          if (cont == 'Y'):
               menu()
          else:
               sys.exit(0)
     elif (option == '13'):
          sys.exit(0)
     else:
          print("Please enter the number from 1 - 13")
          menu()
menu()