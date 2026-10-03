name = input("Enter name: ")
club = input("Enter club name: ")
year = 2026

print(type(name))
print(type(club))
print(type(year))

club_code = club[0:3].upper()
year_str = str(year)
badge_id = club_code + year_str

print("--- MEMBER BADGE ---")
print("Name: " + name)
print("Club: " + club)
print("Badge ID: " + badge_id)