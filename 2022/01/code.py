def main():
    with open("input.txt", "r") as f:
        elfCalories = [sum(elfCalories) for elfCalories in [list(map(int, x)) for x in [z.splitlines() for z in f.read().split("\n\n")]]]
        elfCalories.sort(reverse=True)

        print("Part 1: " + str(max(elfCalories)))
        print("Part 2: " + str(sum(elfCalories[0:3])))

if __name__ == "__main__":
    main()