# Axioms for Expected Utility Theory

For decision making under risk, we require two additional axioms of desirable behaviour to develop a predictive or descriptive model. These additional axioms are continuity and the independence of irrelevant alternatives.

Under the axioms of:

-   Completeness
-   Transitivity
-   Continuity
-   Independence

a decision maker behaves as if choosing between risky prospects by selecting the one with the highest expected utility.

The four axioms of completeness, transitivity, continuity and independence are often called the von Neumann--Morgenstern axioms for a rational decision maker. You can see now we have a second potential benchmark of "rationality".

Note: Preferences under these assumptions are cardinal.

Beyond those four axioms, some additional axioms are often adopted for practical purposes. These are also discussed below.

## Continuity

The idea behind continuity is that people have similar preferences for similar bundles. If $x$ is preferred to $y$, bundles close to $x$ are preferred to bundles close to $y$. There are no "jumps" in utility.

Continuity guarantees that every preference relation can be represented by a continuous utility function (and vice versa).

Here are two formal definitions.

### Definition 1

1.  A preference relation is continuous if for any $x \succ y$ there exists a number $\epsilon > 0$ such that every bundle $a$ that is less distant from $x$ than $\epsilon$ and every bundle $b$ that is less distant from $y$ than $\epsilon$ results in $a \succ b$.

To put this another way, a preference relation is continuous if for any $x \succ y$ there are *some* neighbourhoods $N_\epsilon x$ and $N_\epsilon y$ around $x$ and $y$ such that for every $a\in N_\epsilon x$ and $b\in N_\epsilon x$ we have $a \succ b$.

One way to picture this is to imagine a circle around bundle $x$ of radius $\epsilon$. This circle represents the neighbourhood. There will always exist some circle - even if very small - within which every bundle $a$ is preferred to bundle $y$.

The intuition behind this definition is that a very small change in your bundle should not result in a sudden switch of your preferences. If you prefer 5 bananas to 2 oranges, you will likely prefer 4.9 bananas to 2 oranges. (And if not, there will be some amount of bananas between 4.9 and 5 that you prefer over 2 oranges.)

Here's another intuitive example: if you prefer a Mercedes to a Toyota, there will be *some* level of defect in the Mercedes that you would be willing to accept while still preferring the Mercedes to the Toyota.

### Definition 2

If $x$, $y$ and $z$ are lotteries with $x\succcurlyeq y\succcurlyeq z$, the continuity axiom requires that there exists a probability $p$ such that $y$ is equally as good as a mix of $x$ and $z$. That is, there exists $p$ such that:




$$px+(1-p)z \sim y$$




The below diagram illustrates continuity under this definition.

On the diagram are three bundles: $x$, $y$ and $z$, and each sits on a different indifference curve. The indifference curve that $x$ is on is higher than that of $y$ which is higher than that of $z$. That is, $x\succcurlyeq y\succcurlyeq z$.

Now consider a gamble that pays $x$ with probability $p$ and $z$ with probability $1-p$. Each value of $p$ would result in a gamble with utility falling between that of $x$ and $z$. If we were to draw a line between $x$ and $z$, you could think of the utility of the gamble for each value of $p$ as having the same utility as a bundle on that line. Under the continuity axiom, there would be no holes in that line. For some value of $p$, that gamble will be on the same indifference curve for $y$. At that point, $px+(1-p)z \sim y$.



::: {.cell}
::: {.cell-output-display}
![](axioms-for-expected-utility-theory_files/figure-pdf/unnamed-chunk-1-1.pdf)
:::
:::



Note: If you read the literature about expected utility, you may come across an axiom called the Archimedean property. Only one of continuity or the Archimedean property need be assumed. I will not cover the Archimedean property in this book.

### Example of discontinuous preferences

Lexiographic preferences occur where an agent prefers any amount of a good $x$ to any amount of another good $y$. If choosing between bundles of goods, the agent will choose the bundle with the most $x$, regardless of the amount of $y$. They will only consider the amount of $y$ if the amount of $x$ in two bundles is identical.

Consider an agent with lexiographic preferences who is offered the following combinations of $x$ and $y$.

A. (1, 1)

B. (1, 2)

C. (1.1, 1)

Their preference ranking will be: $C\succ B \succ A$.

This function is not continuous as there is a "jump" whenever there is an increase in $x$, even if $y$ is large. Add an infinitesimal amount $\epsilon$ of $x$ to bundle $A$ and the preference relation between bundle $A$ and bundle $B$ flips.

