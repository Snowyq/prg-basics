def f(word):
    output = ""
    for index, _ in enumerate(word):
        new_word = ""
        for inner_index, char in enumerate(word):
            if inner_index == index:
                new_word += char.upper()
            else:
                new_word += char
        if index + 1 < len(word):
            new_word += "-"
        output += new_word
    return output


print(f("book"))



def f2(word):
    output = []
    for index, char in enumerate(word):
        new_word = "".join(
            char.upper() if i == index else c for i, c in enumerate(word)
        )
        output.append(new_word)
    return '-'.join(output)

print(f2("book"))

print(f2("book")) # à "Book-bOok-boOk-booK" 
print(f2("water")) # à "Water-wAter-waTer-watEr-wateR" 
print(f2("ok")) # à "Ok-oK" 
print(f2("a")) # à "A" 
print(f2("")) # à) "" 