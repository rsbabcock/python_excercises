# STOCK dictionary of ticker symbols and company names
stockDict = { 'GM': 'General Motors', 'CAT':'Caterpillar', 'EK':"Eastman Kodak" }
# list of tuples
purchases = [ ( 'GM', 100, '10-sep-2001', 48 ), ( 'CAT', 100, '1-apr-1999', 24 ), ( 'GM', 200, '1-jul-1998', 56 ) ]
# function syntax
def purchase_history():
    for purchase in purchases:
      for x in stockDict:
        if purchase[0] == x:
            print(f'{stockDict[purchase[0]]} + {purchase[1] * purchase[3]}')
        
purchase_history()

# Create a second purchase summary that which accumulates total 
# investment by ticker symbol. In the above sample data, there are two blocks of GE. 
# These can easily be combined by creating a dict where the key is the ticker and the 
# value is the list of blocks purchased. The program makes one pass through the data to
# create the dict. A pass through the dict can then create a report showing each ticker 
# symbol and all blocks of stock.

# from levi shubert
def report_by_ticker(list=purchases, stocks=stockDict):
	# make an empty dict
	tickers = {}
	# stock is a variable name, like x, etc
	for stock in list:
		name = stocks[stock[0]]
		value = stock[1]
		if name in tickers.keys():
			value += tickers[name]
			print(value)
		tickers.update({name: value})
	return tickers

 report_by_ticker() 