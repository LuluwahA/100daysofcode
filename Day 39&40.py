#first challenge
def power(x,y):
	if(y==1):
	    return x
	else:
	    return x*power(x, y-1)
print(power(5,2))


#second challenge
x=[-4, -6, -5, -1, 2, 3, 7, 9, 88]
def pos(z):
    x1=list(filter(lambda y:(y>=0),z))
    return x1
print(pos(x))

