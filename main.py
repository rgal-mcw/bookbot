
import sys

from stats import get_num_words, counting_chars, report_chars



def main():

    
    if len(sys.argv) != 2:
        raise Exception("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    return report_chars(sys.argv[1])

main()
