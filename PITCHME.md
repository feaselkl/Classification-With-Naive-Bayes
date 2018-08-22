<style>
.reveal section img { background:none; border:none; box-shadow:none; }
</style>

## Classification with Naive Bayes

<a href="http://www.catallaxyservices.com">Kevin Feasel</a> (<a href="https://twitter.com/feaselkl">@feaselkl</a>)
<a href="http://csmore.info/on/naivebayes">http://CSmore.info/on/naivebayes</a>

---

@title[Who Am I?]

@snap[west splitscreen]
<table>
	<tr>
		<td><a href="https://csmore.info"><img src="https://www.catallaxyservices.com/media/Logo.png" height="133" width="119" /></a></td>
		<td><a href="https://csmore.info">Catallaxy Services</a></td>
	</tr>
	<tr>
		<td><a href="https://curatedsql.com"><img src="https://www.catallaxyservices.com/media/CuratedSQLLogo.png" height="133" width="119" /></a></td>
		<td><a href="https://curatedsql.com">Curated SQL</a></td>
	</tr>
	<tr>
		<td><a href="https://wespeaklinux.com"><img src="https://www.catallaxyservices.com/media/WeSpeakLinux.jpg" height="133" width="119" /></a></td>
		<td><a href="https://wespeaklinux.com">We Speak Linux</a></td>
	</tr>
</table>
@snapend

@snap[east splitscreen]
<div>
	<a href="http://www.twitter.com/feaselkl"><img src="https://www.catallaxyservices.com/media/HeadShot.jpg" height="358" width="315" /></a>
	<br />
	<a href="http://www.twitter.com/feaselkl">@feaselkl</a>
</div>
@snapend

---

### What Is Naive Bayes?

Naive Bayes is not an algorithm; it is a **class** of algorithms.  Naive Bayes is very easy to understand and reasonably accurate, making it a great class of algorithms to use when starting a classification project.

---

### Naive Bayes Characteristics

Naive Bayes algorithms follow the general form:
* Probabilistic -- calculate probabilities of each output category and choose the best one
* Probabilities derived from Bayes' Theorem
* Features are independent (hence the "naive" approach)

---

### Motivation

Today's talk will show how the Naive Bayes class of algorithms works, solve for a simplied form, and then use R packages to solve larger-scale problems.

There are several forms of Naive Bayes algorithms that we will not discuss, but they can be quite useful under certain circumstances.

---

@title[Solving Naive Bayes]

## Agenda
1. **Solving Naive Bayes**
2. Solving By Hand -- Features
3. Solving By Hand -- Natural Language
4. R -- Features
5. R -- Natural Language

---

### Bayes' Theorem

The formulation of Bayes' Theorem we will use is:

`$P(B|A) = \dfrac{P(A|B) * P(B)}{P(A)}$`

* P(B|A) [aka, the posterior probability] is the probability of hypothesis B given data A.
* P(A|B) is the probability of data A assuming that hypothesis B is true.
* P(B) [aka, the prior probability] is the likelihood of hypothesis B being true regardless of data.
* P(A) is the probability of seeing data A.

---

### Applying Bayes' Theorem

Supposing multiple inputs, we can combine them together like so:

`$P(B|A) = \dfrac{P(x_1|B) * P(x_2|B) * ... * P(x_n|B)}{P(A)}$`

This is because we assume that the inputs are **independent** from one another.

Given `$B_1, B_2, ..., B_N$` as possible classes, we want to find the `$B_i$` with the highest probability.

---

@title[Solving By Hand -- Features]

## Agenda
1. Solving Naive Bayes
2. **Solving By Hand -- Features**
3. Solving By Hand -- Natural Language
4. R -- Features
5. R -- Natural Language

---

@title[Shall We Golf?]

|Row|Outlook|Temp|Humidity|Windy|Golf?|
|---|-------|----|--------|-----|-----|
|0|Rainy|Hot|High|False|No|
|1|Rainy|Hot|High|True|No|
|2|Overcast|Hot|High|False|Yes|
|3|Sunny|Mild|High|False|Yes|
|4|Sunny|Cool|Normal|False|Yes|
|5|Sunny|Cool|Normal|True|No|
|6|Overcast|Cool|Normal|True|Yes|
|7|Rainy|Mild|High|False|No|

---

@title[Shall We Golf? (cotd)]

