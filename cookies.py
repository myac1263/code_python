# Goal: for the program to output the total cookies sold

# input
start_money = float(input()) # float() helps to cast its argument to a real number
cookies_sold = input()

# processing
# big_cookies = 0 # this is an example of variable initialization
# cookies = 0 
big_cookies = cookies_sold.count('b')
cookies = cookies_sold.count ('c')

# for current_cookies in cookies_sold: 
#     #print(current_cookies) 
#     if current_cookies == "c":
#         #cookies = cookies + 1 slower written verion of below
#         cookies += 1 
#     elif current_cookies == "b": # this is an else if condition
#         big_cookies += 1
#     else: 
#         print(f"{current_cookies} is not a valid sale item.")
# end of for

total_cookies = big_cookies + cookies
profit = (big_cookies * 1.25) + (cookies * 0.75)
end_day = start_money + profit

print(f"We sold {total_cookies} cookies. We made ${profit}. We now have ${end_day}")
