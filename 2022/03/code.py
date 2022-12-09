def get_compartments(rucksack: str):
    c1 = list(set([*rucksack[:len([*rucksack]) // 2]]))
    c2 = list(set([*rucksack[len([*rucksack]) // 2:]]))
    return c1, c2

def get_badge(r1: str, r2: str, r3: str):
    sr1 = set([*r1])
    sr2 = set([*r2])
    sr3 = set([*r3])

    i1 = sr1.intersection(sr2)
    i2 = i1.intersection(sr3)

    return list(i2)[0]

def main():
    priorities = {**{chr(x + 96):x for x in range(1, 27)}, **{chr(x + 64):x + 26 for x in range(1, 27)}}
    totalPrioritiesP1: int = 0
    totalPrioritiesP2: int = 0

    with open("input.txt", "r") as f:
        fileLines = f.readlines()
        for x in fileLines:
            c1, c2 = get_compartments(x.strip())
            for a in c1:
                totalPrioritiesP1 += priorities[a] if a in c2 else 0
        
        for x in range(0, len(fileLines), 3):
            badge = get_badge(fileLines[x].strip(), fileLines[x + 1].strip(), fileLines[x + 2].strip())
            totalPrioritiesP2 += priorities[badge]
    
    print("Part 1: " + str(totalPrioritiesP1))
    print("Part 2: " + str(totalPrioritiesP2))

if __name__ == "__main__":
    main()