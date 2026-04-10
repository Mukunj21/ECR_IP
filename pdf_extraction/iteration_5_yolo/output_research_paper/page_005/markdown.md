This is equivalent to

\[
d_i^R(a-c)+d_i^B(b-d)\le \frac{d_i^B}{d_i}(c-d).
\]

This completes the proof of the proposition.

As a corollary, we have the following result.

**Corollary 1.** The strategy \((R,R,\cdots,R)\) is evolutionary stable if and only if it is Nash equilibrium and \(d_i \ge \frac{a-b}{a-c}\) for each \(i\). The strategy \((B,B,\cdots,B)\) is evolutionary stable if and only if \(d_i \ge \frac{d-c}{d-b}\). Thus if \(b=c\), both \((R,R,\cdots,R)\) and \((B,B,\cdots,B)\) are evolutionary stable. Moreover, the network may have evolutionary stable strategies where both \(R\) and \(B\) are played by the agents in the network.

If \(b=c\), then a Nash equilibrium \(s^*\) is evolutionary stable if and only if

\[
s_i^* = R \text{ and } d_i^B \le d_i^R\left(1-\frac{1}{d_i}\right)\frac{a-b}{d-b}
\]

or

\[
s_i^* = B \text{ and } d_i^R \le d_i^B\left(1-\frac{1}{d_i}\right)\frac{d-b}{a-b}.
\]

## 5. Examples with Specific Network Architectures

In this section, we illustrate our key result using two different examples. Since degrees play a key role in our definition, in the first example we consider a regular network where everyone has the same degree. In the next example we consider a 2-hub-spoke network where agents have different degrees. Moreover the first network allows for cycles while the second one does not.

**Example 1 (Cyclical Network).** Consider a network, where every node has degree 2. This network will have two Nash equilibria \((R,R,\cdots,R)\) and \((B,B,\cdots,B)\).

[Figure: Circular Network with 6 Nodes]

Using Proposition 2, we can deduce the following result. We omit the details since the proof is straight forward.

**Proposition 3.**
1. The strategy profile \((R,\cdots,R)\) is evolutionary stable if, \((a+b)\ge 2c\).
2. The strategy profile \((B,\cdots,B)\) is evolutionary stable if, \((d+c)\ge 2b\).
3. The strategy profile \((R,B,\cdots,R,B)\) is not evolutionary stable while \((R,R,B,B,\cdots)\) is evolutionary stable provided

\[
\frac{1}{2}(d-c)\le c-a+d-b\le \frac{1}{2}(b-a).
\]