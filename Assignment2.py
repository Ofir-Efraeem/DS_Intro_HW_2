def reverse (sentence, reverse_word):
    if (type(sentence)==str) and (type (reverse_word)==str):
        counter = sentence.count(reverse_word)
        lst_sen = sentence.split()
        if counter == 0:
            return "no match word found"
        i=0
        for w in lst_sen:
            if w == reverse_word:
                lst_sen[i]=reverse_word[::-1]
                return " ".join(lst_sen)

            i=i+1

    else:
        return "invalid input"
