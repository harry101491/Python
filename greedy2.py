arr = [2,7,3,4]
# the array that we have to find the multiplication of the values
# before each index like for index = 1 the product is 2.
arr_product_before = [None]*len(arr)
arr_product_before[0] = 1
for i in xrange(1,len(arr)):
	arr_product_before[i] = arr_product_before[i-1]*arr[i-1]

#finding the product backwards 
arr_product_after = [None]*len(arr)
product_so_far = 1
i = len(arr) - 1
while i >= 0:
	#arr_product_after[i] = product_so_far
	product_so_far *= arr[i]
	arr_product_before[i] = arr_product_before[i]*product_so_far
	i -= 1
#print "The array of product after each index is:"
#for i in xrange(len(arr_product_after)):
#	print "%d" %(arr_product_after[i])
# now changing the arr into the arr of product of each index except the 
# current index
for i in xrange(len(arr_product_before)):
	#arr[i] = arr_product_before[i]*arr_product_after[i]
	print arr_product_before[i]
