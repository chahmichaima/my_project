import random
def throw_dice() -> int:
    return random.randint(1, 6)
def throw_until_doubles() -> int:
    throws_count = 0
    while True:
        dice1 = throw_dice()
        dice2 = throw_dice()
        throws_count += 1
        if dice1 == dice2:
            break
    return throws_count
def main():
    results = []
    for _ in range(100):
        total_throws_for_double = throw_until_doubles()
        results.append(total_throws_for_double)
    total_throws = sum(results)
    print(f"Total throws: {total_throws}")
    average_throws = total_throws / len(results)
    print(f"Average throws to reach doubles: {round(average_throws, 2)}")
if __name__ == "__main__":
    main()