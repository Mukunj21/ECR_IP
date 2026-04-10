Example 2 (Hub-Spoke Network with 2 hubs). Consider a network where there are two nodes, say 1 and 2, who act as the two hubs. Each hub is attached to several peripheral nodes. Suppose that the node 1 is connected to n1 peripheral nodes (denoted by the set of nodes L1) besides node 2, and node 2 is connected to n2 peripheral nodes (denoted by the set of nodes L2) besides node 1. Thus N = n1 + n2 + 2, d1 = n1 + 1, d2 = n2 + 1 and the degree of every other node is 1. This network has four possible Nash equilibria (R, R, · · ·, R), (B, B, · · ·, B), (R, R, R, · · ·, R, B, B, B, · · ·, B) and (B, B, B, · · ·, B, R, R, R, · · ·, R). Note that the strategy of the leaf nodes can be different from the hub node’s strategy. In fact, we can show the following.

[Figure: Hub-Spoke Network with 2 Hubs]

Proposition 4. In a Hub-Spoke network, we have the following properties

1. The strategy profile (R, R, · · ·, R) is evolutionarily stable if and only if b ≥ c and max{n1, n2} + 1 ≥ (a-b)/(a-c).
2. The strategy profile (B, B, · · ·, B) is evolutionarily stable if and only if c ≥ b and max{n1, n2} + 1 ≥ (d-c)/(d-b).

We now consider the Nash equilibrium (R, R, R, · · ·, R, B, B, B, · · ·, B). From the previous Proposition, it is necessary that b = c. Otherwise, this strategy profile (R, R, R, · · ·, R, B, B, B, · · ·, B) will not be evolutionarily stable. So, from now, we will assume that b = c. First, note that this strategy profile is a pure Nash equilibrium if and only if

n1 ≥ (d-b)/(a-b) and n2 ≥ (a-b)/(d-b).

Using Proposition 2, we see that n1, n2 must satisfy

n1²/(n1 + 1) ≥ (d-b)/(a-b) and n2²/(n2 + 1) ≥ (a-b)/(d-b).

These are quadratic inequalities in n1 and n2. With a little bit of algebra, we can see that these conditions transform into

n1 ≥ (d-b)/(2(a-b)) + √(((d-b)/(2(a-b)))² + (d-b)/(a-b)),
n2 ≥ (a-b)/(2(d-b)) + √(((a-b)/(2(d-b)))² + (a-b)/(d-b)).

This proves the following result.