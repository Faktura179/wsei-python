import csv
import random
import webbrowser
import statistics

max_year = 0
min_year = 9999  
lego_sets = []
with open('sets.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        lego_sets.append(row)
        year = int(row['year'])
        if(year > max_year):
            max_year = year
        if(year < min_year):
            min_year = year

year = int(input(f"Enter the release year ({min_year} - {max_year}): "))

filtered_sets = []
for lego_set in lego_sets:
    if int(lego_set['year']) == year:
        filtered_sets.append(lego_set)

num_sets = len(filtered_sets)
num_pieces = [int(lego_set['num_parts']) for lego_set in filtered_sets]
average_pieces = statistics.mean(num_pieces)
median_pieces = statistics.median(num_pieces)

print(f"Number of sets released in {year}: {num_sets}")
print(f"Average number of pieces in sets released in {year}: {average_pieces}")
print(f"Median number of pieces in sets released in {year}: {median_pieces}")
random_set = random.choice(filtered_sets)
image_url = random_set['img_url']
webbrowser.open(image_url)
