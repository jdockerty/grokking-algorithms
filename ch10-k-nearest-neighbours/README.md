# K-Nearest Neighbours

- [K-Nearest Neighbours](#k-nearest-neighbours)
  - [Classifying Oranges vs Grapefruit](#classifying-oranges-vs-grapefruit)
  - [Building Recommendation Systems](#building-recommendation-systems)
    - [Regression](#regression)
  - [Picking good features](#picking-good-features)
  - [Introduction to Machine Learning](#introduction-to-machine-learning)
  - [Optical Character Recognition (OCR)](#optical-character-recognition-ocr)
  - [Building a spam filter](#building-a-spam-filter)
- [Recap](#recap)

## Classifying Oranges vs Grapefruit

How do you know whether something is an orange or a grapefruit?

In your mind it might play out with a chart, if something is, well, orange, then it's probably an orange. The more items you have you'd classify as orange, you can say that these are definitely oranges.

What if you have an item which comes in the middle, you might look at how many of its neighbours in a chart are oranges and how many are grapefruits. If you have more oranges, then its an orange. This is the K-nearest neighbour (KNN) algorithm for classification.

This algorithm is simple, but very useful too. If you are trying to classify something, you will probably want to try KNN first.

## Building Recommendation Systems

This provides us with a more real-world example for the use of a KNN algorithm.

Suppose that you are Netflix and you want to build a movie recommendation system for your users. This is quite similar to our problem that was described above, in a very high level way. We could plot users on a graph, by similarity on taste for movies, if you want to recommend a movie to someone you take the movies that their nearest neighbours like and recommend it - since they have similar tastes, they should probably like that movie too!

The big piece missing here is to find out how the users are similar, this is known as *feature extraction*. We could do this through the sign-up process, when someone signs up for our service, we ask them to rate categories of movies that they like from 1 to 5, these are used to base their data on. Now we have a set of ratings for a user when they sign up, which can use to plot a graph with other users too.

When you have the data plotted on a graph, you are simply looking at which are the other closest data points.

### Regression

Suppose we not only want to recommend movies, but also guess how someone will rate it, i.e. Tom Cruise. You could do this by checking how an arbitrary number of people who are closest to Tom Cruise's taste in movies also rated the movie that is being recommended - this will give us an idea on how he would rate it too, since he is similar to those people. Then, we might take an average of those ratings, this is called *regression*.

**The KNN algorithm is made up of classification and regression.**

* Classification = categorise into groups
* Regression = predicting a response

## Picking good features

When working with KNN, it is very important to pick the right features to compare against.

This means:

* Features that directly relate to something you're trying to find out. In this case you might want to be recommending a movie, don't ask people say whether a picture is a cat or a dog, it has nothing to do with movie recommendations!
* Features should not have bias, i.e. do not rate someone's entire taste in movies by only asking them to rate the *Toy Story* triology, get a broad range of movies to go from. 

## Introduction to Machine Learning

KNN is super useful and is an intro to ML.

## Optical Character Recognition (OCR)

We can take a photo of a page of text and the computer is going to automatically read the text for us.

Google uses OCR to digitise books. How does OCR work?

Consider using a number, such as `7`. How would you figure out, being shown a picture of the number 7, that is indeed the number 7. We can KNN:

* Go through a lot of images of numbers, extract features from those numbers.
* When you get a new image, extract the features for the image, and see what its nearest neighbours are.

Generally speaking, OCR algorithms will use lines, points, and curves of a character or number as the features it extracts. When it gets a new one, it'll extract those same features. OCR is a lot more complicated here than in our previous examples, but it still important to understand that even complex technology like this builds upon KNN.

The first step for going through the images of text/numbers to extract features is called *training*. Most ML algorithms will have a training stage. Before the computer can do the task, it must be trained to do it.

## Building a spam filter

Spam filters use a simple algorithm called *Naive Bayes classifier*.

First, we train the algorithm on some data: spam or not spam. Then, once we get some more emails in, we can break up the text into words and check how likely the words are to appear in spam emails from our trained algorithm. E.g. "collect your £10 million now!", maybe in our training the word *million* only showed up in spam emails, so *Naive Bayes classifier* would tag this as spam.

# Recap

* KNN is used for classification and regression, it involves looking at k-nearest neighbours.
* Feature extraction is converting an item (e.g. a user or picture) into a list of numbers to be compared.
* Getting good features is a really important part of a successful KNN algorithm.