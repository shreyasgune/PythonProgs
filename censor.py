def censor(text,word):
    words = []
    words = text.split()
    c=""
    v=0
    print words
    
    for i in words:
        if i == word:
            c=""
            v=words.index(i)
            for n in range(len(word)):
                c+='*'
            words[v] = c
    sord = words
    for i in words:
        print i,
                


censor("Oh bloody hell . Shut the hell up, you idiot! You will go to hell for this","hell")
