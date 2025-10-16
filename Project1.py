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
    flipper_dict = {}
    years = year_list(data)
    for year in years: 
        flipper_list = []
        for item in data:
            if item["sex"] == "female" and item["year"] == year:
                for k,v in item.items():
                    if k == "flipper_length_mm":
                        flipper_list.append(v)
        average = ave_flipper_length(flipper_list)
        flipper_dict[year] = average
    return flipper_dict

def year_list(data):
    lst = []
    for item in data:
        if item["year"] in lst:
            continue
        else:
            lst.append(item["year"])
    lst.sort()
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
    species_list = make_species_list(data)
    for species in species_list:
        d = {}
        for item in data:
            if item["island"] not in d.keys():
                print(item["island"])
                d[item["island"]] = 0
            if item["species"] == species:
                d[item["island"]] += 1
        island_pop[species] = d
    return island_pop

def make_species_list(data):
    lst = []
    for item in data:
        if item["species"] in lst:
            continue
        else:
            lst.append(item["species"])
    lst.sort()
    return lst


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

       
def penguin_mass_comparison(data):
    population = penguin_pop(data)
    total_mass_dict = {}
    print(population)
    for species in population.keys():
        if species not in total_mass_dict.keys():
            total_mass_dict[species] = ""
        d = {}
        for island, island_pop in population[species].items():
            if island_pop == 0:
                d[island] = 0.0
                continue
            body_mass_list = body_mass(species, data)
            total_ave_mass = total_ave(body_mass_list)
            greater_count = 0
            for penguin_dict in body_mass_list:
                if penguin_dict["body mass"] >= total_ave_mass and penguin_dict["island"] == island:
                    greater_count += 1
            percent_greater = round((greater_count / island_pop) * 100, 2)
            d[island] = percent_greater
            print(f"On {island}, {percent_greater}% of {species} penguins have a greater mass than the average {species} mass across islands.")
        total_mass_dict[species] = d
    return total_mass_dict

def csv_writer(filename, output):
    outFile = open(filename, "w")
    csv_writer = csv.writer(outFile)
    csv_writer.writerow([f"Percentage of Penguins on Each Island with a Body Mass Greater than Species Average"])
    for item in output.items():
        csv_writer.writerow(item)
    
