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
| Spend | 10  | 10  | 10  |

At $t=0$ the highest discounted utility is for Save. You plan to save for the jacket.

Save:




```{=tex}
\begin{align*}
U(x)&=0+\beta\delta *0+\beta\delta^2*45 \\
&=0.5*45 \\
&=22.5
\end{align*}
```



Spend:




```{=tex}
\begin{align*}
U(x)&=10+\beta\delta *10+\beta\delta^2*10 \\
&=10+0.5*10+0.5*10 \\
&=20
\end{align*}
```



One month now passes. You have saved for a month. You could now spend both your savings from last month and this month, giving a short term boost, or keep saving for your jacket.

|         | t=1 | t=2 |
|---------|:---:|:---:|
| Save    |  0  | 45  |
| *Spend* | 20  | 10  |

At $t=1$ spending now has the highest discounted utility. After saving for the first period, you spend.

Save:




```{=tex}
\begin{align*}
U(x)&=0+\beta\delta*45 \\
&=0.5*45 \\
&=22.5
\end{align*}
```



Spend:




```{=tex}
\begin{align*}
U(x)&=20+\beta\delta *10 \\
&=20+0.5*10 \\
&=25
\end{align*}
```



You spend despite initially wanting to save.

Now let's consider this problem from the point of view of a sophisticated present-biased agent. They see their full choice set as:

|                       | t=0 | t=1 | t=2 |
|-----------------------|:---:|:---:|:---:|
| Save                  |  0  |  0  | 45  |
| Start spending at t=1 |  0  | 20  | 10  |
| Spend                 | 10  | 10  | 10  |

You work backward through time. At $t=2$, you will buy the jacket.

The utility of each option at $t=1$ is as follows:

Save:




```{=tex}
\begin{align*}
U(x)&=0+\beta\delta*45 \\
&=0.5*45 \\
&=22.5
\end{align*}
```



Spend:




```{=tex}
\begin{align*}
U(x)&=20+\beta\delta *10 \\
&=20+0.5*10 \\
&=25
\end{align*}
```



If you had spent at $t=0$, you have no choice but to spend at $t=2$.

The sophisticated quasi-hyperbolic discounter now knows that saving for the jacket is not available to them as they will spend at $t=1$ regardless of their initial actions. As a result, at $t=0$ they choose between the two feasible options:

Start spending at t=1:




```{=tex}
\begin{align*}
U(x)&=0+\beta\delta *20+\beta\delta^2*10 \\
&=0.5*20+0.5*10 \\
&=15
\end{align*}
```



Spend:




```{=tex}
\begin{align*}
U(x)&=10+\beta\delta *10+\beta\delta^2*10 \\
&=10+0.5*10+0.5*10 \\
&=20
\end{align*}
```



They start to spend at $t=0$. Contrast this with the naïve agent who chooses Save at $t=0$. The sophisticated agent would also prefer Save at $t=0$, but knows that Save is not available to them as they will spend at $t=1$.

Now consider what the sophisticated agent may do in the presence of lay-by.

For payment of an administrative fee equivalent to 1 unit of utility and an initial deposit (your savings in $t=0$), you reserve the jacket, preventing you from spending that money in period 2. The new set of options is:

|                       | t=0 | t=1 | t=2 |
|-----------------------|:---:|:---:|:---:|
| Save                  |  0  |  0  | 45  |
| Start spending at t=1 |  0  | 20  | 10  |
| Spend                 | 10  | 10  | 10  |
| Lay-by                | -1  |  0  | 45  |

The lay-by option is strictly worse than Save. But what happens if lay-by is available to the sophisticated present-biased agent?

Again, working backward, at $t=2$, the agent buys the jacket.

At $t=1$, by the same logic we looked at previously, they spend if they are able to do so. That eliminates Save from their choice set. At \$ $t=0$, they now compare the feasible options:

Start spending at t=1:




```{=tex}
\begin{align*}
U(x)&=0+\beta\delta *20+\beta\delta^2*10 \\
&=0.5*20+0.5*10 \\
&=15
\end{align*}
```



Spend:




```{=tex}
\begin{align*}
U(x)&=10+\beta\delta *10+\beta\delta^2*10 \\
&=10+0.5*10+0.5*10 \\
&=20
\end{align*}
```



Lay-by:




```{=tex}
\begin{align*}
U(x)&=-1+\beta\delta *0+\beta\delta^2*45 \\
&=-1+0.5*0+0.5*45 \\
&=21.5
\end{align*}
```



Lay-by is the preferred option at $t=0$. As it binds the agent in the future, they are able to stick to this plan.

