Proposition 5. In a hub-spoke network with 2 hubs, where the first hub has n₁ peripheral nodes and the second hub has n₂ peripheral nodes, the strategy profile (R,R,R,⋯,R,B,B,B,⋯,B) is evolutionarily stable if and only if b = c, a ≥ b, d ≥ c together with the conditions

n₁ ≥ (d − b) / (2(a − b)) + √(((d − b) / (2(a − b)))² + (d − b) / (a − b))

n₂ ≥ (a − b) / (2(d − b)) + √(((a − b) / (2(d − b)))² + (a − b) / (d − b)).

By interchanging the roles of the two hubs, we can obtain the conditions (essentially the same, the only difference will be that n₁ and n₂ gets replaced) for the strategy profile (B,B,B,⋯,B,R,R,R,⋯,R).

## 6. Conclusion

In this paper we define the notion of ESS for games played on networks. While this is different from the standard ESS, the finite sample version of has to be adapted using player’s degrees to take network structure into account. We apply our formal definition to coordination games and illustrate it the result for a cyclic and a tree network. Let us now consider the two networks shown in Figure 1 and Figure 2. Recall that the first network is 2-colourable while the second one is 3-colourable. It can be verified that if we consider a two player, two strategy anti-coordination network game (see for instance [3, 4]), the first game will have a pure strategy equilibrium while the second game will not have a pure strategy equilibrium. Thus, if we consider anti-coordination games, the ESS will depend on the exact network architecture and degree sequence, even though condition 2 for ESS remains the same in both networks.

## Appendix A. Schaffer’s Notion of Evolutionary Stability for Finite Populations

Consider a finite population of size N. The set of pure strategies of any player in this population is denoted by S = {s₁,s₂,⋯,s_t}, for some t ∈ N. Let Δ denote the corresponding set of mixed strategies. A contest of size C is the game between C randomly drawn people from the population. Let π(s₁|s₂,s₃,⋯,s_C) denote the payoff of the player 1 when he faces C − 1 other players and the chosen strategies of these players is given by (s₁,s₂,⋯,s_C) ∈ S × S × ⋯ × S (C times).

Let s_E ∈ Δ be the incumbent strategy and let s_M(≠ s_E) ∈ Δ be the mutant strategy that will be played by one randomly drawn agent from the chosen population of size C. The payoff to the incumbent is given by

π_E = (1 − (C − 1)/(N − 1))π(s_E|s_E,s_E,⋯,s_E) + ((C − 1)/(N − 1))π(s_E|s_M,s_E,⋯,s_E)  (A.1)

and the payoff to the mutant is given by

π_M = π(s_M|s_E,s_E,⋯,s_E)  (A.2)

Following [10], s_E is said to be finite population ESS when

π_E ≥ π_M.  (A.3)

## References

[1] Venkatesh Bala and Sanjeev Goyal. A noncooperative model of network formation. Econometrica, 68(5):1181–1229, 2000.  
[2] Lawrence E. Blume. The statistical mechanics of strategic interaction. Games Econom. Behav., 5(3):387–424, 1993.  
[3] Yann Bramoullé. Anti-coordination and social interactions. Games Econom. Behav., 58(1):30–49, 2007.