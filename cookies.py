# The program takes 2 user inputs:
#     1. start → the amount of money we had before selling cookies
#     2. String of b or c
#         num_cookies → a string of character ‘c’s to denote the number of cookies sold
#             Example: cccccc → 6 cookies!
#         num_big → a string of character ‘b’s to denote the number of big cookies sold
#             Example: bbb → 3 big cookies!

# The program should output:
#     1. Number of total cookies sold
#     2. Profit (which is calculated as profit = sales - cost of cookie)
#         Cost of Normal Cookie per cookie → $1.25
#         Cost of Big cookie per cookie → $2.00
#         To make a normal cookie → $0.50
#         To make a big cookie → $0.75
#     3. Total amount of money after selling cookies

#inputs
money_before = float(input("The amount of money we had before selling cookies: ")) #float allows for real numbers (decimals)
cookies_sold = input("Numbers of cookies sold: ")

# num_cookies = input("Numbers of normal cookies sold: ") *my version*
# num_big = input("Numbers of big cookies sold: ") *my version*

#processing
big_cookies = cookies_sold.count("b")
cookies = cookies_sold.count("c")

# total_cookies = len(num_cookies) + len(num_big) *my version*

# cost_of_cookie = 0.5*len(num_cookies) + 0.75*len(num_big) *my version*
# sales = 1.25*len(num_cookies) + 2*len(num_big) *my version*
# profit = sales - cost_of_cookie *my version*

total_cookies = cookies + big_cookies

cost_of_cookie = 0.5*cookies + 0.75*big_cookies
sales = 1.25*cookies + 2*big_cookies 
profit = sales - cost_of_cookie 

total_amount = profit + money_before

#outputs
print(f"Numbers of total cookies sold is {total_cookies}. Profit made is ${profit}. Total amount of money after selling cookies is ${total_amount}.")
