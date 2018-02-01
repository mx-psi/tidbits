# Minimal Pairs Anki cards creator

Creates csv compatible with Anki from list of English [minimal pairs](https://en.wikipedia.org/wiki/Minimal_pair) (with Spanish translation).

## Running the script

You need to have Python 3. You also need:

- An `app_id` and an `app_key` of a registered app from [Oxford Dictionaries](https://developer.oxforddictionaries.com/)
- A plain-text file with a `list` of minimal pairs (one word per line, paired words must be one immediately after the other)
- One mp3 file for each word on the list with its pronunciation (`word` for each `word.mp3` or `n.mp3` numbered in the same order as they appear on `list`)
- The [model deck from Fluent Forever](https://fluent-forever.com/gallery/) installed on Anki

Once you have the appropiate files in the same directory as the script just run:

`pairs.py [--csv FILE] [--rename] list app_id app_key`


## Options

- `--csv FILE` sets csv export file name to `FILE`
- `--rename` renames files from numbers (`1.mp3`) to words (`lobes.mp3`)



