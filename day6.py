'''
Profile = {"name" : "Srini", "Age" : 25, "city" : "Chennai"}

#print(Profile['Age'])

Profile["Skill"] = "AI"
print(Profile)

Profile["Age"] += 1

print(Profile)
'''

# Initial profile
def print_profile(profile) :
    print("===== Profile Card =====")
    for key, value in profile.items():
    #print(f"{key}:{value}")
      print(f"{key.title():<10} : {value}")

    print("========================")
  

# Add initial profile
Profile = {"name": "Srini", "Age": 25, "city": "Chennai", "Skill": "AI"}
# Print single profile
print_profile(Profile) 

# List to store multiple profiles
profiles = []

#add initial profile
profiles.append(Profile)

# to Add more profiles dynamically
profiles.append({"name": "Naveena", "Age": 30, "city": "Bangalore", "Skill": "Product Management"})
profiles.append({"name": "Arun", "Age": 28, "city": "Hyderabad", "Skill": "Data Science"})

# Print all profiles
for p in profiles:
    print_profile(p)




'''# Add a skill
Profile["Skill"] = "AI"'''

'''# Increment age
Profile["Age"] += 1
print("After Age Update:", Profile)

# Dynamically change the name
new_name = input("Enter a new name for the profile: ")
if new_name.isalpha():
    Profile["name"] = new_name
    print("Updated Profile:", Profile)
else:
    print("Invalid name! Profile name must contain only letters.")
'''
# There was an issue on this code , unable to pront profile card for other 2 names, issue found via Copilot 
#Inside your print_profile(profile) function, you’re looping over Profile.items() instead of the function argument profile.items(). That means the function always prints the global Profile dictionary, not whichever profile you pass in.

#Tip: Always use the function parameter (profile) inside your function, not the global variable (Profile). That way, the function works for any dictionary you pass in.
