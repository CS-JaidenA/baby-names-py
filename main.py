# BABY NAMES DATA ASSIGNMENT START CODE

import json


def main():
	# Load Baby Data from File
	file = open("baby-names-data.json")
	baby_data = json.load(file)
	file.close()

	# Main Menu
	loop = True
	while loop:
		selection = getMenuSelection()

		if selection == "1":
			displayAll(baby_data)
		elif selection == "2":
			searchGender(baby_data)
		elif selection == "3":
			searchRank(baby_data)
		elif selection == "4":
			searchStartLetter(baby_data)
		elif selection == "5":
			searchNameLength(baby_data)
		elif selection == "6":
			print("\nGOODBYE!\n")
			loop = False


def getMenuSelection():
	# Print Menu & Return User Selection
	print("\n*** BABY DATA - MAIN MENU ***")
	print("* 1: Display All")
	print("* 2: Search by Gender")
	print("* 3: Search by Rank")
	print("* 4: Search by Starting Letter")
	print("* 5: Search by Name Length")
	print("* 6: Exit")

	return input("* Enter Option #: ")


def display(baby):
	print(f"{baby['name']} (Rank: {baby['rank']}, Gender: {baby['gender']})")

def displayAll(baby_data):
	# Display All Baby Data
	print("\nDISPLAY ALL")

	for baby in baby_data:
		display(baby)


def searchGender(baby_data):
	# Dislay All Baby Names based on Gender
	print("\nSEARCH BY GENDER")

	gender = input("Enter a gender (Boy/Girl): ").capitalize()

	for baby in baby_data:
		if baby['gender'] == gender:
			display(baby)


def searchRank(baby_data):
	# Display All Baby Names based on Rank
	print("\nSEARCH BY RANK")

	min = int(input("Enter a minimum rank: "))
	max = int(input("Enter a maximum rank: "))

	count = 0

	for baby in baby_data:
		if baby['rank'] >= min and baby['rank'] <= max:
			count += 1
			display(baby)
	
	print(f"Number of names found: {count}")


def searchStartLetter(baby_data):
	# Insert User Item into a Position
	print("\nSEARCH BY START LETTER")

	count = 0
	letter = input("Enter a starting letter: ").capitalize()

	for baby in baby_data:
		if baby['name'].startswith(letter):
			count += 1
			display(baby)
	
	print(f"Number of names found: {count}")


def searchNameLength(baby_data):
	# Remove item from position
	print("\nSEARCH BY NAME LENGTH")

	count = 0
	length = int(input("Enter a name length: "))

	for baby in baby_data:
		if len(baby['name']) == length:
			count += 1
			display(baby)
	
	print(f"Number of names found: {count}")


# Invoke main to begin program
main()
