
import random

PUNCTUATION = ['.', '!', '?']

def dollarify(wordList, k):
    ''' adds k amount of '$' in front of each sentence '''
    if type(wordList) != list:
        return dollarify(wordList.split(), k)
    elif len(wordList) == 0:
        return []
    else:
        for i in range(len(wordList)):
            if wordList[i][-1] in PUNCTUATION:
                return k*['$'] + wordList[:i + 1] + dollarify(wordList[i + 1:], k)
        return k*['$'] + wordList

def markov_model(wordList, k):
    ''' accept the list of words in the text and return a k-th order Markov model based on that text '''
    dWordList = dollarify(wordList, k)
    D = {}
    i = 0 
    while i < len(dWordList) - k: 
        keyList = dWordList[i:i+k]
        #if len(keyList) == 1 and keyList[0][-1] in PUNCTUATION:
        #    i += k-1 
        #    pass
        if keyList[-1][-1] in PUNCTUATION:
            i += k-1
            pass
        else:
            key = tuple(dWordList[i:i+k])
            if key in D:
                D[key].append(dWordList[i+k])
            else:
                D[key] = [dWordList[i+k]]
        i += 1
    return D


    for i in range(len(dWordList) - (k+1)):
        keyList = dWordList[i:i+k]
        if len(keyList) == 1 and keyList[0][-1] in PUNCTUATION:
            pass
        elif keyList[-1][-1] in PUNCTUATION:
            pass
        else:
            key = tuple(dWordList[i:i+k])
            if key in D:
                L = D[key]
                D[key] = L + [dWordList[i+k]]
            else:
                D[key] = [dWordList[i+k]]
    return D

def gen_from_model(mmodel, numwords):
    ''' accepts a Markov model and an integer which represents the number of words to print from the model '''
    k = findModelNum(mmodel)
    finalL = k*['$']
    out = []
    for i in range(numwords):
        if finalL[-1][-1] in PUNCTUATION:
            L = mmodel[tuple(k*['$'])] 
            finalL +=k*['$']
        else:
            L = mmodel[tuple(finalL[-k:])] 
        word = random.choice(L)
        print(word)
        finalL.append(word)
        out.append(word)
    finalL = finalL[k:]
    finalString = ' '.join(out)
    print(finalString)

def findModelNum(mmodel):
    ''' finds the k value of a markov model'''
    key = []
    while tuple(key) not in mmodel:
        key += ['$']
    return len(key)

def markov(fileName, k, length):
    ''' 
    input: string containing a file name, model parameter k, and integer length
    Takes file, generates k-th order Markov model and generates output using the given length 
    '''
    f = open(fileName, 'r')
    inputList = f.read()
    f.close()
    mmodel = markov_model(inputList, k)
    return gen_from_model(mmodel, length)