<figure>
</figure>


# Evolutionary Stability for Games Played on Networks

Arko Chatterjeeª, K.S. Mallikarjuna Raob, Sudipta Sarangic

@Bain & Company, Gurgaon 122 002, India
b Industrial Engineering and Operations Research, Indian Institute of Technology Bombay, Mumbai 400076, India.
" Department of Economics, Virginia Tech, Blacksburg VA 24061-0316, USA.


## Abstract

In this paper, we propose a notion of evolutionary stability for games played on networks. We then apply
it to a coordination game played on networks.

Keywords: Networks, Nash Equilibrium, Evolutionary stability

JEL: C78, D85


## 1. Introduction

Evolutionary stable strategy (ESS) is the dominant equilibrium notion in evolutionary game theory.
Originally it was defined in the context of infinite populations (see [7, 8]) and as noted in [9, 11], it does not
hold for finite populations. Specifically, [9, pp.110] shows that ESS, as defined by Maynard Smith (see [7, 8]),
can be successfully invaded by a mutant in finite populations. This difficulty motivated [10] to introduce a
finite population version of ESS. Further, Schaffer [10] demonstrates that this notion is a generalisation of
the standard ESS by showing that it coincides with standard ESS when the population size tends to infinity.
In this paper, we adapt the notion of finite ESS to games played on networks. In particular, we consider a
situation where every agent plays a bimatrix game with each of their neighbours and their payoffs are an
aggregation of the payoffs across all neighbours. However, this is not equivalent to the notion introduced
by Schaffer [10] since each agent's neighborhood (hence the network architecture) matters. Simply put,
depending on their degree, every agent has a different number of neighbors and therefore faces a different
finite population. Thus while this network version of ESS continues to be a refinement of Nash equilibrium,
we need the condition that makes ESS robust to invasion to account for players' degrees in a network.

10

<!-- PageNumber="20" -->

To the best of our knowledge, apart from [10] the closest paper, in spirit, is by [5]. In this paper, the
author address robustness of equilibria in network formation games, introduced in [1] by allowing for the
addition of costless links to the network. In particular, a Nash equilibrium is defined to be k-robust if k
is smallest number such that there is an agent who has incentive to deviate from the equilibrium when
k costless links are added to the equilibrium network. In that sense network architecture matters for the
equilibrium. Of course our equilibrium notion is very different from the one studied by [5]; but it is related
since ESS is considered to be one of the ways in which we can justify Nash equilibrium play.

This paper is structured as follows. We describe our model setup in Section 2. In Section 3, we introduce
evolutionary stability in network games. Section 4 focuses on general results for coordination games and
Section 5 discuss the stability conditions for specific networks. Section 6 concludes.

O

<!-- PageFooter="Email addresses: arkotito@gmail.com (Arko Chatterjee), mallik.rao@iitb.ac.in (K.S. Mallikarjuna Rao), ssarangi@vt.edu (Sudipta Sarangi )" -->

Q

<!-- PageFooter="Preprint submitted to Elsevier" -->
<!-- PageFooter="January 24, 2023" -->
<!-- PageFooter="This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4366576" -->
<!-- PageBreak -->


<figure>
</figure>


## 2. Description of the Network Game

Let G be the set of finite, simple, and undirected graphs and let g E G. Note that g is specified by the
set of nodes V = {1,2, ... ,n} and the set of edges E c V x V. With a slight abuse of notation, the graph g
will also be specified by its adjacency matrix g, where gij = 1 if there is an edge between the nodes i and j;
otherwise it is zero. Let S be the finite set of actions of the agents. We consider a game with payoff function
TT : Sx SxG -> R played by the agents corresponding to the nodes of the graph g. Each agent chooses
a strategy si, either pure or mixed (i.e., an element in S or 4, the space of probability distributions on S
respectively). Hence the agents play a two-player game with those they are connected to in the network g.
The strategy profile of the agents is denoted by s = ($1, 82, ... , Sn). The network payoff of an agent i is
given by

Ti(s | g) := >gijT (Si, Sj | g) = >™(Si, Sj | g).
j=1
n
jENi

Observe that this game played on a fixed network can also be called a local interaction game as introduced
in [2, 13] (see also [6] for a survey).

