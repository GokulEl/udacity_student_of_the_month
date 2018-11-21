def remove_capital(sentence):
    result = ''
    words = list(sentence.split())

    # Remove the word with the Capital letter
    for word in words[-1:0:-1]:
        if word[0] == word[0].upper():
            words.remove(word)
            
    # Append the words together
    for word in words:
        if word != words[-1]:
            result += word+' '
        else:
            result += word
    return(result)

remove_capital("I am a God")