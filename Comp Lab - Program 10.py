''' Rye Ledford - Computer Science Lab - Program 10'''


            


while True:
    user_file = input("Enter the name of the file to open ==> ")
    u = open(user_file, 'r')

    try:
        with open(user_file) as file:
            word_dict = dict()
            for line in file:
                for word in line.strip().split(" "):
                    word = word.strip(punctuation)
                    if len(word) <= 3:
                        continue
                    else:
                        if word in word_dict.keys():
                            word_dict[word] = word_dict[word] + 1
                        else:
                            word_dict[word] = 1


            word_dict = dict(sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True))
            counter = 1
            print("Most frequently used words;")
            print("{:>0}{:>15}{:>15}".format('#', 'Word', 'Freq. '))
            print("{:>15}".format("=============================== "))
            for key in word_dict:
                if counter > 10:
                    break
                else:
                    frequency = word_dict[key]
                    print("{:>0}{:>15}{:>15}".format(counter, key, frequency))
                    counter += 1
                    onecount = 0 

            for key in word_dict:
                if word_dict[key] == 1:
                    onecount += 1
            oneword = len(word_dict)

            print("There are", onecount,  "words that occur only once ")
            print("There are", oneword, "unique words in the document ")
            print()
            search()

            def search():
                print()
                again = input('Would you like to check another file? Enter Y/n ==> ')
                print()
                if again == 'Y' or again == 'y':
                    return main()
                elif again == 'N' or again == 'n':
                    print()
                    return goodbye()
                else:
                    print('Please enter a valid option')
                    print()
                    return search()

            def goodbye():
                print('Thank you for using the word counter, have a great day. :)')
                exit(main)
