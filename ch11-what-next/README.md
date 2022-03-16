# What Next

* Trees
  * B-trees
  * Red-black trees
  * Heaps
  * Splay trees
* Inverted Indexes
  * In a simplified way, this is how search engines work.
* Fourier Transforms
  * A brilliant, elegant algorithm with millions of use cases.
  * Analogy:
    * Given a smoothie, the fourier transform will tell you the ingredients. Put another way, given a song it will separate it into different frequencies.
  * This has lots of use cases, e.g. for music you can boost freqencies you care about (bass), lower the ones you don't (treble)
* Parallel algorithms
  * The best you can do with a sorting algorithm is roughtly `O(n log n)`, it is well known you can't sort an array in `O(n)` time. **Unless you use a parallel algorithm, e.g. there is a quicksort variant for O(n) time.**
  * These are very difficult to design for many reasons
    * Overhead of managing the parallelism, split in half then merge? This still takes time to merge.
    * Load balancing - split 10 tasks in a 5-5 way. One CPU gets all the simple computations whilst the other gets all the hard ones, one core sits waiting idle for 10 minutes?
  * MapReduce is a parallel algorithm! It is a distributed algorithm, built up from the idea of a `map` and `reduce` function.
    * `map` function takes an array and applies the function to each item in the array.
    * `reduce` function will reduce an array down to a single item. E.g. you might sum all of the elements to a single value.
* Bloom filters and HyperLogLog
  * bloom filter = probabilistic data structure. Gives an answer which could be wrong, but is probably right. They take up very little space.
  * HyperLogLog approximates the number of unique items in a absolutely massive data sets. It won't be exact, but it'll come very close whilst only using a fraction of the memory that it would take to get the exact answer.
* SHA algorithms
  * Compare files
  * Check passwords
  * Diffe-Hellman key exchange
* Linear programming
  * Maximise something, given particular constraints.
  * The graph algorithms in this book can also be done through linear programming!
  * Simplex algorithm is part of linear programming.