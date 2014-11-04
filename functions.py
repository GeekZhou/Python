__author__ = 'zhengzhou'

def computepay(h,r):
    if h<=40:
        return h*10.5
    else:
    	return (40*10.5+(h-40)*10.5*r);

#hrs = raw_input("Enter Hours:")
p = computepay(float(12),1.5)

print(p)
