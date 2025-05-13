# Import the necessary directories
import os
import json

parsed_directory = "data/parsed"
data_summary = []

for file in os.listdir(parsed_directory):
	with open(os.path.join(parsed_directory, file), "r") as f1:
		data = json.load(f1)
		data_summary.append(data)

# Save the analysis summary
with open("data/summary.json", "w") as out:
	json.dump(data_summary, out, indent=2)