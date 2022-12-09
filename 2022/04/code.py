import re

ELF_REGEX = r"^(\d+)-(\d+),(\d+)-(\d+)"

def find_total_overlaps_sets(pairing: str, part: int = 1) -> bool:
    result = re.search(ELF_REGEX, pairing)
    pair1 = {x for x in range(int(result.group(1)), int(result.group(2)) + 1)}
    pair2 = {x for x in range(int(result.group(3)), int(result.group(4)) + 1)}
    intersection_set = pair1.intersection(pair2)

    if part == 1:
        return pair1.issubset(intersection_set) or pair2.issubset(intersection_set)
    else:
        return not pair1.isdisjoint(pair2)

def main():
    totalOverlapsP1 = 0
    totalOverlapsP2 = 0

    with open("input.txt", "r") as f:
        fileLines = f.readlines()
        for x in fileLines:
            totalOverlapsP1 += 1 if find_total_overlaps_sets(x.strip()) else 0
            totalOverlapsP2 += 1 if find_total_overlaps_sets(x.strip(), 2) else 0

    print(totalOverlapsP1)
    print(totalOverlapsP2)

if __name__ == "__main__":
    main()