# download ecfr_data.py

# At the beginning, import os  
import os
import requests

# Store the files in a directory
raw_directory = "data/raw"
os.makedirs(raw_directory, exist_ok=True)

# Loop through each of the titles (these are the sections in the CEFR)
for title in range(1, 51):
	url = f"https://www.ecfr.gov/current/title-{title}"
	file_path = os.path.join(raw_directory, f"title_{title}.html")

	print(f"Downloading title {title} from {url}...")

	# Use exception handling for getting each of the files
	try:
		# Here, we are attempting to download the HTML file. 
		response = requests.get(url)
		
		# Was the download successful? 
		if response.status_code == 200:
			# Write the downloaded content to a local file 
			with open(file_path, "wb") as file:
				file.write(response.content)
			print(f"Title {title} was successfully downloaded")
		else:
			print(f"Title {title} was not found (Status: {response.status_code})")
		

	except Exception as e:
		# Handle any unexpected errors
		print(f"Error downloading Title {title}: {e}") 