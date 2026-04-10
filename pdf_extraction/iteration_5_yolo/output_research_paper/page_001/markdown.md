# Evolutionary Stability for Games Played on Networks

Arko Chatterjeeᵃ, K.S. Mallikarjuna Raoᵇ, Sudipta Sarangiᶜ

ᵃBain & Company, Gurgaon 122 002, India  
ᵇIndustrial Engineering and Operations Research, Indian Institute of Technology Bombay, Mumbai 400076, India.  
ᶜDepartment of Economics, Virginia Tech, Blacksburg VA 24061-0316, USA.

## Abstract

In this paper, we propose a notion of evolutionary stability for games played on networks. We then apply it to a coordination game played on networks.

*Keywords:* Networks, Nash Equilibrium, Evolutionary stability

*JEL:* C78, D85

# 1. Introduction

Evolutionary stable strategy (ESS) is the dominant equilibrium notion in evolutionary game theory. Originally it was defined in the context of infinite populations (see [7, 8]) and as noted in [9, 11], it does not hold for finite populations. Specifically, [9, pp.110] shows that ESS, as defined by Maynard Smith (see [7, 8]), can be successfully invaded by a mutant in finite populations. This difficulty motivated [10] to introduce a finite population version of ESS. Further, Schaffer [10] demonstrates that this notion is a generalisation of the standard ESS by showing that it coincides with standard ESS when the population size tends to infinity. In this paper, we adapt the notion of finite ESS to games played on networks. In particular, we consider a situation where every agent plays a bimatrix game with each of their neighbours and their payoffs are an aggregation of the payoffs across all neighbours. However, this is not equivalent to the notion introduced by Schaffer [10] since each agent’s neighborhood (hence the network architecture) matters. Simply put, depending on their degree, every agent has a different number of neighbors and therefore faces a different finite population. Thus while this network version of ESS continues to be a refinement of Nash equilibrium, we need the condition that makes ESS robust to invasion to account for players’ degrees in a network.

To the best of our knowledge, apart from [10] the closest paper, in spirit, is by [5]. In this paper, the author address robustness of equilibria in network formation games, introduced in [1] by allowing for the addition of costless links to the network. In particular, a Nash equilibrium is defined to be k-robust if k is smallest number such that there is an agent who has incentive to deviate from the equilibrium when k costless links are added to the equilibrium network. In that sense network architecture matters for the equilibrium. Of course our equilibrium notion is very different from the one studied by [5]; but it is related since ESS is considered to be one of the ways in which we can justify Nash equilibrium play.

This paper is structured as follows. We describe our model setup in Section 2. In Section 3, we introduce evolutionary stability in network games. Section 4 focuses on general results for coordination games and Section 5 discuss the stability conditions for specific networks. Section 6 concludes.