Definition 1. A strategy profile s* is said to be a Nash equilibrium of a game played on a network if

Ti(s* | g) ≥ Ti(si; s *; 1g)

for each i = 1,2, ... , n.

A Nash equilibrium in mixed strategies for a game played on a network always exists.1 However, we are
interested in stability aspects of equilibrium along the lines of ESS in network games.

30


## 3. Evolutionary Stability for Games Played on Networks

Consider a strategy profile s* of the game being played on network g. Intuitively s* will be evolutionarily
stable, that is robust to an invasion, provided when the neighbours in the network deviate to a different
strategy, agents playing s* will have no incentive to deviate from it. Recall that in standard evolutionary
game theory, there is a continuum of players. Hence the magnitude of the players for whom the change
needs to occur is taken as a fraction of the population lying between [0, 1]. However, this does not hold for
finite population games and we need to adapt the concept of finite ESS introduced in [10] to the network
context (see appendix for a brief formal description of the finite ESS notion introduced in [10]). For any
Si E S (or A(S)), (Si, Si, ... , Si) denotes the strategy profile where every agent plays si. We now introduce

n times

<!-- PageNumber="40 evolutionary stability formally." -->

Definition 2. A strategy profile s* is said to be evolutionarily stable (ESS) in the game played on network
g if

1\. s* is Nash equilibrium; and

2\. for every node i E V and for any sk(# s;) € S (or A(S)),
1
TTTi( s; (Sk, 8kg ... , Sk) + (1-T) Ti (8; +i) ≥ Ti(Sk; S+).
di
n-1 times
1
(3.1)

1 Note that when there is no confusion, for notational simplicity we drop the network g when using the definition.

<!-- PageNumber="2" -->
<!-- PageFooter="This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4366576" -->
<!-- PageBreak -->

where di is the degrees of player i. Thus the finite network version of ESS requires the payoffs to be weighted
by the degrees of the players. Note that, if di is large (as di > >), then the second condition will lead to
the Nash equilibrium condition. By expanding and rearranging the terms in (3.1), we can see that for pairs
of players Condition 2 of the definition of ESS is equivalent to

2

(TT(Sk, S;) - TT(s;, s;))

jENi

Esta

\>
jENi

1
di
(TT(S;, Sk) - TT(s;, 8;)).
(3.2)

The LHS term is agent i's gain in the network game when he himself switches from s*, whereas the term on
RHS gives the average gain if the change happens in i's neighbourhood. Thus, under the second condition,
every player prefers the change to come from the neighbourhood rather than changing her own strategy.
Hence this condition can also be interpreted as robustness or rigidity of a player's behavior towards change
(or an invading mutant).

50

Also observe that condition 2 depends on the degree of the nodes in g. To fully appreciate this point, let
us consider the degree sequence of different networks. The degree sequence of a network is the sequence of
degrees of the nodes in an increasing order. Clearly, different networks may have the same degree sequence.
Here we identify two networks by isomorphism. But first let us recall the definition of isomorphism between
two networks. Two graphs G and H are said to be isomorphic if there is a bijection f : G -> H such that if
(u, v) is an edge in G then (f(u), f(v)) is an edge in H. We can construct examples of networks having the
same degree sequence, that are not isomorphic. Consequently, while ESS is a refinement of Nash equilibrium,
condition 2 is not entirely about the network structure - what matters is the number of neighbors or an
agent's degrees. This can be easily seen from the two networks shown below.2


<figure>
<figcaption>Figure 1: 2-colourable Network</figcaption>

C

D

E

A

B

I

F

G

H

</figure>


<figure>
<figcaption>Figure 2: 3-colourable network</figcaption>

A

C

D

E

F

G

H

I

B

</figure>


<!-- PageNumber="60" -->

We can verify that the two graphs given above are not isomorphic (see [12] for the definition of iso-
morphisms of graphs) but the degree sequence of both the networks is (3, 2, 2, 2, 2, 2, 2, 2, 1). In the above
example, both the networks are connected. We can also have examples where one network is connected
while the other is not. For example, we can consider a circular network with 6 nodes. Each node has degree
2. Now, we can consider the disconnected network consisting of two circles, one with four nodes and the
other with 2 nodes. One can immediately see that the structure of Nash equilibria will be different in these
two networks, while the condition 2 of the definition of ESS will remain same.


## 4. Evolutionary Stability in a Network Coordination Game

In this section, we consider the following coordination game played on network g.


<table>
<tr>
<th></th>
<th>R</th>
<th>B</th>
</tr>
<tr>
<td>R</td>
<td>(a,a)</td>
<td>(b,c)</td>
</tr>
<tr>
<td>B</td>
<td>(c,b)</td>
<td>(d,d)</td>
</tr>
</table>


2 A network is k-colourable if we can color it using k distinct colors such that no two adjacent nodes have the same color.

<!-- PageNumber="3" -->
<!-- PageFooter="This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4366576" -->
<!-- PageBreak -->

70

where, a > c and d > b. The network payoff of agent i is defined to be the sum of the payoffs he receives
from the bilateral interactions with her neighbours. To characterise the pure strategy Nash equilibrium,
we require some notation. The number of neighbours of i playing R is denoted by d" and the number of
neighbours playing B is denoted by d2. If, under a strategy profile s, Ti(R; s_i) = Ti(B; s -¿ ) happens for
a player i, then we assume that i prefers R over B. We are, now, ready to characterise Nash equilibrium of
the local interaction game.

Proposition 1. Suppose that s* E S is a pure Nash equilibrium profile of the game on network G. Then,
for any player i E V, if dp = 0, then s; = B; if d = 0, then s; = R; and otherwise,

s+ = R if and only if R ≤ a - c)
(4.1)

dB
(d b)

and

st = B if and only if IR > (d. - 6).
dB
dR
(d b)
(a c)

(4.2)

PROOF. The proof follows from the best response analysis.

Proposition 2. Let s* be a pure Nash equilibrium of the local interaction game, where the underlying
bilateral game is coordination game defined above. Then s* is evolutionary stable if and only if for each i,
one of the two conditions below are satisfied:

s+ = R and d} (c - a) + d? (d - b) ≤ i (b-a)
(4.3)

