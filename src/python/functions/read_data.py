import os

#Hardcoded methods for extracting Games and Programming wikipedia article words in indexed arrays within two arrays (Games, Programming).

game_folder = 'wikipedia/Words/Games'
games = []
game_links_folder = 'wikipedia/Links/Games'
games_links = []

programming_folder = 'wikipedia/Words/Programming'
programming = []
programming_links_folder = 'wikipedia/Links/Programming'
programming_links = []


def read_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data.split()

game_files = os.listdir(game_folder)
game_files.sort(key=lambda x: os.path.getmtime(os.path.join(game_folder, x)))

for file in game_files:
    file_path = os.path.join(game_folder, file)
    words = read_file(file_path)
    games.append({"url" : "https://wikipedia.org/wiki/" + file, "words" : words})

game_link_files = os.listdir(game_links_folder)
game_link_files.sort(key=lambda x: os.path.getmtime(os.path.join(game_links_folder, x)))

for file in game_link_files:
    file_path = os.path.join(game_links_folder, file)
    link = read_file(file_path)
    games_links.append({"link" : link})

programming_files = os.listdir(programming_folder)
programming_files.sort(key=lambda x: os.path.getmtime(os.path.join(programming_folder, x)))

for file in programming_files:
    file_path = os.path.join(programming_folder, file)
    words = read_file(file_path)
    programming.append({"url" : "https://wikipedia.org/wiki/" + file, "words" : words})

programming_link_files = os.listdir(programming_links_folder)
programming_link_files.sort(key=lambda x: os.path.getmtime(os.path.join(programming_links_folder, x)))

for file in programming_link_files:
    file_path = os.path.join(programming_links_folder, file)
    link = read_file(file_path)
    programming_links.append({"link" : link})

