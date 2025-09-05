cutoff_list= [
    ("Pilani", "CS",327),
    ("Pilani", "Chemical", 247),
    ("Pilani", "Msc. Eco", 271),
    ("Pilani", "Msc. Bio", 236),
    ("Goa", "CS", 301),
    ("Goa", "Chemical", 239),
    ("Goa", "Msc. Eco", 263),
    ("Goa", "Msc. Bio", 234),
    ("Hyderabad", "CS", 298),
    ("Hyderabad", "Chemical", 238),
    ("Hyderabad", "Msc. Eco", 261),
    ("Hyderabad", "Msc. Bio", 234),
]

cutoff_dict={}
for campus, branch, score in cutoff_list:
    cutoff_dict.setdefault(campus, {})[branch]=score
print(cutoff_dict)