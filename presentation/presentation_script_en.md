# Presentation Script (English)
## Airbnb Superhost Prediction - Cape Town Cases

---

## Slide 1: Title

Hi everyone. Today I'm going to talk about predicting Airbnb Superhosts using machine learning—and our data comes from Cape Town, South Africa.

But this isn't just about building a model. What I really wanted to figure out was: what actually makes someone a Superhost? Is it just following Airbnb's rules, or is there something more?

---

## Slide 2: Problem Definition

So why should we even care about predicting Superhosts?

Look at these numbers here. Superhosts make about 22% more money than regular hosts. Their booking rate goes up by 60% because guests trust that little badge. And Airbnb gives them a hundred-dollar travel coupon every year.

Here's the question that drove this project: If we could tell in advance who's going to become a Superhost, couldn't we use that to help hosts get there faster? Like, proactively coaching them, or targeting them in marketing campaigns?

This has real business value. Imagine Airbnb identifying promising hosts early and guiding them toward that Superhost status.

---

## Slide 3: Data Overview

Alright, let's talk about the data.

We had about 25,000 listings from Cape Town for training, and 130 for testing. Started with 54 columns, but after all our preprocessing, we ended up with 444 features. I'll explain where those came from in a bit.

One thing we had to deal with was class imbalance. You can see here—64% of hosts weren't Superhosts, only 36% were. That's pretty skewed, so we used upsampling to balance it out.

---

## Slide 4: Preprocessing Pipeline

Here's how we cleaned up the data. Four main steps.

First, missing values. Nothing fancy—median for numbers, most common value for categories.

Second, we had to engineer some features. Dates got converted to "how many days ago was this"—so like, days since last review. Prices had dollar signs and commas we needed to strip out.

Third—and this is the interesting part—we used something called a Sentence Transformer to turn text into numbers. The amenities column had stuff like "Wifi, Kitchen, Beach access" as free text. We converted that into a 384-dimension vector. I'll show you the code in a second.

Fourth, standard one-hot encoding and scaling. That's how we went from 54 to 444 features.

We also grouped 76 property types into 6 clusters, and balanced the classes through upsampling—you can see before and after here.

---

## Slide 5: From the Code

Let me show you what this actually looks like in code.

On the left, you can see how we handled bathroom data. The raw data said things like "2 shared baths"—we parsed that into a number and filled in missing values with the median.

For prices, we just stripped out the dollar signs and commas. Same thing with percentages—get rid of the percent sign and convert to a number.

On the right side, you can see how we handled dates. We picked a reference date and calculated the difference. So instead of "November 15, 2024," the model sees "15 days ago." That captures recency, which matters for things like "when was your last review."

---

## Slide 6: Property-Type Clustering

Here's something cool we did with property types.

The original data had 76 different types—everything from "Entire villa" to "Shepherd's hut." If we one-hot encoded all of those, we'd have this super sparse matrix.

So instead, we used the same Sentence Transformer to understand what these labels mean. "Entire home" and "Entire villa"? Semantically similar. "Tent" and "Cave"? They go together too—outdoor adventure stuff.

We ran K-means clustering with k equals 6, and got these natural groupings you see on the right. Cluster 0 is all the "Entire place" types. Cluster 1 is the quirky outdoor stuff. Cluster 4 is private rooms.

This way, the model understands that "Entire condo" and "Entire apartment" are basically the same thing.

---

## Slide 7: Amenity Embedding

The amenities column was tricky. It's not a normal category—it's a list of stuff like "Wifi, Kitchen, Heating, Beach access, TV."

If we did traditional one-hot encoding, we'd have over 6,000 columns—one for each unique amenity. That's crazy sparse and it loses all the meaning. Like, the model wouldn't know that "Wifi" and "Internet" are basically the same thing.

So we used this transformer model to convert each listing's amenity text into a single 384-number vector. Now the model can understand what kind of amenities a place has, not just check boxes.

