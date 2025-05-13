# Import the necessary libraries
from bs4 import BeautifulSoup
import os
import json
import hashlib

raw_dir = "data/raw"
parsed_dir = "data/parsed"
os.makedirs(raw_dir, exist_ok=True)
os.makedirs(parsed_dir, exist_ok=True)

def extract_text_from_html(html):
	soup = BeautifulSoup(html, "html.parser")
	text = soup.get_text(separator = " ", strip=True)
	return text

for filename in os.listdir(raw_dir):
	if filename.endswith(".html") or filename.endswith(".xml"):
		filepath = os.path.join(raw_dir, filename)

		with open(filepath, "r", encoding="utf-8") as f:
			html_content = f.read()

		title = filename.split("_")[1].split(".")[0]

		text_content = extract_text_from_html(html_content)
		word_count = len(text_content.split())
		agency_name = f"Agency Title {title}"
		checksum = hashlib.md5(text_content.encode("utf-8")).hexdigest()

		parsed_data = {
			"title": title, 
			"agency": agency_name,
			"word_count": word_count,
			"checksum": checksum,
		}

		output_path = os.path.join(parsed_dir, f"title_{title}.json")
		with open(output_path, "w", encoding="utf-8") as out:
			json.dump(parsed_data, out, indent=2)

		print(f"Parsed Title {title} -> {output_path}")