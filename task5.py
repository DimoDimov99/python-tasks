def count_words_from_txt(filename="text.txt") -> dict:
    words_occurance = {}
    text_with_whitespaces = ""
    with open(filename, "r+") as file:
        lines = file.readlines()
        for line in lines:
            text_with_whitespaces += line
    text_manipulated = "".join(text_with_whitespaces.replace("\n", " ")).split(" ")
    for item in text_manipulated:
        if item not in words_occurance:
            words_occurance[item] = 1
        else:
            words_occurance[item] += 1
    sorted_dict = dict(sorted(words_occurance.items(), key=lambda x: x[0].lower()))
    for key, value in sorted_dict.items():
        print(f"{key} : {value}")


if __name__ == "__main__":
    count_words_from_txt()
