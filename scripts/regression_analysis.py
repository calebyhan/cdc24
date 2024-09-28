import json
import pandas as pd
import altair as alt

with open("../data/restaurant_distances_cleaned.txt", "r") as f:
    distances = json.load(f)

with open("../data/london_restaurants_cleaned.txt", "r") as f:
    data = json.load(f)

polarities = [data[i][0] for i in range(len(data))]
num_reviews = [data[i][1] for i in range(len(data))]

# Create a DataFrame
df = pd.DataFrame({
    'Distance': distances,
    'Polarity': polarities,
    'NumReviews': num_reviews
})

# Create heatmap for Distance vs Polarity
heatmap_polarity = alt.Chart(df).mark_rect().encode(
    x=alt.X('Distance:Q', bin=alt.Bin(maxbins=50)),
    y=alt.Y('Polarity:Q', bin=alt.Bin(maxbins=50)),
    color=alt.Color('count():Q', scale=alt.Scale(scheme='inferno'))
).properties(
    title='Distance to closest metro station vs Average review polarity'
)

# Create heatmap for Distance vs Number of Reviews
heatmap_reviews = alt.Chart(df).mark_rect().encode(
    x=alt.X('Distance:Q', bin=alt.Bin(maxbins=50)),
    y=alt.Y('NumReviews:Q', bin=alt.Bin(maxbins=50)),
    color=alt.Color('count():Q', scale=alt.Scale(scheme='inferno'))
).properties(
    title='Distance to closest metro station vs Number of reviews'
)

# Display the charts
heatmap_polarity.save('heatmap_polarity.html')
heatmap_reviews.save('heatmap_reviews.html')
