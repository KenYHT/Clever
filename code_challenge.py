import requests

def main():
	# Get data on all the sections available.
	r = requests.get('https://api.clever.com/v1.1/sections', headers={'Authorization':'Bearer DEMO_TOKEN'})
	sections = r.json()["data"]
	num_sections = r.json()["paging"]["count"]
	num_students = reduce(lambda x, y: len(x["data"]["students"]) + y, sections)
	# Sum the number of students per section
	for section in sections:
		num_students += len(section["data"]["students"])
	print num_students / num_sections
	

if __name__ == '__main__':
	main()