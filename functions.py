holes = [
        "4", "6", "9", "0", "Q", "q", "R", "O", "o", "P", "p", 
        "A", "a", "D", "d", "b", "ъ", "ы", "а", "А", "Р", "р",
        "О", "о", "Д", "д", "Я", "я", "Ь", "ь", "Б", "б", "Ю", "ю"
    ]

double_holes = ["8", "B", "Ф", "ф", "В", "в", "%"]

def count_holes(message):
    text = str(message)
    result = 0
    for i in range(len(text)):
        if text[i] in holes:
            result += 1
        if text[i] in double_holes:
            result += 2
    return result