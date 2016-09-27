#Chapter 2
# Find teh minimum number

#finding minimum number in the list
#Method 1:
#Linear method

smallest=iList[0]
len(iList)
for i in range(1, len(iList)):
    if smallest > iList[i] :
        print (smallest, iList[i])
        smallest = iList[i]
        
print (smallest)

#Method 2:
#Compare each number to every other number on the list O(n2)

user_input = input("Enter a list of numbers separated by commas")
iList = user_input.split(",")

minimum = iList[0]
for i in range (0, len(iList)):
    issmallest= True
    for j in range(0,len(iList)):
        print (iList[i],iList[j])
        if iList[i] > iList[j]:
            
            issmallest = False
    if issmallest:
        minimum = iList[i]
        print ("smallest number is:", minimum)
