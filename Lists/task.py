states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[-1])  # This will give the last in the list
print(states_of_america[0])   # This will give the first in the list. index 0

states_of_america[4] = "Connecticutus"    # We can also modify any item in the list.

states_of_america.append("Jaguar")   # To add item to the end of the list
states_of_america.extend(["Femuye", "Gudular", "Zeduof"])    # To add a bunch of items to the list

print(states_of_america)