# Import the necessary libraries
import os
import json
import hashlib

parsed = "data/parsed"
summary = "data.summary.json"


def calculate_checksum(text):
	return hashlib.md5(text.encode("utf-8")).hexdigest()

def main():
	summary1 = {}

	for file in os.listdir(parsed):
		if file.endswith(".json"):
			path = os.path.join(parsed, file)

			with open(path, "r", encoding="utf-8") as f1:
				data = json.load(f1)

			agency = data["agency"]
			word_count = data["word_count"]

			# Create or update cummary data for the agency
			if agency not in summary1:
				summary1[agency] = {
					"total_words": 0,
					"titles": [],
				}

			summary1[agency]["total_words"] += word_count
			summary1[agency]["titles"].append(data["title"])

	for agency, data in summary1.items():
		total_titles = len(data["titles"])
		data["average_words"] = data["total_words"] / total_titles if total_titles > 0 else 0


	# Save to summary.json
	with open(summary, "w", encoding="utf-8") as f1:
		json.dump(summary1, f1, indent=2)

	print(f"Summary saved to {summary}")