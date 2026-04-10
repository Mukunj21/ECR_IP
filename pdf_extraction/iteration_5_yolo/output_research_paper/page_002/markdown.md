## 2. Description of the Network Game

Let $\mathcal{G}$ be the set of finite, simple, and undirected graphs and let $g \in \mathcal{G}$. Note that $g$ is specified by the set of nodes $V=\{1,2,\cdots,n\}$ and the set of edges $E \subset V \times V$. With a slight abuse of notation, the graph $g$ will also be specified by its adjacency matrix $g$, where $g_{ij}=1$ if there is an edge between the nodes $i$ and $j$; otherwise it is zero. Let $S$ be the finite set of actions of the agents. We consider a game with payoff function $\pi:S \times S \times G \to \mathbb{R}$ played by the agents corresponding to the nodes of the graph $g$. Each agent chooses a strategy $s_i$, either pure or mixed (i.e., an element in $S$ or $\Delta$, the space of probability distributions on $S$ respectively). Hence the agents play a two-player game with those they are connected to in the network $g$. The strategy profile of the agents is denoted by $s=(s_1,s_2,\cdots,s_n)$. The network payoff of an agent $i$ is given by

$$
\pi_i(s\mid g):=\sum_{j=1}^n g_{ij}\pi(s_i,s_j\mid g)=\sum_{j\in N_i}\pi(s_i,s_j\mid g).
$$

Observe that this game played on a fixed network can also be called a local interaction game as introduced in [2, 13] (see also [6] for a survey).

**Definition 1.** A strategy profile $s^*$ is said to be a Nash equilibrium of a game played on a network if

$$
\pi_i(s^*\mid g)\ge \pi_i(s_i;s^*_{-i}\mid g)
$$

for each $i=1,2,\cdots,n$.

A Nash equilibrium in mixed strategies for a game played on a network always exists. However, we are interested in stability aspects of equilibrium along the lines of ESS in network games.

## 3. Evolutionary Stability for Games Played on Networks

Consider a strategy profile $s^*$ of the game being played on network $g$. Intuitively $s^*$ will be evolutionarily stable, that is robust to an invasion, provided when the neighbours in the network deviate to a different strategy, agents playing $s^*$ will have no incentive to deviate from it. Recall that in standard evolutionary game theory, there is a continuum of players. Hence the magnitude of the players for whom the change needs to occur is taken as a fraction of the population lying between $[0,1]$. However, this does not hold for finite population games and we need to adapt the concept of finite ESS introduced in [10] to the network context (see appendix for a brief formal description of the finite ESS notion introduced in [10]). For any $s_i \in S$ (or $\Delta(S)$), $(s_i,s_i,\cdots,s_i)$ denotes the strategy profile where every agent plays $s_i$. We now introduce evolutionary stability formally.

**Definition 2.** A strategy profile $s^*$ is said to be evolutionarily stable (ESS) in the game played on network $g$ if

1. $s^*$ is Nash equilibrium; and  
2. for every node $i \in V$ and for any $s_k(\ne s_i^*) \in S$ (or $\Delta(S)$),

$$
\frac{1}{d_i}\pi_i\!\left(s_i^*;\left(s_k,s_k,\cdots,s_k\right)\right)+\left(1-\frac{1}{d_i}\right)\pi_i(s_i^*;s_{-i}^*)\ge \pi_i(s_k;s_{-i}^*).
$$

(3.1)

*Note that when there is no confusion, for notational simplicity we drop the network $g$ when using the definition.*