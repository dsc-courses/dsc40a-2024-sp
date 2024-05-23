---
layout: page
title: 🧩 Conditional Independence
description: An overview of conditional independence.
nav_exclude: true
---

# 🧩 Conditional Independence

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"> </script>

Here, we'll state the definition of conditional independence and discuss a few strategies for establishing whether or not events are conditionally independent.

## Definition

Two events $$A$$ and $$B$$ are **conditionally independent** given event $$C$$ if given that $$C$$ occurs, $$A$$ and $$B$$ are independent. Formally:

$$\boxed{\mathbb{P}((A \cap B) \mid C) = \mathbb{P}(A \mid C) \cdot \mathbb{P}(B \mid C)}$$

Intuitively, you can think of conditioning on $$C$$ as changing our sample space to consist of only the outcomes that are in $$C$$. **Note that this is the only "formula" for conditional independence you _need_ to know; everything else in this note can be derived from here.**

But, since that definition can be hard to do calculations with directly, let's see if we can re-write it in a way that is easier for us to work with. Using the definition of conditional probability on all three pieces above, we can write

$$\frac{\mathbb{P}(A \cap B \cap C)}{\mathbb{P}(C)} = \frac{\mathbb{P}(A \cap C)}{\mathbb{P}(C)} \cdot \frac{\mathbb{P}(B \cap C)}{\mathbb{P}(C)}$$

If you want to check if $$A$$ and $$B$$ are conditionally independent given $$C$$, this formula is bulletproof; it will never lead you astray.

