# Present bias examples

## Example 1

Choice 1: Would you like \$100 today or \$110 next week? 

Choice 2: Would you like \$100 next week or \$110 in two weeks? 

### The exponential discounter

Suppose we have an exponential discounter with $\delta=0.95$ and utility each period of $U(x_n)=x_n$.

Choice 1:  Would this agent prefer \$100 today ($t=0$) or \$110 next week ($t=1$)?

We have already worked through this problem and determined that an exponential discounter will prefer to receive \$110 next week.

Choice 2: Would this agent prefer \$100 next week ($t=1$) or \$110 in two weeks ($t=2$)? 

Similarly, we previously determined that the exponential discounter will prefer to receive \$110 in two weeks. The set of decisions across Choice 1 and Choice 2 are time consistent.

### The present-biased agent

Suppose we have a present biased agent with $\delta=0.95$, $\beta=0.95$ and utility each period of $U(x_n)=x_n$.

Choice 1: Would this agent prefer \$100 today ($t=0$) or \$110 next week ($t=1$)? 

\begin{align*}
U_0(0,\$100)&=u(\$100)\\
&-100
\end{align*}

\begin{align*}
U_0(1,\$110)&=\beta\delta u(\$110) \\
&=0.95*0.95*110 \\
&=99.275
\end{align*}
        
As $U_0(0,\$100) > U_0(1,\$110)$, the present-biased agent will prefer to receive \$100 this week.

Choice 2: Would this agent prefer \$100 next week ($t=1$) or \$110 in two weeks ($t=2$)? 

\begin{align*}
U_0(1,\$100)&=\beta\delta u(\$100) \\
&=0.95*0.95*100 \\
&=90.25
\end{align*}

\begin{align*}
U_0(2,\$110)&=\beta\delta^2 u(\$110) \\
&=0.95*0.95^2*110 \\
&=94.31
\end{align*}

As $U_0(1,\$100) < U_0(2,\$110)$, the present-biased agent will prefer to receive \$110 in two weeks.

Putting those two choices together:

Choice 1: The present-biased agent will prefer \$100 now to \$110 in one week. Their preference for benefits now ($\beta$) leads them to prefer the immediate payoff.

Choice 2: The present-biased agent will prefer \$110 in two weeks to \$100 in one week. They are willing to wait longer for a larger reward, with both outcomes in the future and subject to the short-term discount ($\beta$).

Consider what would happen if they selected the \$110 in two weeks in Choice 2, but after one week were asked if they would like to reconsider their choice. They are effectively being offered Choice 1. This would then lead them to change their mind and take the immediate \$100.

This combination of decisions is time inconsistent. The agent’s actions are not consistent with their own initial plan.
