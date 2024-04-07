"""
Reverse of a string is equal to the original string

"""
class Palindromecheck:

    def __init__(self, word):
        self.word = word
        self.ispalindrome_result = self.ispalindrome()

    def ispalindrome(self):
        return self.word.lower() == self.word.lower()[::-1]

    def __str__(self):
        status = 'is' if self.ispalindrome_result else ' is not'
        return f'The word {self.word}  {status} a palindrome word'

def main():
    palindrome = Palindromecheck('cigarre')
    print(palindrome)


if __name__ == '__main__':
    main()


