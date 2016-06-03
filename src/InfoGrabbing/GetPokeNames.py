import re

poke_filename = "pokeXML.txt"
out_filename = "../../Data/PokemonNames.txt"

'''
import urllib.request
poke_page = urllib.request.urlopen('http://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number')
print(poke_page)
'''


def main(lines):
    out_file = open(out_filename, "w")
    poke_pattern = r"<td>.*title=\"(\w+)\"><img.*src=\"(\S+)\" .*$"

    for line in lines:
        hasPoke = re.match(poke_pattern, line)
        if hasPoke:
            name = hasPoke.group(1)
            pic = hasPoke.group(2)

            out_file.write(name)
            out_file.write("\n")


if __name__ == '__main__':
    try:
        with open(poke_filename, "r") as file:
            raw_lines = file.readlines()

        main(raw_lines)
    except IOError:
        print("ya dun messed up.")

