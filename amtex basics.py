#list
#list can change and it is a order indexed
#allow dublicates
#[]
"""x=["math","science","comp","physics"]
#print("math" in x)
for index,item in enumerate(x):
    print(index,item)
    if(item=="science"):
        print(x,"i am here")
    else:
        print(x,"i am not there")"""

#list joining
"""x=["math","science","comp","physics"]
z=" - ".join(x)
print(z)"""

#tuples
#tuples can't change and it is a order indexed
#allows dublicate
#()
"""x=(2,3,4,5,6,7)
print(x)
#here we cant add the value in tuple and we converting to list and we are adding it
z=list(x)
m=z.append(22)
print(z)
"""
#sets
#unordered,unchangeable,
#not allow dublicate,unidexed
#{}
#it is used mathemetical expression
x={12,34,"hello","89","89"}
y={12,879,78,"hello",45}
print(x.intersection(y)) #here we are using mathemetiacla interaction
print(x.union(y)) # to merge the both we are using
print(x)
