#!python

def word_count(string):
    word_list = string.split()
    return len(word_list)


if __name__ == "__main__":
    print(word_count("Hello World"))
    print(word_count("This is a sentence"))
