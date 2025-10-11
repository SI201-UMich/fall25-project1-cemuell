#Name: Cora Mueller
#Student ID: 59369139
#Student Email: cemuell@umich.edu
# No use of GenAI

#MAKE SURE EACH CALCULATION UTILIZES 3 DIFF COLUMNS

import csv

def open_file(file):
    with open(file) as f:
        csvFile = csv.reader(f)
        data = []
        headers = next(csvFile)
        for line in csvFile:
            d = {}
            if len(line) == 9:
                species = line[1]
                d[headers[1]] = species
                island = line[2]
                d[headers[2]] = island
                bill_length_mm = line[3]
                d[headers[3]] = bill_length_mm
                bill_depth_mm = line[4]
                d[headers[4]] = bill_depth_mm
                flipper_length_mm = line[5]
                d[headers[5]] = flipper_length_mm
                body_mass_g = line[6]
                d[headers[6]] = body_mass_g
                sex = line[7]
                d[headers[7]] = sex
                year = line[8]
                d[headers[8]] = year
                data.append(d)
        f.close()
        return data

def female_flipper(data, species):
    flipper_list = []
    for item in data:
        if item["species"] == species and item["sex"] == "female":
            for k,v in item.items():
                if k == "flipper_length_mm":
                    flipper_list.append(v)
    return flipper_list

def ave_flipper_length(lst):
    total = 0
    counted_penguins = 0
    for num in lst:
        if num == "NA":
            total += 0
        else: 
            total += int(num)
            counted_penguins += 1
    return total / counted_penguins

def penguin_pop(data):
    island_pop = {}
    for item in data: 
        if item["island"] in island_pop.keys():
            island_pop[item["island"]] += 1
        else:
            island_pop[item["island"]] = 1
    print(island_pop)
    return island_pop

def main():
    penguin_data = open_file("penguins.csv")
    adelie_flipper_list = female_flipper(penguin_data, "Adelie")
    gentoo_flipper_list = female_flipper(penguin_data, "Gentoo")
    print(f"Average Female Adelie Flipper Length: {ave_flipper_length(adelie_flipper_list)}")
    print(f"Average Female Gentoo Flipper Length: {ave_flipper_length(gentoo_flipper_list)}")
    island_penguins = penguin_pop(penguin_data)

main()

#USE UNITTEST MODULE
#unittest()