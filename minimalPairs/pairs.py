#! /usr/bin/python3
# Author: Pablo Baeyens
# Usage:
#   ./pairs.py -h
# for usage info and options
# Creates csv compatible with Anki from list of minimal pairs

import os
import csv
import argparse
import requests

API_URL = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/en/'


def ipa(word, header):
  """ Gets IPA pronunciation (RP) from Oxford Dictionary.
    Empty if no suitable answer is found."""
  
  req = requests.get(API_URL + word.lower(), headers = header)
  
  if req.status_code == 200:
    entries = req.json()["results"][0]["lexicalEntries"]
    for entry in entries:
      if "pronunciations" in entry:
        return entry["pronunciations"][0]["phoneticSpelling"]
  return ""


def to_es(word, header):
  """ Gets Spanish translation from Oxford Dictionary.
    Empty if no suitable answer is found."""
  
  req = requests.get(
    API_URL + word.lower() + '/translations=es', headers = header)
  
  if req.status_code == 200:
    senses = req.json(
    )["results"][0]["lexicalEntries"][0]["entries"][0]["senses"]
    
    for sense in senses:
      if "translations" in sense:
        return sense["translations"][0]["text"]
      elif "subsenses" in sense:
        for subsense in sense["subsenses"]:
          if "translations" in subsense:
            return subsense["translations"][0]["text"]
  return ""


if __name__ == "__main__":
  parser = argparse.ArgumentParser(
    description = "Generates csv compatible with Anki from list of words")
  parser.add_argument("words", help = "file with list of words")
  parser.add_argument(
    "app_id", help = "ID of Oxford Dictionaries registered app")
  parser.add_argument(
    "app_key", help = "Key of Oxford Dictionaries registered app")
  parser.add_argument(
    "--csv",
    nargs = 1,
    help = "Name of export FILE",
    metavar = "FILE",
    default = ["cards.csv"])
  parser.add_argument(
    "--rename",
    help = "Rename mp3 files from Audacity numbers to names",
    action = "store_true")
  args = parser.parse_args()
  
  words = open(args.words).read().splitlines()
  cards_csv = csv.writer(open(args.csv[0], 'a'), delimiter = ',')
  header = {'app_id': args.app_id, 'app_key': args.app_key}
  
  for num, word in enumerate(words, start = 1):
    if args.rename:
      os.rename("{}.mp3".format(num), "{}.mp3".format(word))
    
    if num % 2 == 1:
      prev = word
    else:
      cards_csv.writerow(
        [
          prev, "[sound:{}.mp3]".format(prev),
          ipa(prev, header),
          to_es(prev, header)
        ] + [
          word, "[sound:{}.mp3]".format(word),
          ipa(word, header),
          to_es(word, header)
        ])