class project_Test(unittest.TestCase):
    def setUp(self):
        self.open = open_file("penguins.csv")
        sample = [
        {"species":"Chinstrap","island":"Dream","bill_length_mm": 45.4, "bill_depth_mm": 18.7, "flipper_length_mm": 188, "body_mass_g": 3525,"sex": "female", "year": 2007},
        {"species":"Chinstrap","island":"Dream","bill_length_mm": 40.9, "bill_depth_mm": 16.6, "flipper_length_mm": 187, "body_mass_g": 3200,"sex": "female", "year": 2008},
        {"species":"Chinstrap","island":"Dream","bill_length_mm": 58, "bill_depth_mm": 17.8, "flipper_length_mm": 181, "body_mass_g": 3700,"sex": "female", "year": 2007},
        {"species":"Chinstrap","island":"Dream","bill_length_mm": 49.3, "bill_depth_mm": 19.9, "flipper_length_mm": 203, "body_mass_g": 4050,"sex": "male", "year": 2009},
        {"species":"Gentoo","island":"Biscoe","bill_length_mm": 49.5, "bill_depth_mm": 16.2, "flipper_length_mm": 229, "body_mass_g": 5800,"sex": "male", "year": 2008},
        {"species":"Gentoo","island":"Biscoe","bill_length_mm":47.7,"bill_depth_mm":17.5, "flipper_length_mm": 216, "body_mass_g": 4750, "sex": "female","year": 2008},
        {"species":"Gentoo","island":"Biscoe","bill_length_mm":50.5,"bill_depth_mm":15.9,"flipper_length_mm":222,"body_mass_g":5550,"sex":"male","year":2008},
        {"species":"Gentoo","island":"Biscoe","bill_length_mm": 43.4,"bill_depth_mm":14.4,"flipper_length_mm":218,"body_mass_g":4600,"sex":"female","year":2009},
        {"species":"Adelie","island":"Torgersen","bill_length_mm": 39.1, "bill_depth_mm": 18.7, "flipper_length_mm": 181, "body_mass_g": 3750,"sex": "male", "year": 2007},
        {"species":"Adelie","island":"Torgersen","bill_length_mm": "NA", "bill_depth_mm": "NA", "flipper_length_mm": "NA", "body_mass_g": "NA","sex": "NA", "year": 2007},
        {"species":"Adelie","island":"Dream","bill_length_mm": 37.3, "bill_depth_mm": 16.8, "flipper_length_mm": 192, "body_mass_g": 3000,"sex": "female", "year": 2009},
        {"species":"Adelie","island":"Biscoe","bill_length_mm": 38.1, "bill_depth_mm": 17, "flipper_length_mm": 181, "body_mass_g": 3175,"sex": "female", "year": 2009},
        {"species": "Adelie", "island":"Dream","bill_length_mm":40.3, "bill_depth_mm":18.5, "flipper_length_mm": 196, "body_mass_g": 4350,"sex": "male", "year": 2008}
        ]
        #Test flipper lengths
        self.fem_flip = female_flipper(sample)
        #Edge Case 1 Flipper (only male input)
        self.fem_flip2 = female_flipper(sample[3:5])
        self.year = year_list(sample)
        example = (123,"NA",47)
        self.ave_flip = ave_flipper_length(example)
        #Edge Case 2 Flipper (all NA values)
        example2 = ("NA","NA")
        self.ave_flip2 = ave_flipper_length(example2)
        self.year = year_list(sample)
        #Test body mass
        self.pop = penguin_pop(sample)
        self.penguin_mass = penguin_mass_comparison(sample)
        self.penguin_mass2 = penguin_mass_comparison(sample)


    def test_csv(self):
        self.assertIsInstance(self.open, list)
        self.assertIsInstance(self.open[0], dict)

    #FLIPPER LENGTH-FEMALE-ISLAND

    def test_final_flipper(self):
        #Normal case
        dict = {2007: 184.5, 2008: 201.5, 2009: 197}
        self.assertEqual(self.fem_flip, dict)
        #Edge Case 1
        dict2 = {2008: "No values exist, so none could be calculated", 2009: "No values exist, so none could be calculated"}
        self.assertEqual(self.fem_flip2, dict2)

    def test_ave_flipper(self):
        #Normal case
        average = (123 + 47) / 2
        self.assertEqual(self.ave_flip, average)
        #Edge Case 2
        average2 = "No values exist, so none could be calculated"
        self.assertEqual(self.ave_flip2, average2)

    def test_island_list(self):
        #Normal case
        lst = [2007, 2008, 2009]
        self.assertEqual(self.year, lst)

    #BODY MASS-SPECIES-ISLAND

    def test_pop(self):
        #Normal Case, Adelie has same population on Torgersen and Dream islands (2 penguins in this sample)
        self.assertTrue(self.pop["Adelie"]["Torgersen"] == self.pop["Adelie"]["Dream"])
        #Edge Case 1, No Chinstrap penguins on Torgersen
        self.assertEqual(self.pop["Chinstrap"]["Torgersen"], 0)

    def test_penguin_mass(self):
        #Normal Case, 50% of Adelie penguins on Torgersen are above the average Adelie mass
        self.assertEqual(self.penguin_mass["Adelie"]["Torgersen"], 50.0)
        #Edge Case 2, No Gentoo on Dream so it defaults to 0.0 mass
        self.assertEqual(self.penguin_mass["Gentoo"]["Dream"], 0.0)
    

def main():
    penguin_data = open_file("penguins.csv")
    info = penguin_mass_comparison(penguin_data)
    csv_writer("output_file.csv", info)
    unittest.main(verbosity=2)

main()
