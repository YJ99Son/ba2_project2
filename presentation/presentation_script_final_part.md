# Presentation Script: Final Part (Slide 10 - 13)
*Target Time: ~3 Minutes | Style: Direct & Professional*

---

### Slide 10: Airbnb Official Criteria

So, does our model actually align with Airbnb's real standards?

First, let's look at the official rules. To be a Superhost, you need exactly four things:
1.  **10 stays** a year.
2.  **90% response rate**.
3.  **Less than 1% cancellations**.
4.  And a **4.8 rating**.

Airbnb checks this every quarter. It's a strict checklist.

### Slide 11: What the Model Learned

Now, let's see what our model thinks is important.

Look at features 2, 3, and 4 on the chart. Rating, Reviews, Response rate.
They match the official rules perfectly. This confirms our model learned the core logic correctly.

**But look at Number 1.**
The most critical feature is **`host_listings_count`**.
This is NOT in the official rulebook.

We interpret this as **Economies of Scale**.
Hosts who manage multiple properties run this like a business. They have established management systems, which makes them more consistent and reliable than someone doing this as a hobby.

### Slide 12: When They Disagree

To prove this, we compared the Rules vs. Our Model.
They disagreed in about **19% of cases**.

**Look at Case 16.**
This host has perfect scores and exactly 10 reviews.
By the official rules? **Pass.** They are a Superhost.
But our Model says? **Fail.**

Why?
The rules just check if you crossed the minimum line.
But our model sees the bigger picture. It detects that this host barely passed and lacks the **scale and experience** of a true professional.
The model values **proven reliability**, not just hitting a minimum number.

### Slide 13: Conclusion

Let's wrap up with three key takeaways.

1.  **High Accuracy:** Our Random Forest model hit **93% accuracy**. It's reliable.
2.  **Validation:** We proved Airbnb's official rules are solid—we agree with them 80% of the time.
3.  **Key Insight:** We found the hidden factor: **Scale**.

**Business Implication?**
Airbnb shouldn't just check boxes. They can use this to **coach hosts** on how to scale their operations, and identify high-quality partners **earlier** than the traditional rules allow.

Thank you.
