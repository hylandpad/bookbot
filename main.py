import sys

if len(sys.argv) != 2:
	print('Usage: python3 main.py <path_to_book>')

from stats import get_book_text

def main():
	print(get_book_text())

main()
