# https://www.hackerrank.com/challenges/the-minion-game/problem
def minion_game(string):
    kevin = 0 #kevin's score
    stuart = 0 #stuart's score
    vowels = "AEIOU" #string of vowels
    for i in range(len(string)):
        if string[i] in vowels: #check's if the character in string is in the vowels string
             #adds up all the letters after that letter because the word 
             # would still start with a vowel
            kevin += (len(string) - i) 
        else:
            stuart += (len(string) - i)
    
    if kevin > stuart:
        print("Kevin %d" % kevin)
    elif stuart > kevin:
        print("Stuart %d" % stuart)
    else:
        print("Draw")
        
if __name__ == '__main__':
    s = input()
    minion_game(s)