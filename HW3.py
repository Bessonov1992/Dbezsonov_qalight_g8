string = "Мені дуже подобається вивчати пайтон! Здається, це найлегша з потужних мов для вивчення"  # first
print(len(string))

print(len([i for i in string.split(" ")]))  # second

string = string.split(" ")  # third
answer3 = []
for i in string:
    tmp_str = ""
    for j in i:
        if j in ("а", "е", "э", "и", "і", "ї", "о", "у", "ю", "я"):
            tmp_str += "#"
        else:
            tmp_str += j
    answer3.append(tmp_str)
print(answer3)

answer4 = ""  # fourth
for i in answer3:
    if answer3.index(i) == 0:
        answer4 += i
    else:
        answer4 += " " + i
print(answer4)