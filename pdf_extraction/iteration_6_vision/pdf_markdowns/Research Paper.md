## Start of Page 1

```markdown
## Evolutionary Stability for Games Played on Networks

Arko Chatterjeea, K.S. Mallikharjuna Raob, Sudipta Sarangic

a Bain & Company, Gurgaon 122 002, India  
b Industrial Engineering and Operations Research, Indian Institute of Technology Bombay, Mumbai 400076, India.  
c Department of Economics, Virginia Tech, Blacksburg VA 24061-0316, USA.

---

### Abstract

In this paper, we propose a notion of evolutionary stability for games played on networks. We then apply it to a coordination game played on networks.

*Keywords:* Networks, Nash Equilibrium, Evolutionary stability

*JEL:* C78, D85

---

## 1. Introduction

Evolutionary stable strategy (ESS) is the dominant equilibrium notion in evolutionary game theory. Originally it was defined in the context of infinite populations (see [7, 8]) and as noted in [9, 11], it does not hold for finite populations. Specifically, [9, pp.110] shows that ESS, as defined by Maynard Smith (see [7, 8]), can be successfully invaded by a mutant in finite populations. This difficulty motivated [10] to introduce a finite population version of ESS. Further, Schaffer [10] demonstrates that this notion is a generalisation of the standard ESS by showing that it coincides with standard ESS when the population size tends to infinity.

In this paper, we adapt the notion of finite ESS to games played on networks. In particular, we consider a situation where every agent plays a bimatrix game with each of their neighbours and their payoffs are an aggregation of the payoffs across all neighbours. However, this is not equivalent to the notion introduced by Schaffer [10] since each agent’s neighborhood (hence the network architecture) matters. Simply put, depending on their degree, every agent has a different number of neighbors and therefore faces a different finite population. Thus while this network version of ESS continues to be a refinement of Nash equilibrium, we need the condition that makes ESS robust to invasion to account for players’ degrees in a network.

To the best of our knowledge, apart from [10] the closest paper, in spirit, is by [5]. In this paper, the author address robustness of equilibria in network formation games, introduced in [1] by allowing for the addition of costless links to the network. In particular, a Nash equilibrium is defined to be k-robust if k is smallest number such that there is an agent who has incentive to deviate from the equilibrium when k costless links are added to the equilibrium network. In that sense network architecture matters for the equilibrium. Of course our equilibrium notion is very different from the one studied by [5]; but it is related since ESS is considered to be one of the ways in which we can justify Nash equilibrium play.

This paper is structured as follows. We describe our model setup in Section 2. In Section 3, we introduce evolutionary stability in network games. Section 4 focuses on general results for coordination games and Section 5 discusses the stability conditions for specific networks. Section 6 concludes.

---

*Email addresses:* akrotito@gmail.com (Arko Chatterjee), nallik.rao@iitb.ac.in (K.S. Mallikharjuna Rao), ssarangi@vt.edu (Sudipta Sarangi)  

*Preprint submitted to Elsevier*  
*January 24, 2023*
```


## Start of Page 2

