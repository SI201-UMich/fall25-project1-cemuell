#Name: Cora Mueller
#Student ID: 59369139
#Student Email: cemuell@umich.edu
# No use of GenAI

#ADD FAILSAFES FOR NO ANSWER

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
                d[headers[1]] = line[1]
                d[headers[2]] = line[2]
                d[headers[3]] = line[3]
                d[headers[4]] = line[4]
                d[headers[5]] = line[5]
                d[headers[6]] =  line[6]
                d[headers[7]] = line[7]
                d[headers[8]] = line[8]
                data.append(d)
        f.close()
        return data

#Fulfill 3 column requirement?
def female_flipper(data, species):
    flipper_list = []
    for item in data:
        if item["species"] == species and item["sex"] == "female":
            for k,v in item.items():
                if k == "flipper_length_mm":
                    flipper_list.append(v)
    #call other function in here
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
    return round(total / counted_penguins, 2)

def penguin_pop(data):
    island_pop = {}
    for item in data: 
        if item["island"] in island_pop.keys():
            island_pop[item["island"]] += 1
        else:
            island_pop[item["island"]] = 1
    print(island_pop)
    return island_pop

def percent_population(island, species, data):
    island_pop = penguin_pop(data)
    total_pop = island_pop[island]
    count = 0
    for item in data:
        if item["island"] == island and item["species"] == species:
            count += 1
    percent = count / total_pop * 100
    percent = round(percent, 2)
    print(f"Percentage of {species} on {island} island: {percent}%")
    return percent

def body_mass(species, data):
    mass_list = []
    for item in data:
        d = {}
        if item["species"] == species:
            d["island"] = item[2]
            d["body mass"] = item[6]
            mass_list.append(d)
    print(mass_list[3])
    return mass_list

def total_ave(lst):
    total = 0
    count = 0
    for dct in lst:
        total += dct["body mass"]
        count += 1
    ave = total / count
    return ave

def island_ave(island, lst):
    mass_total = 0 
    count = 0
    for dct in lst:
        if dct["island"] == island:
            mass_total += dct["body mass"]
            count += 1
    mass_ave = mass_total / count
    return mass_ave
        

#for specific penguins on specific island, compare body mass to average?
def penguin_mass_comparison(island, species, data):
    percent = percent_population(island, species, data)
    if percent == 0.0:
        return "Calculation cannot be performed; no penguins are on this island"
    body_mass_list = body_mass(species, data)
    total_ave_mass = total_ave(species, body_mass_list)
    great_count = 0
    less_count = 0 
    greater_dict = {}
    lesser_dict = {}
    for penguin_dict in body_mass_list:
        if penguin_dict["body mass"] >= total_ave_mass:
            great_count += 1
            greater_dict[great_count] = penguin_dict["body mass"]
        else:
            less_count += 1
            lesser_dict[less_count] = penguin_dict["body mass"]
    population = penguin_pop(data)
    island_pop = population[island]
    percent_greater = great_count / island_pop
    print(f"On {island}, {percent_greater} of {species} penguins are greater than the average {species} mass across islands.")
    return percent_greater


#how to know whether to write output to a csv/txt file? it's confusing


# need test case for ave_flipper_length since its called in a different function?
# FOUR test cases for each function
# What does it mean that the test cases shouldn't use the whole dataset, just a sample?
class project_Test(unittest.TestCase):
    def setUp(self):
        self.open = open_file("penguins.csv")
        self.a_fem_flip = female_flipper(self.open, "Adelie")
        self.g_fem_flip = female_flipper(self.open, "Gentoo")
        self.c_fem_flip = female_flipper(self.open, "Chinstrap")
        self.pop = penguin_pop(self.open)
        self.da_percent = percent_population("Dream", "Adelie", self.open)
        self.tg_percent = percent_population("Torgersen", "Gentoo", self.open)
        self.bc_percent = percent_population("Biscoe", "Chinstrap", self.open)
        self.dc_percent = percent_population("Dream", "Chinstrap", self.open)

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

#need another test
    def test_ave_flipper(self):
        self.assertAlmostEqual(self.a_fem_flip, 187.79)
        self.assertAlmostEqual(self.g_fem_flip, 212.71)
        self.assertAlmostEqual(self.c_fem_flip, 191.74)

#need more tests
    def test_pop(self):
        pop_dict = {"Torgersen": 52, "Biscoe": 168, "Dream": 124}
        self.assertEqual(self.pop, pop_dict)


    def test_percent(self):
        self.assertAlmostEqual(self.da_percent, 45.16)
        self.assertAlmostEqual(self.tg_percent, 0.0)
        self.assertAlmostEqual(self.bc_percent, 0.0)
        self.assertAlmostEqual(self.dc_percent, 54.84)
        

def main():
    unittest.main(verbosity=2)


main()


