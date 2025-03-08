# Movie Recommendation System

This project recommends movies to users based on their preferences using the **MovieLens dataset**. It uses **collaborative filtering** and **content-based filtering** techniques.

---

## Table of Contents
1. [Overview](#overview)
2. [Dataset](#dataset)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Results](#results)
7. [Contributing](#contributing)
8. [License](#license)

---

## Overview

A **Movie Recommendation System** suggests movies to users based on their past behavior or similarities between movies. In this project, we:
- Use **collaborative filtering** to recommend movies based on user ratings.
- Use **content-based filtering** to recommend movies based on genres.
- Evaluate the performance of the recommendation system.

---

## Dataset

The dataset used is the [MovieLens dataset](https://grouplens.org/datasets/movielens/), which contains:
- **Movies**: Movie titles and genres.
- **Ratings**: User ratings for movies.
- **Tags**: User-generated tags for movies.

---

## Project Structure

The project is organized as follows:
movie_recommendation/
│
├── data/
│ └── movies.csv # Movie metadata
│ └── ratings.csv # User ratings
├── models/
│ └── user_item_matrix.pkl # User-item matrix
│ └── user_similarity.pkl # User similarity matrix
├── scripts/
│ └── movie_recommendation.py # Python script for the project
├── README.md # Project documentation
└── requirements.txt # List of dependencies

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/benny-daniel6/Movie_recommendation.git
   cd Movie_recommendation
2. Install the required dependencies:
   pip install -r requirements.txt
3. Download the dataset:
Download the MovieLens dataset.
Place the movies.csv and ratings.csv files in the data/ folder.

## Usage
Running the Script
To train the model and get movie recommendations, run the Python script:
python scripts/movie_recommendation.py
What the Script Does:
1. Loads the dataset from data/movies.csv and data/ratings.csv.
2. Preprocesses the data:
Creates a user-item matrix.
Computes user similarity using cosine similarity.
3. Recommends movies based on user similarity (collaborative filtering).
4. Recommends movies based on genres (content-based filtering).
5. Saves the user-item matrix and user similarity to the models/ folder.

## Results
Collaborative Filtering:
Top 5 Recommendations: The top 5 movies recommended for a user based on similar users' preferences.

Content-Based Filtering:
Top 10 Recommendations: The top 10 movies recommended based on genres.

## Contributing
Contributions are welcome! If you'd like to contribute:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/YourFeature).
3. Commit your changes (git commit -m 'Add some feature').
4. Push to the branch (git push origin feature/YourFeature).
5. Open a pull request.

## License
This project is licensed under the MIT [License]. See the LICENSE file for details.