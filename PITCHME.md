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

Naive Bayes is not an algorithm; it is a **series** of algorithms.  Naive Bayes is very easy to understand and reasonably accurate, making it a great algorithm to use when starting a classification project.

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
4. R - Features
5. R - Natural Language

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
4. R - Features
5. R - Natural Language

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

Suppose today = ( Sunny, Hot, Normal, False ).  We can compare the probability of playing golf versus the probability of not playing golf:

`$P(Y|t) = \dfrac{P(O_s|Y) \cdot P(T_h|Y) \cdot P(H_n|Y) \cdot P(W_f|Y) \cdot P(Y)}{P(t)}$`

`$P(N|t) = \dfrac{P(O_s|N) \cdot P(T_h|N) \cdot P(H_n|N) \cdot P(W_f|N) \cdot P(N)}{P(t)}$`

Note the common denominator:  because we're comparing P(Yes|today) versus P(No|today), the common denominator cancels out.

---

### Testing A Day

Suppose we have a day like: today = ( Sunny, Hot, Normal, False ).

The probability of playing golf:
`$P(Yes|today) = \dfrac{2}{9} \cdot \dfrac{2}{9} \cdot \dfrac{6}{9} \cdot \dfrac{6}{9} \cdot \dfrac{9}{14} = 0.0141$`

The probability of not playing golf:
`$P(No|today) = \dfrac{3}{5} \cdot \dfrac{2}{5} \cdot \dfrac{1}{5} \cdot \dfrac{2}{5} \cdot \dfrac{5}{14} = 0.0068$`

---

### Wrapping Up

To learn more, go here:  <a href="http://csmore.info/on/naivebayes">http://CSmore.info/on/naivebayes</a>

And for help, contact me:  <a href="mailto:feasel@catallaxyservices.com">feasel@catallaxyservices.com</a> | <a href="https://www.twitter.com/feaselkl">@feaselkl</a>
