#####  Store your, name, email, student_id and class_number as STRINGS #####
#exercise = "strings"
#name = jaden quak
#np_email = s10225042@connect.np.edu.sg
#student_id = S10225042C
#class_number = TC08

# ---------- Write a program to allow a user to enter some text ----------#

# The program will:
    # 1. Convert any uppercase strings to lowercase strings.
    # 2. After step 1, it will replace lowercase character of z, b, t, g, h with 1, 2, 3, 4, 5 respectively.

entertext = input("Enter What you want: ") 
entertextlower = entertext.lower()

print(entertextlower)


entertextlower = entertextlower.replace('z', '1')
entertextlower = entertextlower.replace('b', '2')
entertextlower = entertextlower.replace('t', '3')
entertextlower = entertextlower.replace('g', '4')
entertextlower = entertextlower.replace('h', '5')

print(entertextlower) 






# When your program file is executed, it will look like this:

    # Enter some text in uppercase: I LOVE SINGAPORE ZOO BEST
    # Converted your text to lower case: i love singapore zoo best
    # Replaced any character of z, b, t, g, h with 1, 2, 3, 4, 5: i love sin4apore 1oo 2es3

# You should assign a variable and named it as `text` to store the user input.

# Note:
# `I LOVE SINGAPORE ZOO BEST` is the user input text.
# `i love singapore zoo best` and `i love sin4apore 1oo 2es3` are the output of the program
