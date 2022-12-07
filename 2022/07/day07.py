#!/usr/bin/python3
import sys
from typing import Dict, List

class Node:

    def __init__(self, name: str, parent, size: int = 0, is_directory: bool = False):
        self.name = name
        self.parent = parent
        self.size = size
        self.is_directory = is_directory
        self.children = []

        if parent != None:
            parent.children.append(self)

    def get_root(self):
        root = self
        while True:
            if root.parent == None:
                break
            root = root.parent

        return root

    def calculate_size(self) -> int:
        for child in self.children:
            self.size += child.calculate_size()

        return self.size

    def add_child(self, name: str, size: int = 0, is_directory: bool = False):
        child = Node(name, self, size, is_directory)
        if not child in self.children:
            self.children.append(child)

    def get_directories(self):
        dirs = [self]
        for child in self.children:
            if child.is_directory:
                dirs += child.get_directories()

        return dirs

    def __str__(self, indent: int = 1) -> str:
        children_str = ''

        for child in self.children:
            children_str += "- "*indent + child.__str__(indent+1)
        

        result = f'{self.name} [{self.size}]\n' + children_str

        return result



def main(args):
    if len(args) < 2:
        print('[ERROR] Enter a file name!')
        print(f'\tUsage: python {args[0]} <filename>')
        sys.exit(1)

    filename = args[1]
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]

    total_space = 70000000
    unused_space_req = 30000000
    upper_limit = 100000

    print('Part One')

    i = 0
    current_directory: Node = None
    root_node: Node = None
    while i < len(lines):
        line = lines[i]
        if line.startswith('$ '):
            if line.startswith('$ cd '):
                dirname = line[5:]
                
                if dirname == '..':
                    current_directory  = current_directory.parent
                else:
                    current_directory = Node(dirname, current_directory, is_directory=True)
                    if root_node == None:
                        root_node = current_directory

            elif line == '$ ls':
                while True:
                    if i+1 == len(lines) or lines[i+1][0] == '$':
                        break

                    i += 1
                    line = lines[i]
                    if not line.startswith('dir'):
                        foo = line.split(' ')
                        size, filename = int(foo[0]), foo[1]
                        current_directory.add_child(filename, size)

        i += 1
            
    root_node.calculate_size()
    print(root_node)
    dirs = root_node.get_directories()

    result = 0
    for d in dirs:
        if d.size < upper_limit:
            result += d.size
    print(f'Result: {result}')

    print('Part Two')

    unused_space = total_space - root_node.size
    directory_req = unused_space_req - unused_space
    print(f'Missing space: {directory_req}')

    dirs.sort(key=lambda x: x.size, reverse=True)
    for idx, d in enumerate(dirs):
        if d.size <= directory_req:
            break

    dir_to_remove = dirs[idx-1]

    print(f'Remove directory {dir_to_remove.name} with size {dir_to_remove.size}')


if __name__ == '__main__':
    main(sys.argv)
