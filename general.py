import os


def read_directory_contents(directory):
    contents = set()
    for file in os.listdir(directory):
        file_path = directory + '\\' + file
        contents.add(read_file(file_path))
    return contents


def read_file(file_name):
    with open(file_name, 'r', errors='ignore') as f:
        contents = f.read()
    # in_file = open(file_name, 'rt', encoding="utf-8")
    # text = in_file.read()
    # in_file.close()
    # return text
    return contents


def write_to_file(Article_name, Website, avg1, avg2):
    with open('out.txt', 'a') as f:
        f.write(Article_name + '\t\t' + Website + '\t\t' + str(avg1) + str(avg2))
    f.close()
