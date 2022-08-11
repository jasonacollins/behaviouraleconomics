# Commitment

A commitment device is a mechanism which locks yourself into a course of action that you might not otherwise choose but that produces the desired result.

Commitment devices may work through the following channels:

-   Artificially depressing the value of the bad course of action

-   Artificially increasing the value of the optimal course of action

-   Forcing the agent to maintain the optimal course of action.

## Commitment examples

### Forcing the optimal course of action

Recall what the sophisticated agent did when faced with a choice of (0, \$6; 1, \$10; 2, \$16). First they realised that next week they would take the \$10 straight away.




```{=tex}
\begin{align*}
U_1(1,\$10)&=u(\$10) \\
&=10
\end{align*}
```

```{=tex}
\begin{align*}
U_1(2,\$16)&=\beta\delta u(\$16) \\
&=0.5*1*16 \\
&=8
\end{align*}
```



Knowing this is the case, they then chose to take the \$6 today.




```{=tex}
\begin{align*}
U_0(0,\$6)&=u(\$6) \\
&=6
\end{align*}
```

```{=tex}
\begin{align*}
U_0(1,\$10)&=\beta\delta u(\$10) \\
&=0.5*1*10 \\
&=5
\end{align*}
```



But when they compare all three, they would prefer the \$16 in two weeks. It is only because they can foresee their future failing after one week that they don't wait.




```{=tex}
\begin{align*}
U_0(0,\$6)&=u(\$6) \\
&=6
\end{align*}
```

```{=tex}
\begin{align*}
U_0(1,\$10)&=\beta\delta u(\$10) \\
&=0.5*1*10 \\
&=5
\end{align*}
```

```{=tex}
\begin{align*}
U_0(2,\$16)&=\beta\delta^2 u(\$16) \\
&=0.5*1^2*16 \\
&=8
\end{align*}
```



But what if they could commit themselves today?

Suppose that not only could they select an option today, but they could also choose to bind themselves to that decision such that they could not change it in the future. The result of that: a sophisticated present-biased agent would choose the \$16 in two weeks, and bind their future self from changing their mind.




$$U_0(0,\$6)=6$$

$$U_0(0,\$10)=5$$

$$U_0(0,\$16)=6$$




### Forcing the optimal course of action: Odysseus

Another example of forcing the agent to maintain the optimal course of action is the story of Odysseus.

Odysseus was required to sail past the sirens at $t=1$. At that time he can either jump off his ship to join the sirens (and die) or sail on past and live.

As Odysseus is a sophisticated present-biased agent, he considers what he is likely to do at that time. He realises that he will jump of the ship for the immediate benefit of joining the sirens at the loss of the longer-term benefit of living.

But from the perspective of Odysseus today, with both the benefits of the siren and living in the future, Odysseus would prefer to live. As a result, he decides to commit himself to that course of action by instructing his crew to tie him to the mast (plus leaving his ears unplugged so that he also gets some benefits from the siren song).

![[John William Waterhouse, Ulysses and the Sirens (1891)](https://commons.wikimedia.org/wiki/File:John_William_Waterhouse_-_Ulysses_and_the_Sirens_(1891).jpg)](img/John_William_Waterhouse_-_Ulysses_and_the_Sirens_(1891).jpg)

### Forcing the optimal course of action: lay-by

Lay-by involves paying a deposit and administrative fee toward the purchase of a product. You receive your purchase when you make payment in full some time later.

Let us see how that could help a quasi-hyperbolic discounter with discount factors $\delta=1$ and $\beta=1/2$.

Suppose you want a new jacket for work. You need to save for three months to purchase the jacket. But each month you save you forgo consumption that would boost your utility. Today you decide whether you will save for the jacket or not.

You receive the following payoffs for each course of action:

|       | t=0 | t=1 | t=2 |
|-------|:---:|:---:|:---:|
| Save  |  0  |  0  | 45  |
| Spend |  10  |  10  |  10  |

At $t=0$ the highest discounted utility is for Save. You plan to save for the jacket.

Save:

\begin{align*}
U(x)&=0+\beta\delta *0+\beta\delta^2*45 \\
&=0.5*45 \\
&=22.5
\end{align*}

Spend:

\begin{align*}
U(x)&=10+\beta\delta *10+\beta\delta^2*10 \\
&=10+0.5*10+0.5*10 \\
&=20
\end{align*}

One month now passes. You have saved for a month. You could now spend both your savings from last month and this month, giving a short term boost, or keep saving for your jacket.

|         | t=1 | t=2 |
|---------|:---:|:-------------:|
| Save    |  0  |      45       |
| *Spend* | 20  |       10       |

At $t=1$ spending now has the highest discounted utility. After saving for the first period, you spend.

Save:

\begin{align*}
U(x)&=0+\beta\delta*45 \\
&=0.5*45 \\
&=22.5
\end{align*}

Spend:

\begin{align*}
U(x)&=20+\beta\delta *10 \\
&=20+0.5*10 \\
&=25
\end{align*}

You spend despite initially wanting to save.

Now let's consider this problem from the point of view of a sophisticated present-biased agent. They see their full choice set as:

|                       | t=0 | t=1 | t=2 |
|-----------------------|:---:|:---:|:---:|
| Save  |  0  |  0  | 45  |
| Start spending at t=1 |  0  | 20  |  10  |
| Spend                 |  10  |  10  |  10  |

You work backward through time. At $t=2$, you will buy the jacket.

The utility of each option at $t=1$ is as follows:

Save:

\begin{align*}
U(x)&=0+\beta\delta*45 \\
&=0.5*45 \\
&=22.5
\end{align*}

Spend:

\begin{align*}
U(x)&=20+\beta\delta *10 \\
&=20+0.5*10 \\
&=25
\end{align*}

If you had spent at $t=0$, you have no choice but to spend at $t=2$.

The sophisticated quasi-hyperbolic discounter now knows that saving for the jacket is not available to them as they will spend at $t=1$ regardless of their initial actions. As a result, at $t=0$ they choose between the two feasible options:

Start spending at t=1:

\begin{align*}
U(x)&=0+\beta\delta *20+\beta\delta^2*10 \\
&=0.5*20+0.5*10 \\
&=15
\end{align*}

Spend:

\begin{align*}
U(x)&=10+\beta\delta *10+\beta\delta^2*10 \\
&=10+0.5*10+0.5*10 \\
&=20
\end{align*}

They start to spend at $t=0$. Contrast this with the naïve agent who chooses Save at $t=0$. The sophisticated agent would also prefer Save at $t=0$, but knows that Save is not available to them as they will spend at $t=1$.

