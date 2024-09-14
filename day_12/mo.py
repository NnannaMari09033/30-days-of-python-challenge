#Exercise 1
#Generating hexadecimal colours
import random

def generate_hex_colours(n=10):
   hex_colours = []
   for i in range(n):
      hex_colour = "#" + ''.join([hex(i)[2:].zfill(2) for i in [random.randint(0, 15) for _ in range(3)]])
      hex_colours.append(hex_colour)
   return hex_colours
def generate_hex_colours():
   hex_colours = []
   for i in range(10):
      hex_colour = "#" + ''.join([hex(i)[2:].zfill(2) for i in [random.randint(0, 15) for _ in range(3)]])
      hex_colours.append(hex_colour)
   return hex_colours

print(generate_hex_colours()) #hexadecimal values takes zero positional arguments

# #list of rgb colors
# def hex_to_rgb(hex_colour):
#    hex_colour = hex_colour.lstrip('#')
#    return tuple(int(hex_colour[i:i+2], 16) for i in (0, 2, 4))

# def generate_rgb_colours(hex_colours):
#    rgb_colours = []
#    for hex_colour in hex_colours:
#       rgb_colours.append(hex_to_rgb(hex_colour))
#    return rgb_colours

# print(generate_rgb_colours('hex_colours'))

#functions to generate rgb_colours and hexadecimal values
def hex_to_rgb(hex_colour):
   hex_colour = hex_colour.lstrip('#')
   return tuple(int(hex_colour[i:i+2], 16) for i in (0, 2, 4))

def generate_rgb_colours(hex_colours):
   rgb_colours = []
   for hex_colour in hex_colours:
      rgb_colours.append(hex_to_rgb(hex_colour))
   return rgb_colours
print ("rgb_colour")



#creating a function called shift list to return a list of parameters


def shift_list(lst, n):
   return lst[n:] + lst[:n]
print(shift_list)

#writing a function called return arrays of random numbers
import random

def generate_random_numbers(n=10, min_val=1, max_val=100):
   return [random.randint(min_val, max_val) for _ in range(n)]

print(generate_random_numbers())

#THANK YOU LORD!!!!!!!!