skill = {"python", "Git", "Python"} # duplicates are removed automatically
print(skill)

required = {"python", "SQL"} # Operation
common = skill & required #intersection
print(common)

frozen = frozenset(skill) # immutable set
print(frozen)

#Try all Operations. Using frozen set try loop
# - Sets automatically remove duplicates → "Python" and "python" are treated differently because of case sensitivity. & gives the intersection.- frozenset makes the set immutable (you can’t add/remove elements).

print("Looping through frozen set:")
for item in frozen:
    print("-", item)