|Row|Outlook|Temp|Humidity|Windy|Golf?|
|---|-------|----|--------|-----|-----|
|8|Rainy|Cool|Normal|False|Yes|
|9|Sunny|Mild|Normal|False|Yes|
|10|Rainy|Mild|Normal|True|Yes|
|11|Overcast|Mild|High|True|Yes|
|12|Overcast|Hot|Normal|False|Yes|
|13|Sunny|Mild|High|True|No|

---

### Solving The Problem

Goal:  determine, based on input conditions, whether we should go play golf.

Steps:
1. Find the probability of playing golf (prior probability).
2. Find the probability of golfing given each variable:  Outlook, Temp, Humidity, Wind.
3. Plug values from new data into our formula.

---

### Prior Probability

|Golf?|Count|P(Yes)/P(No)|
|-----|-----|------------|
|Yes|9|9/14|
|No|5|5/14|
|Total|14|100%|

---

### Outlook

|Outlook|Yes|No|P(Yes)|P(No)|
|-------|---|--|------------|
|Sunny|2|3|2/9|3/5|
|Overcast|4|0|4/9|0/5|
|Rainy|3|2|3/9|2/5|
|Total|9|5|100%|100%|

---

### Temperature

|Temp|Yes|No|P(Yes)|P(No)|
|----|---|--|------------|
|Hot|2|2|2/9|2/5|
|Mild|4|2|4/9|2/5|
|Cool|3|1|3/9|1/5|
|Total|9|5|100%|100%|

---

### Humidity

|Humidity|Yes|No|P(Yes)|P(No)|
|--------|---|--|------------|
|High|3|4|3/9|4/5|
|Normal|6|1|6/9|1/5|
|Total|9|5|100%|100%|

---

### Windy

|Windy|Yes|No|P(Yes)|P(No)|
|-----|---|--|------------|
|False|6|2|6/9|2/5|
|True|3|3|3/9|3/5|
|Total|9|5|100%|100%|

---

### Testing A Day

Suppose today = ( Sunny, Hot, Normal, False ).  Let's compare the P(golf) versus P(no golf):

`$P(Y|t) = \dfrac{P(O_s|Y) \cdot P(T_h|Y) \cdot P(H_n|Y) \cdot P(W_f|Y) \cdot P(Y)}{P(t)}$`

`$P(N|t) = \dfrac{P(O_s|N) \cdot P(T_h|N) \cdot P(H_n|N) \cdot P(W_f|N) \cdot P(N)}{P(t)}$`

Note the common denominator:  because we're comparing P(Yes|today) versus P(No|today), the common denominator cancels out.

---

### Testing A Day

Putting this in numbers:

The probability of playing golf:
`$P(Yes|today) = \dfrac{2}{9} \cdot \dfrac{2}{9} \cdot \dfrac{6}{9} \cdot \dfrac{6}{9} \cdot \dfrac{9}{14} = 0.0141$`

The probability of not playing golf:
`$P(No|today) = \dfrac{3}{5} \cdot \dfrac{2}{5} \cdot \dfrac{1}{5} \cdot \dfrac{2}{5} \cdot \dfrac{5}{14} = 0.0068$`

Time to golf!

---

@title[Solving By Hand -- Natural Language]

## Agenda
1. Solving Naive Bayes
2. Solving By Hand -- Features
3. **Solving By Hand -- Natural Language**
4. R -- Features
5. R -- Natural Language

---

### Natural Language Sample

|Text|Tag|
|----|---|
|Stock prices fell|Business|
|Shares were up thirty percent|Business|
|Pitched out of a tough situation|Baseball|
|Bullish investors seized on the opportunity|Business|
|Threw a no hitter|Baseball|
|Runners on second and third with nobody out|Baseball|

---

### Test Text And Process

Our test text:  **Threw out the runner**

Goal:  determine, based on input conditions, whether we should categorize this as a baseball phrase or a business phrase.

1. Find the probability of a phrase being business or baseball (prior probability).
2. Find the probability of the words in the phrase being business or baseball.
3. Plug values from new data into our formula.

---

### Calculating Values

Calculating the prior probability is easy:  the count of "Baseball" categories versus the total number of 
phrases is the prior probability of selecting the Baseball category:  `$\dfrac{3}{6}$`, or 50%.  The same goes for Business.

So what are our features?  The answer is, **individual words**!

---

### Words

