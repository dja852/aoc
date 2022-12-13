class FileDirectory:
    
    def __init__(self, name: str, parent = None, is_dir: bool = False, size: int = 0, children: list = []) -> None:
        self.name = name
        self.parent = parent
        self.is_dir = is_dir
        self.size = size
        self.children = children

    def __str__(self):
        return self.name + " " + str(self.size) + " " + str(self.is_dir)

    def print_tree(self, level = 0):
        print("{} {} {} {}".format(level, self.name, self.size, self.is_dir))  
        if self.children:
            for child_dir in self.children:
                child_dir.print_tree(level + 1)

    def update_sizes(self, size = 0):
        if self.children is None:
            return self.size
        
        else:
            total_sizes = sum(
                [child_file.update_sizes(size) for child_file in self.children]
            )
            self.size += total_sizes
            
            return self.size
    
    def sum_dir_max_size(self, maxSize):
        runningSum = 0
        if self.is_dir and self.size <= maxSize:
            runningSum += self.size
        
        if self.children:
            for child_dir in self.children:
                runningSum += child_dir.sum_dir_max_size(maxSize)
        
        return runningSum

    def find_min_del_size(self, diskSpace, updateSpace, neededSpace = 0):
        dirSizeList = []
        if self.is_dir and self.parent is None:
            neededSpace = updateSpace - (diskSpace - self.size)
        
        if self.is_dir and self.size >= neededSpace:
            dirSizeList.append(self.size)
        
        if self.children:
            for child_dir in self.children:
                dirSizeList += child_dir.find_min_del_size(diskSpace, updateSpace, neededSpace)
        
        return [min(dirSizeList)] if len(dirSizeList) > 0 else dirSizeList

def process_input(fileName: str):
    
    root_dir = None 
    curr_dir = None
    next_dir = None

    with open(fileName, "r") as f:
        terminalInput = f.read().strip().splitlines()
    
    for command in terminalInput:
        
        match command.split(" "):

            case "$", "cd", file_dir:
                
                match file_dir:

                    case "/":

                        root_dir = FileDirectory(file_dir, None, True)
                        curr_dir = root_dir

                    case "..":

                        curr_dir = curr_dir.parent

                    case _:
                        
                        next_dir = [child_dir for child_dir in curr_dir.children if child_dir.name == file_dir]
                        curr_dir = next_dir[0]
            
            case "$", "ls":
                continue
            
            case "dir", file_dir:
                curr_dir.children.append(FileDirectory(file_dir, curr_dir, True, 0, []))

            case file_size, file_dir:
                curr_dir.children.append(FileDirectory(file_dir, curr_dir, False, int(file_size), None))
            
            case _:
                continue

    root_dir.update_sizes()

    return root_dir

def main():
    root_dir = process_input("input.txt")
    print(root_dir.sum_dir_max_size(100000))
    print(root_dir.find_min_del_size(70000000, 30000000))

if __name__ == "__main__":
    main()