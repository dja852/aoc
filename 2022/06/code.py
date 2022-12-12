def main():
    with open("input.txt", "r") as f:
        file_string = f.read()
    
    print(get_set_index(file_string, 4))
    print(get_set_index(file_string, 14))
    
def get_set_index(signal_string: str, num_of_chars: int = 4) -> int:
    signal_list = [x for x in signal_string]

    for x in range(0, len(signal_list)):
        signal_set = set(signal_list[x:min(x + num_of_chars, len(signal_list))])
        if len(signal_set) == num_of_chars:
            return x + num_of_chars
    
    return 0

if __name__ == "__main__":
    main()