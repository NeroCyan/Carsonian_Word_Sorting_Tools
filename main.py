import re


def expander(key):  # Expands description to full key
    numbers = re.findall(r'\d+', key)
    for char in numbers:
        key = key.replace(char, "".join(["*" * int(char)]))
    return key


def seeker(key):  # Compares full key to dict_words of same length and returns Trues
    char_count = len([char for char in key if char.isalpha()])
    keyII = dict((index, value) for (index, value) in enumerate(key) if value.isalpha())
    with open("engFullDict.txt") as f:
        match = []
        for line in f:
            if len(line) - 1 == len(key):
                keeper = []
                for i, j in keyII.items():
                    if line[i] == j:
                        keeper.append(j)
                if len(keeper) == char_count:
                    match.append(line)
        return match


def ellipses(rough):   # Loops through "."s with each possible integer value
    result = []
    dot_pos = [i for i, x in enumerate(rough) if x == "."]
    for pos in dot_pos:
        for x in range(1, 29):
            holding = rough[:pos] + str(x) + rough[pos+1:]
            temp = seeker(expander(holding))
            if len(temp) != 0:
                result.extend(temp)

    return result


if __name__ == '__main__':  # Enter word description
    description = input("Enter word description :")
    if description.count(".") == 0:
        print(seeker(expander(description)))
    elif description.count(".") != 0:
        print(ellipses(description))


