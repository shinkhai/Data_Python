# Text manipulation
![](https://images.unsplash.com/photo-1528817587692-6baf815de178?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=08167240cdb7dbc95397fe6338aed518&auto=format&fit=crop&w=1000&q=80)

## Objectives
* Understand how powerful list comprehensions are
* Get a glimpse at text processing

## Guidelines
In this exercice, you'll write a program that process some text data. Open
`src/text_processing.py`.


### 1. Split the sentence into words (tokens)
That's a common operation when working with text data, we transform sentences
into list of words. Call `tokens` the result of your work and print it out.

### 2. Lowercase each token
Now, using a list comprehension and `tokens`, you need to return the list with
all values of `tokens` lowercased.
Name your result `lowercase_tokens` and print it out.

### 3. Removing stopwords
Often when working with text data, we encouter very common words with little to no semantic meaning ; words like `the`, `a`, `is`. These are very common words with little to no semantic meaning, and are called [stop words](https://en.wikipedia.org/wiki/Stop_words), and often when doing text analysis we want to remove them. You're given such stop words in `STOPWORDS` (can you tell why it's written in all caps?), and your goal is to remove all those stop words from `lowercase_tokens`, call `no_stops` your result.

_Since you're here, can you tell what is the type of `STOPWORDS`?_
