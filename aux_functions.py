import json
import csv
import pykakasi     # pip install pykakasi


# -------------------------------------------------------------
# loading file to list
def read_file(filename):
    if 'json' in filename:
        with open(filename, 'r', encoding='utf-8', newline='') as f:
            return json.load(f)
    if 'csv' in filename:
        return csv_list(filename)


def csv_list(filename):
    data = []
    with open(filename, 'r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for item in reader:
            data.append(item)
    # print(f'reading csv_list data: \n{data}')
    return data
# ------------------------------------------------------------------------


# writing list to file
def write_file(filename, list_data):
    if 'json' in filename:
        with open(filename, 'w') as f:
            json.dump(list_data, f, indent=4)
    if 'csv' in filename:
        with open(filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(list_data)


# cleaning of csv format
def clean_csv(file='jp_file.csv'):
    # initial 'cleaning'
    data = []
    with open(file, 'r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            item = row[0]
            item.strip('\"')    # unnecessary
            # csv.reader() acts a parser--(avoids , issues)
            item = next(csv.reader([item]))
            data.append(item)
        # print(data)

    # writing to new file
    write_file('jp_dict.csv', data)


# function that translates and cuts words
def translator(lst):
    kks = pykakasi.kakasi()
    romaji = []
    # start = time.perf_counter()
    for item in lst:
        roman = kks.convert(item)   # returns a list of dictionaries, hence [index][key]
        word = [roman[0]['hepburn']]    # listizing the words
        if 5 < len(word[0]) < 7:    # sorting
            romaji.append(word)
    return romaji
    # end = time.perf_counter()
    # print(f'{end - start:.5f} seconds') # so basically doesn't take a while luckily

