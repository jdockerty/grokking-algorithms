# Exercises

**10.1**

    In the Netflix example, you calculated the distance between two different users using the distance formula. But not all users rate movies the same way. Suppose you have two users, Yogi and Pinky, who have the same taste in movies. But Yogi rates any movie he likes as a 5, whereas Pinky is choosier and reserves the 5s for only the best. They’re well matched, but according to the distance algorithm, they aren’t neighbors. How would you take their different rating strategies into account?

Using a weighted strategy. In this case, Pinky's 5 is going to have a much greater impact than Yogi's, since he gives them for everything he likes. E.g. Yogi's 5 might be similar to the average users 3. *This is called normalisation.*

*Later in the chapter there is a mention of cosine similarity, instead of measuring the distance as a vector. We measure the difference of the angles of the two vectors, this is much better at dealing with nuances, like those presented above.*

**10.2**

    Suppose Netflix nominates a group of “influencers.” For example, Quentin Tarantino and Wes Anderson are influencers on Netflix, so their ratings count for more than a normal user’s. How would you change the recommendations system so it’s biased toward the ratings of influencers?

Similar to above, their ratings are worth more. You could do this with something along the lines of Anderson's ratings are much greater impact, e.g. as though he was 100 users.

**10.3**

    Netflix has millions of users. The earlier example looked at the five closest neighbors for building the recommendations system. Is this too low? Too high?

Too low, there will be a huge amount of variance with such a small number. Using more will likely be more accurate.

*The rule of thumb is if you have N users, you should look at sqrt(N) neighbours.*