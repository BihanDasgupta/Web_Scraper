import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# Load scraped data
df = pd.read_csv("news_headlines.csv")

# Split and count words
word_list = " ".join(df["Headline"]).split()
word_counts = Counter(word_list)

# Get 10 most common words
common_words = word_counts.most_common(10)

# Convert to DataFrame for visualization
word_df = pd.DataFrame(common_words, columns=["Word", "Frequency"])

# Plot the data
plt.figure(figsize=(10, 6))
plt.bar(word_df["Word"], word_df["Frequency"], color="skyblue")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top 10 Common Words in Headlines")
plt.xticks(rotation=45)
plt.show()

