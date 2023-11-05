# Auction program

print("Welcome to the secret auction program.")
auction = {"bidders": [], "bidding": []}
bid_continue = True

while bid_continue:
    people = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    auction["bidders"].append(people)
    auction["bidding"].append(bid)
    loop = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if loop == 'no':
        bid_continue = False

max_bid = 0
for value in auction["bidding"]:
    if value > max_bid:
        max_bid = value

position = auction["bidding"].index(max_bid)
highest_bidder = auction["bidders"][position]
print(f"The highest bidder is {highest_bidder}")