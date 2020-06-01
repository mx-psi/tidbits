#!/usr/bin/env python3
# Author: Pablo Baeyens
# Usage: ./$0 [src.json] [dest.csv]
# Description: Transforms JSON list in file to CSV file

import sys
import json
import csv
import logging

logging.basicConfig(format="[%(levelname)s] %(message)s", level=logging.DEBUG)


if len(sys.argv) < 3:
    logging.error("Incorrect number of arguments")
    print("Usage: %s [src.json] [dest.csv]", sys.argv[0])
    sys.exit(1)
JSON_PATH = sys.argv[1]
CSV_PATH = sys.argv[2]


logging.info("Reading JSON from '%s'", JSON_PATH)
with open(JSON_PATH, "r") as json_file:
    json_data = json.load(json_file)
    if (
        not isinstance(json_data, list)
        or len(json_data) == 0
        or not isinstance(json_data[0], dict)
    ):
        logging.error("%s does not contain a dict list or is empty", JSON_PATH)
        sys.exit(1)


logging.info("Writing CSV to '%s'", CSV_PATH)
with open(CSV_PATH, "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=",", quoting=csv.QUOTE_MINIMAL)

    # Attempts to get available fields preserving original order
    header = max(json_data, key=lambda datapoint: len(datapoint.keys()))
    all_fields = set.union(*(set(dato.keys()) for dato in json_data))
    if set(header) != all_fields:
        logging.warning("Couldn't preserve order of fields")
        header = all_fields

    writer.writerow(header)
    for datapoint in json_data:
        writer.writerow(datapoint.get(key, None) for key in header)
