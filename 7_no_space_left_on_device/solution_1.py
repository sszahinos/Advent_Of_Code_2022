FILE_PATH = "./test.txt"
MAX_SIZE = 100000


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __str__(self):
        return "{}".format(self.name)

class Folder:
    files = []
    folders = []

    def __init__(self, name: str, parent=None):
        self.name = name
        self.parent = parent

    def __str__(self):
        # tree = ""
        # tree += str(self.name) + "\n"
        # print(self.files)
        # for file in self.files:
        #     tree += "-f {}\n".format(file.name)
        # for folder in self.folders:
        #     tree += "-d {}\n".format(str(folder))
        #return tree
        return str(self.name)

    def add_file(self, file: File):
        self.files.append(file)

    def add_folder(self, folder):
        self.folders.append(Folder(folder))

    def get_folder(self, name):
        for folder in self.folders:
            if folder.name == name:
                return folder

    def get_file_size(self):
        max_size = 0
        for file in self.files:
            max_size += file.size
        return max_size

    def contains_file(self, file_name: str):
        if file_name in self.files:
            return 1
        return 0


def main():
    input_file = open(FILE_PATH, "r")
    data = input_file.readlines()
    print("Total sizes: {}".format(get_total_size(data)))


def get_total_size(data):
    tree = None
    current_folder = None
    for index, aux in enumerate(data):
        line = aux.split(' ')
        if line[0] == '$' and line[1] == "cd":
            tree, current_folder = execute_cd(line[2].strip('\n'), tree, current_folder)
        elif line[0] == '$' and line[1].strip('\n') == "ls":
            execute_ls(data, index, current_folder)
    return calc_size(tree)


def execute_cd(command, tree: Folder, current_folder: Folder):
    if command == '..' and current_folder is not None:
        current_folder = current_folder.parent
    elif not folder_exists(command, tree):
        print("Creating new folder: {}".format(command))
        new_folder = Folder(command)
        if tree is None:
            tree = new_folder
        else:
            new_folder.parent = current_folder
            tree.add_folder(new_folder)
        current_folder = new_folder
    else:
        if not current_folder:
            return
        current_folder = current_folder.get_folder(command)
    return tree, current_folder


def execute_ls(data, index, current_folder: Folder):
    i = 1
    while data[i + index][0] != '$' and i + index < len(data) - 1:
        line = data[i + index].split(' ')
        print(line)
        if line[0] != "dir" and not current_folder.contains_file(line[0]):
            print("Creating new file: {} with size: {}".format(line[1].strip('\n'), line[0]))
            current_folder.add_file(File(line[1].strip('\n'), int(line[0])))
        i += 1
    # hace falta devolver o la clase se actualiza?


def calc_size(folder: Folder):
    total_size = 0
    # print("entra")
    # for subfolder in folder.folders:
    #     total_size += calc_size(subfolder)
    # total_size += folder.get_file_size()
    return total_size if total_size < MAX_SIZE else 0


def folder_exists(name, tree):
    pass


if __name__ == "__main__":
    main()
