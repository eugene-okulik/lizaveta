import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("path", help="Path to folder with logs")
parser.add_argument("-t", "--text", help="text for search", required=True)
args = parser.parse_args()

files = []

if os.path.isfile(args.path):
    print('this is file')
    files.append(args.path)
elif os.path.isdir(args.path):
    print('this is dir')
    for file in os.listdir(args.path):
        print(os.path.join(args.path, file))
        files.append(os.path.join(args.path, file))
else:
    print('no path found')

blocks = {}
for file_path in files:
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('2022'):
                time = line[:23]
                blocks[time] = [file_path, line]

            else:
                blocks[time][1] += line
found = 0
for time, value in blocks.items():
    if args.text in value[1]:
        print(os.path.basename(value[0]), time)
        words = value[1].split()
        for i in range(len(words)):
            if args.text in words[i]:
                start = max(0, i - 5)
                print(' '.join(words[start: i + 6]))
                break
        found = found + 1
if found == 0:
    print('no text found')
else:
    print('found', found)
