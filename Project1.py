#Name: Cora Mueller
#Student ID: 59369139
#Student Email: cemuell@umich.edu
# No use of GenAI


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
                d[headers[6]] = line[6]
                d[headers[7]] = line[7]
                d[headers[8]] = line[8]
                data.append(d)
        f.close()
        return data

def female_flipper(data):
    flipper_list = []
    flipper_dict = {}
    years = year_list(data)
    for year in years: 
        for item in data:
            if item["sex"] == "female" and item["year"] == year:
                for k,v in item.items():
                    if k == "flipper_length_mm":
                        flipper_list.append(v)
        average = ave_flipper_length(flipper_list)
        flipper_dict[year] = average
    print(f"FLIPPERS: {flipper_dict}")
    return flipper_dict

def year_list(data):
    lst = []
    for item in data:
        if item["year"] in lst:
            continue
        else:
            lst.append(item["year"])
    return lst

def ave_flipper_length(lst):
    total = 0
    counted_penguins = 0
    for num in lst:
        if num == "NA":
            total += 0
        else: 
            total += int(num)
            counted_penguins += 1
    if total == 0:
        return "No values exist, so none could be calculated"
    else: 
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
    print(f"Percentage of {species} on {island} island: {round(percent, 2)}%")
    return percent

def body_mass(species, data):
    mass_list = []
    for item in data:
        d = {}
        if item["species"] == species and item["body_mass_g"] != "NA":
            d["island"] = item["island"]
            mass = int(item["body_mass_g"])
            d["body mass"] = mass
            mass_list.append(d)
    return mass_list

def total_ave(lst):
    total = 0
    count = 0
    for dct in lst:
        total += dct["body mass"]
        count += 1
    ave = total / count
    return ave


#MAKE A GIANT NESTED DICTIONARY        
def penguin_mass_comparison(species, data):
    population = penguin_pop(data)
    total_mass_dict = {}
    for island, island_pop in population.items():
        percent = percent_population(island, species, data)
        if percent == 0.0:
            total_mass_dict[island] = 0.0
            continue
        body_mass_list = body_mass(species, data)
        total_ave_mass = total_ave(body_mass_list)
        greater_count = 0
        species_pop_island = percent * island_pop
        for penguin_dict in body_mass_list:
            if penguin_dict["body mass"] >= total_ave_mass:
                greater_count += 1
        percent_greater = round((greater_count / species_pop_island) * 100, 2)
        total_mass_dict[island] = percent_greater
        print(f"On {island}, {percent_greater}% of {species} penguins have a greater mass than the average {species} mass across islands.")
    print(f"MASS: {total_mass_dict}")
    return total_mass_dict

def csv_writer(filename, output):
    outFile = open(filename, "w")
    csv_writer = csv.writer(outFile)
    csv_writer.writerow([f"Flipper Length Averages per Year for Female Penguins"])
    for item in output.items():
        csv_writer.writerow(item)
    

class project_Test(unittest.TestCase):
    def setUp(self):
        self.open = open_file("penguins.csv")
        sample = [{"species":"Chinstrap","island":"Dream","bill_length_mm": 45.4, "bill_depth_mm": 18.7, "flipper_length_mm": 188, "body_mass_g": 3525,"sex": "female", "year": 2007},{"species":"Gentoo","island":"Biscoe","bill_length_mm": 49.5, "bill_depth_mm": 16.2, "flipper_length_mm": 229, "body_mass_g": 5800,"sex": "male", "year": 2008},{"species":"Adelie","island":"Torgersen","bill_length_mm": 39.1, "bill_depth_mm": 18.7, "flipper_length_mm": 181, "body_mass_g": 3750,"sex": "male", "year": 2007},{"species":"Adelie","island":"Dream","bill_length_mm": 37.3, "bill_depth_mm": 16.8, "flipper_length_mm": 192, "body_mass_g": 3000,"sex": "female", "year": 2009}]
        self.a_fem_flip = female_flipper(self.open)
        example = (123,"NA",47)
        self.ave_flip = ave_flipper_length(example)
        example2 = ("NA","NA")
        self.ave_flip2 = ave_flipper_length(example2)
        self.year = year_list(self.open)
        self.pop = penguin_pop(self.open)
        self.da_percent = percent_population("Dream", "Adelie", self.open)
        self.penguin_mass = penguin_mass_comparison("Gentoo", self.open)
        self.penguin_mass2 = penguin_mass_comparison("Adelie", self.open)
        self.writer = csv_writer("output_file.csv", self.a_fem_flip)


    # MAKE TWO EDGE CASES
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

    #FLIPPER LENGTH-FEMALE-ISLAND (2 EDGE CASES)

    def test_final_flipper(self):
        truth = {"2007": 194.22, "2008": 196.6, "2009": 197.36}
        self.assertEqual(self.a_fem_flip, truth)

    def test_ave_flipper(self):
        average = (123 + 47) / 2
        self.assertEqual(self.ave_flip, average)
        #Edge Case
        average2 = "No values exist, so none could be calculated"
        self.assertEqual(self.ave_flip2, average2)

    def test_island_list(self):
        lst = ["2007", "2008", "2009"]
        self.assertEqual(self.year, lst)


    #BODY MASS-SPECIES-ISLAND

    def test_pop(self):
        pop_dict = {"Torgersen": 52, "Biscoe": 168, "Dream": 124}
        self.assertEqual(self.pop, pop_dict)


    def test_percent(self):
        self.assertAlmostEqual(self.da_percent, 45.16129032258064)

    def test_penguin_mass(self):
        mass_dict = {"Torgersen": 0.0, "Biscoe": 0.47, "Dream": 0.0}
        self.assertEqual(self.penguin_mass, mass_dict)


def main():
    unittest.main(verbosity=2)

main()
