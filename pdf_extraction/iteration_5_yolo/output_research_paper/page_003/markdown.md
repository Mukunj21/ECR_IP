where \(d_i\) is the degrees of player \(i\). Thus the finite network version of ESS requires the payoffs to be weighted by the degrees of the players. Note that, if \(d_i\) is large (as \(d_i \to \infty\)), then the second condition will lead to the Nash equilibrium condition. By expanding and rearranging the terms in (3.1), we can see that for pairs of players Condition 2 of the definition of ESS is equivalent to

\[
\sum_{j \in N_i} \left(\pi(s_k, s_j^*) - \pi(s_i^*, s_j^*)\right) \le \frac{1}{d_i} \sum_{j \in N_i} \left(\pi(s_i^*, s_k) - \pi(s_i^*, s_j^*)\right).
\]

(3.2)

The LHS term is agent \(i\)’s gain in the network game when he himself switches from \(s^*\), whereas the term on RHS gives the average gain if the change happens in \(i\)’s neighbourhood. Thus, under the second condition, every player prefers the change to come from the neighbourhood rather than changing her own strategy. Hence this condition can also be interpreted as robustness or rigidity of a player’s behavior towards change (or an invading mutant).

Also observe that condition 2 depends on the degree of the nodes in \(g\). To fully appreciate this point, let us consider the degree sequence of different networks. The degree sequence of a network is the sequence of degrees of the nodes in an increasing order. Clearly, different networks may have the same degree sequence. Here we identify two networks by isomorphism. But first let us recall the definition of isomorphism between two networks. Two graphs \(G\) and \(H\) are said to be isomorphic if there is a bijection \(f : G \to H\) such that if \((u,v)\) is an edge in \(G\) then \((f(u), f(v))\) is an edge in \(H\). We can construct examples of networks having the same degree sequence, that are not isomorphic. Consequently, while ESS is a refinement of Nash equilibrium, condition 2 is not entirely about the network structure — what matters is the number of neighbors or an agent’s degrees. This can be easily seen from the two networks shown below.\(^2\)

[Figure: 2-colourable Network]

Figure 1: 2-colourable Network

[Figure: 3-colourable network]

Figure 2: 3-colourable network

We can verify that the two graphs given above are not isomorphic (see [12] for the definition of isomorphisms of graphs) but the degree sequence of both the networks is \((3,2,2,2,2,2,2,2,1)\). In the above example, both the networks are connected. We can also have examples where one network is connected while the other is not. For example, we can consider a circular network with 6 nodes. Each node has degree 2. Now, we can consider the disconnected network consisting of two circles, one with four nodes and the other with 2 nodes. One can immediately see that the structure of Nash equilibria will be different in these two networks, while the condition 2 of the definition of ESS will remain same.

## 4. Evolutionary Stability in a Network Coordination Game

In this section, we consider the following coordination game played on network \(g\).

|   | R | B |
|---|---|---|
| R | (a,a) | (b,c) |
| B | (c,b) | (d,d) |