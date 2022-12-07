from enum import Enum

class RPSPlay(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class WinLoseDraw(Enum):
    WIN = 6
    LOSE = 0
    DRAW = 3

PLAY_MAP = {
    "A": RPSPlay.ROCK,
    "B": RPSPlay.PAPER,
    "C": RPSPlay.SCISSORS,
    "X": RPSPlay.ROCK,
    "Y": RPSPlay.PAPER,
    "Z": RPSPlay.SCISSORS
}

WIN_MAP = {
    RPSPlay.ROCK: (RPSPlay.SCISSORS, "C", "B"),
    RPSPlay.PAPER: (RPSPlay.ROCK, "A", "C"),
    RPSPlay.SCISSORS: (RPSPlay.PAPER, "B", "A")
}

def main():
    totalScoreP1: int = 0
    totalScoreP2: int = 0
    with open("input.txt", "r") as f:
        for x in f:
            fileLine = str(x.strip("\n")).split(" ")
            totalScoreP1 += calc_strategy_guide(fileLine[0], fileLine[1])
            totalScoreP2 += calc_strategy_guide(fileLine[0], (lambda elf_play, your_play: elf_play if your_play == "Y" else (WIN_MAP[PLAY_MAP[elf_play]][2] if your_play == "Z" else WIN_MAP[PLAY_MAP[elf_play]][1]))(fileLine[0], fileLine[1]))
    print("Part 1: " + str(totalScoreP1))
    print("Part 2: " + str(totalScoreP2))

def calc_strategy_guide(elf_play: str, your_play: str) -> int:
    if PLAY_MAP[elf_play] == PLAY_MAP[your_play]:
        return WinLoseDraw.DRAW.value + PLAY_MAP[your_play].value
    elif WIN_MAP[PLAY_MAP[your_play]][0] == PLAY_MAP[elf_play]:
        return WinLoseDraw.WIN.value + PLAY_MAP[your_play].value
    else:
        return WinLoseDraw.LOSE.value + PLAY_MAP[your_play].value

if __name__ == "__main__":
    main()