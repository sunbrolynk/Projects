def calculate_love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    true_score = 0
    love_score = 0
    total = ""
    true = ["t","r","u","e"]
    love = ["l","o","v","e"]
    for letter in name1:
        if letter in true:
            true_score += 1
        if letter in love:
            love_score += 1
    for letter in name2:
        if letter in true:
            true_score += 1
        if letter in love:
            love_score += 1
    total = str(true_score) + str(love_score)
    print(total)
calculate_love_score("Shane Wagar", "Natasha Walton")
