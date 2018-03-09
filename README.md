# 5525Lab3

Homework worth 25 points, bonus extensions up to 10 additional points.

##Part 0 (required, 23 points):

a) Implement the MFCC calculation algorithm.  

b) Adapt the Dynamic Time Warping algorithm to allow you to calculate a score comparing two waveforms.  Local distances should be calculated by comparing two vectors of speech representations (see part c) using a suitable distance metric.

c) For the dataset given, compare the scores (and possibly alignments) between pairs of wavefiles that you choose, using both MFCC representations and Log Spectral representations.  What do you observe in terms of overall scores?  What do you notice in matched vs. mismatched pairs?

d) Create a classifier that uses the "a" versions of the wave files as templates, and "b" as the test items.  How accurate are both representations?

##Extension 1 (2 points):  
Record your own set of digits (zero through nine plus oh) for each of your group members.  Use these as test items against the "a" templates.  What is the accuracy?  If you use all data except one person's data as the templates, does accuracy change?  Rotate your test set through all of the group members' speech.  (Make sure to create a zip file with your recorded speech for the TA to be able to grade.)

##Extension 2 (2 points): 
Develop a visualization of the alignment between two waveforms similar to that on slide 28 of Week 8's slides.  Describe what you see when you align 5a.wav against 9a.wav.

##Extension 3 (10 points):  
Train a Mixture of Gaussians on the MFCC slices from all "a" templates.  You may use an off-the-shelf Mixture of Gaussian implementation for this purpose (just be sure it can handle multivariate Gaussians).  Since you are using MFCCs, you can assume diagonal covariance matrices.   Train a reasonable number of Gaussians (start with 32).  Each Gaussian can be used as a local estimator of the log likelihood -- log P(acoustics|class).  Now transform your template recognition problem into one where you use the distance between the log likelihoods of all Gaussians instead of distance between MFCCs.  Plot accuracy against number of Gaussians (ranging from 2 to 128), using 5 different initializations of the MoG algorithm to get a sense of the accuracy variance.
