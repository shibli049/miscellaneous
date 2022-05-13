"""
# History & Problem statement
The Monty Hall problem is a brain teaser, in the form of a probability puzzle, loosely based on the American television game show, 
"Let's Make a Deal" and named after its original host, Monty Hall. 

The problem was originally posed (and solved) in a letter by Steve Selvin to the American Statistician in 1975.
It became famous as a question from reader Craig F. Whitaker's letter quoted in Marilyn vos Savant's "Ask Marilyn" column in Parade magazine in 1990.

`Suppose you're on a game show, and you're given the choice of three doors: 
  Behind one door is a car; behind the others, goats. 
  You pick a door, say No. 1, and 
  the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat.
  He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?`

source: https://en.wikipedia.org/wiki/Monty_Hall_problem
"""

# ---------------- helpers ----------------

import random
# creates a random number between 0 and n
def rand_range(n):
    return random.randrange(n)

# choose an item randomly from the list
def rand_item(lst):
    return random.choice(lst)

def put_the_prize_behind_door(door_num):
    # initialize the doors
    doors = [0] * door_num
    # choose a random door to put the prize behind the door
    choosen = rand_range(door_num)
    # prize is set
    doors[choosen] = 1
    return doors,choosen


def show_door(door_num, choosen, player_choice):
    # remove the door player choose, and the door behind which the prize is
    choice = [ele for ele in range(door_num) if ele not in [choosen, player_choice]]
    return rand_item(choice)
  
def switch_to_new_door(doors, player_choice, shown):
    # remove the shown door and player choice and choose the 3rd door
    return [doors[ind] for ind, elem in enumerate(doors) if ind not in [shown, player_choice]]
  
def generate_stat(switch_door, success_count, total):
    return f"Switch door: {switch_door}, Total: {total}, Success: {success_count}, percent: {((1.0 * success_count)/total) * 100}"
  
# ---------------- the game ----------------
# player choose a door, and switch based on flag
def play_the_game(switch_door = False):
    # number of doors
    door_num = 3
    doors, choosen = put_the_prize_behind_door(door_num)
    # player choose a random door
    player_choice = rand_range(door_num)
    if switch_door:
        # host show a door, behind which there is a goat
        shown = show_door(door_num, choosen, player_choice)
        final_choice = switch_to_new_door(doors, player_choice, shown)
        return len(final_choice) == 1 and final_choice[0] == 1
    else:
        # no matter which door the presenter shows, player's decision is final
        return doors[player_choice] == 1
  

# ---------------- tests ----------------
def simulate(N = 10001, switch_door = False):
    success_count = 0
    for i in range(N):
        if play_the_game(switch_door):
            success_count += 1
    return generate_stat(switch_door, success_count, N)



if __name__ == "__main__":
    n = 9999_99 # the bigger the size, the better the result
    
    switch_rates = simulate(n, True)
    print(switch_rates)
    
    other_rates = simulate(n, False)
    print(other_rates)