```markdown
## 2. Description of the Network Game

Let $\mathcal{G}$ be the set of finite, simple, and undirected graphs and let $g \in \mathcal{G}$. Note that $g$ is specified by the set of nodes $V = \{1, 2, \cdots , n\}$ and the set of edges $E \subseteq V \times V$. With a slight abuse of notation, the graph $g$ will also be specified by its adjacency matrix $g$, where $g_{ij} = 1$ if there is an edge between the nodes $i$ and $j$ otherwise it is zero. Let $S$ be the finite set of actions of the agents. We consider a game with payoff function $\pi : S \times S \times \mathcal{G} \rightarrow \mathbb{R}$ played by the agents corresponding to the nodes of the graph $g$. Each agent chooses a strategy $s_i$, either pure or mixed (i.e., an element in $S$ or $\Delta$, the space of probability distributions on $S$ respectively). Hence the agents play a two-player game with those they are connected to in the network $g$. The strategy profile of the agents is denoted by $s = (s_1, s_2, \cdots , s_n)$. The network payoff of an agent $i$ is given by

$$
\pi_i(s \ | \ g) := \sum_{j=1}^{n} g_{ij} \pi(s_i, s_j \ | \ g) = \sum_{j \in N_i} \pi(s_i, s_j \ | \ g).
$$

Observe that this game played on a fixed network can also be called a local interaction game as introduced in [2, 13] (see also [6] for a survey).

**Definition 1.** A strategy profile $s^*$ is said to be a Nash equilibrium of a game played on a network if

$$
\pi_i(s^* \ | \ g) \geq \pi_i(s_i; s^*_{-i} \ | \ g)
$$

for each $i = 1, 2, \cdots , n$.

A Nash equilibrium in mixed strategies for a game played on a network always exists. ¹ However, we are interested in stability aspects of equilibrium along the lines of ESS in network games.

## 3. Evolutionary Stability for Games Played on Networks

Consider a strategy profile $s^*$ of the game being played on network $g$. Intuitively $s^*$ will be evolutionarily stable, that is robust to an invasion, provided when the neighbours in the network deviate to a different strategy, agents playing $s^*$ will have no incentive to deviate from it. Recall that in standard evolutionary game theory, there is a continuum of players. Hence the magnitude of the players for whom the change needs to occur is taken as a fraction of the population lying between $[0, 1]. However, this does not hold for finite population games and we need to adapt the concept of finite ESS introduced in [10] to the network context (see appendix for a brief formal description of the finite ESS notion introduced in [10]). For any $s_i \in S$ (or $\Delta(S)$), $(s_i, s_i, \cdots , s_i \ |\ n \  \text{times})$ denotes the strategy profile where every agent plays $s_i$. We now introduce evolutionary stability formally.

**Definition 2.** A strategy profile $s^*$ is said to be evolutionarily stable (ESS) in the game played on network $g$ if

1. $s^*$ is Nash equilibrium; and
2. for every node $i \in V$ and for any $s_k(\neq s^*_i) \in S$ (or $\Delta(S)$),

$$
\frac{1}{d_i} \pi_i \left( s^*_i; (s_i, s_k, \cdots , s_k) \ |\ n \ \text{times} \right) + \left(1 - \frac{1}{d_i}\right) \pi_i (s^*_i; s^*_{-i}) \geq \pi_i(s_k; s^*_{-i}).
$$

![Note that when there is no confusion, for notational simplicity we drop the network $g$ when using the definition.]
```


## Start of Page 3

```markdown
where $d_i$ is the degrees of player $i$. Thus the finite network version of ESS requires the payoffs to be weighted by the degrees of the players. Note that, if $d_i$ is large (as $d_i \rightarrow \infty$), then the second condition will lead to the Nash equilibrium condition. By expanding and rearranging the terms in (3.1), we can see that for pairs of players Condition 2 of the definition of ESS is equivalent to

$$
\sum_{j \in N_i} \left( \pi(s_k, s^*_j) - \pi(s^*_i, s^*_j) \right) \leq \frac{1}{d_i} \sum_{j \in N_i} \left( \pi(s^*_i, s_k) - \pi(s^*_i, s^*_j) \right).
$$

(3.2)

The LIIS term is agent $i$'s gain in the network game when he himself switches from $s^*_i$, whereas the term on RIIS gives the average gain if the change happens in $i$'s neighbourhood. Thus, under the second condition, every player prefers the change to come from the neighbourhood rather than changing her own strategy. Hence this condition can also be interpreted as robustness or rigidity of a player’s behavior towards change (or an invading mutant).

Also observe that condition 2 depends on the degree of the nodes in $G$. To fully appreciate this point, let us consider the degree sequence of different networks. The degree sequence of a network is the sequence of degrees of the nodes in an increasing order. Clearly, different networks may have the same degree sequence. Here we identify two networks by isomorphism. But first let us recall the definition of isomorphism between two networks. Two graphs $G$ and $H$ are said to be isomorphic if there is a bijection $f : G \rightarrow H$ such that if $(u, v)$ is an edge in $G$ then $(f(u), f(v))$ is an edge in $H$. We can construct examples of networks having the same degree sequence, that are not isomorphic. Consequently, while ESS is a refinement of Nash equilibrium, condition 2 is not entirely about the network structure — what matters is the number of neighbors or an agent’s degrees. This can be easily seen from the two networks shown below.

![Figure 1: 2-colourable Network](#)

![Figure 2: 3-colourable network](#)

We can verify that the two graphs given above are not isomorphic (see [12] for the definition of isomorphisms of graphs) but the degree sequence of both the networks is $(3, 2, 2, 2, 2, 2, 2, 1)$. In the above example, both the networks are connected. We can also have examples where one network is connected while the other is not. For example, we can consider a circular network with 6 nodes. Each node has degree 2. Now, we can consider the disconnected network consisting of two circles, one with four nodes and the other with 2 nodes. One can immediately see that the structure of Nash equilibria will be different in these two networks, while the condition 2 of the definition of ESS will remain same.

## 4. Evolutionary Stability in a Network Coordination Game

In this section, we consider the following coordination game played on network $g$.

|   | R   | B   |
|---|-----|-----|
| R | (a,a) | (b,c) |
| B | (c,b) | (d,d) |

2. A network is $k$–colourable if we can color it using $k$ distinct colors such that no two adjacent nodes have the same color.

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4366576
```


