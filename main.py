import argparse
from bs4 import BeautifulSoup
from collections import Counter
import re
import requests

# Initialize parser
parser = argparse.ArgumentParser(description='Displays the most common words used in a portion of a webpage.')
parser.add_argument("-n", "--num_words", help = "Number of words to return", type=int, default=10)
parser.add_argument("excluded_words", help = "Words to exclude", nargs="*", type=str)
args = parser.parse_args()

# Parse arguments
url = "https://en.wikipedia.org/wiki/Microsoft"
print("Webpage to crawl: % s" % url)
num_words = args.num_words
print("Number of words to return: % s" % num_words)
excluded_words = args.excluded_words
print("Words to exclude: % s" % excluded_words)

# Grab webpage contents
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

# Find the text between History section and Corporate affairs
pattern = r'<h2><span class="mw-headline" id="History">History</span></h2>(.*?)<h2><span class="mw-headline" id="Corporate_affairs">Corporate affairs</span></h2>'
match = re.search(pattern, str(soup), re.DOTALL)

if match:
    # Grab portion contents
    html_content = match.group(1).strip()
    soup = BeautifulSoup(html_content, 'html.parser')
    extracted_text = soup.get_text()

    # Tokenize the text into words
    words = re.findall(r'\w+', extracted_text)

    # Count the words using collections.Counter
    word_counts = Counter(words)

    # Sort the words and counts by counts in descending order
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Print the sorted list of words and their counts
    i = 0
    for word, count in sorted_word_counts:
        # Exclude words from result
        if word in excluded_words:
            continue

        # Only print top {num_words} words
        if i == num_words:
            break

        print(f'{word}: {count}')
        i = i + 1
        
# Done! Next steps could be to generify the pattern and specify (as args) the url and portion