#List Less Then Ten
#01-03-2018
#
#Take a list of numbers and print a message with all the elements less than five
#
#Extras: instead of printing elements less than five, make a new list that has all elements less than five
#                   and print the new list
#            write that in one line of Python
#            Ask user for a  number, return all elements from original list that are smaller than that number

##Preset list for debugging, coment out user-created-list-block
##a = [10, 6, 15, 64, 88, 32, 22, 8, 9, 44, 7, 3, 5, 1, 3, 15, 64]

a = []
looping = 'true'
while looping == 'true':
    apnd = input("Give me an integer, or enter 'N/n' to complete list:  ")
    if (len(a) < 2  and (apnd == "" or (apnd == "N" or apnd == "n"))):
        print("You must add at least two integers to the list. Please try again.")
    elif apnd == "N" or apnd == "n":
        looping = 'false'
    elif apnd == "":
        print("Oops, try again. Don't enter a blank line.")
    else:
        a.append(int(apnd))
print (a)

#Check for duplicates, add them to a new list (use "set(your_list)" to remove all duplicates from list.)
a = list(set(a))

#Remove elements larger than 10
#Using while instead of for loop because for loop has restricted control on index iterable
i = 0
userThreshold = int(input("Give me another integer. I will remove all elements in your list greater than the given number:  "))
while i < len(a):
    if int(a[i]) > userThreshold:
        a.remove(a[i])
        i -= 1
    i += 1
    print(str(i))


#My own extra: reorder elements in ascending value AFTER LIST HAS BEEN PRUNED OF LARGER VALUES FOR EFFICIENCY
#create a for loop that iterates through each element, comparing it to first element in the list
for i in range(len(a)):
    print("Outer loop: INDEX = " + str(i) + " ||| ELEM = " + str(a[i]))
    for j in range(len(a)):
        if int(a[j]) > int(a[i]): #if second element is larger than first element switch location
            print (str(a[j]) + " is greater than " + str(a[i]))
            print(a)
            a[i], a[j] = a[j], a[i] #switching location here
            print(a)
        






