import argparse

# Initialize parser
parser = argparse.ArgumentParser(description='Displays the most common words used in a portion of a webpage.')
parser.add_argument("-u", "--url", type=str, help='Webpage to crawl', default="https://en.wikipedia.org/wiki/Microsoft")
parser.add_argument("-p", "--portion", type=str, help='Portion of the webpage to crawl', default="history")
parser.add_argument("-n", "--num_words", help = "Number of words to return", type=int, default=10)
parser.add_argument("excluded_words", help = "Words to exclude", nargs="*", type=str)
args = parser.parse_args()

url = args.url
print("Webpage to crawl: % s" % args.url)

portion = args.url
print("Portion to crawl: % s" % args.portion)

num_words = args.num_words
print("Number of words to return: % s" % args.num_words)

excluded_words = args.excluded_words
print("Words to exclude: % s" % args.excluded_words)