## Start of Page 4

```markdown
where, $a > c$ and $d > b$. The network payoff of agent $i$ is defined to be the sum of the payoffs he receives from the bilateral interactions with her neighbours. To characterise the pure strategy Nash equilibrium, we require some notation. The number of neighbours of $i$ playing $R$ is denoted by $d_i^R$ and the number of neighbours playing $B$ is denoted by $d_i^B$. If, under a strategy profile $s$, $\pi_i(R; s_{-i}) = \pi_i(B; s_{-i})$ happens for a player $i$, then we assume that $i$ prefers $R$ over $B$. We are, now, ready to characterise Nash equilibrium of the local interaction game.

## Proposition 1

Suppose that $s^* \in S$ is a pure Nash equilibrium profile of the game on network $G$. Then, for any player $i \in V$, if $d_i^R = 0$, then $s_i^* = B$; if $d_i^B = 0$, then $s_i^* = R$; and otherwise,

$$s_i^* = R \text{ if and only if } \frac{d_i^B}{d_i^R} \leq \frac{(a - c)}{(d - b)} \tag{4.1}$$

and

$$s_i^* = B \text{ if and only if } \frac{d_i^B}{d_i^R} > \frac{(a - c)}{(d - b)} \tag{4.2}$$

**Proof.** The proof follows from the best response analysis.

## Proposition 2

Let $s^*$ be a pure Nash equilibrium of the local interaction game, where the underlying bilateral game is coordination game defined above. Then $s^*$ is evolutionary stable if and only if for each $i$, one of the two conditions below are satisfied:

$$s_i^* = R \text{ and } d_i^R(c - a) + d_i^B(d - b) \leq \frac{d_i^R}{d_i}(b - a) \tag{4.3}$$

or

$$s_i^* = B \text{ and } d_i^R(c - a) + d_i^B(d - b) \geq \frac{d_i^B}{d_i}(d - c) \tag{4.4}$$

**Proof.** Before starting the proof, note that in the first case (i.e., when $s_i^* = R$) $d_i^R(c - a) + d_i^B(d - b) \leq 0$, while in the second case (i.e., $s_i^* = B$) $d_i^R(c - a) + d_i^B(d - b) > 0$. This follows from the Proposition 1.

Choose a player $i \in V$ such that $s_i^* = R$. Consider the strategy profile \((B, B, \cdots, B)\). The second condition of definition (3.1) (which is equivalent to (3.2)), now, translates into

$$\sum_{j \in N_i} \pi(B, s_j^*) - \pi(R, s_j^*) \leq \frac{1}{d_i} \sum_{j \in N_i} (\pi(R, B) - \pi(R, s_j^*))$$

which reduces to

$$d_i^Rc + d_i^Bd = d_i^Ra - d_i^Bb \leq -\frac{d_i^R}{d_i} a - \frac{d_i^B}{d_i} b = \frac{d_i^R}{d_i} (b - a).$$

This is equivalent to

$$d_i^R(c - a) + d_i^B(d - b) \leq \frac{d_i^R}{d_i} (b - a).$$

We will next consider the case where $s_i^* = B$. Obviously $s_k = R$ and hence, the second condition of evolutionary stability (3.1) translates into

$$\sum_{j \in N_i} \pi(R, s_j^*) - \pi(B, s_j^*) \leq \frac{1}{d_i} \sum_{j \in N_i} (\pi(R, B) - \pi(B, s_j^*))$$

which reduces to

$$d_i^Ra + d_i^Bb - d_i^Rc - d_i^Bd \leq c \frac{d_i^R}{d_i} a - \frac{d_i^B}{d_i} c = \frac{d_i^B}{d_i} (c - d).$$

---

_Page 4_

This preprint research paper has not been peer reviewed. Electronic copy available at: [https://ssrn.com/abstract=4366576](https://ssrn.com/abstract=4366576)
```

