
def get_max_profit_yesterday(prices):
    if len(prices) <= 1:
        return 0

    minimum_price = prices[0]
    max_profit = 0 # profit can't be negative

    for current_price in prices:
        minimum_price = min(current_price, minimum_price)
        current_profit = current_price - minimum_price
        max_profit = max(max_profit, current_profit)

    return max_profit


def test_run(input_arr):
    print "\n====Running Test====\n"
    print "Input list of prices : {0}".format(input_arr)
    print "Max profit that can be earned : {0}".format(get_max_profit_yesterday(input_arr))
    print "\n====Test Complete=====\n"


stock_prices_yesterday_samples = [
            [10, 7, 5, 8, 11, 9],
            [9,8,7,6,5,4,3,1],
            [1,2,3,4,5,6],
            [10,7,100],
            [100,38,7,1,1000],
            [1],
            []
        ]

for stock_prices in stock_prices_yesterday_samples:
    test_run(stock_prices)
