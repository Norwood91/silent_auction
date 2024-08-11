users = []

def silent_auction(list):
    highest_bid = 0

    for user in list:
        index = list.index(user)
        bid = list[index]['bid']
        if bid > highest_bid:
            highest_bid = bid
            user_name = list[index]['username']
            location = list[index]['location']

    print(f"The highest bid goes to {user_name}, from {location}! With a bid of ${highest_bid}!")


def run_program():
    running = True
    while running:

        user_name = input("What is your name?:\n").title()
        print(f"Welcome, {user_name}, to the Silent Auction!")
        location = input("What city do you currently live in?:\n").title()
        user_bid = int(input("How much would you like to bid today?: $"))
        other_users = input("Are there more people, beside you, bidding today? Type 'yes' if so, or 'no' if it's just "
                            "you:\n").lower()
        user_dict = {'username': user_name, 'location': location, 'bid': user_bid}
        users.append(user_dict)

        if other_users == 'no':
            running = False
            silent_auction(users)


if __name__ == "__main__":
    run_program()
