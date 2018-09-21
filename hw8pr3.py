tree = ("Is it bigger than a breadbox?", ("an elephant", None, None), ("a mouse", None, None))

def play(tree):
    ''' plays the tree '''
    if tree[1] == None and tree[2] == None:
        return playLeaf(tree)
    else:
        root, yesChild, noChild = tree
        answer = input(root + " ")
        if answer.lower() == 'yes':
            return (root, play(yesChild), noChild)
        else:
            return (root, yesChild, play(noChild))

def playLeaf(tree):
    ''' 
    plays the leaf
    if user answer is not in tree, it adds the leaf
    else it returns a win statement
    '''
    root, left, right = tree
    answer = input('Is it ' + root + "? ")
    if answer.lower() == 'yes':
        print('I got it!')
        return tree
    else:
        newLeaf = input('Gosh darnit! What was it? ')
        newRoot = input('What\'s a question that distinguishes between ' + newLeaf + ' and ' + root + '? ')
        LorR = input('And what\'s the answer for ' + newLeaf + '? ')
        if LorR.lower() == 'yes':
            return (newRoot, (newLeaf, None, None), (root, None, None))
        else:
            return (newRoot, (root, None, None), (newLeaf, None, None))

def saveTree(tree, fileName):
    ''' saves the tree as a text file'''
    f = open(fileName, 'w')
    f.write(format(tree))
    f.close()

def format(tree):
    ''' formats the tree to save '''
    root, left, right = tree
    if left == None and right == None:
        return root + '\n Leaf \n'
    else:
        return root + '\n Internal Node \n' + format(left) + format(right)

def main():
    ''' main function to play 20 questions '''
    print('Welcome to 20 questions!')
    tree = ("Is it bigger than a breadbox? ", ("an elephant", None, None), ("a mouse", None, None))
    while True:
        tree = play(tree)
        pAgain = input('Play again? ')
        if pAgain.lower() != 'yes':
            break 
    save = input('Would you like to save this tree for later? ')
    if save.lower() == 'yes':
        fName = input('Please enter file name: ')
        saveTree(tree, fName)
        print('Thank you! The file has been saved.')
    print('Bye!')