from collections import deque
import copy

def main():
    with open("input.txt", "r") as f:
        box_stacks, move_instructions = (x.splitlines() for x in f.read().strip("\n").split("\n\n"))

    stacks = setupStacks(box_stacks)

    stacksP1 = crateMover9000(copy.deepcopy(stacks), move_instructions)
    stacksP2 = crateMover9001(copy.deepcopy(stacks), move_instructions)

    part1, part2 = "", ""

    for x in range(1, max(stacks) + 1):
        part1 += str(stacksP1[x][-1])
        part2 += str(stacksP2[x][-1])
    
    print(part1, part2)

def setupStacks(box_stacks: list) -> dict:
    stacks = {int(x) : deque([]) for x in box_stacks[-1].strip().split()}
    for x in sorted(box_stacks[:-1], reverse=True):
        for i, y in enumerate(x):
            if y.isupper():
                stacks[(i // 4) + 1].append(y)
    return stacks

def crateMover9000(stacks: dict, move_instructions: list) -> dict:
    for x in move_instructions:
        _, qty, _, src, _, dst = x.split()
        for _ in range(1, int(qty) + 1):
            stacks[int(dst)].append(stacks[int(src)].pop())
    
    return stacks

def crateMover9001(stacks: dict, move_instructions: list) -> dict:
    for x in move_instructions:
        _, qty, _, src, _, dst = x.split()
        tempStack = deque([])
        for _ in range(1, int(qty) + 1):
            tempStack.append(stacks[int(src)].pop())
        tempStack.reverse()
        stacks[int(dst)] += tempStack
        
    return stacks

if __name__ == "__main__":
    main()