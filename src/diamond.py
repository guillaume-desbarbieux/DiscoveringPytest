def make_diamond(char):
    if char=="A":
        return "A"

    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    index = letters.index(char)
    resultat = ""
    for i in range(index +1) :
        if i == 0:
            resultat += " "*(index - i) + "A"
        else:
            resultat += " "*(index - i) + letters[i] + " "*(i*2-1) + letters[i]
        if char == letters[i]:
            break
        else:
            resultat += "\n"

    for i in range(index-1, 0, -1):
        resultat += "\n" + " "*(index - i) + letters[i] + " "*(i*2-1) + letters[i]

    resultat += "\n" + " "*index + "A"
    return resultat