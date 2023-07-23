# basic version
# simple program that recommends shows based on input

import pandas as pd
import random
import requests

# store information of the show
shows = ['a', 'b']


def randomized_show():
    try:
        show = show = random.choice(shows)
    except:
        print("Ran out of shows :(")
        return False
    print("randomized show: " + show)
    print("\nAre you satisifed with the show? Y/N")
    shows.remove(show)
    res = input().capitalize()
    while res != 'Y' and res != 'N':
        print("Please input Y/N")
        res = input().capitalize()
    if res == "Y":
        return False
    return True


def ask_for_recommendation():
    run = True
    while run:
        print("Is there any shows you like to see?\n1. Surprise me\n2. End Program")
        res = int(input())
        if res == 1:
            run = randomized_show()
            print('\n')
        elif res == 2:
            run = False
    return


if __name__ == "__main__":
    # ask_for_recommendation()
    # url = "https://api.jikan.moe/v4/genres/anime"
    url = "https://api.jikan.moe/v4/anime?order_by=9"
    response = requests.get(url).json()
    print(response)
    # df = pd.DataFrame([[d['v'] for d in x['c']] for x in response['rows']],
    #                   columns=[d['label'] for d in response['cols']])
    # print(df)