These three bundles $A$, $B$ and $C$ are represented graphically below.

First, let's consider these preferences in terms of Definition 1. Around $A$ I have drawn a circle of radius $\epsilon$ (the neighbourhood). No matter how small I draw this circle (no matter how small $\epsilon$), any bundle within the circle that lies to the right of $A$ (that is, contains $x>1$) is preferred to bundle $B$. There is a jump in preferences to the right of A.



::: {.cell}
::: {.cell-output-display}
![](axioms-for-expected-utility-theory_files/figure-pdf/unnamed-chunk-2-1.pdf)
:::
:::



To consider this in terms of the second formal definition, there is no $p$ for which:




$$pA+(1-p)C \sim B$$




When $p=1$, $B \succ A$. For any $p<1$, $pA+(1-p)C \succ B$ as any non-zero share of $C$ makes the combination of $A$ and $C$ preferred.

One interesting feature of lexiographic preferences is that you cannot draw indifference curves on this figure. If a bundle differs from another, it must be strictly preferred to the other as no amount of $y$ can make up for any amount of $x$.

## Independence of irrelevant alternatives {#sec-independence}

Under independence of irrelevant alternatives, a person who mixes two gambles with an irrelevant third gamble will maintain the same order of preference between those two original gambles as when the two are presented independently of the third.

Formally, if:

-   $x$ and $y$ are lotteries with $x\succcurlyeq y$ and
-   $p$ is the probability that a third option $z$ is present, then:




$$pz+(1-p)x\succcurlyeq pz+(1-p)y$$




The third choice, $z$, is irrelevant. The order of preference for $x$ before $y$ holds. It is independent of the presence of $z$.

### Example of independence of irrelevant alternatives

Suppose $x$ is an orange and $y$ is an apple. I strictly prefer an orange to an apple.

Suppose there is not a third possibility $z$ of receiving no fruit. Under the independence of irrelevant alternatives, if I prefer oranges to apples, I will prefer a gamble with a 50% chance of getting an orange and 50% chance of receiving nothing to a gamble with a 50% chance of getting an apple and a 50% chance of receiving nothing.

That is:




$$\text{orange}\succ \text{apple}  \Longrightarrow 50\% \text{ chance of orange}\succ 50\% \text{ chance of apple}$$




## Auxilliary axioms

Beyond completeness, transitivity, continuity and independence, economists often adopt other axioms. These are not required for expected utility theory, but make analysis more practicable.

These include:

-   Utility is calculated over total wealth.

-   Non-satiation: No matter what you have, there is always another (nearby) bundle that you would rather have.

-   Monotonicity: Preferences are monotone if more of any good in the bundle makes the agent strictly better off. Non-satiation is implied by monotonicity, but not the other way around. Monotonicity implies downward sloping indifference curves.

-   Convexity: Convexity means that people have a preference for variety or combination (indifference curves bulge toward the origin).

-   Diminishing marginal utility: Each successive additional unit of consumption delivers a smaller (diminishing) amount of utility than the last.

I provide further detail on convexity and diminishing marginal utility below.

### Convexity

Convexity means that people have a preference for variety or combination (indifference curves bulge toward the origin). Averages are better than extremes.

In many contexts this makes sense. For example, suppose an agent is indifferent between two beers and two meat pies. Under this assumption, any mix of the two (e.g. a beer and a pie) will be at least as preferred as the two beers or two pies.

Formally, a preference relation is convex if, for any $x\succcurlyeq y$ and for every $\theta\in[0,1]$:




$$\theta x+(1-\theta)y\succcurlyeq y$$




Strict convexity is where, for any $x\sim y$, $x\neq y$ and for every $\theta\in[0,1]$:




$$\theta x+(1-\theta)y\succcurlyeq y$$

$$\theta x+(1-\theta)y\succcurlyeq x$$




For two equivalent goods or bundles, a weighted average of the two bundles is better than each of those bundles.

### Diminishing marginal utility

Marginal utility is how much utility you get or lose from an incremental decrease or increase in consumption. Under diminishing marginal utility, each successive additional unit of consumption delivers a smaller (diminishing) amount of utility than the last.

Diminishing marginal utility leads to risk averse preferences.

Diminishing marginal utility is related to the axiom of convexity. Diminishing marginal utility will lead to convex indifference curves. However, the reverse relationship does not always hold.
