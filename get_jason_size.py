# File name: get_jason_size.py
# Author: Oscar A. Rangel
# Creation date: 2023-04-17
# Last modified date: 2023-04-17
# Description: A Python script that translates text in a JSON file using OpenAI's GPT-3.5-turbo model.
# License: MIT

import json

file_path = 'alpaca_english_data.json'

with open(file_path, 'r') as f:
    data = json.load(f)

# Determine the type of JSON object and its length
if isinstance(data, list):
    length = len(data)
elif isinstance(data, dict):
    length = len(data.keys())
else:
    print("The JSON object is neither a list nor a dictionary.")
    length = 0

if length > 0:
    # Calculate the beginning and end indexes
    begin_index = 0
    end_index = length - 1

    # Print the results
    print(f"Size of data: {length}")
    print(f"Beginning index: {begin_index}")
    print(f"End index: {end_index}")
else:
    print("Invalid or empty JSON object.")

# Size of data: 52002
# Beginning index: 0
