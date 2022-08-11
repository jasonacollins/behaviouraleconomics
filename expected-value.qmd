# Expected value

The expected value of a gamble is the amount you can expect to win on average, in the long run, when you play a gamble.

Example: We flip a coin. I give you \$1 if it is heads and you give me \$1 if it is tails. What is the expected value of this gamble?

The expected value is \$0. You lose \$1 half the time and gain \$1 half the time.

Formally, given a gamble, the expected value $E[X]$ of the random variable $X$ is:\

\begin{align*}
E[X]&=p_1x_1+p_2x_2+...+p_nx_n \\
&=\sum_{i=1}^np_ix_i
\end{align*}

$p_i$ is the probability of $x_i$.

## Expected value examples

### Example 1

You are offered bet with a 50% chance of winning \$10 and a 50% chance of losing $8.

The expected value of the gamble is:

\begin{align*}
E[X]&=\sum_{i=1}^n p_ix_i \\[6pt]
&=0.5(10)+0.5(-8) \\[6pt]
&=\$1
\end{align*}

\newpage
Your chance of winning increases to 60%. The expected value of the gamble is:

\begin{align*}
E[X]&=\sum_{i=1}^n p_ix_i \\[6pt]
&=0.6(10)+0.4(-8) \\[6pt]
&=\$2.80
\end{align*}

### Example 2

You are offered a bet with a 50% bet chance of winning 50% of your wealth and a 50% of chance of losing 40% of your wealth.

The expected value of the bet is:

\begin{align*}
E[X]&=\sum_{i=1}^n p_ix_i \\[6pt]
&=0.5*(0.5W)+0.5*(-0.4W) \\[6pt]
&=0.05W
\end{align*}

The expected value is 5% of your wealth.
