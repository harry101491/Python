stock_price_yesterday = [10,7,5,8,11,9]
def get_max_profit(stock_price_yesterday):
	"This will get the maximum profit from the array"
	max = 0
	for i in xrange(0,4):
		for j in xrange(i+1,5):
			if((stock_price_yesterday[j]-stock_price_yesterday[i]) > max):
				max = stock_price_yesterday[j]-stock_price_yesterday[i]
	return max

print "The profit returned is: %d" % (get_max_profit(stock_price_yesterday))