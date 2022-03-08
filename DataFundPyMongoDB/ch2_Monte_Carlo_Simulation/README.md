# Chapter 2 - Monte Carlo Simulation and Density Functions

## Randomness Using Probabliity and Cumulative Density Functions
-------------------------------------------------------------

Randomness masquerades as reality (the natural world) in data science, since the future cannot be predicted.

That is, randomization is the way data scientists simulate reality.

More data means better accuracy and prediction (more realism).

It plays a key role in discrete event simulation and deterministic problem solving.

Randomization is used in many fields such as statistics, MCS, cryptography, statistics, medicine, and science.


### Probability Density Function - PDF
-------------------------------------------------------------

The density of a continuous random variable is its probability density function (PDF).

PDF is the probability that a random variable has the value x, where x is a point within the interval of a sample.

This probability is determined by the integral of the random variable’s PDF over the range (interval) of the sample.

That is, the probability is given by the area under the density function, but above the horizontal axis and between the lowest and highest values of range.

An integral (integration) is a mathematical object that can be interpreted as an area under a normal distribution curve.

### Cumulative Distribution Function - CDF
-------------------------------------------------------------

A cumulative distribution function (CDF) is the probability that a random variable has a value less than or equal to x.

That is, CDF accumulates all of the probabilities less than or equal to x.

### Percent Point Function - PPF
-------------------------------------------------------------

The percent point function (PPF) is the inverse of the CDF.

It is commonly referred to as the inverse cumulative distribution function (ICDF) .

ICDF is very useful in data science because it is the actual value associated with an area under the PDF.

### Density Function Reference
-------------------------------------------------------------

Please refer to www.itl.nist.gov/div898/handbook/eda/section3/eda362.htm for an excellent explanation of density functions.


## Matplot lib color map
-------------------------------------------------------------
https://matplotlib.org/examples/color/colormaps_reference.html