or

st = B and de(c- a) + d3 (d - b) ≥ 1 (d-c).

di
dB
(4.4)

PROOF. Before starting the proof, note that in the first case (i.e., when s; = R) dR (c- a) + d? (d -b) ≤ 0,
while in the second case (i.e., s; = B) dR(c-a) +d?(d-b) > 0. This follows from the Proposition 1.

Choose a player i E V such that s; = R. Consider the strategy profile (B, B, ... , B). The second
n times

condition of definition (3.1) (which is equivalent to (3.2)), now, translates into

jENi
TT(B, s;) - T(R, s;) ≤ __ (T(R,B)-T(R, s;))
jENi
di

which reduces to

dc+d;d-da-dabsb-cia-ib=(b-a).
di
di

di

This is equivalent to

d?(c-a) + d}(d-b) ≤di-(b-a).
dR
di

We will next consider the case where s; = B. Obviously Sk = R and hence, the second condition of
evolutionary stability (3.1) translates into

jENi
TT(R, s;)- T(B, s;) ≤ __ (T(B,R)-T(B, s;))
di
1
jENi
dR
dB
dB
di
di
di

which reduces to

da+db-dic-d d<c-ic-id=1(c-d).

<!-- PageNumber="4" -->
<!-- PageFooter="This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4366576" -->

1

di
dR

<!-- PageBreak -->


<figure>
</figure>


This is equivalent to

d?(a-c) + d; (b-d) ≤ 1 (c-d).
di
dB

This completes the proof of the proposition.

As a corollary, we have the following result.

80

Corollary 1. The strategy (R, R, ... , R) is evolutionarily stable if and only if it is Nash equilibrium and
n times

di ≥ a-b for each i. The strategy (B, B, ... , B) is evolutionarily stable if and only if di ≥ 2-6. Thus
if b = c, both (R, R, ... , R) and (B, B, ... , B) are evolutionarily stable. Moreover, the network may have
n times
n times
n times
evolutionary stable strategies where both R and B are played by the agents in the network.

If b = c, then a Nash equilibrium s* is evolutionarily stable if and only if

s+ = R and d" { dR (1 --
1
di

a - b
d - b

or

