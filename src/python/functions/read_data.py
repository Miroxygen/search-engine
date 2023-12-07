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

url_prefix = "https://wikipedia.org/wiki/"

def read_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data.split()

for file in os.listdir(game_folder):
    file_path = os.path.join(game_folder, file)
    words = read_file(file_path)
    games.append({"url" : "https://wikipedia.org/wiki/" + file, "words" : words})

for file in os.listdir(game_links_folder):
    file_path = os.path.join(game_links_folder, file)
    link = read_file(file_path)
    games_links.append({"link" : link})

for file in os.listdir(programming_folder):
    file_path = os.path.join(programming_folder, file)
    words = read_file(file_path)
    programming.append({"url" : "https://wikipedia.org/wiki/" + file, "words" : words})

for file in os.listdir(programming_links_folder):
    file_path = os.path.join(programming_links_folder, file)
    link = read_file(file_path)
    programming_links.append({"link" : link})





