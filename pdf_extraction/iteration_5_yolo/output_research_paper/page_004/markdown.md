where, \(a > c\) and \(d > b\). The network payoff of agent \(i\) is defined to be the sum of the payoffs he receives from the bilateral interactions with her neighbours. To characterise the pure strategy Nash equilibrium, we require some notation. The number of neighbours of \(i\) playing \(R\) is denoted by \(d_i^R\) and the number of neighbours playing \(B\) is denoted by \(d_i^B\). If, under a strategy profile \(s\), \(\pi_i(R; s_{-i}) = \pi_i(B; s_{-i})\) happens for a player \(i\), then we assume that \(i\) prefers \(R\) over \(B\). We are, now, ready to characterise Nash equilibrium of the local interaction game.

Proposition 1. Suppose that \(s^* \in S\) is a pure Nash equilibrium profile of the game on network \(G\). Then, for any player \(i \in V\), if \(d_i^R = 0\), then \(s_i^* = B\); if \(d_i^B = 0\), then \(s_i^* = R\); and otherwise,

\[
s_i^* = R \text{ if and only if } \frac{d_i^B}{d_i^R} \le \frac{(a - c)}{(d - b)}
\qquad (4.1)
\]

and

\[
s_i^* = B \text{ if and only if } \frac{d_i^B}{d_i^R} > \frac{(a - c)}{(d - b)}.
\qquad (4.2)
\]

PROOF. The proof follows from the best response analysis.

Proposition 2. Let \(s^*\) be a pure Nash equilibrium of the local interaction game, where the underlying bilateral game is coordination game defined above. Then \(s^*\) is evolutionary stable if and only if for each \(i\), one of the two conditions below are satisfied:

\[
s_i^* = R \text{ and } d_i^R(c - a) + d_i^B(d - b) \le \frac{d_i^R}{d_i}(b - a)
\qquad (4.3)
\]

or

\[
s_i^* = B \text{ and } d_i^R(c - a) + d_i^B(d - b) \ge \frac{d_i^B}{d_i}(d - c).
\qquad (4.4)
\]

PROOF. Before starting the proof, note that in the first case (i.e., when \(s_i^* = R\)) \(d_i^R(c - a) + d_i^B(d - b) \le 0\), while in the second case (i.e., \(s_i^* = B\)) \(d_i^R(c - a) + d_i^B(d - b) > 0\). This follows from the Proposition 1.

Choose a player \(i \in V\) such that \(s_i^* = R\). Consider the strategy profile \((B, B, \cdots, B)\). The second condition of definition (3.1) (which is equivalent to (3.2)), now, translates into

\[
\sum_{j \in N_i} \pi(B, s_j^*) - \pi(R, s_j^*) \le \frac{1}{d_i} \sum_{j \in N_i} \bigl(\pi(R, B) - \pi(R, s_j^*)\bigr)
\]

which reduces to

\[
d_i^R c + d_i^B d - d_i^R a - d_i^B b \le b - \frac{d_i^R}{d_i} a - \frac{d_i^B}{d_i} b = \frac{d_i^R}{d_i}(b - a).
\]

This is equivalent to

\[
d_i^R(c - a) + d_i^B(d - b) \le \frac{d_i^R}{d_i}(b - a).
\]

We will next consider the case where \(s_i^* = B\). Obviously \(s_k = R\) and hence, the second condition of evolutionary stability (3.1) translates into

\[
\sum_{j \in N_i} \pi(R, s_j^*) - \pi(B, s_j^*) \le \frac{1}{d_i} \sum_{j \in N_i} \bigl(\pi(B, R) - \pi(B, s_j^*)\bigr)
\]

which reduces to

\[
d_i^R a + d_i^B b - d_i^R c - d_i^B d \le c - \frac{d_i^R}{d_i} c - \frac{d_i^B}{d_i} d = \frac{d_i^B}{d_i}(c - d).
\]