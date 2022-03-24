import sys

for string in sys.stdin:
    while "AAAAA" in string:
        index_y = string.find("YYY")
        if index_y >= 0:
            string = string[:index_y] + "A" + string[index_y + 3:]
        index_a = string.find("AAA")
        if index_a >= 0:
            string = string[:index_a] + "Y" + string[index_a + 3:]
    print(string)