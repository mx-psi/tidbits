#!/usr/bin/python3
# Author: Pablo Baeyens
# Attempts to rename videos and subtitles by removing unimportant bits

import os
import re
import argparse

# What file extensions the script will consider
video_extensions = [".mkv",".srt",".avi",".mp4"]

# Anything after these is removed from the filename
to_remove  = ["1080p","720p","BrRip","DVDRip","YIFY",
              "BOKUTOX","x264","WEB-DL","HDTV","H264",
              "AAC","HDRip","AC3-EVO","x265","WEBRip",
              "x264-[MULVAcoded]"]

def pretty_name(path, sep="."):
    """Takes a path and prettifies
    it omitting unimportant bits"""

    bare_path,ext = os.path.splitext(path)
    elements = re.split(r"\.|[ ]|_",bare_path)

    new_path = ""

    for element in elements:
        if element in to_remove:
            break
        else:
           new_path += element + " "

    return new_path[:-1] + ext


def is_video(path):
  """Checks if path stands for a video or subtitles."""

  _,ext =  os.path.splitext(path)

  return ext in video_extensions


def rename_files(files, *, dry = False):
    """Renames listed video files"""
    for path in files:
        if os.path.isfile(path) and is_video(path):
          if dry:
            print(path, "→", pretty_name(path))
          else:
            os.rename(path,pretty_name(path))


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Prettifies names of videos and subtitles")
  parser.add_argument("-n", "--dry-run", help="Only shows renames", action="store_true")
  args  = parser.parse_args()
  rename_files(os.listdir("."), dry = args.dry_run)
