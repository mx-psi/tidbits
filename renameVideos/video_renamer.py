#!/usr/bin/python3
# Author: Pablo Baeyens
# Attempts to rename videos and subtitles by removing unimportant bits

import os
import re
import argparse

# What file extensions the script will consider
VALID_EXTENSIONS = {
    "mkv", "srt", "avi", "mp4", "idx", "sub", "mpg", "rmvb", "m4v"
}

# Anything after these is removed from the filename
to_remove = [
    'x265',
    'x264-w4f',
    'x264',
    'mkv',
    'iT00NZ',
    'h.265',
    'MULVAcoded',
    'YIFY',
    'XviD',
    'ETRG',
    'WEBRip',
    'WEBRip',
    'WEB',
    'TorrentCouch.com',
    'SVA',
    'SRS',
    'SHORTBREHD',
    'PREAiR',
    'Mini',
    'HDTV',
    'HDRip',
    'H264',
    'H.264',
    'DVDScr',
    'DVDRip',
    'DD5.1',
    'DL',
    'BrRip',
    'BluRay',
    'BOKUTOX',
    'AVS',
    'AC3-EVO',
    "AC3 5.1",
    'AC3',
    'AAC2.0',
    'AAC',
    '480p',
    "m720p",
    '720p',
    '2.0-EVO',
    '1080p',
    'ITSat',
    "600MB",
    "1 GB",
    "Stealthmaster",
    "BDRip",
    "www.DivxTotaL.CoM",
    "720x552",
    "sujaidr",
    "DD 5.1",
    "HQ",
    "EtMovies",
] + [
    'pseudo', 'KILLERS', 'INTERNAL', 'FLEET', 'eSc', "RARBG", "ettv",
    "DTS-JYK", "Team Nanban", "iExTV", "Limited", "LokiHD", "c4tv", "Hive-CM8",
    "HEVC", "BRSHNKV", '[PriME]', "[FUM]"
]

matcher = re.compile(
    r"|".join(r"[\.\[\- _]*{}[\.\]\- _]*".format(re.escape(word))
              for word in to_remove), re.IGNORECASE)


def pretty_name(path):
    """Takes a path and prettifies
    it omitting unimportant bits"""

    bare_path, ext = os.path.splitext(path)
    return matcher.sub("", bare_path) + ext


def is_video(path):
    """Checks if path stands for a video or subtitles."""

    _, ext = os.path.splitext(path)
    return ext[1:] in VALID_EXTENSIONS


def rename_files(files, *, dry=False, recursive=False, verbose=False):
    """Renames listed video files"""
    for path in files:
        if os.path.isfile(path) and is_video(path):
            change = path != pretty_name(path)
            if not change:
                continue

            if dry or verbose:
                print(path, "→", pretty_name(path))

            if not dry:
                os.rename(path, pretty_name(path))
        elif recursive and os.path.isdir(path):
            os.chdir(path)
            rename_files(os.listdir(),
                         dry=dry,
                         recursive=recursive,
                         verbose=verbose)
            os.chdir("..")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Prettifies names of videos and subtitles")

    parser.add_argument("-n",
                        "--dry-run",
                        help="Only shows renames",
                        action="store_true")

    parser.add_argument("-R",
                        "--recursive",
                        help="Run recursively",
                        action="store_true")

    parser.add_argument("-v",
                        "--verbose",
                        help="Be verbose",
                        action="store_true")

    args = parser.parse_args()

    rename_files(os.listdir(),
                 dry=args.dry_run,
                 recursive=args.recursive,
                 verbose=args.verbose)
