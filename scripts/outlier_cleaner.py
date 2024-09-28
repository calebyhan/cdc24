import json

TYPE_TRANSPORT = "bus"

with open("../data/london_restaurants.txt", "r") as f:
    polarities = json.load(f)

cleaned = []
new_polarities = []

for i in range(len(polarities)):
    if polarities[i][1] > 85:
        cleaned.append(i)
    else:
        new_polarities.append(polarities[i])

with open("../data/london_restaurants_cleaned.txt", "w") as f:
    f.write(str(new_polarities))

new_distances = []

if TYPE_TRANSPORT == "metro":
    with open("../data/restaurant_distances_metro.txt", "r") as f:
        distances = json.load(f)

    for i in range(len(distances)):
        if i in cleaned:
            continue
        else:
            new_distances.append(distances[i])

    with open("../data/restaurant_distances_metro_cleaned.txt", "w") as f:
        f.write(str(new_distances))
else:
    with open("../data/restaurant_distances_bus.txt", "r") as f:
        distances = json.load(f)

    for i in range(len(distances)):
        if i in cleaned:
            continue
        else:
            new_distances.append(distances[i])

    with open("../data/restaurant_distances_bus_cleaned.txt", "w") as f:
        f.write(str(new_distances))
