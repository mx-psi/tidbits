# Find closest words

Finds list of closest words from a list to a given query word.

## Running the script

You need to have [Python 3](https://www.python.org/downloads) and [editdistance](https://github.com/aflc/editdistance) installed. Once installed just run:

``` sh
./words.py [--n NUM] dictionary word
```

Two default dictionaries are included in the `dictionaries` folder. 
I got them from [javierarce/palabras](https://github.com/javierarce/palabras) (`spanish.dat`) and [dwyl/english-words](https://github.com/dwyl/english-words) (`english.dat`).

Dictionaries should have one word per line.

## Options

- `--n NUM` show `NUM` closest words (default is 10).
