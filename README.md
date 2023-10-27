# Crawler Coding Challenge

This application will display the most common words used in the History section of [https://en.wikipedia.org/wiki/Microsoft](https://en.wikipedia.org/wiki/Microsoft)

## Set up your virtual environment

```bash
pipenv install
pipenv shell
```

## Run the application

```
python main.py
```

## Configurable options

```
$ python main.py -h
usage: main.py [-h] [-n NUM_WORDS] [excluded_words ...]

Displays the most common words used in a portion of a webpage.

positional arguments:
  excluded_words        Words to exclude

options:
  -h, --help            show this help message and exit
  -n NUM_WORDS, --num_words NUM_WORDS
                        Number of words to return
```

## Thanks for reading and have a nice day!