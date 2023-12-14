import json,re,editdistance
from collections import defaultdict

Actual_derived_col= ['revisionDate', 'classId', 'discipline', 'closest3D', 'latestChangeDateSubq', 'documentStatusDescription', 'externalLink', 'isActive', 'dataStore', 'publishFile', 'isLive', 'desc', 'k2Handle', 'title', 'processUnitCode', 'documentType', 'isCheckedOut', 'safetyCritical', 'isLatest', 'disciplineDescription', 'plantCode', 'documentStatusCode', 'revisionFileName', 'documentTypeDescription', 'revision', 'class', 'description', 'floc', 'project']

#edit distance algorithm
def match_words_with_edit_distance(input, actual):
    # Calculate the Levenshtein distance between the lowercase versions of the words
    distance = editdistance.eval(input, actual)
    threshold = len(input) - len(actual)

    # Check if the distance is below the threshold
    if distance <= threshold:
        if threshold == distance:
         return True
        else:
          if input.find(actual) != -1:
            return True
          else :
            return False
    else:
        return False

file_name = 'InputAttributes.json'

Matching_Result = defaultdict(list)
with open(file_name, 'r') as file:
    json_data = json.load(file)

# Convert JSON data to a string
json_string = json.dumps(json_data, indent=2)
#change regex according to input.json
id_pattern = re.compile(r'"(\w[^"]+)":',re.DOTALL)
id_matches = id_pattern.findall(json_string)
input_string = list(set(id_matches))

for i in range(len(input_string)):
  for j in range(len(Actual_derived_col)):
    result = match_words_with_edit_distance(input_string[i].lower(), Actual_derived_col[j].lower())
    if result:
      Matching_Result[Actual_derived_col[j]].append(input_string[i])

print("######")
print("Atrributes Extracted from input\n")
print(input_string)
print("#######")
print("Actual Deried Property\n")
print(Actual_derived_col)

print("\nResult Dictionary\n")
print(Matching_Result)