Note that lay-by is strictly worse than Save as the agent must pay the administrative fee. But it is chosen by the sophisticated quasi-hyperbolic discounter as the only feasible way to get their jacket. Without lay-by they will spend at $t=1$ and end up with lower utility from the perspective of their $t=0$ self.

### Depressing the value of the bad course of action

[stickK](https://www.stickk.com) is a online platform that enables people to commit to future courses of action. stickK works as follows:

1.  You state a time-based goal, such as not smoking during the next month, losing 5kg over the next 90 days, or writing the next chapter of your PhD thesis by Christmas.

2.  You commit a stake that will be paid to a charity (or an anti-charity) if you fail to meet your goal.

3.  At the stated time you report (or a referee appointed by you reports) whether you have met your goal.

4.  If you fail to report or report that you failed to meet your goal, your credit card is debited by the staked amount.

![](img/stickk.jpg)

The following is an illustration of how it works mathematically.

A sophisticated present-biased agent with $\delta=1$ and $\beta=1/2$ enjoys smoking. Smoking gives utility of 5. However, the agent also likes being healthy. Higher health gives utility of 8.

At $t=0$ the agent is deciding whether to smoke over the next month ($t=1$). If the agent doesn't smoke, it will have better health at $t=2$.

The sophisticated agent works backward through time. At $t=1$ its payoffs are:




```{=tex}
\begin{align*}
U_1(smoking)&=5 \\
\\
U_1(healthy)&=\beta\delta*8 \\
&=4
\end{align*}
```



The agent decides to smoke.

As a result, at $t=0$, knowing that it will cave at $t=1$, the agent doesn't bother committing to not smoking, even though from the perspective of $t=0$ refraining from smoking is the better option:




```{=tex}
\begin{align*}
U_0(smoking)&=\beta\delta*5 \\
&=2.5
\\
U_0(healthy)&=\beta\delta^2*8 \\
&=4
\end{align*}
```



But now suppose the agent learns about stickK. The agent now has the option of staking a sum at $t=0$ to prevent it from smoking. The agent decides to stake an amount equivalent to utility 5 that would be incurred at $t=2$.

Working backward through time, the agent knows that at $t=1$ if it has not staked any money with stickK, it will smoke. But what if it has?




```{=tex}
\begin{align*}
U_1(stickK+smoking)&=5-\beta\delta*5 \\
&=2.5
\\
U_1(stickK+healthy)&=\beta\delta*8 \\
&=4
\end{align*}
```



The agent would refrain from smoking at $t=1$ due to the penalty it would have to pay.

This means the agent's options at $t=0$ are effectively:




```{=tex}
\begin{align*}
U_0(smoking)&=\beta\delta*5 \\
&=2.5
\\
U_0(stickK+healthy)&=\beta\delta^2*8 \\
&=4
\end{align*}
```



The agent chooses to commit using stickK.

For a problem of this form the agent could always successfully use stickK to commit to any action. The agent just needs to make the stake high enough.

### Increasing the value of the optimal action: temptation bundling

“Temptation bundling” involves increasing the value of the optimal course of action by adding a temptation to that course.

Consider the following example.

Beth has the choice between the following options:

- Exercising at $t=0$ (utility = 0) which leads her to being healthy and happy at time 1 (utility = 12)

- Watching television at time 0 (utility = 6) and being unhealthy and unhappy at time 1 (utility = 0) 

Beth discounts the future quasi-hyperbolically. Beth’s $\beta=1/2$ and her $\delta=2/3$. Does Beth exercise? 

We solve as follows:




```{=tex}
\begin{align*}
U_0(exercise)&=u(x_0)+\beta\delta u(x_1) \\
&=0+\frac{1}{2}*{2}{3}*12 \\
&=4
\\
U_0(television)&=u(x_0)+\beta\delta u(x_1) \\
&=6+\frac{1}{2}*{2}{3}*0 \\
&=6
\end{align*}
```




Beth chooses to watch television.

But what if Beth loved massages and remembers she has a massage voucher she has been saving? What if she decides that if she exercises today, she will go for a massage straight after? Let us assume that the utility of a massage is 3.

We solve as follows:




```{=tex}
\begin{align*}
U_0(exercise+massage)&=u(x_0)+\beta\delta u(x_1) \\
&=3+\frac{1}{2}*{2}{3}*12 \\
&=7
\\
U_0(television)&=u(x_0)+\beta\delta u(x_1) \\
&=6+\frac{1}{2}*{2}{3}*0 \\
&=6
\end{align*}
```




Beth now chooses to exercise.

This example is not strictly a commitment device as Beth could cheat. Beth could watch television and get the massage. But people are often good at creating “mental accounts” by which they make certain money or activities out-of-bounds unless certain conditions are met.

