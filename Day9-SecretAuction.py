print( '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')

#from replit import clear
#setup
bid_list={}
add_more='yes'

#Find highest bidder
def find_highest(lst):
    max_price=0
    for name in lst:
        if lst[name]>max_price:
            max_price=lst[name]
            max_bidder=name
    print(f"The winner is {max_bidder} with a bid of ${max_price}.")

while add_more=='yes':
    name=input("What is your name? ")
    price=int(input("What is your bid? $"))
    bid_list[name]=price
    add_more=input("Are there any other bidders? Type 'yes' or 'no'.")

    if add_more=='no':
        find_highest(bid_list)
