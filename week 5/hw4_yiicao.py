import requests
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib 
from matplotlib.patches import Polygon
import random as random
from matplotlib.path import Path
import json
import statistics

response = requests.get("https://dsl.richmond.edu/panorama/redlining/static/downloads/geojson/MIDetroit1939.geojson")
# print(response.text)
json_str = response.text
json_dict = json.loads(json_str)
# print(type(json_dict))



thisDict = {
    "Coordinates": [feature["geometry"]["coordinates"][0][0] for feature in json_dict["features"]], #add lists of coordinates from the json file for each district
    "Holc_Grade": [feature["properties"]["holc_grade"] for feature in json_dict["features"]], #add the grades from the json file for each district
    "Holc_Color": [], #add the appropriate color for each district based on the instructions below
    "name": [json_dict["features"].index(feature) for feature in json_dict["features"]], #the name of the district is up to you, you might use a number or other iterator
}

for feature in json_dict["features"]:
    if feature["properties"]["holc_grade"] == "A":
        thisDict["Holc_Color"].append("darkgreen")
    if feature["properties"]["holc_grade"] == "B":
        thisDict["Holc_Color"].append("cornflowerblue")
    if feature["properties"]["holc_grade"] == "C":
        thisDict["Holc_Color"].append("gold")
    if feature["properties"]["holc_grade"] == "D":
        thisDict["Holc_Color"].append("maroon")


districts = []
fig, ax = plt.subplots()

for i in range(238):
    polyg = Polygon(thisDict["Coordinates"][i], True, edgecolor="black", facecolor=thisDict["Holc_Color"][i])
    districts.append(polyg)

for u in districts:
    ax.add_patch(u)

ax.autoscale()
plt.rcParams["figure.figsize"] = (15,15)
plt.show()

random.seed(33)
xgrid = np.arange(-83.5, -82.8, .004) #form an array from -83.5 to -82.8 and the step is .004
ygrid = np.arange(42.1, 42.6, .004) #form an array from 42.1 to 42.6 and the step is .004
xmesh, ymesh = np.meshgrid(xgrid, ygrid) #return coordinate matrices from coordinate vector [xgrid, ygrid]
points = np.vstack((xmesh.flatten(), ymesh.flatten())).T #use flatten() to get the given array into one dimension and use vstack() to stack these arrays vertically to make a single array

coordinate_list = []
for j in range(238):
    p = Path(thisDict["Coordinates"][j]) #use Path class to draw the path of each in the thisDict["Coordinates"]
    grid = p.contains_points(points) #return whether the path contains the given points
    # print(j, " : ", points[random.choice(np.where(grid)[0])]) #generate a random choice from the first element of grid if it has the points
    coordinate_list.append(points[random.choice(np.where(grid)[0])])


census_tract_code = []
county_code = []
for coordinate in coordinate_list:
    response = requests.get("https://geo.fcc.gov/api/census/area?lat=" + str(coordinate[1]) + "&lon=" + str(coordinate[0]) + "&format=json")
    json_str = response.text
    json_dict = json.loads(json_str)
    census_tract_code.append(json_dict["results"][0]["block_fips"][5:11])
    county_code.append(json_dict["results"][0]["block_fips"][2:5])

thisDict["Census_Tract_Code"] = census_tract_code
# print(census_tract_code)


response2 = requests.get("https://api.census.gov/data/2015/acs/acs5?get=NAME,B19013_001E&for=tract:*&in=state:26&in=county:*&key=603abf639ea36b11998d13a07bd2fd9672804616")
json_str2 = response2.text
income_total_list = json.loads(json_str2)
# print(json_dict2)



selected_results_list = []
for tract in census_tract_code:
    for result in income_total_list[1:]:
        if tract == result[4]:
            selected_results_list.append(result)

median_income_list = []
for county in county_code:
    for result in selected_results_list:
        if county == result[3] and int(result[1]) > 0:
            median_income_list.append(result[1])

# print(median_income_list)

thisDict["median_income"] = median_income_list


with open("thisDict.json", "w") as outfile:
    json.dump(thisDict, outfile)

with open("thisDict.json", "r") as json_file:
    data = json.load(json_file)

A_income = []
for i in range(len(data["Holc_Grade"])):
    if data["Holc_Grade"][i] == "A":
        A_income.append(int(data["median_income"][i]))

A_mean_income = statistics.mean(A_income)
A_median_income = statistics.median(A_income)
print("A_mean_income is {}.".format(A_mean_income))
print("A_median_income is {}.".format(A_median_income))

B_income = []
for i in range(len(data["Holc_Grade"])):
    if data["Holc_Grade"][i] == "B":
        B_income.append(int(data["median_income"][i]))

B_mean_income = statistics.mean(B_income)
B_median_income = statistics.median(B_income)
print("B_mean_income is {}.".format(B_mean_income))
print("B_median_income is {}.".format(B_median_income))

C_income = []
for i in range(len(data["Holc_Grade"])):
    if data["Holc_Grade"][i] == "C":
        C_income.append(int(data["median_income"][i]))

C_mean_income = statistics.mean(C_income)
C_median_income = statistics.median(C_income)
print("C_mean_income is {}.".format(C_mean_income))
print("C_median_income is {}.".format(C_median_income))

D_income = []
for i in range(len(data["Holc_Grade"])):
    if data["Holc_Grade"][i] == "D":
        D_income.append(int(data["median_income"][i]))

D_mean_income = statistics.mean(D_income)
D_median_income = statistics.median(D_income)
print("D_mean_income is {}.".format(D_mean_income))
print("D_median_income is {}.".format(D_median_income))