## Start of Page 5

```markdown
This is equivalent to

$$
d_i^R(a-c) + d_i^B(b-d) \leq \frac{d_i^R}{d_i^B}(c-d).
$$

This completes the proof of the proposition.

As a corollary, we have the following result.

## Corollary 1

The strategy \( (R, R, \ldots, R) \) is evolutionarily stable if and only if it is Nash equilibrium and

\[ d_i \geq \frac{a-b}{a-c} \]

for each \( i \). The strategy \( (B, B, \ldots, B) \) is evolutionarily stable if and only if \( d_i \geq \frac{c-d}{d-b} \). Thus if \( b = c \), both \( (R, R, \ldots, R) \) and \( (B, B, \ldots, B) \) are evolutionarily stable. Moreover, the network may have evolutionary stable strategies where both \( R \) and \( B \) are played by the agents in the network.

If \( b = c \), then a Nash equilibrium \( s^* \) is evolutionarily stable if and only if

\[ s_i^* = R \ \text{and} \ d_i^B \leq d_i^R \left(1 - \frac{1}{d_i}\right) \frac{a-b}{d-b} \]

or

\[ s_i^* = B \ \text{and} \ d_i^R \leq d_i^B \left(1 - \frac{1}{d_i}\right) \frac{d-b}{a-b} \]

## 5. Examples with Specific Network Architectures

In this section, we illustrate our key result using two different examples. Since degrees play a key role in our definition, in the first example we consider a regular network where everyone has the same degree. In the next example we consider a 2-hub-spoke network where agents have different degrees. Moreover the first network allows for cycles while the second one does not.

### Example 1 (Cyclical Network)

Consider a network, where every node has degree 2. This network will have two Nash equilibria \( (R, R, \ldots, R) \) and \( (B, B, \ldots, B) \).

![Figure: Circular Network with 6 Nodes](#)

Using Proposition 2, we can deduce the following result. We omit the details since the proof is straightforward.

### Proposition 3

1. The strategy profile \( (R, \ldots, R) \) is evolutionarily stable if, \( (a + b) \geq 2c \).
2. The strategy profile \( (B, \ldots, B) \) is evolutionarily stable if, \( (d + c) \geq 2b \).
3. The strategy profile \( (R, B, \ldots, R, B) \) is not evolutionarily stable while \( (R, R, B, B, \ldots) \) is evolutionary stable provided

   \[
   \frac{1}{2}(d-c) \leq c-a+d-b \leq \frac{1}{2}(b-a).
   \]
```


## Start of Page 6