$ = B and dR & d? (1 --
di

d - b
a - b
.


## 5. Examples with Specific Network Architectures

In this section, we illustrate our key result using two different examples. Since degrees play a key role
in our definition, in the first example we consider a regular network where everyone has the same degree.
In the next example we consider a 2-hub-spoke network where agents have different degrees. Moreover the
first network allows for cycles while the second one does not.

Example 1 (Cyclical Network). Consider a network, where every node has degree 2. This network will
have two Nash equilibria (R, R, ... , R) and (B, B, ... , B).

N times

N times


<figure>
<figcaption>Figure 3: Circular Network with 6 Nodes</figcaption>

C2

C1

C3

C6

C4

C5

</figure>


90

Using Proposition 2, we can deduce the following result. We omit the details since the proof is straight
forward.

Proposition 3. 1. The strategy profile (R, ... , R) is evolutionarily stable if, (a + b) ≥ 2c.

2\. The strategy profile (B, ... , B) is evolutionarily stable if, (d + c) ≥ 2b.

3\. The strategy profile (R, B, ... , R, B) is not evolutionarily stable while (R, R, B, B, ... ) is evolutionary
stable provided

Q

1

1

5(d-c) <c-a+d-bs- (b-a).

<!-- PageNumber="5" -->
<!-- PageFooter="This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4366576" -->
<!-- PageBreak -->

Example 2 (Hub-Spoke Network with 2 hubs). Consider a network where there are two nodes, say
1 and 2, who act as the two hubs. Each hub is attached to several peripheral nodes. Suppose that the
node 1 is connected to n1 peripheral nodes (denoted by the set of nodes L1) besides node 2, and node 2 is
connected to n2 peripheral nodes (denoted by the set of nodes L2) besides node 1. Thus N = n1 + n2 + 2,
d1 = n1+1, d2 = n2+1 and the degree of every other node is 1. This network has four possible Nash equilibria
(R, R, ... , R), (B, B, ... , B), (R, R, R, ... , R, B, B, B, ... , B) and (B, B, B, ... , B, R, R, R, ... , R). Note

100
☒ ☒

N times

N times

nı times

n2 times
nı times
n2 times
that the strategy of the leaf nodes can be different from the hub node's strategy. In fact, we can show the
following.


<figure>
<figcaption>Figure 4: Hub-Spoke Network with 2 Hubs</figcaption>
</figure>


Proposition 4. In a Hub-Spoke network, we have the following properties

1\. The strategy profile (R, R, ... , R) is evolutionarily stable if and only if b > c and max{n1, n2} + 1 >
a-b
☒
N times

a-c'

2\. The strategy profile (B, B, ... , B) is evolutionarily stable if and only if c > b and max{n1, n2} + 1 >
☒
N times

d-c
d-b .

We now consider the Nash equilibrium (R, R, R, ... , R, B, B, B, ... , B). From the previous Proposition,
nı times
n2 times

it is necessary that b = c. Otherwise, thi strategy profile (R, R, R, ... , R, B, B, B, ... , B) will not be evo-
lutionarily stable. So, from now, we will assume that b = c. First, note that this strategy profile is a pure
n2 times
Nash equilibrium if and only if
nı times
d - b
a - b

Using Proposition 2, we see that n1, n2 must satisfy

n1 2 and n2 gb
a - b
d - b
a - b

n2
n2+1 - d -b
2

a - b

n1+1
and 12 >

These are quadratic inequalities in n1 and n2. With a little bit of algebra, we can see that these conditions
transform into

n1 2
-2 (a - b) + V (2 (a- b)
d - b

d - b
a - b'

22>

a - b
2(d - b)
+

V
d - b

a - b
2(d - b)

2

\+
\+
a - b
d - b
.

This proves the following result.

<!-- PageNumber="6" -->
<!-- PageFooter="This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4366576" -->
<!-- PageBreak -->

Proposition 5. In a hub-spoke network with 2 hubs, where the first hub has ni peripheral nodes and the
second hub has n2 peripheral nodes, the strategy profile (R, R, R, ... , R, B, B, B, ... , B) is evolutionarily

nı times
n2 times

stable if and only if b = c, a > b, d > c together with the conditions

d - b

1 - 2 (a - b) + V (2 (a- b) + - 6

n2 >

a - b
2(d - b)

\+

V
d - b
a - b
2(d - b)

2
2

d b
d - b
a - b

110

By interchanging the roles of the two hubs, we can obtain the conditions (essentially the same, the only
difference will be that n1 and n2 gets replaced) for the strategy profile (B, B, B, ... , B, R, R, R, ... , R).
nı times
n2 times


## 6. Conclusion

In this paper we define the notion of ESS for games played on networks. While this is different from the
standard ESS, the finite sample version of has to be adapted using player's degrees to take network structure
into account. We apply our formal definition to coordination games and illustrate it the result for a cyclic
and a tree network. Let us now consider the two networks shown in Figure 1 and Figure 2. Recall that the
first network is 2-colourable while the second one is 3-colourable. It can be verified that if we consider a two
player, two strategy anti-coordination network game (see for instance [3, 4]), the first game will have a pure
strategy equilibrium while the second game will not have a pure strategy equilibrium. Thus, if we consider
anti-coordination games, the ESS will depend on the exact network architecture and degree sequence, even
though condition 2 for ESS remains the same in both networks.

120


## Appendix A. Schaffer's Notion of Evolutionary Stability for Finite Populations

Consider a finite population of size N. The set of pure strategies of any player in this population is
denoted by S = {$1, 82, ... , St}, for some t E N. Let A denote the corresponding set of mixed strategies. A
contest of size C is the game between C randomly drawn people from the population. Let Tr($1|82, 83, ... , Sc)
denote the payoff of the player 1 when he faces C - 1 other players and the chosen stratgies of these players
is given by ($1, 82, . . . , sc) € S x S x .. . x S (C times).

Let SE E A be the incumbent strategy and let SM( SE) € A be the mutant strategy that will be played
by one randomly drawn agent from the chosen population of size C. The payoff to the incumbent is given
by

TE =
1

C-1

N -1.

TT(SE|SE, SE, ... , SE) +
C -1
N-1
TT(SE|SM, SE, ... , SE)
(A.1)

and the payoff to the mutant is given by

TTM = TT (SM|SE, SE, ... , SE)
(A.2)

Following [10], SE is said to be finite population ESS when

TE ZTM.
(A.3)


## References

[1] Venkatesh Bala and Sanjeev Goyal. A noncooperative model of network formation. Econometrica, 68(5):1181-1229, 2000.

[2] Lawrence E. Blume. The statistical mechanics of strategic interaction. Games Econom. Behav., 5(3):387 - 424, 1993.

[3] Yann Bramoullé. Anti-coordination and social interactions. Games Econom. Behav., 58(1):30-49, 2007.

<!-- PageNumber="130" -->
<!-- PageNumber="7" -->
<!-- PageFooter="This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4366576" -->

\+

.

<!-- PageBreak -->

140

[4] Arko Chaterjee. (Anti)-Coordination and Stability Perspectives in Games on Networks. PhD thesis, Indian Institute of
Technology Bombay, India, 2017.

[5] Khai Xiang Chiong. Robustness in network formation games. Preprint, 2016.

[6] Andrea Galeotti, Sanjeev Goyal, Matthew O. Jackson, Fernando Vega-Redondo, and Leeat Yariv. Network games. The
Review of Economic Studies, 77(1):218-244, 2010.

[7] J. Maynard Smith and G. R. Price. The logic of animal conflict. Nature, 246:15, 1973.

[8] John Maynard Smith. Evolution and the theory of games. Cambridge University Press Cambridge; New York, 1982.

[9] John G. Riley. Evolutionary equilibrium strategies. Journal of Theoretical Biology, 76(2):109 - 123, 1979.

[10] Mark E. Schaffer. Evolutionarily stable strategies for a finite population and a variable contest size. Journal of Theoretical
Biology, 132(4):469 - 478, 1988.

[11] William L. Vickery. How to cheat against a simple mixed strategy ess. Journal of Theoretical Biology, 127(2):133 - 139,
1987.

[12] Douglas B. West. Introduction to graph theory. Prentice Hall, Inc., Upper Saddle River, NJ, 1996.

[13] H. Peyton Young. Individual Strategy and Social Structure: An Evolutionary Theory of Institutions. Princeton University
Press, 2001.

Preprint not peer retweeten

<!-- PageNumber="8" -->
<!-- PageFooter="This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4366576" -->
