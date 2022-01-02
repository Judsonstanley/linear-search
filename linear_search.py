#linear search
def search(list,number,length):
	for i in range(0,length):
		if(list[i]==number):
			return i
	return -1               #false

#get a value from the user
list=[2,5,9,1,7]
number=int(input("enter a number to be searched"))
length=len(list)
result=search(list,number,length)


#condition
if(result==-1):
	print("Value not found")

else:
	print("the result is",result)