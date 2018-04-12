# use of list comprehension

nums=[1,2,3,4,5]
print(nums)
squares=[n*n for n in nums]
print(squares)

strs = ['aaa','BBB','SvRR']
print(strs)
upperStrs = [s.upper() for s in strs]
print(upperStrs)
