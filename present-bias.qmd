# Present bias

Present bias occurs when we place additional weight on costs and benefits at the present time.

## The $\beta\delta$ model

One simple model of present bias is the quasi-hyperbolic discounting model (it is a discrete time version of hyperbolic discounting).

\begin{align*}
U_0&=u(x_0)+\beta \delta u(x_1)+\beta \delta^2 u*(x_2)+ ... + \beta \delta^T u(x_T) \\
&=u(x_0)+\beta \sum_{t=1}^{t=T}\delta^t u(x_t)
\end{align*}

$0\leq \delta \leq 1$

$0\leq \beta \leq 1$

$\beta$ is the short-term discount factor: it scales down all future dates utility.

$\delta$ is the usual discount factor.

The degree of discounting in this equation evolves over time as 1, $\beta\delta$, $\beta\delta^2$, $\beta\delta^3$, $\beta\delta^4$ and so on. This progression results in a larger discount for the first period of delay ($\beta\delta$) than the degree of discount for each subsequent period of delay ($\delta$). There is a relative weighting toward the present. Present bias of this nature can result in time inconsistency, with decisions at one point reversed at another if given the opportunity.

## Assumptions

Under the $\beta\delta$ model we are loosening the assumption of time consistency. An agent may change their initial plan through time.
However, we are maintaining many of the other assumptions that we used when we examined exponential discounting. We are maintaining the assumptions of:

- Consumption independence: Utility in period $t+k$ is independent of consumption in any other period. An outcome’s utility is unaffected by outcomes in prior or future periods.

- Stationary preferences: $U_t=U_{t+k}$. That is, the utility function is stationary across periods, that is: functional form of $U_t$ = functional form of $U_{t+1}$, $U_{t+2}$ etc.

- Utility Independence: All that matters is maximizing the sum of discounted utilities. Decision makers are assumed to have no preference for the distribution of utilities.
