# JSON objects in Python are formatted strings
# We can create JSON strings from dicts, and we can also create dicts from strings containing json.
import json

jsonString = '{ "firstName":  "Clark", "lastName": "Kent"}'
print(f"Our json is {jsonString} with type {type(jsonString)}")

# To use this in the same way we would use a dictionary, we need to convert it.
jsonDict = json.loads(jsonString)

# Test the dictionary
print(f"The type of jsonDict is {type(jsonDict)}")
print(f"Our superhero name is {jsonDict['firstName']} {jsonDict['lastName']}")
# Add a new key
jsonDict['age'] = '201'

# Dump to a new JSON string - with indent for pretty printing
newJsonString = json.dumps(jsonDict, indent=4)
print(f"Our new json is {newJsonString} with type {type(newJsonString)}")

