# use of sorted method for sorting elements of a list

strs = ['axa','byb','cdc','xyz']

def myFn(s):
    return s[-1] #this will creat proxy values for sorting algorithm

print(strs)
print(sorted(strs,key=myFn))