```markdown
## Example 2 (Hub-Spoke Network with 2 hubs)

Consider a network where there are two nodes, say 1 and 2, who act as the two hubs. Each hub is attached to several peripheral nodes. Suppose that the node 1 is connected to \(n_1\) peripheral nodes (denoted by the set of nodes \(L_1\)) besides node 2, and node 2 is connected to \(n_2\) peripheral nodes (denoted by the set of nodes \(L_2\)) besides node 1. Thus \(N = n_1 + n_2 + 2\), \(d_1 = n_1 + 1\), \(d_2 = n_2 + 1\) and the degree of every other node is 1. This network has four possible Nash equilibria

\[
(R, R, \ldots , R), \quad (B, B, \ldots , B), \quad (R, R, R, \ldots , R, B, B, B, \ldots , B) \quad \text{and} \quad (B, B, B, \ldots , B, R, R, R, \ldots , R).
\]

\[ 
\underbrace{N \text{ times}}_{N \text{ times}} \quad \underbrace{n_1 \text{ times}}_{n_2 \text{ times}} \quad \underbrace{n_1 \text{ times}}_{n_2 \text{ times}}
\]

Note that the strategy of the leaf nodes can be different from the hub node's strategy. In fact, we can show the following.

![Figure: Hub-Spoke Network with 2 Hubs](#)

### Proposition 4

In a Hub-Spoke network, we have the following properties:

1. The strategy profile \((R, R, \ldots , R)\) is evolutionarily stable if and only if \(b \ge c\) and \(\max\{n_1, n_2\} + 1 \ge \frac{a - b}{a - c}\).

   \[
   \frac{a - b}{a - c}
   \]

2. The strategy profile \((B, B, \ldots , B)\) is evolutionarily stable if and only if \(c \ge b\) and \(\max\{n_1, n_2\} + 1 \ge \frac{d - c}{d - b}\).

   \[
   \frac{d - c}{d - b}
   \]

We now consider the Nash equilibrium \((R, R, R, \ldots , R, B, B, B, \ldots , B)\). From the previous Proposition, it is necessary that \(b = c\). Otherwise, this strategy profile \((R, R, R, \ldots , R, B, B, B, \ldots , B)\) will not be evolutionarily stable. So, from now, we will assume that \(b = c\). First, note that this strategy profile is a pure Nash equilibrium if and only if

\[
n_1 \ge \frac{d - b}{a - b} \quad \text{and} \quad n_2 \ge \frac{a - b}{d - b}
\]

Using Proposition 2, we see that \(n_1, n_2\) must satisfy

\[
\frac{n_1^2}{n_1 + 1} \ge \frac{d - b}{a - b} \quad \text{and} \quad \frac{n_2^2}{n_2 + 1} \ge \frac{a - b}{d - b}.
\]

These are quadratic inequalities in \(n_1\) and \(n_2\). With a little bit of algebra, we can see that these conditions transform into

\[
n_1 \ge \frac{d - b}{2(a - b)} + \sqrt{\frac{(d - b)^2}{2(a - b)} + \frac{d - b}{a - b}}
\]

\[
n_2 \ge \frac{a - b}{2(d - b)} + \sqrt{\frac{(a - b)^2}{2(d - b)} + \frac{a - b}{d - b}}
\]

This proves the following result.

---

This preprint research paper has not been peer reviewed. Electronic copy available at: [https://ssrn.com/abstract=4366576](https://ssrn.com/abstract=4366576)
```


## Start of Page 7