Calculate `$P(threw|Baseball)$` => count how many times "threw" appears in Baseball texts, divided by the number of words in Baseball texts.

The answer here is `$\dfrac{1}{18}$`.

---

### Missing Words

What about the word "the"?  It doesn't appear in any of the baseball texts, so it would have a result of `$\dfrac{0}{18}$`.

Because we multiply all of the word probabilities together, a single 0 leads us to a total probability of 0%. 
But you're liable to see new words, so this isn't a good solution.

---

### Laplace Smoothing

To fix the zero probability problem, we can apply Laplace smoothing:  add 1 to each count so it is never zero.  Then, add N (the number of unique words) to the denominator.

There are **29** unique words in the entire data set:
a and bullish fell hitter investors no nobody of on opportunity out percent pitched prices runners second seized shares situation stock the third thirty threw tough up were with

---

@title[Calculating Values -- Table]

|Word|P(Baseball)|P(Business)|
|----|----------------|----------------|
|threw|`$\dfrac{1+1}{18+29}$`|`$\dfrac{0+1}{14+29}$`|
|out|`$\dfrac{2+1}{18+29}$`|`$\dfrac{0+1}{14+29}$`|
|the|`$\dfrac{0+1}{18+29}$`|`$\dfrac{1+1}{14+29}$`|
|runner|`$\dfrac{0+1}{18+29}$`|`$\dfrac{0+1}{14+29}$`|

**NOTE:** "runner" is not the same as "runners" here!
---

@title[Calculating Values -- Final Calculation]

`$P(Baseball|totr) = \dfrac{2}{47} \cdot \dfrac{3}{47} \cdot \dfrac{1}{47} \cdot \dfrac{1}{47} \cdot \dfrac{3}{6} = 6.15 \times 10^-7$`

`$P(Business|totr) = \dfrac{1}{43} \cdot \dfrac{1}{43} \cdot \dfrac{2}{43} \cdot \dfrac{1}{43} \cdot \dfrac{3}{6} = 2.93 \times 10^-7$`

Baseball is therefore the best category for our phrase.

---

### Making Results Better

Ways that we can improve prediction quality:

1. Remove stopwords (e.g., a, the, on, of, etc.)
2. Lemmatize words:  group together inflections of the same word (runner, runners)
3. Use n-grams (sequences of multiple words; "threw out the" and "out the runner" are 3-grams)
4. Use TF-IDF (term frequency - inverse document frequency):  penalize words which appear frequently in most of the texts. 

---

@title[R -- Features]

## Agenda
1. Solving Naive Bayes
2. Solving By Hand -- Features
3. Solving By Hand -- Natural Language
4. **R -- Features**
5. R -- Natural Language

---

### Using The `naivebayes` Package

The `naivebayes` package is a fast Naive Bayes solver, with built-in versions of the `plot` and 
`predict` functions.

First, we will use the famous iris data set.

---

```r
if(!require(naivebayes)) {
  install.packages("naivebayes")
  library(naivebayes)
}
if(!require(caret)) {
  install.packages("caret")
  library(caret)
}

data(iris)

set.seed(1773)
irisr <- iris[sample(nrow(iris)),]
irisr <- irisr[sample(nrow(irisr)),]

iris.train <- irisr[1:120,]
iris.test <- irisr[121:150,]

nb <- naivebayes::naive_bayes(Species ~ ., data = iris.train)
#plot(nb, ask=TRUE)

iris.output <- cbind(iris.test, 
				prediction = predict(nb, iris.test))
table(iris.output$Species, iris.output$prediction)
confusionMatrix(iris.output$prediction, iris.output$Species)
```

@[1-4](Install the naivebayes package to generate a Naive Bayes model.)
@[5-8](Install the caret package to generate a confusion matrix.)
@[12-14](Pseudo-randomize the data set. This is small so we can do it by hand.)
@[16-17](Generate training and test data sets.)
@[19](Building a Naive Bayes model is as simple as a single function call.)
@[22-25](Generate predictions and analyze the resulting predictions for accuracy.)

---

### Demo Time

---

@title[Solving By Hand -- Natural Language]

## Agenda
1. Solving Naive Bayes
2. Solving By Hand -- Features
3. Solving By Hand -- Natural Language
4. R -- Features
5. **R -- Natural Language**

---

### R -- Natural Language

