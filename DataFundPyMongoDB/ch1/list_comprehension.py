if __name__ == "__main__":
    miles = [100, 10, 9.5, 1000, 30]
    kilometers = [x * 1.60934 for x in miles]

    print("miles to kilometers:")
    for i, row in enumerate(kilometers):
        print(f"{miles[i]:>4} miles is {round(row, 2):>8} km")

    print("\npet:")
    pet = ["cat", "dog", "rabbit", "parrot", "guinea pig", "fish"]
    print(pet)

    print("\npets:")
    # Add plural if pet is not a fish
    pets = [x + "s" if x != "fish" else x for x in pet]
    print(pets)

    print("\nmost common pets:")
    # Hard coded to say dogs and cats are the most common, not data driven
    subset = [
        x
        for x in pets
        if x != "fish" and x != "rabbits" and x != "parrots" and x != "guinea pigs"
    ]
    print(subset[1], "and", subset[0])

    print("\nbonuses:")
    sales = [9000, 20000, 50000, 100000]
    bonus = [
        0 if x < 10000 else x * 0.02 if x >= 10000 and x <= 20000 else x * 0.03
        for x in sales
    ]
    print(bonus)

    print("\nbonus dict:")
    people = ["dave", "sue", "al", "sukki"]
    d = {}
    for i, row in enumerate(people):
        d[row] = bonus[i]
    print(d, "\n")

    print("Bonus Table:")
    headers = ("EMPLOYEE", "BONUS")
    print(f"{headers[0]:<8} {headers[1]:<5}")
    for k, y in d.items():
        print(f"{k:<8} {y:>6}")

# OUTPUT
"""
miles to kilometers:
 100 miles is  160.93 km
  10 miles is   16.09 km
 9.5 miles is   15.29 km
1000 miles is 1609.34 km
  30 miles is   48.28 km

pet:
['cat', 'dog', 'rabbit', 'parrot', 'guinea pig', 'fish']

pets:
['cats', 'dogs', 'rabbits', 'parrots', 'guinea pigs', 'fish']

most common pets:
dogs and cats

bonuses:
[0, 400.0, 1500.0, 3000.0]

bonus dict:
{'dave': 0, 'sue': 400.0, 'al': 1500.0, 'sukki': 3000.0} 

emp   bonus
dave       0
sue    400.0
al    1500.0
sukki 3000.0
"""