**Important note:** Unless $$C$$ is equal to the entire sample space (which wouldn't be very meaningful), $$\mathbb{P}(C) \neq 1$$.

---

## Example

Let's suppose we consider all outcomes when rolling a 9-sided die, so $$S = \{1, 2, 3, 4, 5, 6, 7, 8, 9\}$$. Suppose the coin is fair, meaning that all outcomes are equally likely.

Let $$A$$ be the event that the roll is even, and let $$B$$ be the event that the roll is a multiple of three. That is, $$A = \{2, 4, 6, 8\}$$ and $$B = \{3, 6, 9\}$$.

Note that without any other information, $$A$$ and $$B$$ are not independent. This is because $$\mathbb{P}(A) = \frac{4}{9}$$, $$\mathbb{P}(B) = \frac{1}{3}$$, $$\mathbb{P}(A \cap B) = \mathbb{P}(\{6\}) = \frac{1}{9}$$, and $$\mathbb{P}(A) \cdot \mathbb{P}(B) = \frac{4}{27}$$ is not equal to $$\mathbb{P}(A \cap B) = \frac{1}{9}$$.


### Part 1
First, let's let $$C$$ be the event the roll is less than 9, i.e. $$C = \{1, 2, 3, 4, 5, 6, 7, 8 \}$$. Let's try and determine if $$A$$ and $$B$$ are conditionally independent given $$C$$. There are a few pieces we need to calculate first:

- $$\mathbb{P}(C) = \frac{8}{9}$$
- $$\mathbb{P}(A \cap B \cap C) = \mathbb{P}(\{6\}) = \frac{1}{9}$$
- $$\mathbb{P}(A \cap C) = \mathbb{P}(\{2, 4, 6, 8 \}) = \frac{4}{9}$$
- $$\mathbb{P}(B \cap C) = \mathbb{P}(\{3, 6\}) = \frac{2}{9}$$
    
Now, all we need to do is check if $$\frac{\mathbb{P}(A \cap B \cap C)}{\mathbb{P}(C)} = \frac{\mathbb{P}(A \cap C)}{\mathbb{P}(C)} \cdot \frac{\mathbb{P}(B \cap C)}{\mathbb{P}(C)}$$. 
- Left-hand side: $$\frac{\mathbb{P}(A \cap B \cap C)}{\mathbb{P}(C)} = \frac{\frac{1}{9}}{\frac{8}{9}} = \frac{1}{8}$$.
- Right-hand side: $$\frac{\mathbb{P}(A \cap C)}{\mathbb{P}(C)} \cdot \frac{\mathbb{P}(B \cap C)}{\mathbb{P}(C)} = \frac{\frac{4}{9}}{\frac{8}{9}} \cdot \frac{\frac{2}{9}}{\frac{8}{9}} = \frac{4}{8} \cdot \frac{2}{8} = \frac{1}{8}$$.
    
Both $$\frac{\mathbb{P}(A \cap B \cap C)}{\mathbb{P}(C)}$$ and $$\frac{\mathbb{P}(A \cap C)}{\mathbb{P}(C)} \cdot \frac{\mathbb{P}(B \cap C)}{\mathbb{P}(C)}$$ are equal to $$\frac{1}{8}$$, thus $$A$$ and $$B$$ are conditionally independent given $$C$$.

### Part 2

What if instead we let $$C$$ be the event that the roll is greater than 4, i.e. $$C = \{5, 6, 7, 8, 9\}$$? Let's again try and see if $$A$$ and $$B$$ are conditionally independent given $$C$$.

- $$\mathbb{P}(C) = \frac{5}{9}$$
- $$\mathbb{P}(A \cap B \cap C) = \mathbb{P}(\{6\}) = \frac{1}{9}$$
- $$\mathbb{P}(A \cap C) = \mathbb{P}(\{6, 8 \}) = \frac{2}{9}$$
- $$\mathbb{P}(B \cap C) = \mathbb{P}(\{6, 9\}) = \frac{2}{9}$$
    
Now, all we need to do is check if $$\frac{\mathbb{P}(A \cap B \cap C)}{\mathbb{P}(C)} = \frac{\mathbb{P}(A \cap C)}{\mathbb{P}(C)} \cdot \frac{\mathbb{P}(B \cap C)}{\mathbb{P}(C)}$$. 
- Left-hand side: $$\frac{\mathbb{P}(A \cap B \cap C)}{\mathbb{P}(C)} = \frac{\frac{1}{9}}{\frac{5}{9}} = \frac{1}{5}$$.
- Right-hand side: $$\frac{\mathbb{P}(A \cap C)}{\mathbb{P}(C)} \cdot \frac{\mathbb{P}(B \cap C)}{\mathbb{P}(C)} = \frac{\frac{2}{9}}{\frac{5}{9}} \cdot \frac{\frac{2}{9}}{\frac{5}{9}} = \frac{2}{5} \cdot \frac{2}{5} = \frac{4}{25}$$.
    
$$\frac{\mathbb{P}(A \cap B \cap C)}{\mathbb{P}(C)}$$ is $$\frac{1}{5}$$ while $$\frac{\mathbb{P}(A \cap C)}{\mathbb{P}(C)} \cdot \frac{\mathbb{P}(B \cap C)}{\mathbb{P}(C)}$$ is $$\frac{4}{25}$$; since these are not equal, $$A$$ and $$B$$ are **not** conditionally independent given $$C$$.

**Note that while in this example all outcomes in $$S$$ were equally likely, this process works regardless of what the probabilities of the outcomes are.**

---

## An equivalent form

Note that we can take the equation we used in the previous section, 

$$\frac{\mathbb{P}(A \cap B \cap C)}{\mathbb{P}(C)} = \frac{\mathbb{P}(A \cap C)}{\mathbb{P}(C)} \cdot \frac{\mathbb{P}(B \cap C)}{\mathbb{P}(C)}$$

and divide both sides by $$\frac{\mathbb{P}(A \cap C)}{\mathbb{P}(C)}$$ to get an equivalent definition of conditional independence:

$$\frac{\mathbb{P}(A \cap B \cap C)}{\mathbb{P}(A \cap C)} = \frac{\mathbb{P}(B \cap C)}{\mathbb{P}(C)}$$

The above equation is equivalent to

$$\mathbb{P}(B | (A \cap C)) = \mathbb{P}(B | C)$$

This is saying that if we know for sure that $$C$$ happens, then $$A$$ and $$B$$ are conditionally independent given $$C$$ if $$A$$ happening has no impact on $$B$$ happening. Note that if you remove the $$C$$s, this looks like the definition of (non-conditional) independence, $$\mathbb{P}(B \mid A) = \mathbb{P}(B)$$. The only difference is that here we must consider the fact that $$C$$ happens on both sides.

---

## Thinking in terms of proportions

If **all outcomes in our sample space $$S$$ are equally likely**, there is a slightly more intuitive way to think about conditional independence.

In lecture, we stated that, assuming that all outcomes are equally likely, two events $$A$$ and $$B$$ are (non-conditionally) independent if the following two proportions are equal:
- the proportion of values in $$A$$ that are taken up by $$B$$
- the proportion of values in the sample space that are taken up by $$B$$

This is just an interpretation of $$\mathbb{P}(B \mid A) = \mathbb{P}(B)$$.

The analogue in terms of conditional independence is as follows. Again, assuming that all outcomes are equally likely, two events $$A$$ and $$B$$ are conditionally independent given $$C$$ if, **within $$C$$**, the following two proportions are equal:

- the proportion of values in $$A$$ that are taken up by $$B$$
- the proportion of values in $$C$$ that are taken up by $$B$$

It is crucial to realize that the first proportion is only looking at the proportion of values in $$A$$ **that are also in $$C$$** that are taken up by $$B$$.

Let's use this interpretation on our two examples from before.

### Part 1

Recall:
- $$S = \{1, 2, 3, 4, 5, 6, 7, 8, 9\}$$, all outcomes are equally likely
- $$A = \{2, 4, 6, 8\}$$, $$B = \{3, 6, 9\}$$, $$C = \{1, 2, 3, 4, 5, 6, 7, 8\}$$

Let's check if $$A$$ and $$B$$ are conditionally independent given $$C$$.
- There is only one outcome in all of $$A$$, $$B$$, and $$C$$: 6. If we only consider the outcomes in $$C$$, there are 4 outcomes in $$A$$ total: 2, 4, 6, and 8. Thus, within $$C$$, the proportion of values in $$A$$ that are taken up by $$B$$ is $$\frac{1}{4}$$.
- There are 2 outcomes in $$C$$ that are taken up by $$B$$: 3 and 6. There are 8 outcomes in $$C$$ total. So, the proportion of outcomes in $$C$$ taken up by $$B$$ is $$\frac{2}{8} = \frac{1}{4}$$.

Since $$\frac{1}{4} = \frac{1}{4}$$, $$A$$ and $$B$$ are conditionally independent given $$C$$.

### Part 2
- $$S = \{1, 2, 3, 4, 5, 6, 7, 8, 9\}$$, all outcomes are equally likely
- $$A = \{2, 4, 6, 8\}$$, $$B = \{3, 6, 9\}$$, $$C = \{5, 6, 7, 8, 9\}$$

Again, let's check if $$A$$ and $$B$$ are conditionally independent given $$C$$.
- There is only one outcome in all of $$A$$, $$B$$, and $$C$$: 6. If we only consider the outcomes in $$C$$, there are only 2 outcomes in $$A$$ total: 6 and 8. Thus, within $$C$$, the proportion of outcomes in $$A$$ that are taken up by $$B$$ is $$\frac{1}{2}$$.
- There are 2 outcomes in $$C$$ taken up by $$B$$: 6 and 9. There are 5 outcomes in $$C$$ total. So, the proportion of outcomes in $$C$$ taken up by $$B$$ is $$\frac{2}{5}$$.

Since $$\frac{1}{2} \neq \frac{2}{5}$$, $$A$$ and $$B$$ are not conditionally independent given $$C$$.

**This "proportions" approach will only work if all outcomes in your sample space are equally likely!**

---

## Overlapping rectangles and independence

**Note**: This brief diversion is about independence more generally, not just conditional independence.

In lecture, we noted that if we can write the sample space $$S$$ as a grid and events $$A$$ and $$B$$ as overlapping rectangles as part of that grid, it indicates that $$A$$ and $$B$$ are independent. In the lecture example, we drew one card uniformly at random from a deck of 52 cards. Let's look at that one more time.

![](https://i.imgur.com/Ry0YTxh.png)

In our sample space, rows represent suits and columns represent face values. Note that if we look at any one row and any one column of our sample space, there is exactly one element in the intersection. For instance, there is exactly one Queen of Hearts, and it's at the intersection of the hearts row and Queens column). When choosing a card at random from a deck:
- The probability of any one card, such as the Queen of Hearts, $$\frac{1}{52}$$.
- The probability of a heart is $$\frac{1}{4}$$.
- The probability of a Queen is $$\frac{1}{13}$$.
- Since $$\frac{1}{4} \cdot \frac{1}{13} = \frac{1}{52}$$, the events "card is a heart" and "card is a Queen" are independent. The same applies for any suit and any face value.

What about multiple suits and multiple face values? Let's try and generalize this result.
- Suppose event $$A$$ is that the card is one of $$k$$ suits (e.g. "card is a heart or spade"). The probability a randomly selected card is from one of the $$k$$ specified suits is $$\mathbb{P}(A) = \frac{k}{4}$$.
- Suppose event $$B$$ is that the card is one of $$f$$ face values (e.g. "card is a 4 or 7 or Queen"). The probability that a randomly selected card is one of the $$f$$ specified face values is $$\mathbb{P}(B) = \frac{f}{13}$$.
- There are $$k \cdot f$$ cards that come from one of our $$k$$ specified suits AND $$f$$ specified face values (e.g. there are 6 cards whose suit is either heart or spade, and whose face value is either 4, 7, or Queen). Thus, the probability a randomly selected card comes from one of our specified suits and one of our specified face values is $$\mathbb{P}(A \cap B) = \frac{k \cdot f}{52}$$.
- Since $$\mathbb{P}(A) \cdot \mathbb{P}(B) = \frac{k}{4} \cdot \frac{f}{13} =  \frac{k \cdot f}{52} = \mathbb{P}(A \cap B)$$, the events "card's suit is ___" and "card's face value is ___" are independent.

Note that $$A$$ here corresponds to $$k$$ entire rows of the sample space, and $$B$$ corresponds to $$f$$ entire columns of the sample space. **These are the rectangles we're talking about.** It doesn't matter how many rows are in $$A$$ or how many columns are in $$B$$, this result will still hold.

If $$A$$ doesn't take up entire rows and/or $$B$$ doesn't take up entire columns, then $$A$$ and $$B$$ may not be independent. For instance, if $$A$$ is the event that "the card is a heart" and $$B$$ is the event that "the card is a red Queen", $$A$$ and $$B$$ are not independent:
- The probability that a randomly selected card is a heart is $$\mathbb{P}(A) = \frac{1}{4}$$.
- The probability that a randomly selected card is a red Queen is $$\mathbb{P}(B) = \frac{2}{52} = \frac{1}{26}$$, since there are 2 red Queens in the deck.
- The probability that a randomly selected card is a heart and a red Queen is $$\mathbb{P}(A \cap B) = \frac{1}{52}$$.
- $$\mathbb{P}(A) \cdot \mathbb{P}(B) = \frac{1}{4} \cdot \frac{1}{26} \neq \frac{1}{52} = \mathbb{P}(A \cap B)$$, so $$A$$ and $$B$$ are not independent. Intuitively this makes sense as if a card is a red Queen, this increases the chances that it is a heart from $$\frac{1}{4}$$ to $$\frac{1}{2}$$.

In other examples, if you are able write your sample space as a grid and **all outcomes are equally likely**, you may be able to use similar techniques.