We can use the `naivebayes` package in R to solve Natural Language Processing problems as well.  Just like
before, we need to featurize our language samples.  Also like before, we will use the bag of words technique
to build our corpus.

Unlike before, we will perform several data cleanup operations beforehand to normalize our input data set.

---

```r
if(!require(naivebayes)) {
  install.packages("naivebayes")
  library(naivebayes)
}
if(!require(tidyverse)) {
  install.packages("tidyverse")
  library(tidyverse)
}
if(!require(tm)) {
  install.packages("tm")
  library(tm)
}
if(!require(caret)) {
  install.packages("caret")
  library(caret)
}

df <- readr::read_csv("data/movie-pang02.csv")
#glimpse(df)

set.seed(1773)
df <- df[sample(nrow(df)),]
df <- df[sample(nrow(df)),]
df$class <- as.factor(df$class)

corpus <- tm::Corpus(tm::VectorSource(df$text))
corpus.clean <- corpus %>%
  tm::tm_map(tm::content_transformer(tolower)) %>% 
  tm::tm_map(tm::removePunctuation) %>%
  tm::tm_map(tm::removeNumbers) %>%
  tm::tm_map(tm::removeWords, tm::stopwords(kind="en")) %>%
  tm::tm_map(tm::stripWhitespace)

dtm <- tm::DocumentTermMatrix(corpus.clean)
inspect(dtm[40:50,10:15])

df.train <- df[1:1500,]
df.test <- df[1501:2000,]

dtm.train <- dtm[1:1500,]
dtm.test <- dtm[1501:2000,]

corpus.clean.train <- corpus.clean[1:1500]
corpus.clean.test <- corpus.clean[1501:2000]

# 1500 rows and 38957 columns (unique words)
dim(dtm.train)
#remove infrequently used terms--must have been used 
# in at least 5 reviews
fiveFreq <- tm::findFreqTerms(dtm.train, 5)
#12144 terms remain
length(fiveFreq)

dtm.train.nb <- tm::DocumentTermMatrix(corpus.clean.train, 
					control=list(dictionary = fiveFreq))
dtm.test.nb <- tm::DocumentTermMatrix(corpus.clean.test, 
					control=list(dictionary = fiveFreq))

convert_count <- function(x) {
  y <- ifelse(x > 0, 1, 0)
  y <- factor(y, levels=c(0, 1), labels=c("No", "Yes"))
  y
}

trainNB <- apply(dtm.train.nb, 2, convert_count)
testNB <- apply(dtm.test.nb, 2, convert_count)

classifier <- naivebayes::naive_bayes(trainNB, df.train$class, 
				laplace = 1)
pred <- predict(classifier, newdata=testNB)

table("Predictions" = pred, "Actual" = df.test$class)
conf.mat <- caret::confusionMatrix(pred, df.test$class)
conf.mat
conf.mat$byClass
conf.mat$overall
conf.mat$overall["Accuracy"]
```

@[1-4](Install the naivebayes package to generate a Naive Bayes model.)
@[5-8](Install the tidyverse package to do some data cleanup and use the %>% pipe.)
@[9-12](Install the tm package to perform text mining.)
@[13-16](Install the caret package to generate a confusion matrix.)
@[21-24](Pseudo-randomize the data set and make `class` a factor.)
@[26-32](Create a corpus and clean up the dictionary.)
@[34-35](Represent the words as a Document Term Matrix.)
@[37-44](Split into training and test data sets.)
@[46-52](Pick terms used in several reviews.)
@[46-52](Pick terms used in several reviews.)
@[54-57](Build up DTMs using the frequently-used products.)
@[59-66](Because occurrence matters more than frequency, convert non-zero numbers to 1.)
@[68-70](Train the model with Laplace smoothing and generate predictions.)

---

### Demo Time

---

### Wrapping Up

The Naive Bayes class of algorithms are simple to understand and are reasonably accurate, making them
a good starting point for data analysis.  There are a number of superior algorithms for specific problems,
but starting with Naive Bayes will give you an idea of whether the problem is solvable and what your
expected baseline of success should be.

---

### For More

To learn more, go here:  <a href="http://csmore.info/on/naivebayes">http://CSmore.info/on/naivebayes</a>

And for help, contact me:  <a href="mailto:feasel@catallaxyservices.com">feasel@catallaxyservices.com</a> | <a href="https://www.twitter.com/feaselkl">@feaselkl</a>
