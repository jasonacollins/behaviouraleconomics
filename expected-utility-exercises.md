# Expected utility exercises

## Question 1.

Anika is an expected utility maximiser with the following utility function:




$$U(x)=\sqrt{x}$$




Anika is offered the following choice:

A)  A 50% chance of winning \$10 and a 50% chance of winning nothing
B)  \$4 for certain

Anika has zero wealth besides this offer.

\(a\) What is the expected value of option A)?

::: {.callout-tip collapse="true"}
## Question 1(a) answer

The expected value of option A) is:




```{=tex}
\begin{align*}
E[A]&=\sum_{i=1}^n p_ix_i \\[12pt]
&=0.5*\$10+0.5*0 \\[6pt]
&=\$5
\end{align*}
```



:::

\(b\) Will Anika choose A) or B)? Why?

::: {.callout-tip collapse="true"}
## Question 1(b) answer

We need to determine the expected utility of each option. Anika will selection the option with the highest expected utility.

The expected utility of option A) is:




```{=tex}
\begin{align*}
EU(A)&=p_1U(x_1)+p_2U(x_2) \\
&=0.5*\sqrt{10}+0.5*\sqrt{0} \\
&=1.58
\end{align*}
```



The expected utility of option B) is:




```{=tex}
\begin{align*}
EU(B)&=U(4) \\
&=\sqrt{4} \\
&=2
\end{align*}
```




Anika will choose option B) as it gives her higher expected utility. Anika is risk averse.
:::

\(c\) What is the certainty equivalent of option A?

::: {.callout-tip collapse="true"}
## Question 1(c) answer

To calculate the certainty equivalent of option A, we calculate what payment with certainty would deliver equivalent expected utility. That is:




```{=tex}
\begin{align*}
EU(CE)&=1.58 \\
\sqrt{CE}&=1.58 \\
CE&=1.58^2 \\
&=2.5
\end{align*}
```




The certainty equivalent of option A is \$2.50. That is, Anika would be indifferent between option A and a payment of \$2.50 for certain.
:::

\(d\) Draw a graph showing Anika's utility curve, the expected value of option A, the expected utility of options A) and B) and the certainty equivalent of option A).

::: {.callout-tip collapse="true"}
## Question 1(d) answer

![](img/expected-utility-exercises-question-1.jpg)
:::

## Question 2

Consider the following gamble:

> (0.5; \$550; 0.5, -\$500)

This gamble provides a 50% chance of winning \$550 and a 50% chance of losing \$500.

\(a\) Would a risk neutral agent (who maximises expected value) be willing to pay \$20 to play this gamble? What is the most they would be willing to pay to play?

::: {.callout-tip collapse="true"}
## Question 2(a) answer

The expected value of the gamble is:




```{=tex}
\begin{align*}
E[X]&=\sum_{i=1}^n p_ix_i \\[12pt]
&=0.5(550)+0.5(-500) \\[6pt]
&=25
\end{align*}
```




This is greater than \$20, so a risk neutral agent will be willing to pay \$20 to participate in the gamble.

We could also have solved this by determining the expected value if they had paid \$20:




```{=tex}
\begin{align*}
E[X]-c&=\sum_{i=1}^n p_ix_i-c \\[12pt]
&=0.5(550)+0.5(-500)-20 \\[6pt]
&=5
\end{align*}
```




As the expected value is positive, the agent would be willing to pay \$20.
:::

\(b\) Would a risk averse expected utility maximiser with wealth \$1000 and utility function $U(x)=x^{1/2}$ be willing to pay \$20 to play this gamble? What is the most they would be willing to pay to play?

::: {.callout-tip collapse="true"}
## Question 2(b) answer

The expected utility of the gamble for the risk averse agent if they paid \$20 to play is:




```{=tex}
\begin{align*}
EU(x)&=p_1(W+x_1-c)+p_2(W+x_2-c) \\[6pt]
&=0.5(1000+550-20)^{1/2}+0.5(1000-500-20)^{1/2} \\[6pt]
&=30.51
\end{align*}
```




The expected utility of not playing the gamble is:




```{=tex}
\begin{align*}
EU(x)&=(1000)^{1/2} \\[6pt]
&=31.62
\end{align*}
```




They would not pay \$20 as they would have higher utility if they turned down the gamble.

In fact, they would not pay any positive sum to participate in the gamble. If they were offered the gamble for free, their expected utility would be:




```{=tex}
\begin{align*}
EU(x)&=0.5(1000+550)^{1/2}+0.5(1000-500)^{1/2} \\[6pt]
&=30.86
\end{align*}
```




This is less than if they simply turned down the gamble. They would be willing to pay to avoid the gamble. How much?

We can determine this by asking what wealth a utility of 30.86 is:




```{=tex}
\begin{align*}
W^{1/2}&=30.86 \\[6pt]
W&=30.51^2 \\[6pt]
&=\$952.67
\end{align*}
```




The certainty equivalent of the gamble is \$952.67. The agent would be willing to pay up to \$47.33 to avoid the gamble.
:::

\(c\) Would the expected utility maximiser with utility function $U(x)=x^{1/2}$ change their decision if they had \$1 million in wealth? Explain.

::: {.callout-tip collapse="true"}
## Question 2(c) answer

If they now have \$1 million in wealth, we simply repeat the calculations above with the new wealth.




```{=tex}
\begin{align*}
EU(x)&=0.5(1000000+550-20)^{1/2}+0.5(1000000-500-20)^{1/2} \\[6pt]
&=1000.00247
\end{align*}
```





The expected utility of not playing the gamble is:




```{=tex}
\begin{align*}
EU(x)&=(1000000)^{1/2} \\[6pt]
&=1000
\end{align*}
```




They would be willing to pay \$20 as they would have higher utility if they accepted the gamble.

What is the most they would be willing to pay? If they were offered the gamble for free, their expected utility would be:




```{=tex}
\begin{align*}
EU(x)&=0.5(1000000+550)^{1/2}+0.5(1000000-500)^{1/2} \\[6pt]
&=1000.0125
\end{align*}
```




How much would they be willing to pay for this opportunity? We can determine this by asking what wealth a utility of 1000.0125 is:




```{=tex}
\begin{align*}
W&=(1000.0124655)^2 \\[6pt]
&=\$1000024.93
\end{align*}
```




The agent would be willing to pay up to \$24.93 for the gamble. This is close to the expected value of \$25.

Intuitively, as the agent's wealth increases their utility function becomes increasingly linear (second derivative approaches zero) and they become closer to risk neutral.
:::
