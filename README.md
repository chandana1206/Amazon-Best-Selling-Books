# Amazon-Best-Selling-Books

This project provides a comprehensive analysis of a dataset containing information on best-selling books. The dataset includes details such as book titles, authors, publication years, user ratings, prices, and genres. This repository includes code to clean, analyze, and export insights from the data, as well as additional visualizations to better understand book trends.

Dataset
The dataset (bestsellers.csv) includes the following columns:

Title: Title of the book
Author: Name of the author
Publication Year: Year of publication
Rating: User rating (on a scale of 1 to 5)
Price: Price of the book (in USD)
Genre: Genre of the book
Analysis Overview
The project performs the following key tasks:

Data Cleaning:
Removal of duplicate rows.
Renaming columns for readability.
Converting Price to a float datatype for analysis.
Descriptive Analysis:

Basic summary statistics on price, rating, and publication year.
Counts of books by author and average rating by genre.

Advanced Analysis:
Average price by genre and year.
Most common ratings.
Top 10 highest-rated books.
Most expensive books.
Authors with the highest-rated books.
Popular genres by year.

Data Export:
Results are exported to CSV files for further use:
top_authors.csv: Contains the top 10 most frequently published authors.
avg_rating_by_genre.csv: Average user rating by genre.
popular_genres_by_year.csv: Popular genres broken down by publication year.
top_rated_books.csv: Top 10 highest-rated books.
most_expensive_books.csv: Top 10 most expensive books.

Visualizations:
Visual representations of average prices and ratings by genre for better insights.
