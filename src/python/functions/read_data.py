import os

#Hardcoded methods for extracting Games and Programming wikipedia article words in indexed arrays within two arrays (Games, Programming).

game_folder = 'wikipedia/Words/Games'
games = []

programming_folder = 'wikipedia/Words/Programming'
programming = []

def read_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data.split()

for file in os.listdir(game_folder):
    file_path = os.path.join(game_folder, file)
    data = read_file(file_path)
    games.append(data)

for file in os.listdir(programming_folder):
    file_path = os.path.join(programming_folder, file)
    data = read_file(file_path)
    programming.append(data)




