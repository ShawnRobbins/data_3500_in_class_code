# import random

# num = 10
# int_list = [1, 3, 5, 7, 9]

# def random_list_num(num, int_list):
#     rand_num = random.randint(0, num)
#     while rand_num in int_list:
#         rand_num = random.randint(0, num)
#     return rand_num

# print(random_list_num(num, int_list))

# Dictionary

lance = {}

lance["name"] = "Lance Nielsen"
lance["age"] = 25
lance["car"] = {"make": "Hyundai", "model":"Sonata", "year":2010, "mileage":185000, "transmission":"Automatic", "color":"Blue", "num_doors": 4}
lance["major"] = "Information Systems"
lance["married"] = True
lance["schedule"] = ["DATA3500", "DATA4330", "IS3600", "MSLE3890", "DATA5360"]
lance["fav_temp"] = 72.5

# print("lance:", lance)
print(lance["age"])
print(lance["schedule"])
print(lance["car"])

# how do I access a list element for a list stored in a dictionary?
print(lance["schedule"][2])
lance["schedule"].append("STAT1040")
print(lance)

print(lance["car"]["num_doors"])

for key in lance["car"].keys():
    print("key:", key)

print("Profile Maker:")
years_in_cv = float(input("How many years have you lived in Cache Valley? "))
fav_color = input("What is your favorite color? ")
fav_prog_lang = input("What is your favorite programming language? ")

survey = {"years_in_CV":years_in_cv, "fav_color":fav_color, "fav_prog_lang":fav_prog_lang}
for key in survey.keys():
    print("key:", key, "value:", survey[key])

