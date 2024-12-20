import random
# import my_module    #when you want different module to handle different part of the project... just create a file of the project and and do the task there if you want to use the task solution created in the new file in another module then you need to first import the file to the current file and then call it.
#
# rand_integer = random.randint(1, 12)   # to create random integer btw 1 and 12 with 1 and 12 inclusive the input 1, 12 is used to express the range you want the random number to take. However for float randomization, no need for inout there.
# print(rand_integer)
#
#
# print(my_module.my_favourite_number)
#
# # creating random number for floating number
#
# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)
#
#
# random_float = random.uniform(1, 12)
# print(random_float)

coin_flip = random.choice(['Heads', 'Tails'])
print(coin_flip)

#OR

coin_flip = random.randint(0, 1)
if coin_flip == 0:
    print("Heads")
else:
    print("Tails")