```markdown
## Proposition 5

In a hub-spoke network with 2 hubs, where the first hub has \( n_1 \) peripheral nodes and the second hub has \( n_2 \) peripheral nodes, the strategy profile \( (R, R, R, \ldots , R, B, B, B, \ldots , B) \) is evolutionarily stable if and only if \( b = c, a \geq b, d \geq c \) together with the conditions

\[
n_1 \geq \frac{d-b}{2(a-b)} + \sqrt{\left( \frac{d-b}{2(a-b)} \right)^2 + \frac{d-b}{a-b}}
\]

\[
n_2 \geq \frac{a-b}{2(d-b)} + \sqrt{\left( \frac{a-b}{2(d-b)} \right)^2 + \frac{a-b}{d-b}}
\]

By interchanging the roles of the two hubs, we can obtain the conditions (essentially the same, the only difference will be that \( n_1 \) and \( n_2 \) gets replaced) for the strategy profile \( (B, B, B, \ldots , B, R, R, R, \ldots , R) \).

## 6. Conclusion

In this paper we define the notion of ESS for games played on networks. While this is different from the standard ESS, the finite sample version of has to be adapted using player’s degrees to take network structure into account. We apply our formal definition to coordination games and illustrate it the result for a cyclic and a tree network. Let us now consider the two networks shown in Figure 1 and Figure 2. Recall that the first network is 2-colourable while the second one is 3-colourable. It can be verified that if we consider a two player, two strategy anti-coordination network game (see for instance [3, 4]), the first game will have a pure strategy equilibrium while the second game will not have a pure strategy equilibrium. Thus, if we consider anti-coordination games, the ESS will depend on the exact network architecture and degree sequence, even though condition 2 for ESS remains the same in both networks.

## Appendix A. Schaffer’s Notion of Evolutionary Stability for Finite Populations

Consider a finite population of size \( N \). The set of pure strategies of any player in this population is denoted by \( S = \{ s_1, s_2, \ldots , s_l \} \), for some \( l \in \mathbb{N} \). Let \( \Delta \) denote the corresponding set of mixed strategies. A contest of size \( C \) is the game between \( C \) randomly drawn people from the population. Let \( \pi(s_1|s_2, s_3, \ldots , s_C) \) denote the payoff of the player 1 when he faces \( C - 1 \) other players and the chosen strategies of these players is given by \( (s_1, s_2, \ldots , s_C) \in S \times S \times \cdots \times S \) (\( C \) times).

Let \( s_E \in \Delta \) be the incumbent strategy and let \( s_M (\neq s_E) \in \Delta \) be the mutant strategy that will be played by one randomly drawn agent from the chosen population of size \( C \). The payoff to the incumbent is given by

\[
\pi_E = \left( 1 - \frac{C-1}{N-1} \right) \pi(s_E|s_E, s_E, \ldots , s_E) + \left( \frac{C-1}{N-1} \right) \pi(s_E|s_M, s_E, \ldots , s_E)
\]

\[
(A.1)
\]

and the payoff to the mutant is given by

\[
\pi_M = \pi(s_M|s_E, s_E, \ldots , s_E)
\]

\[
(A.2)
\]

Following [10], \( s_E \) is said to be finite population ESS when

\[
\pi_E \geq \pi_M
\]

\[
(A.3)
\]

## References

1. Venkatesh Bala and Sanjeev Goyal. A noncooperative model of network formation. *Econometrica*, 68(5):1181–1229, 2000.

2. Lawrence E. Blume. The statistical mechanics of strategic interaction. *Games Econom. Behav.*, 5(3):387 – 424, 1993.

3. Yann Bramoullé. Anti-coordination and social interactions. *Games Econom. Behav.*, 58(1):30–49, 2007.
```


## Start of Page 8

```markdown
[4] Arko Chaterjee. *(Anti)-Coordination and Stability Perspectives in Games on Networks*. PhD thesis, Indian Institute of Technology Bombay, India, 2017.

[5] Khai Xiang Chong. Robustness in network formation games. *Preprint*, 2016.

[6] Andrea Galeotti, Sanjeev Goyal, Matthew O. Jackson, Fernando Vega-Redondo, and Leeat Yariv. Network games. *The Review of Economic Studies*, 77(1):218–244, 2010.

[7] J. Maynard Smith and G. R. Price. The logic of animal conflict. *Nature*, 246:15, 1973.

[8] John Maynard Smith. *Evolution and the theory of games*. Cambridge University Press Cambridge; New York, 1982.

[9] John G. Riley. Evolutionary equilibrium strategies. *Journal of Theoretical Biology*, 76(2):109 – 123, 1979.

[10] Mark E. Schaffer. Evolutionarily stable strategies for a finite population and a variable contest size. *Journal of Theoretical Biology*, 132(4):469 – 478, 1988.

[11] William L. Vickery. How to cheat against a simple mixed strategy ess. *Journal of Theoretical Biology*, 127(2):133 – 139, 1987.

[12] Douglas B. West. *Introduction to graph theory*. Prentice Hall, Inc., Upper Saddle River, NJ, 1996.

[13] H. Peyton Young. *Individual Strategy and Social Structure: An Evolutionary Theory of Institutions*. Princeton University Press, 2001.
```


