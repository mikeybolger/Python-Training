spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    # Since spam is an integer to get the string version use str(spam)
    print ("spam is " + str(spam))
