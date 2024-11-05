import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('bestsellers.csv')

# first 5 rows
print(df.head())

print('-------------------------------------------')
print()

# shape and size of the data
print(df.shape)
print(df.size)

print('-------------------------------------------')
print()

# column names
print(df.columns)

print('-------------------------------------------')
print()

# summary stats of each columns
print(df.describe())

print('-------------------------------------------')
print()

# drop duplicate rows
df.drop_duplicates(inplace=True)

# rename columns
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)

# change datatype of price to float
df["Price"] = df["Price"].astype(float)

# author counts
author_counts = df['Author'].value_counts()
print(author_counts)

print('-------------------------------------------')
print()

# group avg rating by genres 
avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)

print('-------------------------------------------')
print()

# Average price by genre
avg_price_by_genre = df.groupby("Genre")["Price"].mean()
print(avg_price_by_genre)

print('-------------------------------------------')
print()

# Average price over time
avg_price_by_year = df.groupby("Publication Year")["Price"].mean()
print(avg_price_by_year)

print('-------------------------------------------')
print()

# Most common ratings
rating_counts = df["Rating"].value_counts()
print(rating_counts)

print('-------------------------------------------')
print()

# Top 10 highest-rated books
top_rated_books = df.sort_values("Rating", ascending=False).head(10)
print(top_rated_books[["Title", "Author", "Rating"]])

print('-------------------------------------------')
print()

# Top 10 most expensive books
top_expensive_books = df.sort_values("Price", ascending=False).head(10)
print(top_expensive_books[["Title", "Author", "Price"]])

print('-------------------------------------------')
print()

# Authors with high-rated books (rating > 4.5)
high_rated_books = df[df["Rating"] > 4.5]
top_authors_high_rated = high_rated_books["Author"].value_counts()
print(top_authors_high_rated)

print('-------------------------------------------')
print()

# Count of genres by publication year
genre_counts_by_year = df.groupby(["Publication Year", "Genre"]).size().unstack()
print(genre_counts_by_year)

print('-------------------------------------------')
print()

# Average price by genre plot
plt.figure(figsize=(10, 6))
sns.barplot(x=avg_price_by_genre.index, y=avg_price_by_genre.values)
plt.title("Average Price by Genre")
plt.ylabel("Average Price")
plt.xlabel("Genre")
plt.show()

# Average rating by genre plot
plt.figure(figsize=(10, 6))
sns.barplot(x=avg_rating_by_genre.index, y=avg_rating_by_genre.values)
plt.title("Average Rating by Genre")
plt.ylabel("Average Rating")
plt.xlabel("Genre")
plt.show()

# Export popular genres by year
genre_counts_by_year.to_csv("popular_genres_by_year.csv")

# Export top-rated books
top_rated_books.to_csv("top_rated_books.csv", index=False)

# Export most expensive books
top_expensive_books.to_csv("most_expensive_books.csv", index=False)

# Export top selling authors to a CSV file
author_counts.head(10).to_csv("top_authors.csv")

# Export average rating by genre to a CSV file
avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")
