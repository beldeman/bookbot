def main():
    book_path = "github.com/beldeman/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    words = text.split()
    strin = str(words).lower()
    words_count = 0
    letter_count = {}
    for word_count in words:
        words_count += 1
    for word in strin:
        for letter in word:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    report = []
    for letters in letter_count:
        if letters.isalpha() == True:
            tuple = (letter_count[letters],letters)
            report.append(tuple)
    sorted_report = sorted(report, reverse=True)
    print(f"--- Begin report of {book_path} ---")
    print(f"{words_count} words found in document")
    for letter in sorted_report:
        print(f"the '{letter[1]}' character was found {letter[0]} times")
    print("--- End report ---")
    
        


    
    


def get_book_text(path):
    with open(path) as f:
        return f.read()





main()