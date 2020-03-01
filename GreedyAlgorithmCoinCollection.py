def optimal_small_change(denom, total_amount):
    sorted_denominations = sorted(denom, reverse=True)

    series = []
    for j in range(len(sorted_denominations)):
        term = sorted_denominations[j:]

        number_of_denoms = []
        local_total = total_amount
        for i in term:
            div = local_total // i
            local_total = local_total % i
            if div > 0:
                number_of_denoms.append((i, div))

        series.append(number_of_denoms)

    return series

print(optimal_small_change([1,5,8],14))

'''Coin-counting problem
Let's examine a very simple use of this greedy technique. In some arbitrary country, 
we have the denominations 1 GHC, 5 GHC, and 8 GHC. Given an amount such as 12 GHC, 
we may want to find the least possible number of denominations needed to provide change. 
Using the greedy approach, we pick the largest value from our denomination to divide 12 GHC. 
We use 8 because it yields the best possible means by which we can reduce the amount 12 GHC into lower denominations.

The remainder, 4 GHC, cannot be divided by 5, so we try the 1 GHC denomination and realize that we can multiply it by 4 to obtain 4 GHC. 
At the end of the day, the least possible number of denominations to create 12 GHC is to get a one 8 GHC and four 1 GHC notes.

So far, our greedy algorithm seems to be doing pretty well. A function that returns the respective denominations is as follows:

    def basic_small_change(denom, total_amount): 
        sorted_denominations = sorted(denom, reverse=True) 

        number_of_denoms = [] 

        for i in sorted_denominations: 
            div = total_amount / i 
            total_amount = total_amount % i 
            if div > 0: 
                number_of_denoms.append((i, div)) 

        return number_of_denoms 
This greedy algorithm always starts by using the largest denomination possible. 
denom is a list of denominations. sorted(denom, reverse=True) will sort the list in reverse so that we can obtain the largest denomination at index 0.
 Now, starting from index 0 of the sorted list of denominations, sorted_denominations, we iterate and apply the greedy technique:

    for i in sorted_denominations: 
        div = total_amount / i 
        total_amount = total_amount % i 
        if div > 0: 
            number_of_denoms.append((i, div)) 
The loop will run through the list of denominations. Each time the loop runs, it obtains the quotient, div, by dividing the total_amount by the current denomination, i. total_amount is updated to store the remainder for further processing. If the quotient is greater than 0, we store it in number_of_denoms.

Unfortunately, there are instances where our algorithm fails. For instance, when passed 14 GHS, our algorithm returns one 8 GHC and four 1 GHS. This output is, however, not the optimal solution. The right solution will be to use two 5 GHC and two 1 GHC denominations.

A better greedy algorithm is presented here. This time, the function returns a list of tuples that allow us to investigate the better results:

    def optimal_small_change(denom, total_amount): 

        sorted_denominations = sorted(denom, reverse=True) 

        series = [] 
        for j in range(len(sorted_denominations)): 
            term = sorted_denominations[j:] 

            number_of_denoms = [] 
            local_total = total_amount 
            for i in term: 
                div = local_total / i 
                local_total = local_total % i 
                if div > 0: 
                    number_of_denoms.append((i, div)) 

            series.append(number_of_denoms) 

        return series 
The outer for loop enables us to limit the denominations from which we find our solution:

    for j in range(len(sorted_denominations)): 
        term = sorted_denominations[j:] 
        ...     
Assuming that we have the list [5, 4, 3] in sorted_denominations, slicing it with [j:] helps us obtain the sublists [5, 4, 3], [4, 3], and [3], from which we try to get the right combination to create the change.'''