You can see the code on the left, and on the right is the explanation of why this matters. The vector captures the quality and completeness of amenities, not just whether they exist.

---

## Slide 8: Model Comparison

Okay, now the fun part—which model works best?

We tried six different approaches. You can see the results in this table.

Random Forest got us 93% accuracy—the highest. The neural network, PyTorch MLP, actually had the best F1 score at 76.4%. And Naive Bayes caught the most actual Superhosts with 87% recall.

But we went with Random Forest. And I want to explain why, because the choice matters a lot.

---

## Slide 9: Model Selection

So why did we pick Random Forest when other models beat it on some metrics?

Think about this from a business perspective. What happens if we get it wrong?

If we miss a real Superhost—okay, that's not great, but it's not the end of the world. They'll prove themselves eventually.

But if we say someone's going to be a Superhost when they're not? That's bad. Imagine Airbnb featuring this host prominently, putting them in a special coaching program, maybe even giving them early access to benefits. And then they turn out to be mediocre. That destroys trust and wastes resources.

That's why accuracy matters more than recall here. We want to be right when we say "yes."

Random Forest gives us 93% accuracy, plus something really valuable—we can see which features matter most. Look at this list on the right.

Number one is how many listings the host has. Then overall rating, recent reviews, and response rate. Notice something? The top feature—number of listings—isn't even in Airbnb's official criteria. The model found this pattern on its own.

---

## Slide 10: Airbnb Official Criteria

We first examined the official Superhost criteria provided by Airbnb.

There are four specific requirements: at least 10 completed stays (or 100 nights) per year, a 90% response rate, a cancellation rate below 1%, and an overall rating of 4.8 or higher. Airbnb evaluates these metrics quarterly based on performance over the preceding 12 months.

Our objective was to determine if our model's logic aligns with these established rules or if it identifies different patterns.

---

## Slide 11: What the Model Learned

Comparing the official criteria with our model's feature importance reveals a significant insight.

As shown on the right, features 2, 3, and 4—rating, review frequency, and response rate—align perfectly with Airbnb's official guidelines. This confirms that our model successfully learned the core rules.

However, the model identified `host_listings_count` as the most critical feature. This is not part of the official criteria. This suggests that hosting scale is a primary driver of Superhost status. From a management perspective, this reflects **economies of scale**. Hosts managing multiple properties likely have established professional systems for cleaning, communication, and operations, making them more consistent and reliable than single-listing hosts.

---

## Slide 12: When They Disagree

To validate this finding, we compared our model's predictions against a strict rule-based assessment on the test dataset.

We observed a disagreement rate of approximately 19% (25 out of 130 cases).

Case 16 illustrates this difference. This host meets all official thresholds: 100% response rate, 5.0 rating, and exactly 10 reviews. The rule-based system classifies them as a Superhost. However, our model rejects this case. The model likely detects that despite meeting the minimum cutoff, the host lacks the operational scale or depth of experience typically associated with sustained high performance.

Case 5 shows a scenario where both agree. Despite high quality metrics, the host has only 8 reviews. Both the rules and our model correctly identify that this volume is insufficient.

In summary, while the rule-based approach is binary—simply checking if thresholds are met—our model evaluates the holistic reliability and operational maturity of the host.

---

## Slide 13: Conclusion

In conclusion, our project offers three key takeaways.

First, the Random Forest model achieved 93% accuracy, demonstrating high reliability for practical application.

Second, we validated the official Airbnb criteria, with our model agreeing with the rule-based assessment in over 80% of cases.

Third, and most importantly, we discovered that **scale and professionalization** are hidden predictors of Superhost success.

For business application, these insights can be used to optimize **host coaching programs**—guiding potential hosts to scale their operations—and to refine **platform quality management** by identifying high-potential hosts earlier than the traditional criteria allow.

Thank you.

---

*Estimated time: 8-10 minutes*
