import pypopulation as p
import json

# print(p.get_population_a2("MU"))

# Open JSON File
with open('log.json') as f:
    data_dict = json.load(f)

collection_str = json.dumps(data_dict)
collection_json = json.loads(collection_str)

for collection in collection_json:
    # print(collection_json[collection])
    # Update JSON Object with Population Value retrieved from pypolulation
    collection_json[collection]['Population'] = p.get_population_a2(collection_json[collection]['CountryCode'])

# Print Updated JSON Collection
# for collection in collection_json:
#     print(collection_json[collection])

# Update JSON File with latest Population Figures
with open("log.json", "w") as jsonFile:
    json.dump(collection_json, jsonFile)
    jsonFile.close()
