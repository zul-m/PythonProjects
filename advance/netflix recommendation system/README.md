## Netflix Recommendation System

Netflix is a subscription-based streaming platform that allows users to watch movies and TV shows without advertisements. One of the reasons behind the popularity of Netflix is its recommendation system. It recommends movies and TV shows based on the user’s interest. If you want to learn how to create a Netflix recommendation system, this project is for you.

### How Netflix Recommendation System Works

The recommendation system of Netflix shows you movies and TV shows according to your interests. Netflix has a lot of data because of its user base. Its recommendation system predicts a personalised catalogue for you based on factors like:
 1. your viewing history
 2. the viewing history of other users with similar tastes and preferences as yours
 3. genres, category, description, and more information about the content that you watched in the past

The genre of the content is one of the most valuable factors that helps Netflix recommend more content even to new users.

### Netflix Recommendation System using Python

The dataset I am using to build a Netflix recommendation system using Python is downloaded from Kaggle. The dataset contains information about all the movies and TV shows on Netflix as of 2021. **You can download the dataset from [here](https://www.kaggle.com/datasets/satpreetmakhija/netflix-movies-and-tv-shows-2021)**.

In the first impressions on the dataset, I can see that the Title column needs preparation as it contains `#` before the name of the movies or tv shows. The dataset also contains null values. Before removing the null values, we select the columns that we can use to build a Netflix recommendation system.

As the name suggests:
 1. The title column contains the titles of movies and TV shows on Netflix
 2. Description column describes the plot of the TV shows and movies
 3. The Content Type column tells us if it’s a movie or a TV show
 4. The Genre column contains all the genres of the TV show or the movie

We clean the Title column as it contains some data preparation. Then, we use the Genres column as the feature to recommend similar content to the user. I'm using the concept of cosine similarity here. Then we set the Title column as an index so that we can find similar content by giving the title of the movie or TV show as an input. Finally, we write a function to recommend Movies and TV shows on Netflix.

### Output

```
                                Show Id                          Title  ... Content Type         Date Added
0  cc1b6ed9-cf9e-4057-8303-34577fb54477                       (Un)Well  ...      TV Show                NaN
1  e2ef4e91-fb25-42ab-b485-be8e3b23dedb                         #Alive  ...        Movie  September 8, 2020
2  b01b73b7-81f6-47a7-86d8-acb63080d525  #AnneFrank - Parallel Stories  ...        Movie       July 1, 2020
3  b6611af0-f53c-4a08-9ffa-9716dc57eb9c                       #blackAF  ...      TV Show                NaN
4  7f2d4170-bab8-4d75-adc2-197f7124c070               #cats_the_mewvie  ...        Movie   February 5, 2020

[5 rows x 13 columns]
Show Id                  0
Title                    0
Description              0
Director              2064
Genres                   0
Cast                   530
Production Country     559
Release Date             3
Rating                   4
Duration                 3
Imdb Score             608
Content Type             0
Date Added            1335
dtype: int64
                           Title  ...                                          Genres
0                       (Un)Well  ...                                      Reality TV
1                         #Alive  ...  Horror Movies, International Movies, Thrillers
2  #AnneFrank - Parallel Stories  ...             Documentaries, International Movies
3                       #blackAF  ...                                     TV Comedies
4               #cats_the_mewvie  ...             Documentaries, International Movies

[5 rows x 4 columns]
[nltk_data] Downloading package stopwords to
[nltk_data]     
[nltk_data]   Package stopwords is already up-to-date!
3297             octopus teacher
5944                 zig  sharko
5923                         son
2123               hot girl want
664                  bike border
5307                       wiggl
1789                 gerald game
5354                        even
3906    remast two kill sam cook
2570           kocan kadar konus
Name: Title, dtype: object
395       apach life carlo tevez
396                        apach
1052                cocain coast
1131           crime diari night
1132          crime diari candid
1193                  dark desir
1403    drug squad costa del sol
1456                   el cartel
1457                  el cartel
1462              el desconocido
Name: Title, dtype: object
```

### Summary

The recommendation system of Netflix predicts a personalised catalogue for you based on factors like your viewing history, the viewing history of other users with similar tastes and preferences, and the genres, category, descriptions, and more information of the content you watched.