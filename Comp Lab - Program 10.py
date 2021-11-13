if __name__ == '__main__':
    def main():



        while True:
            user_file = input("Enter the name of the file to open ==> ")
            word_dict = dict()
            punct = ('.',',',';',':')
            with open(user_file,'r') as file:   
                for line in file:       
                    for word in line.split():
            '''no_p = word_dict.translate(str.maketrans('', '', string.punctuation))'''
            for line in word:
                if len(word) <= 3:
                    continue
                else:
                    if word in word_dict.keys():
                        word_dict[word] = word_dict[word] + 1
                    else:
                        word_dict[word] = 1
                
                word_dict = dict(sorted(word_dict.items(), reverse=True))
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

main()
