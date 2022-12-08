
TOTAL_SIZE = 70000000
FREE_NEEDED = 30000000


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __str__(self):
        return "{}".format(self.name)


class Folder:
    def __init__(self, name: str, parent=None):
        self.name = name
        self.parent = parent
        self.files = []
        self.folders = []

    def __str__(self):
        return str(self.name)

    def add_file(self, file: File):
        self.files.append(file)

    def add_folder(self, folder):
        self.folders.append(folder)

    def get_folder(self, name):
        for folder in self.folders:
            if folder.name == name:
                return folder
        return None

    def get_size(self):
        max_size = 0
        for file in self.files:
            max_size += file.size
        for folder in self.folders:
            max_size += folder.get_size()
        return max_size

    def contains_file(self, file_name: str):
        if file_name in self.files:
            return 1
        return 0


def main():
    input_file = open(FILE_PATH, "r")
    data = input_file.readlines()
    print("Size to delete: {}".format(get_total_size(data)))


def get_total_size(data):
    tree = None
    current_folder = None
    for index, aux in enumerate(data):
        line = aux.split(' ')
        if line[0] == '$' and line[1] == "cd":
            tree, current_folder = execute_cd(line[2].strip('\n'), tree, current_folder)
        elif line[0] == '$' and line[1].strip('\n') == "ls":
            execute_ls(data, index, current_folder)
    free_space = TOTAL_SIZE - tree.get_size()
    print("Current free space: ", free_space)
    print("Required: ", FREE_NEEDED - free_space)
    return calc_size(tree, FREE_NEEDED - free_space, 697596299)


def execute_cd(command, tree: Folder, current_folder: Folder):
    if command == '..' and current_folder is not None:
        print("Moving back to ", current_folder.parent.name)
        current_folder = current_folder.parent
    elif current_folder is None or not current_folder.get_folder(command):
        new_folder = Folder(command)
        if tree is None:
            tree = new_folder
            print("Creating root folder ", command)
        elif current_folder:
            new_folder.parent = current_folder
            print("Creating new folder '{}' inside '{}'".format(new_folder.name, current_folder.name))
            current_folder.add_folder(new_folder)
        current_folder = new_folder
    else:
        if not current_folder:
            return
        current_folder = current_folder.get_folder(command)
    return tree, current_folder


def execute_ls(data, index, current_folder: Folder):
    i = 1
    while i + index <= len(data) - 1 and data[i + index][0] != '$':
        line = data[i + index].split(' ')
        if line[0] != "dir" and not current_folder.contains_file(line[0]):
            print("Creating new file '{}' with size {}".format(line[1].strip('\n'), line[0]))
            current_folder.add_file(File(line[1].strip('\n'), int(line[0])))
        i += 1


def calc_size(folder: Folder, free_required, to_delete=None):
    size = folder.get_size()
    if to_delete is None or (size >= free_required and size < to_delete):
        to_delete = size
    for subfolder in folder.folders:
        to_delete = calc_size(subfolder, free_required, to_delete)
    return to_delete


# def calc_size(folder: Folder, free_available, to_delete=None):
#     for subfolder in folder.folders:
#         aux = subfolder.get_size()
#         print("aux ", aux)
#         if to_delete is None or ((free_available + to_delete < free_available + aux)
#                                  and free_available + aux >= FREE_NEEDED):
#             to_delete = aux
#         calc_size(subfolder, free_available, to_delete)
#     #print(to_delete)
#     return to_delete


if __name__ == "__main__":
    main()
