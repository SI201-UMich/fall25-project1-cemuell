#Name: Cora Mueller
#Student ID: 59369139
#Student Email: cemuell@umich.edu
# No use of GenAI

#MAKE SURE EACH CALCULATION UTILIZES 3 DIFF COLUMNS

import csv
import unittest

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
    average = ave_flipper_length(flipper_list)
    print(f"Average Female {species} Flipper Length: {average}")
    return average

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

#ADD THIRD COLUMN >:()
def percent_population(island_pop, island, species, data):
    total_pop = island_pop[island]
    count = 0
    for item in data:
        if item["island"] == island and item["species"] == species:
            count += 1
    percent = count / total_pop * 100
    percent = round(percent, 2)
    print(f"Rounded Percentage of {species} on {island} island: {percent}%")
    return percent

#how to know whether to write output to a csv/txt file?


#need test case for ave_flipper_length since its called in a different function?
# FOUR test cases for each function
class project_Test(unittest.TestCase):
    def setUp(self):
        self.open = open_file("penguins.csv")
        self.fem_flip = female_flipper(self.open, "Adelie")
        self.pop = penguin_pop(self.open)
        self.percent = percent_population(self.pop, "Dream", "Adelie", self.open)

    def test_csv(self):
        #Checks self.open is a list, and each item is a dict
        self.assertIsInstance(self.open, list)
        self.assertIsInstance(self.open[0], dict)
        #Checks bill length of first penguin
        self.assertEqual(self.open[0]["bill_length_mm"], '39.1')
        #Checks island of 52nd penguin
        self.assertEqual(self.open[51]["island"], 'Biscoe')
        #Checks sex of 14th penguin
        self.assertEqual(self.open[13]["sex"], 'male')

    def test_ave_flipper(self):
        return

    def test_pop(self):
        return

    def test_percent(self):
        return

def main():
    unittest.main(verbosity=2)

    """
    penguin_data = open_file("penguins.csv")
    adelie_flipper_list = female_flipper(penguin_data, "Adelie")
    gentoo_flipper_list = female_flipper(penguin_data, "Gentoo")
    print(f"Average Female Adelie Flipper Length: {ave_flipper_length(adelie_flipper_list)}")
    print(f"Average Female Gentoo Flipper Length: {ave_flipper_length(gentoo_flipper_list)}")
    island_penguins = penguin_pop(penguin_data)
    adelie_percent_dream = percent_population(island_penguins, "Dream", "Adelie", penguin_data)
    print(f"Rounded Percentage of Adelie on Dream island: {adelie_percent_dream}%")
    """

main()


