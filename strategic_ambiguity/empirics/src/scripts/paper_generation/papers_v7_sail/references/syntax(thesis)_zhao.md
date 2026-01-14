---
modified:
  - 2026-01-13T13:06:29-05:00
---

# Flexibility in Platform Operations

**By:** Jiayu Zhao  
**Submitted to:** The Sloan School of Management, MIT  
**Date:** May 2, 2025  
**Degree:** Doctor of Philosophy in Operations Research  

## Abstract

This thesis studies how modern service platforms, through algorithmic and market design, leverage agents' flexibility to enhance operational efficiency. The last decade has witnessed the booming growth of such platforms in ride-hailing (e.g., Uber), e-commerce (e.g., Amazon), and hospitality (e.g., OpenTable). A central operational challenge in these systems lies in the heterogeneity across both supply and demand. For example, Uber cannot match a rider and a driver who are far apart in time or location. To address such challenges, platforms increasingly rely on *flexibility levers*—interventions that encourage market participants to be more accommodating in when or how they interact with the platform. For instance, Uber's "wait and save" option offers a discount to riders who are willing to wait longer, making it easier to find compatible matches.

Motivated by the growing use of such flexibility incentives, this thesis examines how flexibility can be structured, coordinated, and optimized in modern platforms. It focuses on two central dimensions of flexibility: 
1. How flexibility levers interact across a platform's ecosystem.
2. How flexibility decisions can be optimized to improve operational performance.

**Part I** of this thesis examines the interactions and implications of platforms' flexibility decisions. Decisions around flexibility on platforms influence both (i) horizontal dynamics across market sides and (ii) vertical dynamics in a supply chain. **Chapter 2** investigates the horizontal interaction between demand-side and supply-side flexibility incentives. While such incentives are common on both the demand (e.g., "wait and save" feature at Uber) and the supply side (Ride streak bonuses at Uber) of platforms, they have been treated in isolation in the literature and in practice. Chapter 2 initiates the study of two-sided flexibility in platforms: by modeling how these incentives influence the likelihood of compatibility between agents and the resulting matching size, we study whether and when platforms should invest in flexibility across both market sides. Moreover, we identify that platforms may realize significant efficiency gains by incorporating the horizontal interplay of flexibility when designing different incentives.

In an orthogonal direction, **Chapter 3** investigates the vertical supply chain implications of ride-hailing platforms' flexibility decisions. When dual-sourcing autonomous vehicles (AVs) and flexible human drivers with self-scheduling capacity, platforms (e.g., Uber's operations in Phoenix and Austin) make dispatch prioritization decisions to fulfill demand through a hybrid fleet. These decisions affect the incentives of AV suppliers and human drivers, and the self-scheduling nature of gig workers introduces novel supply chain challenges. We study how these challenges can hinder successful AV deployments and provide contracting solutions to overcome them.

**Part II** of the thesis focuses on optimizing specific operational levers for flexibility. The digitization of modern platforms allows for algorithms that provide better customization and timing to harness flexibility. For instance, booking platforms can adjust their admission control decisions in real-time by considering customers' heterogeneous probabilities of being no-shows (i.e., not requiring service) and their compensation requirements for overbooking. 

In **Chapter 4** we analyze an online resource allocation problem that allows overbooking and propose a policy that improves the additive profit loss guarantee (compared to a clairvoyant) in $T$ periods from an order of $\sqrt{T}$ in the literature to a bounded constant.

A related application appears in e-commerce, where retailers seek to use promotional discounts to align customer demand with their inventory position. **Chapter 4** (sic) investigates how platforms can leverage an "opaque selling" strategy to dynamically time these discounts to influence purchase behavior and balance inventory. We propose a class of dynamic inventory-balancing algorithms that adapt opaque selling to real-time inventory states, achieving order-optimal fulfillment costs. This chapter demonstrates how demand-side flexibility can be operationalized through pricing levers for better inventory management.

**Thesis Supervisor:** Daniel Freund  
**Title:** Assistant Professor in Operations Management, MIT Sloan School of Management

---

## Contents

### 1. Introduction
* **1.1** General Motivation
* **1.2** Interactions of Flexibility Incentives in Two-sided Platforms
* **1.3** Implications of Flexible Operations on Technology Adoption
* **1.4** Optimizing Flexibility Decisions in Platforms

### Part I: Interactions and Implications of Flexibility Decisions

### 2. Two-sided Flexibility in Platforms
* **2.1** Introduction
    * 2.1.1 Contributions
    * 2.1.2 Related Work
* **2.2** Model
* **2.3** Flexibility Cannibalization
    * 2.3.1 Proof sketch of Lemma 1
    * 2.3.2 Proof sketch of Lemma 2
* **2.4** Flexibility Asymmetry
* **2.5** Identifying the Right Allocation Across All Parameters
* **2.6** Managerial Implications for Platform Experimentation
* **2.7** Robustness in Alternative Graph Models
    * 2.7.1 Local Model
    * 2.7.2 Spatial Matching
    * 2.7.3 Imbalanced Market
* **2.8** Conclusion

### 3. On the Supply of Autonomous Vehicles in Platforms
* **3.1** Introduction
    * 3.1.1 Contributions
    * 3.1.2 Related Work
* **3.2** The Model
    * 3.2.1 Other Deployment Models
    * 3.2.2 Discussion of Model Assumptions
* **3.3** The AV Underutilization Effect
    * 3.3.1 Dispatch Prioritization
    * 3.3.2 The Profit Ratio
* **3.4** Supply Chain Coordination Contracts
* **3.5** Alternative Deployment Models
    * 3.5.1 AV-only Model
    * 3.5.2 Leasing Models
* **3.6** Prioritization Schemes in Spatial Matching Systems
* **3.7** Numerical Results
* **3.8** Conclusion

### Part II: Optimizing Levers for Flexibility

### 4. Overbooking with Bounded Loss
* **4.1** Introduction
    * 4.1.1 Motivation
    * 4.1.2 Technical challenges and algorithmic techniques
    * 4.1.3 Related work
* **4.2** Model
    * 4.2.1 Algorithm and benchmark policies
    * 4.2.2 Further notation
* **4.3** Main result
* **4.4** Proofs of auxiliary results
    * 4.4.1 Proof of Lemma 4 and Lemma 5
    * 4.4.2 Proof of Theorem 10
    * 4.4.3 Proof of Lemma 6
* **4.5** Numerical results
* **4.6** Conclusion

### 5. On the Power of Delayed Flexibility
* **5.1** Introduction
    * 5.1.1 Our Contributions
    * 5.1.2 Related work
* **5.2** Preliminaries
* **5.3** Optimality of Late-Stage Flexing for Balls-into-Bins
    * 5.3.1 Warm-Up: Approximate Optimality of Non-Adaptive Late-Stage Flexing
    * 5.3.2 Optimality of a Semi-Dynamic Threshold Policy
* **5.4** Application: Late-Stage Opaque Selling for Inventory Management
    * 5.4.1 Basic Setup
    * 5.4.2 Benchmark Policies
    * 5.4.3 Leveraging Balls-Into-Bins for Effective Late-Stage Opaque Selling
* **5.5** Computational Experiments
    * 5.5.1 Balls-into-Bins
    * 5.5.2 Opaque Selling
* **5.6** Conclusion

### 6. Conclusion


----

Chapter 1 Introduction

1.1 General Motivation

This thesis studies how modern service platforms, via algorithm and market designs, incentivize agents’ flexibility to enhance operational efficiency. Over the past decade, platforms such as Uber, Amazon, and OpenTable have transformed service delivery in industries like ride-hailing, e-commerce, and hospitality. In matching the supply and demand sides of the market, a major operational challenge faced by these platforms is the heterogeneity on both sides. For instance, platforms such as Uber cannot match a rider and a driver that are spatially or temporally far apart. An important lever that platforms use to handle such heterogeneity is to make the two sides of the market more flexible. Uber, as an example, offers a “wait and save” discount to riders who are willing to be patient, which makes it easier for platforms to find matches for these riders. Motivated by the increasing uses of such flexibility incentives today, this thesis focuses on the following two aspects of platforms’ flexibility decisions.

Examining the interactions and implications of flexibility decisions. Flexibility incentives used by platforms often interact in complex ways. On two-sided platforms, such incentives are commonly used on both the demand and supply sides: for example, ride-hailing platforms like Uber employ options such as “wait and save” on the demand side to encourage passengers to wait longer for a match, while offering incentives such as ride streak bonuses on the supply side to motivate drivers to stay committed and accept dispatches. While each of these incentives aims to facilitate matches by increasing the likelihood of compatibility between riders and drivers, their combined effect is much more subtle. Should platforms invest in flexibility on just one side of the market, or is it better to encourage some degree of flexibility on both sides? This points to a gap in the platform literature, as studies to date have examined these incentives in isolation rather than as part of a matching system.

In addition to horizontal interactions, flexibility decisions can also have vertical supply chain implications as they influence the behavior of the platform’s upstream suppliers. For instance, a ride-hailing platform that relies on both autonomous vehicles (AVs) and selfscheduled human drivers must decide how to prioritize dispatch using this hybrid fleet. While human drivers provide a form of flexible supply that helps the platform adapt to demand fluctuations, their prioritization comes at the expense of AV suppliers’ incentives to invest. These tensions raise important questions about how platforms can balance flexibility with long-term supply commitments. Together, these examples point to the need for a deeper understanding of both the horizontal interactions between market sides and the vertical implications that flexibility has for supply chain coordination.

Optimizing decisions around flexibility in platforms. The digitization of modern platforms has opened up new opportunities to optimize flexibility-related decisions in a more targeted and dynamic manner. For instance, booking platforms can analyze which customers are likely to be no-shows and implement admission-control policies that allow for overbooking, thereby reducing wasted capacity. Similarly, e-commerce platforms can track how promotional discounts influence customer choices across products. This enables them to strategically leverage demand-side flexibility, offering dynamic discounts to balance inventory and minimize fulfillment costs. These examples underscore the need for algorithmic approaches that customize and time flexibility incentives to enhance platform performance.

The overall goal of this thesis is to address the challenges outlined above. Below, we provide a roadmap of how the thesis approaches these challenges, summarize the main results, and outline the organization of the chapters.

1.2 Interactions of Flexibility Incentives in Two-sided Platforms

In two-sided matching platforms, flexibility may occur as a feature on both market sides. The widespread use of flexibility incentives raises a critical question: should flexibility be jointly allocated across different sides? While the literature on process flexibility in manufacturing systems has traditionally focused on the supply side [1–3], and studies on flexibility incentives in online marketplaces primarily target the demand side [4, 5], in Chapter 2 we initiate the study of two-sided flexibility in matching platforms. We postulate a parsimonious matching model in random graphs, in which flexibility is captured through flexible nodes (on either side) that have an increased probability of forming edges with nodes on the opposite side; the objective is the expected size of a maximum matching. Our findings highlight the value of studying two-sided flexibility allocations: for a fixed flexibility budget, the resulting matching size can vary greatly depending on how the budget is allocated. In particular, we uncover two effects – flexibility cannibalization and flexibility asymmetry – that determine whether it is better to have flexibility on both sides or only on one side:

• Flexibility cannibalization: When flexible nodes form many edges among themselves, they cannibalize each other because each node is incident to at most one edge in a matching. We refer to this effect as flexibility cannibalization, and it is strongest in a balanced allocation with an equal number of flexible nodes on both sides.

• Flexibility asymmetry: When regular nodes on one side of the graph are much less likely to form edges due to a lack of flexible nodes on the opposite side, there may be a

24 Figure 1.1: The heatmap presents ratios of (i) the asymptotic matching size of a balanced allocation over (ii) that of a one-sided allocation. That is, the balanced (resp. one-sided) allocation dominates when the ratio is greater (resp. smaller) than 1. The results cover different values of α f and α, which parameterize the degrees of regular and flexible nodes. The plot highlights the parameter regimes where the ratio is highest or lowest due to the dominance of the flexibility cannibalization or the asymmetry effect.

large number of isolated nodes. We refer to this effect as flexibility asymmetry, and it is most pronounced in a one-sided allocation with all flexible nodes on the same side.

In Chapter 2, we characterize the typical parameter regimes where each effect dominates, as illustrated in Fig. 1.1. In physical matching markets (e.g., ride-hailing) with low edge density, incentivizing flexibility on both sides can be wasteful due to the cannibalization effect. This corresponds to the region with small α f and α in Fig. 1.1. Conversely, in online marketplaces (e.g., freelancing) where flexible nodes may have a much higher degree than regular nodes, it can be beneficial for platforms to employ flexible agents on both sides to accommodate hard-to-match agents on the opposite side. This corresponds to the region where α f ≫ α in Fig. 1.1. In either case, the sub-optimality gap is large, and we show that costly mistakes can be made if flexibility decisions on the demand and supply sides of platforms are optimized independently (e.g., by separate teams in a company) rather than jointly.

Our main technical contributions compare the maximum matching sizes of different flexibility designs in sparse bipartite random graphs. Computing the maximum matching sizes in such graphs is a decades-old challenge in random graph theory [6, 7]. On the one hand, some of our results generalize tools from this literature, such as the Karp-Sipser algorithm [8], to specific settings of our model; on the other hand, we introduce new tools (e.g., a coupling construction) that allow us to compare the matching sizes of different flexibility allocations without explicitly computing the matching size.

Chapter 2 is based on a joint work with Daniel Freund and Sébastien Martin [9].

1.3 Implications of Flexible Operations on Technology Adoption

Operational flexibility also has significant upstream implications for how platforms adopt new technologies. In Chapter 3, we study this with a focus on autonomous vehicles (AVs), a

25 rapidly advancing technology that has been deployed (operationally or as pilots) in at least 18 U.S. cities. Enabled by partnerships between AV technology companies (e.g., Waymo) and traditional ride-hailing platforms (e.g., Uber), platforms may operate a hybrid fleet of AVs and flexible human drivers who work as independent contractors (ICs); this occurs already in Phoenix. We model the distinct flexibility and cost characteristics of ICs and AVs: ICs provide greater supply flexibility but incur higher marginal costs due to labor costs, while AVs have lower marginal costs but require substantial upfront capital expenditure and offer less flexibility in quantity. Since there is significant variability in hourly demand for rides (see Fig. 1.2), there can be operational value in complementing a rigid AV fleet with flexible ICs to fulfill rides when demand is high. However, unlike dual-sourcing in traditional supply chains, the self-scheduling nature of gig workers adds complexity to the platform’s dispatch prioritization decisions. For instance, consider the platform’s dispatch decisions on Friday evenings, when the expected demand is high but volatile. Even if the realized demand is low enough for AVs alone to fulfill it, the platform’s need to attract ICs on Friday evenings still requires it to protect the ICs’ utilization despite their higher marginal cost. We refer to this phenomenon as the AV underutilization effect and investigate its impact on AV supply chain efficiency through game-theoretic equilibrium analyses.

Figure 1.2: Hourly demand for riders based on 2023 NYC Taxi and Limousine Commission data

To capture current industry expectations, we focus on an open platform model, where AV suppliers and human drivers both bring their vehicles into a platform. We then compare its efficiency with that of an integrated supply chain where the AV supplier and ride-hailing platform integrates into a single entity. Surprisingly, due to AV underutilization, the supply chain profit of an open platform model can be arbitrarily smaller than that of the integrated benchmark. To avoid such market failures, we explore potential contracting solutions and demonstrate the value of usage commitments in improving the efficiency guarantee. In particular, with usage commitments, an open platform exhibits stronger theoretical guarantees and superior numerical performance compared to the other operational models, such as a ride-hailing platform served by only AVs (e.g., Waymo in San Francisco) or a platform that sources AVs through short or long-term leasing contracts. Our work highlights that additional flexibility in platforms, including the ability to dual-source AVs and ICs, may lead to tension between short-term operational decisions and long-term capacity decisions, and provides solutions to overcome the incentive misalignment therein.

Chapter 3 is based on a joint work with Daniel Freund and Ilan Lobel [10].

26 1.4 Optimizing Flexibility Decisions in Platforms

This thesis also studies algorithmic challenges in the customization and timing of flexibility decisions.

Overbooking and Admission Control. No-shows are common in the travel and hospitality industries, and modern platforms, including Booking.com and OpenTable, manage the risk of no-shows by overbooking customers who are flexible with their needs. To obtain a tractable problem, traditional overbooking models often assume that customers have a homogeneous no-show probability and require the same compensation if overbooked. However, in reality, customer behaviors are diverse, which provides opportunities for modern booking platforms to use digital tools to dynamically adjust their admission control policies based on varying customer characteristics and real-time resource availability. To incorporate such behaviors, Chapter 4 studies a setting with heterogeneous customer no-show probabilities. In particular, we resolve the open question of providing an algorithm with uniformly bounded loss for a classical problem in revenue management: quantity-based, single-resource revenue management with no-shows. In this problem, a firm observes a sequence of T customers drawn i.i.d. from k different types. The firm decides irrevocably whether to accept or reject requests in an online fashion. Each accepted service request yields a type-dependent revenue and has a type-dependent probability of being a no-show. The firm has a capacity of resources B and pays a fixed compensation for each overbooked customer. With a clairvoyant that knows all arrivals ahead of time, as a benchmark, we provide the first algorithm with a uniform additive loss bound, that is, its expected loss is independent of T. This improves upon prior works achieving Ω( √ T) guarantees [11]. The algorithm extends the state-of-the-art compensated coupling technique [12] to a class of problems with nonlinear objectives and resolves an optimization program in each period to dynamically adjust the parameters of its index-based admission control.

Chapter 4 is based on a joint work with Daniel Freund [13].

Inventory Balancing in E-Commerce. E-commerce platforms such as Amazon face the challenge of managing vast inventories to meet customer demand effectively. One innovative solution to the challenge is the use of opaque selling discounts, where customers receive a discount for agreeing to be flexible with the exact product they receive, e.g., they may receive a similar product with a different color [4]. This approach allows the platform to optimize inventory levels of different products by directing customers to those with higher stock levels. In Chapter 5, we leverage this inventory-balancing idea to design algorithms that determine, based on real-time inventory data, whether to offer an opaque selling discount. Traditional load-balancing algorithms that target (approximately) balanced loads throughout a decision-making horizon of T periods need to exert such flexibility in Θ(T) periods in expectation. However, inventory cost minimization only requires balancedness at the end of each replenishment cycle, and we employ an adaptive threshold policy to achieve this goal while only exerting flexibility in O( √ T) periods, which matches a natural lower bound. We then adapt these algorithms to develop order-wise optimal policies for the

27 opaque selling problem. We also illustrate how similar “limited-flexibility” algorithms can be adapted to improve the efficiency of cloud computing resource allocation and parcel delivery for e-commerce fulfillment.

Chapter 5 is based on a joint work with Daniel Freund and Chamsi Hssaine [14].

28 Part I Interactions and Implications of Flexibility Decisions

29 
# Chapter 2 Two-sided Flexibility in Platforms

2.1 Introduction

Flexibility is one of the fundamental topics in operations research and computer systems. As an operational concept, it classically applies to a range of settings including (1) the ability of a plant to process multiple types of products in a manufacturing system [2], e.g., the long chain design illustrated in Fig. 2.1 (a), (2) the ability of servers, due to cross-training, to handle multiple types of requests [15], or (3) the pooling of resources in a network of newsvendors [16]. In these applications, flexibility is widely recognized for its value in hedging against demand uncertainty and improving system performance.

(a) Process flexibility

(b) Flexibility in platforms

Figure 2.1: The plots contrast process flexibility in manufacturing systems with flexibility in platforms. The red edges in the long chain design highlight the additional compatibility introduced deterministically into the system. In contrast, platform flexibility is achieved through agents with a higher probability of being compatible with other agents. The figure shows one realization of this compatibility; notice that the flexible red rider is willing to accept further away matches.

Many modern service platforms face similar uncertainty on both the demand and the supply side, which motivates the natural question whether flexibility can also be leveraged in

31 their operations. For instance, the matching problem solved by ride-hailing platforms has a bipartite structure, with riders on the demand side and drivers on the supply side. As illustrated in Fig. 2.1 (b), the edges between agents represent their compatibility (here, whether it is possible to match a given driver and rider), and the platform finds a matching using these available edges. Though the problems in Fig. 2.1 (a) and (b) share a similar bipartite structure and additional edges are valuable in both systems, there are fundamental differences in how these edges are created. In a manufacturing system, additional compatibility is configured deterministically by a central planner who invests in equipment for the corresponding plants. In contrast, the impact of flexibility in modern platforms is better modeled in a stochastic way. For instance, the “Wait and Save” option in Fig. 2.2 (a) illustrates how platforms incentivize riders to be more flexible with their pickup times. A rider choosing this option accepts to wait longer before being matched. This allows the platform to match her with drivers within a wider radius, providing flexibility to generate more efficient matches overall. However, the number of drivers within the radius is stochastic. Therefore, a flexible rider will likely be compatible with more drivers, but not always. For example in Fig. 2.1 (b) the flexible rider has two edges, but there are non-flexible riders with three edges, as, in this situation, the flexible rider is further away from available drivers. This is why, more generally, the flexibility of an agent (supply or demand) can be interpreted as its likelihood of being compatible with agents on the other side. In a more abstract matching terminology, a flexible node is a node that is more likely to have edges with other nodes, which, in turn, helps platforms find more profitable matching solutions. However, a second fundamental difference in how flexibility arises on platforms is due to the fact that platforms cannot compel agents to be flexible; rather they offer incentives to encourage flexibility. In contrast to the manufacturing setting, where a central decision maker configures flexible edges deterministically, we thus model flexibility in two stochastic stages. In the first, agents opt-in to be flexible, and in the second, edges realize based on the agents’ choices and additional conditional randomness.

(a) “Wait and Save” Option

(b) “Ride Streak” Mode

Figure 2.2: Examples of flexibility incentives on demand and supply sides of Lyft, a ridehailing platform.

Another fundamental aspect of platform flexibility, and the main focus of this paper, is that it is really two-sided. As detailed in Table 2.1, different platforms have different levers to promote flexibility among agents on both market sides. Consider, for example, Lyft’s

32 incentives for drivers and riders. In addition to the above-descrived Wait & Save option, Lyft also provides “Ride Streak” driver bonuses to its drivers, see Fig. 2.2 (b). This bonus incentivizes drivers to work for longer on the platform and to decline rides from competitors like Uber. Suppose, for instance, that Lyft wanted to match a driver with a rider 10 minutes away; without the bonus, the platform may assume that the driver would not accept the ride, preferring to instead wait for a closer match, and therefore treat the driver-rider pair as non-compatible. However, given the Ride Streak bonus, the driver is more likely to accept the match despite the long pick-up time. Therefore, both drivers and riders become more “flexible” in our graph representation in the sense that they are incident to more edges and thus more “flexible” in Lyft’s matching optimization. In Appendix A.1 we discuss in greater detail how other matching platforms deploy incentives on both market sides and thereby enhance the likelihood of compatible connections between demand and supply.

Industry

Ride-hailing Food delivery Freelancing

Platform(s)

Lyft Uber Eats Upwork

Demand side lever

Wait and save No rush delivery Project catalog

Supply side lever

Ride streak Surge incentives Upwork academy

Table 2.1: Examples of two-sided platforms that use flexibility incentives on both the supply and demand sides. These incentives are designed to increase the likelihood that agents on one side are compatible with those on the opposite side of the market.

The examples illustrate that flexibility can simultaneously exist on both the demand and supply sides, which raises the question of how flexible agents on both sides interact with each other. Specifically, what flexibility structure is best for matching? Is it more effective to concentrate flexibility on one side of the platform, or is it better to invest in both sides? Despite the significant investments through which platforms create flexibility on both the demand and the supply side, the interaction of flexibility on both sides is not well-understood. Indeed, we know of no work in the literature that examines the interaction of two-sided flexibility on platforms. And, in practice, platforms usually have different teams managing flexibility incentives on each market side, with each team focusing on a single lever and using experimentation to determine the optimal incentive level. Such a one-sided experimentation-driven approach neither reveals nor exploits the interaction of different flexibility incentives, and we will show that it can come at a great cost.

Motivated by this gap in the literature, we study how a given budget of flexibility should be allocated across the two sides of a platform. Our focus on the allocation question differs from traditional studies of flexibility that usually focus on just one flexibility lever, rather than their interactions. Since Table 2.1 shows that two-sided flexibility can arise in a variety of settings, we focus on highlighting general effects that are likely relevant to any matching platform. We develop a parsimonious matching model to identify a platform’s optimal flexibility investment on both market sides. Our matching problem is represented as a bipartite random graph, where flexible nodes (on either side) have a higher chance of forming connections with the other side of the graph compared to regular nodes. The platform’s objective is to maximize the expected number of matches in a maximum matching. We study how a fixed flexibility

33 budget should be allocated, and whether and when platforms should invest in flexibility on both market sides.

Our results show that the choice of flexibility allocation has a significant impact on the performance of a two-sided matching platform. Even with a fixed flexibility budget, the matching probability (and consequently the profit of a matching platform) can vary significantly depending on how the budget is allocated between the two sides of the platform (see Fig. 2.14). Moreover, by comparing two natural flexibility allocation strategies: (1) the one-sided allocation, which places flexibility only on one side, and (2) the balanced allocation, which evenly distributes half of the flexibility budget to both sides, we find that either of these allocations can improve the matching size by more than 8% compared to the other (see Fig. 2.5). Hence, matching platforms with flexibility levers on both sides may pay a high price if they only optimize their flexibility budget but not its allocation.

Despite the impact of the flexibility allocation, optimizing it poses nontrivial difficulties. Even in a simple and symmetric matching model, the geometry of the maximum matching size (as a function of the flexibility allocation) reveals saddle points in which a platform might get stuck. In particular, the current practice of many platforms, wherein separate teams optimize separate flexibility levers on different market sides, might converge to such saddle points. Near these saddle points, both teams mistakenly perceive themselves to be at an optimum, as flexibility should neither be increased nor decreased on either market side; however, the platform would benefit from jointly reducing flexibility on one side while increasing it on the other. These structural insights are unique to our study of two-sided flexibility, and our numerical results show that they generalize beyond our particular models. We show that these geometries and the dominance of different flexibility allocations are driven by an interplay of two opposing effects: flexibility cannibalization and flexibility asymmetry. These effects lend strength to the one-sided and the balanced allocations respectively, and they allow us to outline the parameter regimes where each effect and the corresponding flexibility allocation dominate. In identifying these different behaviors, and their first-order impact on performance, our results underscore the need to understand the interactions of different flexibility levers to enable more efficient market designs.

2.1.1 Contributions

Our work initiates the study of two-sided flexibility in platforms. It characterizes the interactions between different flexibility levers through a parsimonious matching model and allows us to study different questions regarding the optimal allocation of flexibility. Optimal flexibility structures. Our study of one-sided and balanced flexibility allocations reveals that either structure can dominate the other. In Sections 2.3 and 2.4, we introduce two key effects – flexibility cannibalization and flexibility asymmetry – that respectively drive the dominance of the one-sided and balanced allocations. Intuitively, flexibility cannibalization is a waste of flexibility in the balanced allocation: as flexible nodes form edges with each other, their degree increases while their incident edges are wasted since each flexible node can only be matched once. In contrast, flexibility asymmetry arises in the one-sided allocation, where regular nodes on the same side as the flexible nodes cannot have any flexible neighbors and are thus much less likely to form any edges at all when compared to regular nodes on the opposite side. The asymmetry can result in a large number of degree-0 nodes in the one-sided

34 allocation, leaving the isolated nodes unmatched. In Section 2.3 and 2.4, we characterize the parameter regimes where these effects are most pronounced, and in Section 2.5 we identify the dominant allocation across all parameters. Our structural insights have profound implications for platform experimentation, which we explore in Section 2.6. There, we highlight a potential inefficiency when the supply and demand sides conduct independent searches for the optimal flexibility incentives. Beyond the matching model considered in Section 2.2, Section 2.7 demonstrates the robustness of our findings in models that exhibit spatial structures and imbalanced market sizes.

Analyses of sparse bipartite random graphs. Our main technical contributions lie in analyzing the asymptotic maximum matching sizes in sparse bipartite random graphs with heterogeneous node types. Characterizing the asymptotic size of maximum matchings in random graphs is a long-studied but notoriously challenging area in extremal combinatorics. To compare the maximum matching sizes of different flexibility designs, we develop three distinct techniques. In Section 2.3 we design a careful coupling between realizations under the balanced and the one-sided flexibility allocations and show, for certain parameters, that flexibility cannibalization leads to a smaller matching size for the balanced allocation. Then, in Section 2.4 we apply concentration bounds for parameters where flexible nodes have high average degrees. In such settings, both allocations match almost all flexible nodes, but the balanced allocation is better at matching regular ones. Finally, in Section 2.5 we analyze the Karp-Sipser (KS) algorithm [8] to explicitly characterize the asymptotic matching probability in the so-called subcritical regime. Our KS-style analysis innovates upon prior works in that we (i) analyze a graph with heterogeneous node types, and (ii) explicitly compute the asymptotic matching probability with a provable level of precision in order to compare different flexibility allocations in computer-aided proofs.

2.1.2 Related Work

Flexibility in operations. Flexibility has a long history in operations with early works, dating back to [17] and [1], focusing on the ability of a manufacturing system to produce multiple types of products. Most early works in this literature have focused on determining the optimal amount of flexible manufacturing capacity [1, 3, 18, 19], thus optimizing over a single dimension on the supply side. In contrast, our decision also involves the demand side. More importantly, we identify not just the optimal flexibility investment, but also structural properties that arise from the interplay of flexibility on both sides and can cause potential pitfalls in practice.

In our focus on structural insights, our study relates more closely to those works in process flexibility that aim to identify the optimal flexibility design rather than the optimal amount of flexibility. The seminal work of [2] first introduced the “long chain”, which enables a small amount of flexibility (2n carefully placed edges in a manufacturing system with n plants and n types of products) to yield almost all the benefits of a perfectly flexible system (one with all n 2 edges). Since then, a vast literature has studied process flexible designs and the value thereof for manufacturing and service systems [20–25]. Effective flexibility designs have also been investigated in staffing [15], queuing [26], and network interdiction [27], among other settings. A key distinction between our work and this stream of work lies in the structure of our flexibility levers: as most contemporary matching platforms involve stochastically

35 formed edges that connect the supply and demand sides, we cannot model flexibility as a fixed compatibility design. Instead, platforms use various incentive levers to increase the likelihood of compatibility between the supply and demand sides of the market. As such, our approach optimizes over the fraction of flexible nodes on each side, rather than optimizing over specific edges, and requires a fundamentally different toolkit.

Our work also relates to papers that study flexibility on online marketplaces, though they focus on flexibility on a single side. In ride-hailing services, prior works study supply-side levers such as driver repositioning incentives [28] or a priority mode [29], and demand-side levers such as waiting mechanisms [30] or subscriptions [31]. More explicitly focused on demand-side flexibility, some works study opaque selling [32] and flexible time windows [33] in online retail. Our work differs from all of these in that we focus on the interplay of two different flexibility levers.

In-organization Incentives. A reasonable interpretation of our structural results is that modern platforms are unlikely to find the optimal flexibility allocation if they optimize over two sides independently (see Section 2.6). Nonetheless, given the organizational structure of many platforms, with separate verticals working on the supply and the demand side, jointly experimenting and thus optimizing over levers on different market sides is uncommon. This misalignment relates to a stream of literature that identifies conflicting organizational incentives, e.g., the so-called marketing-operations alignment. There, organizations may face inefficiencies due to two departments (marketing and operations) having opposing incentives [34]. Solutions for marketing-operations conflicts focus on aligning incentives, including through internal integration of different functional teams within an organization [35], increasing the interface between manufacturing and marketing management [36], and achieving a strategic alignment between external positioning and internal arrangement [37]. In our work, the separate verticals do not have misaligned incentives. Instead, the inefficiency arises from a lack of visibility, i.e., without joint experimentation, both teams lack visibility over the interplay between the two flexibility decisions.

Random graphs. Our technical contribution consists of different asymptotic analyses of the maximum matching size in sparse random graphs. A classical tool for these types of analyses is the Karp-Sipser (KS) algorithm [8], which is asymptotically optimal for the canonical maximum matching problem in sparse Erdős–Rényi random graphs with n nodes and a uniform edge probability c/n between any two nodes (for constant c as n → ∞). Moreover, it gives rise to a system of nonlinear equations that characterize the asymptotic matching size. Since then, decades of research have extended this type of analysis to characterize the expected size of a maximum matching in random graphs with different generating processes [6, 38–40]. This is a notoriously difficult problem with each of these papers, like ours, only extending the analysis to new special cases. The closest setting to ours is the “configuration model” studied by [6]; however, their model does not capture our setting with flexible and regular nodes. 1 Moreover, beyond the canonical setting, the KS-style analyses often encounter fundamental limitations as the average expected degree of a node exceeds e, the Euler’s number [7, 41]. Our work primarily differs from this literature in that our ultimate goal is to compare the maximum matching sizes under different flexibility allocations rather than

1 E.g., our model, but not theirs, allows two nodes with positive expected degree to have 0 probability of being adjacent.

36 to just characterize these quantities. To do so, we employ two approaches: (1) we identify parameter regimes where the matching sizes under different allocations are so different that we can compare them without characterizing them explicitly (Theorems 1 and 2); (2) we extend the KS-style analysis to some parameter regimes of our types of random graphs and use the resulting characterization in a proof that requires continuity arguments and a computer-aided grid search. Despite computer-aided proofs having a long tradition in combinatorics, including proofs of the four-color theorem [42, 43], we know of no other papers with provable comparisons of the limiting behavior of different random graphs that rely on these sets of tools. In that regard, [44] may be closest to our approach, though they only compute a single explicit solution to a nonlinear equation (to compute the size of a largest independent set), whereas our grid search requires us to solve, within provable tolerance, approximately ≈ 6 × 10 6 systems of nonlinear equations.

2.2 Model

We study two-sided flexibility in platforms through a model of maximum matching in a random bipartite graph G, wherein nodes on both sides are either flexible or regular. Here, we formally introduce our parsimonious model, which we analyze throughout Sections 2.3–2.6. Section 2.7 and its appendices will study closely related variants of our main model and show how our findings apply more broadly.

Random Graph Generation. We begin by describing the random bipartite graph G through which we model flexibility. Denote the set of nodes on the left-hand side and right-hand side of G by V l and V r , respectively, and let V = V l ∪ V r . Each node on one side represents a demand agent (e.g., a rider) and each node on the other represents a supply agent (e.g., a driver). We assume that there are n ∈ N + nodes on each side 2 and index them such that V l = { v 1 l , ..., v n l } and V r = { v 1 r , ..., v n r } ; [n] denotes the set { 1, ..., n } . Whether a node is flexible or regular is determined by the decision variable b = (b l , b r ) ∈ [0, 1] 2 , where b l and br  respectively specify the probability that a node on the left-hand side and right-hand side opts into being flexible. Formally, for all i ∈ [n], k ∈ { l, r } we independently sample a Bernoulli random variable F i k ∼ Bernoulli(b k ) and node v i k ∈ V k is flexible if F i k = 1; otherwise, it is regular.

We model compatibility, i.e., the presence of an edge (v i l , v j r ), as an independent Bernoulli random variable R ij , such that the edge realizes if and only if R ij = 1. In line with the examples in the introduction, we want edges with flexible nodes to be more likely to exist. Therefore, the probability that R ij = 1 must be increasing in F i l (the left node is flexible) and F j r (the right node is flexible). We focus on the sparse random graph regime, where the expected degree of each node remains constant as the size of the graph n scales large.3  Specifically, we take non-negative parameters α f > α as given and define p n f = α f /n and p n = α/n. Then, the probability of an edge forming between two regular nodes is 2p n , the

2 While we focus on balanced bipartite graphs in most of the paper, we also consider imbalanced markets in Section 2.7.3.

3 [45] proved for c > 1 that a random graph with n nodes and i.i.d. edge probability c · log(n)/n almost

surely possesses a perfect matching as n → ∞. Thus, subsequent studies [6, 8] often focus on the case where the edge probability is in O(1/n) and each node’s expected degree is O(1).

37 probability of an edge between two flexible nodes is 2p n f , and the probability of an edge between a flexible and a regular node is p n + p n f . Formally, this can be written as

P = 1 | F i l , F j r + (F i l + F j r ) · (p n f − p n ), ∀i, j ∈ [n]. Rij  = 2pn  [ ]

Intuitively, α and α f control how likely regular and flexible nodes are to be compatible with nodes on the other side, which is why we have α f > α. We illustrate the resulting edge probabilities in Fig. 2.3. This setting is symmetric, as flexibility on either side contributes equally to form an edge, with such contributions being additive and independent of i and j. This additive edge probability is a careful modeling choice: indeed, note that the expected total number of edges in the graph is given by n 2 (2p n +(b l +b r )(p n f −p )). This is a function of B = b l + b r , which can be interpreted as the total “flexibility level” inn the platform. Therefore, the expected number of edges in the graph is invariant to (b l , b r ) for fixed B – it only depends on the total flexibility, not how we allocate it. 4 As discussed later, this feature allows us to investigate effects that are driven by the distribution of edges within a graph rather than the number of edges.

Figure 2.3: Illustration of the edge probabilities between possible types of nodes.

Maximum Matching. In the resulting n × n random bipartite graph G, we use the random variable M n (b l , b r ) to denote the size of a maximum matching. A matching is a set of edges in the bipartite graph such that each node can be in at most one edge, and a maximum matching contains the largest possible number of edges across all matchings. We define the matching probability µ n (b l , b r ) as the expected fraction of nodes that are part of a maximum matching, i.e., µ n (b l , b r ) = E [ M n (b l , b r )/n ] . Maximizing µ n (b l , b r ) is a good parsimonious model for the objective of a matching platform that tries to make as many matches as possible. We are interested in the asymptotic behavior of µ n (b l , b r ) with respect to (b l , b r ) as n → ∞, a conventional scale of interest in the study of random graphs. We denote this asymptotic quantity by µ (b l , b r ) := lim sup n→∞ µ n (b l , b r ), which is equal to lim n→∞ µ n (b l , b r ) when the latter exists. By focusing on the expected size of a maximum matching instead of simplified matching heuristics (e.g., greedy), we guarantee that our results are truly driven by the interactions of two-sided flexibility and not by artifacts of suboptimal matching schemes. At the same time, this introduces significant analytical challenges since the asymptotic size of a maximum matching is notoriously difficult to compute, with an active area of research identifying special cases for particular sparse random graphs of interest (see Section 2.1.2). Some of our results can be seen as advancing that area as our model creates a new special case that is of particular interest to matching platforms.

4 In Section 2.7.2, we consider a spatial setting that relaxes this invariance assumption.

38 We complement our theoretical results on µ (b l , b r ) with simulations that compute the empirical matching probability for given (b l , b r ). Provided with s samples of random graph that yield maximum matching sizes M n 1 (b l , b r ), M n 2 (b l , b r ), . . . , M n s (b l , b r ), we compute the empirical mean as ′ M (b l , b r ) ∑s ′  µ n,s EMP (b l , b r ) := s ·s n n . Since the samples are independently and identically distributed (i.i.d.), the Law of Large Numbers (LLN) implies that µ n,s EMP (b l , b r ) → µ n (b l , b r ) almost surely as s → ∞. In our experiments, unless stated otherwise, we use n = 100, s = 10000 and omit the dependency of µ n,s EMP (b l , b r ) on n and s for brevity.

Objective. Our work examines whether and when platforms should invest in flexibility across both market sides. As we are particularly interested in the flexibility allocation problem (i.e., what is the best way to allocate a given amount of flexibility), most of the paper assumes a fixed flexibility budget B = b l +b r ≥ 0 and compares two different allocations (b l , b r ) of that budget: the one-sided allocation does not make use of flexibility across both market sides and instead invests the entire budget on one side, whereas the balanced allocation allocates the flexibility budget equally on both sides.5 

Definition 1. For a given budget B ∈ (0, 1], the flexibility allocation b = (B, 0) or b = (0, B) is called the one-sided allocation, whereas b = (B/2, B/2) is called the balanced allocation.

At first sight, fixing the budget B may not seem realistic. However, the problem of deciding both b l and b r can be decomposed into the problem of choosing B and the allocation problem. Most of the paper focuses on the allocation problem, as our goal is to study the interplay between the two types of flexibility. Then, Section 2.6 will study the general problem where the platform can choose b l and b r to maximize profit.

Figure 2.4: Illustration of µ EMP (b l , B − b l ) with respect to b l /B for varying values of B, α f and α.

Surprisingly, depending on the parameters, either of the two allocations can lead to a significantly higher matching probability than the other (see Figures 2.4 and 2.5). Since the

5 We could study all allocations such that b l + b r = B instead of limiting ourselves to the balanced and one-sided allocations. However, (i) these are the two most natural choices given the symmetry of the problem, (ii) these allocations have nice symmetry properties that simplify our already arduous analysis, and (iii) our numerical results suggest, as displayed in Figure 2.4, that the optimal allocation is always either the one-sided or the balanced allocation.

39 (a) B = 0.6

(b) B = 1

Figure 2.5: The heatmaps present values of µ EMP µ EMP (B/2,B/2) (B,0) for varying α and α f −α and highlight the parameter regimes where the ratio is highest or lowest due to the dominance of the flexibility cannibalization or the asymmetry effect.

expected number of edges in our model is invariant to different allocations of a fixed budget B, the differences between µ (B, 0) and µ (B/2, B/2) must be driven by the distribution of edges within a graph rather than the number of edges. This occurs because a maximum matching does not contain all edges in the graph and some allocations of flexibility yield many realized edges that do not produce additional matches. Our work uncovers the effects that determine when each flexibility allocation is particularly conducive to matching and thus helps realize the significant efficiency gains from the optimal flexibility allocation.

Plans for the subsequent sections. In Sections 2.3 and 2.4 we describe two key effects – flexibility cannibalization (which favors the one-sided allocation) and flexibility asymmetry (which favors the balanced one). Together, they guide the search for the optimal flexibility allocation. We provide intuitions for the types of platforms on which the effects emerge and formalize them by characterizing the parameter regimes where they are most consequential. Specifically, in Section 2.3, we exploit the flexibility cannibalization effect to show that the one-sided dominates the balanced allocation when B = 1 and α = 0, regardless of the value of α f . In contrast, we show that when B < 1 and α is a small positive value, flexibility asymmetry emerges, and the balanced allocation may yield a significantly larger maximum matching size, especially when α f is large (see Section 2.4). Then, in Section 2.5 we adapt classical approaches in random graph theory to further compare different allocations. We prove that the Karp-Sipser algorithm characterizes the asymptotic matching size for special cases of our bipartite graph model. However, it faces fundamental limitations in providing theoretical results beyond the cases where α f and α are small. 6 Nonetheless, our analysis provides us with a surrogate function µ KS (b l , b r ) that offers a more complete numerical picture and allows us to quantify the difference between the one-sided and the balanced allocations across varying B, α f and α.

Subsequently, in Section 2.6 we incorporate the cost of flexibility to find the flexibility designs that optimize over both the budget B and its allocation. We identify geometric properties of µ (b l , b r ) and highlight their managerial implications for platform experimentation. Last but not least, in Section 2.7, we show that our findings are robust under different matching platform models. We conclude with open directions for future research in Section 2.8.

6 Prior works had shown comparable results for other classes of sparse random graphs (see Section 2.1.2).

40 2.3 Flexibility Cannibalization

In the balanced allocation, flexible nodes on one side may form edges with flexible nodes on the other side, despite such edges likely being wasteful as we would prefer the flexible nodes to be paired with harder-to-match regular nodes: we call this the flexibility cannibalization effect. To understand it, recall that a feasible matching includes at most one of the edges incident to any given node. As such, flexibility designs should strive to avoid having many edges incident to the same node, many of which would be wasted. And, as the expected total number of edges is fixed given B, wasting edges can lead to fewer matches. The left side of Fig. 2.6 illustrates how flexible nodes tend to have a higher average degree in the balanced allocation than in the one-sided allocation. In the balanced allocation, it shows that edges concentrate in the subgraph of flexible nodes. The right side of the figure shows that this may create edges that are incident to the same flexible nodes, which cannibalize each other while leaving many regular nodes unmatched.

This intuition is confirmed with a simple computation: in expectation, the average degree of flexible nodes in allocation (b , B − b l ) is (α f + α) + (α f − α) ·l 2b l (B − b l )/B. The first term, (α f + α), is independent of l b l , whereas the term (α f − α) · 2b (B − b l )/B captures the contribution of edges between flexible nodes. This contribution is maximized when b l = B/2, i.e., in the balanced allocation, which, therefore, is particularly likely to have edges incident to flexible nodes cannibalizing each other. Of course, this is just a description of the flexibility cannibalization effect, not proof that the balanced allocation is suboptimal. Before diving into the mathematical formalization to understand when this is the case, we now provide an example of how flexibility cannibalization may arise in practice.

Figure 2.6: Illustration of flexibility cannibalization. Plots (a)-(b) compare edge probabilities and plots (c)-(d) illustrate possible realizations of one-sided and balanced allocations. In the balanced allocation, edges are more likely to realize in the upper subgraph of flexible nodes than in the lower subgraph. Consequently, despite plots (c) and (d) containing the same number of realized edges, (d) leads to fewer matches due to the cannibalization of edges in the upper subgraph.

Consider the example of the ride-hailing platform from the introduction and Fig. 2.2. It employs flexibility incentives on both market sides: “Wait and Save” on the demand side and “Ride Streak” on the supply side – this can be interpreted as the balanced allocation in our parsimonious model. Flexibility cannibalization occurs when flexible drivers and

41 flexible riders end up clustered in the same area, which often happens naturally due to the stochastic nature of supply and demand. The platform then has no choice but to match flexible drivers with flexible riders, as there are no regular alternatives around. The platform also has difficulty finding feasible matches in other areas without flexible drivers and riders. In our model, this is analogous to edge realizations such that flexible nodes form edges with each other rather than with regular nodes in the balanced allocation. In that situation, the platform has to pay twice the cost of flexibility for each flexible-flexible match (Wait and Save discount and Ride Streak bonus), and this flexibility does not help with the harder-to-match regular nodes. In contrast, by incentivizing only one side of the market, the platform avoids ever ending up paying twice for flexibility, and all the flexibility is guaranteed to be used to help match regular nodes.

Returning to the theory, Theorem 1 constructs a coupling that exploits the flexibility cannibalization effect to prove the dominance of the one-sided allocation when B = 1 and

α = 0.

Theorem 1. If (i) B = 1 (“half of the nodes are flexible”), and (ii) α = 0 (“no edges between regular nodes”), then µ (B, 0) ≥ µ (B/2, B/2).

The conditions B = 1 and α = 0 identify a parameter regime wherein, due to flexibility cannibalization, the one-sided allocation dominates for any α f . However, while cannibalization also exists in regimes when B < 1 and α > 0, Section 2.4 will show that another effect can counteract cannibalization. Before diving into that second effect, we use the rest of this section to showcase the proof of Theorem 1, wherein we develop a novel coupling technique to highlight the role of flexibility cannibalization.

Proof of Theorem 1. We prove that the one-sided allocation dominates the balanced one when B = 1 and α = 0. Below, we state two lemmas and prove they imply the theorem, deferring the proofs and constructions for the lemmas to Section 2.3.1-2.3.2 and the corresponding appendices.

We first introduce a new bipartite random graph distribution, denoted G n b . This distribution is easier to analyze than the balanced allocation random graph (denoted G n (1/2, 1/2)) but has the same asymptotic matching probability. In G n b , exactly n/2 nodes are flexible on each side (see Fig. 2.7). Each flexible node generates directed edges to the nodes on the other side (flexible or not), independently and with a probability p n f for each edge. This means that an edge between two flexible nodes can be generated in both directions (as shown in the right plot of Fig. 2.7). When computing a maximum matching in G n b we ignore the directionality of the edges and treat such double edges between nodes as just a single edge. We introduce G n b as its realizations can be more easily coupled with the random graph of the one-sided allocation. Denoting the size of a realized maximum matching in G n b by the random variable M b n and that of G n (1/2, 1/2) by M n (1/2, 1/2), we show nodes in G n b and G n (1/2, 1/2) have the same asymptotic matching probability.

Lemma 1. With the above construction, lim sup n→∞ E [ M n (1/2, 1/2) − Mn b 

] /n = 0.

Now, we compare G n b to the random graph with one-sided allocation. We denote the latter by G n o and its maximum matching size by M n (1, 0). The next lemma compares M b n and M n (1, 0) in a non-asymptotic way. This is the key step of this proof, relying on an intricate coupling of interest in its own right.

42 Lemma 2. With the above construction, E [ Mn b 

]

≤

E [ M n (1, 0) ] ∀n.

In the following derivation, Lemma 1 gives us the second equality and Lemma 2 the inequality:

M n (1/2, 1/2) M b n M n (1, 0) µ (1/2, 1/2) = lim sup E = lim sup E ≤ lim sup E = µ (1, 0), n→∞ [ n ] n→∞ [ n ] n→∞ [ n ]

which completes the proof of Theorem 1.

2.3.1 Proof sketch of Lemma 1

As illustrated in Fig. 2.7, the graph G n b is a directed random graph that contains edges generated from left to right (denoted R ij l ) and edges generated from right to left (R ij r ). The edge probabilities are given by:

P = 1 , ∀i ∈ [n/2], j ∈ [n] and P = 1 , ∀j ∈ [n/2], i ∈ [n]. Rij l  = pn f  Rij r  = pn f  [ ] [ ]

(2.1)

Figure 2.7: Illustration of G n (1/2, 1/2) and G n b . In G n b we assume that the top n/2 nodes on each side are “flexible” nodes that generate a directed edge towards any node on the opposite side with probability p n f .

G n b differs from G n (1/2, 1/2) in two ways: (i) G n b contains n/2 flexible nodes on each side of the bipartite graph, whereas every node in G n (1/2, 1/2) is flexible with probability 1/2; (ii) in G n b an edge between v i l and v j r , i, j ∈ [n/2], is generated from each side with probability p n f , instead of being generated only once with probability 2p n f . It is intuitive that neither (i) or (ii) significantly change the asymptotic matching size: standard concentration bounds guarantee that (i) affects o(n) nodes, and (ii) affects ∑ i,j ∈ [n/2] ( p n f ) 2 = ∑ i,j ∈ [n/2] ( α f /n ) 2 ∈ O(1) possible edges in expectation. In Appendix A.3.1, we formalize this intuition.

2.3.2 Proof sketch of Lemma 2

In our proof, we construct a coupling between pairs of realizations of G n b and of G n o to compare the maximum matching sizes therein. First, we show that this coupling is valid in the sense

43 that the coupled realizations occur with the same probability in their respective graphs. Second, we show that the sum of the maximum matching size in the pair of realizations in G n b is smaller-equal to that in G n o for any realization. We present the key steps of our proof here and defer the complete proof to Appendix A.3.1.

Coupling the Realizations of Graphs. We partition the directed edges in a realization of G n b into sets X 1 , X 2 , X 3 and X 4 , depending on whether they are from left/right to top/bottom (see Fig. 2.8 (A)).

Figure 2.8: Illustration of the edges’ coupling in graph (A) - (D)

We couple each realization of edges, i.e., of sets X 1 , X 2 , X 3 and X 4 , with a second realization (B), also from G n b , that occurs with the same probability (Fig. 2.8 (B)). Essentially, ~ ~ we “flip” the edges in X 3 and X 4 across the vertical axis to obtain the sets X 3 and X 4 . Then, we couple (A) and (B) with two realizations, (C) and (D) (see Fig. 2.8 (C) and (D)), of G n o . There, we “flip” the edges in X 1 from the upper subgraph in (A) and (B) to the lower subgraph in (C) and (D). Intuitively, as flexibility cannibalization can happen in the upper subgraph of G n b , where the edges in X 1 and X 2 are concentrated, we want our coupling to “flip” the edges in X 1 to the less dense lower subgraph and thereby hopefully increase the number of matches. However, denoting by M A , M B , M C , M D the maximum matching sizes in the respective graphs, it is not always true that M A ≤ M C or M B ≤ M D . Instead, we will show that M A + M B ≤ M C + M D holds for all X 1 , X 2 , X 3 , and X 4 , and thereby guarantee that E [ M n b ] ≤ E [ M n (1, 0) ] . We include the formal coupling in Appendix A.3.1.

Proving the Dominance of One-sided Allocation. Our proof concludes by showing that the required property M A + M B ≤ M C + M D indeed holds for arbitrary X 1 , X 2 , X3  and X 4 , which shows that the flexibility cannibalization in the upper graphs of (A) and (B) indeed induces a lower number of matches. As illustrated in Fig. 2.9, in (A) we denote by sets Y i ⊂ X i the edges that are part of a given maximum matching; similarly, in (B), we denote by sets Y 1 ′ ⊂ X 1 , Y 2 ′ ⊂ X 2 , ˜Y 3 ⊂ ˜X 3 and ˜Y 4 ⊂ ˜X 4 the edges that are part of a maximum matching. We then injectively map all edges of M A and M B (i.e., those in Y 1 , Y 2 , Y 3 , Y 4 , Y 1 ′ , Y 2 ′ , ˜Y 3 and ˜Y 4 ) into existing edges of (C) and (D) that also form a matching; this immediately proves M A + M B ≤ M C + M D . We construct this mapping in two steps.

Step 1: mapping Y 1 , Y 2 , Y 1 ′ and Y 2 ′ . We start by directly copying the matched edges from Y 1 , Y 2 , Y 1 ′ and Y 2 ′ into (C) and (D), following the coupling rules. This corresponds to the red, blue, pink, and navy edges in Fig. 2.9.

44 Figure 2.9: Illustration of the matches in (A) and (B), and the position they are copied into in (C) and (D).

Figure 2.10: The plot illustrates the mapping of edges in Y 3 and ˜Y 3 (the yellow edges) to (C) and (D) through the constructed graph G ′ . The labels indicate the correspondence between nodes/edges in G ′ and those in graphs (A)-(D). A second graph G ′′ can be constructed to map the edges in Y 4 and ˜Y 4 (the green edges) into the indicated positions in (C) and (D).

Step 2: mapping Y 3 , Y 4 , ˜Y 3 and ˜Y 4 . The rest of the matched edges (the yellow and green edges) can also be mapped into (C) and (D), but this mapping is not static and depends on the matches that are already copied into the graphs. As the nodes in (C) and (D) that are matched through these copied edges can no longer be matched to any other node in the graphs, we denote the remaining nodes in (C) and (D) by ¯C and ¯D and the set of edges among these nodes by E(¯C) and E(¯D). Then, it suffices to show that we can injectively map all other matches (that we have not copied already) in (A) and (B) to M(¯C) ∪ M(¯D), where M(¯C) and M(¯D) are respectively matchings that we construct in E(¯C) and E(¯D). We construct such a mapping for edges in Y 3 and ˜Y 3 based on a n × n colored bipartite 2 2 multigraph G ′ (see Fig. 2.10). G ′ includes all edges from Y 3 and ˜Y 3 that occur in graph (A) and (B); we label edges in G ′ that come from Y 3 as type A edges and edges from ˜Y 3 as type B edges (there can be two edges, one of type A and one of type B, between a pair of nodes in G ′ ). We color the nodes in G ′ based on whether the corresponding nodes in (A) and (B) are incident to Y 1 , Y 2 , Y 1 ′ and Y 2 ′ . Analogous to G ′ , we create a second graph G ′′ that contains all the edges from X 4 that are part of maximum matchings in (A) and (B). We show that edges in G ′ , G ′′ can be mapped into graphs (C) and/or (D) based on their types

45 and the colors of their incident nodes so that, together with the already copied edges, they produce feasible matchings in (C) and (D). As a result, each edge from M A and M B can be found in a matching in either (C) or (D), implying that M A + M B ≤ M C + M D . Thus, E [ M n b ] ≤ E [ M n (1, 0) ] , ∀n when α = 0. We formalize these constructions in Appendix A.3.1.

2.4 Flexibility Asymmetry

Moving away from the parameter regimes in Theorem 1, we now study when the balanced allocation may dominate the one-sided one. This dominance is driven by a second effect, which we refer to as flexibility asymmetry and which is particularly strong for large α f .

Unlike cannibalization, asymmetry is an effect that focuses on regular nodes. When B < 1 (i.e., less than half the nodes are flexible), any flexibility allocation has regular nodes on both sides. When the allocation is not perfectly balanced, regular nodes on the side of the graph with more flexible nodes — on the left in Figure 2.11 (a) and (c) — have fewer neighbors in expectation than regular nodes on the other side. This is most pronounced in a one-sided allocation. When B < 1 (so that there are regular nodes on both sides), it can be easily found that the (1 − B)n regular nodes on the side of the graph where flexibility is allocated have an expected degree of 2α (all their potential neighbors are regular nodes). In contrast, the ones on the other side have an expected degree of 2α + B(α f − α), which grows with α f − α. Therefore, the imbalance of the flexibility allocation creates an asymmetry in the random graph, where regular nodes on one side may be “easier” to match than regular nodes on the other. For example, for small α, the small expected degree of some regular nodes may cause many of those to be isolated and thus impossible to match. This intuition is confirmed in our next result: when B < 1 and α f − α is large, the balanced allocation provably yields the fewest isolated nodes across all possible allocations, while the one-sided allocation maximizes their number.

Proposition 1. For any B ∈ (0, 1), α ≥ 0 and α f − α > 1−B 2 , the asymptotic fraction of degree-0 nodes (as n → ∞) is minimized at allocation (B/2, B/2) and maximized at (B, 0)

This shows that there may be an issue with the one-sided allocation, as isolated nodes cannot be part of a maximum matching, and that this issue arises when B is smaller than 1 (not many flexible nodes) and α f is large (flexibility is strong). The fact that α f must be large is intuitive: it weakens the cannibalization effect, as the high degree of flexible nodes makes the wastefulness of flexible-flexible edges a less pressing concern. However, the intricate combinatorial nature of a maximum matching is much more complex than simply counting the number of isolated nodes. To understand intuitively why asymmetry can reduce the matching probability in the one-sided allocation, consider an example when flexibility is so strong that flexible nodes can be matched with any node, as illustrated in Figure 2.11 (a) and (b). In that specific case, a simpler two-stage matching algorithm is optimal. First, we find a maximum match in the subgraph of regular nodes (marked in blue in the figure), and then we add the flexible nodes to make as many additional matches as possible. Interestingly, when α is small enough, regardless of the allocation, there are almost always sufficiently many regular nodes unmatched after the first stage for the second stage to add exactly Bn matches

46 Figure 2.11: To gain intuition for the flexibility asymmetry effect, plots (a) and (b) assume that each flexible node is connected to all nodes on the other side of the graph, which resembles the case of α f being large. A perfect matching in (a) requires the realization of one of the three dashed edges, while (b) requires one of four dashed edges to realize. This intuition holds at a larger scale: the expected number of edges in the subgraph of regular nodes is (1 − B/2) 2 /(1 − B) > 1 times greater for the balanced allocation in (d) than for the one-sided allocation in (c). Since the size of a maximum matching is close to the number of edges when α is small, the balanced allocation is more conducive to matching the regular nodes among themselves.

by matching all flexible nodes to available regular nodes. Therefore, when α is small enough, the allocation that maximizes the probability of a match is the one that is best in the first stage, i.e., the allocation that can maximize the probability of a match in the regular node subgraph. Interestingly, Figure 2.11 and its caption illustrate that the one-sided regular node subgraph is asymmetric and explain why asymmetric graphs lead to fewer matches as long as α > 0. In other words, when flexibility is strong but limited, and when it is not too easy to match regular nodes with regular nodes, the best allocation is the one that enables the maximum number of regular-regular matches. The following theorem formalizes this intuition, but instead of taking α f to infinity, we use similar ideas to find a range of parameters where the balanced allocation provably dominates.

Theorem 2. If (i) α f µ (B, 0).

≥

22 , (ii) α ∈ [0.01, 0.05], and (iii) B ∈ [0.4, 0.8], then µ (B/2, B/2) >

We can prove that the balanced allocation dominates in a parameter regime where the asymmetry effect is particularly strong: (i) flexible nodes must be especially easy to match (α f ≥ 22); (ii) regular nodes should be hard – but not impossible – to match so that regular-regular matches matter (α ∈ [0.01, 0.05]); (iii) B should not be close to 1 (otherwise, all allocations are equivalent because flexible nodes are sufficient to match everyone) and more than 0 (otherwise, all allocations are equivalent because there is no flexibility). Before discussing the proof of the theorem, we want to highlight that there are important applications in this parameter regime. For instance, the freelancing platform Upwork offers a digital learning program called “Upwork Academy” to train highly skilled freelancers to handle a wide range of tasks. This type of flexibility is valuable in allowing the high-skilled freelancers to be

47 matched with demanding customers who otherwise cannot be served. On the demand side, similarly, the platform uses a feature called “Project Catalog” to incentivize users to choose from a standardized pool of tasks that most freelancers can fulfill. Essentially, employing flexibility on both market sides allows the platform to match flexible agents on each side with “difficult” agents on the opposite side. With flexible agents on only one side of the platform, it can be difficult to match regular agents on that side of the platform. In particular, when some freelancers are well-trained but all customers are quite demanding, it becomes difficult for freelancers with a limited skill set to find a job. Similarly, when some customers have standard requests but no freelancers receive specialized training, it becomes difficult for the platform to serve the demanding customers.

Proof sketch of Theorem 2. Our proof (Appendix A.3.2) leverages the two-stage matching procedure to analyze µ (B/2, B/2): we first study the size of a maximum matching among the regular nodes (stage 1), and then quantify the additional matches that can be added using the flexible nodes (stage 2). This allows us to derive a lower bound on the number of matched nodes under balanced flexibility. Similarly, we derive an upper bound on the maximum matching size under one-sided flexibility by bounding the number of isolated nodes in the graph. We then prove the theorem by verifying that the upper bound is dominated by the lower bound in the specified parameter regime.

Lower bound on the number of matched nodes for balanced flexibility. For balanced flexibility, we lower bound the size of a maximum matching among the regular nodes, and then show that almost all flexible nodes can be matched afterward. As illustrated in Fig. 2.11 (d), in stage 1, the balanced allocation faces an equal number of regular nodes on both sides. We prove (Appendix A.3.2) the following bound on the maximum matching size in a (1 − B/2)n × (1 − B/2)n graph of regular nodes, 7 denoted by random variable m 1 :

Lemma 3. E [m 1 ] ≥ 2 · ( 1 − B/2 ) n

1 − (1 − B/2)α − e −2α(1−B/2) as n → ∞. [ ]

Intuitively, for small α the expected maximum matching size should be close to the expected number of edges because very few nodes have a degree more than 1. Our proof explicitly characterizes this, and lower bounds m 1 by subtracting the number of “redundant edges” (those incident to nodes with degree > 1) from the total number of edges. This allows us to derive the lower bound for E [m 1 ] in Lemma 3.

Upper bound on the number of matched nodes for one-sided flexibility. To upper-bound the matching size under one-sided flexibility, we simply quantify the expected number of isolated regular nodes on the side on which there is flexibility. As illustrated in Fig. 2.11 (c), since there are about (1 − B)n regular nodes on this side, about (1 − B)ne −2α of these are isolated. It follows that at most (1 − B)(1 − e −2α )n of these regular nodes can be matched.

Combining the bounds. For the purposes of this proof sketch, we assume that all flexible nodes can be matched to regular nodes in stage 2 of the algorithm. Then, the number of matches under the one-sided allocation is at most Bn + (1 − B)(1 −1 e −2α )n whereas the number of matches under the balanced allocation is at least Bn + E [m ]. By verifying that

Bn for α ∈ [0.01, 0.05] and B ∈ [0.4, 0.8], we confirm that the balanced allocation creates more matches than the one-sided allocation in the stated regime. In Appendix A.3.2 we show that the gap in the above inequality is sufficiently large to account for the fact that, in the balanced allocation, some flexible nodes may not be matched in stage 2. We highlight that α > 0 is necessary for this comparison as otherwise no regular nodes could be matched in stage 1 (under either allocation) and the two sides of the inequality would be equal.

2.5 Identifying the Right Allocation Across All Parameters

In this section, we analyze the properties of µ (b l , b r ) for a broader range of parameters using the Karp-Sipser (KS) algorithm, a less intuitive but more classical tool in the study of sparse random graphs. As formalized in Algorithm 3 in Appendix A.3.3, the KS algorithm iteratively matches and prunes nodes with degree 1 until no such nodes remain; thereafter, it randomly selects edges to match. This algorithm has two advantages: first, its simple “greedy” structure makes it amenable to theoretical study, and prior works have described its behavior on random graphs. Second, it can be optimal in sparse settings. For example, it is always optimal if the graph is a tree and yields asymptotically optimal matchings for some classes of sparse random graphs [6, 8]. These two facts combined make it a valuable tool to study maximum matching in sparse settings. Though prior works do not encapsulate the random graphs we study (see Section 2.1.2), we show that the KS algorithm is amenable to our model. However, to formalize the additional complexity arising from the comparisons between different flexibility allocations, we additionally require computer-aided proofs. We include the derivations and proofs corresponding to this section in Appendix A.3.3.

Our analysis is based on the quantity µ KS (b l , b r ), which is constructed from a set of nonlinear equations (see Equation (A.9) and Theorem 18 in the appendix). Such equations are common in KS-based analyses to characterize the fraction of nodes that are a “target” or a “loser” [8]. Whereas Karp and Sipser’s original analysis focused on a homogeneous Erdős–Rényi graph and thus relied on just 2 of these equations, ours requires 8 equations to determine the probability for flexible or regular nodes on either side to be either a target or a loser. When B = 1, Theorem 3 below states the equivalence of µ (b l , b r ) and µ KS (b l , b r ) for the one-sided and balanced allocations in almost all of the subcritical regime, classically defined [38] as the setting where the average expected degree of a node, α f + α in our case, is smaller than Euler’s number e.

Theorem 3. When 10 −4 < α < α f , α f +α < e, and b = (1, 0) or (1/2, 1/2), µ (b l , b r ) = µ KS (b l , b r ).

Though Theorem 3 characterizes a region in which µ (·, ·) = µ KS (·, ·), this does not suffice to make formal comparisons between µ (1, 0) and µ (1/2, 1/2); since there are no closed-form solutions to these nonlinear equations, we need to show that we can solve the nonlinear equations characterizing µ KS (b l , b r ) to provable numerical precision for the region specified by the theorem (see (A.23) in Appendix A.3.3). This then allows us to compare µ (1, 0) and f KS µ (1/2, 1/2) for these values of α and α. Moreover, we derive a continuity property of µ in α f and α, that lets us construct local lower bounds for µ (1, 0) − µ (1/2, 1/2) (see (A.21)

49 and (A.22)). We conclude by verifying in a computer-aided proof that these lower bounds exceed 0 across the parameters specified in the following theorem:

Theorem 4. µ (1, 0) > µ (1/2, 1/2) when (i) α f + α < e and (ii) 10 −4 < α < 0.77α f − 0.16.8 

Theorem 4 allows us to prove the dominance of the one-sided allocation for a wider set of parameters in which α f + α remains relatively small (recall that Theorem 1 allows for arbitrarily large α f but requires α = 0). Beyond the subcritical regime, KS-style analyses have fundamental limitations for two reasons: first, the asymptotic optimality of KS is not known for bipartite graphs beyond the subcritical regime (see [7, 41]); and secondly, our computer-aided comparison of different flexibility allocations requires the nonlinear equations to have a unique set of solutions, which is known [8, Lemma 1] to require the subcritical regime.

Figure 2.12: The plots present ( µ KS (b l , b r ) − µ n EMP (b l , b r ))/ µ n EMP (b l , b r ) across varying (b l , b r ) as n scales large.

Despite the analytical challenges in extending Theorem 3 and 4 to other parameter regimes, our numerical results (see Fig. 2.12) suggest that µ n EMP (b l , b r ) approaches µ KS (b l , b r ) as n → ∞ for a much wider set of parameters. We, therefore, use µ KS (b l , b r ) as a surrogate function to evaluate different flexibility allocations, not just the balanced and one-sided one, across a wider range of parameters. This is not doable with µ EMP due to the heavy computations needed to evaluate it with high precision. Specifically, we conduct a grid search over B, α f , α, b l , br  with the set of parameters denoted S (details in Appendix A.3.3); we trust this to give a better estimate of the true asymptotic matching probability while also being computationally more efficient. We highlight the following observations:

Either the one-sided or the balanced allocation is optimal. In line with the findings in Fig. 2.4, our more extensive numerical results show that, across our grid search, µ KS (b l , b r )

8 The boundary in condition (ii) arises from the ability for a computer-aided proof to verify the inequality within a reasonable runtime: for δ f > 0, we construct and compute a lower bound the value of µ (1, 0) f µ (1/2, 1/2) within each set of [α , α + δ) × [α, α + δ) within the subcritical regime. Taking δ = 0.001 yields the boundary in Theorem 4 (ii) and runs in about 20 hours.

50 Figure 2.13: The plots present the values of µ KS µ (B/2,B/2) KS (B,0) across varying α f , α − α f and B: the ratio is smaller than 1 in the red region (light red if between 0.99 and 1) and greater than 1 in blue region (light blue if between 1 and 1.01). The dashed line highlights the boundary of the subcritical regime, and regions (I)-(II) indicate where the two allocations have comparable performances.

is always maximized by one of the one-sided or the balanced allocation. It thus supports our focus on comparing these two. Intuitively, the one-sided allocation (i) minimizes the cannibalization effect by eliminating potential flexible-to-flexible edges, but (ii) maximizes the asymmetry effect by making it harder to match regular nodes with each other. For the balanced allocation, these two are exactly reversed. Our numerical findings suggest an optimal allocation always minimizes one of the two effects.

In the subcritical regime, the one-sided allocation is better. In Theorem 4, we proved this result for most of the subcritical regime and B = 1. When B < 1, our computer-aided proof breaks because we cannot prove that the nonlinear equations in (A.9) have a unique set of solutions. However, we still find numerically that the one-sided allocation is better within the subcritical regime for all tested values of B (see Fig. 2.13). This also matches our theoretical findings in that α f cannot be too large in the subcritical regime, which naturally limits the effect of flexibility asymmetry (see Theorem 2). In particular, even though Proposition 1 shows that the balanced allocation may be minimizing and the one-sided allocation may be maximizing the fraction of isolated nodes in this regime, this is outweighed by the effect of flexibility cannibalization.

When B = 1 or α = 0 the one-sided allocation is better. We find that B = 1 and α = 0 are the special cases where the one-sided allocation always dominates, 9 regardless of the value of α f . Comparing this with our two-stage matching procedure in Section 2.4, we find that these are exactly the cases where the flexibility asymmetry effect dissipates. This also explains why the coupling technique presented in Section 2.3 is specific to B = 1 and α = 0: for large α f , Fig. 2.13 shows that the dominance of the one-sided allocation breaks down very close to the regime where B = 1 and α = 0.

Characterizing when the flexibility allocation matters. Finally, our numerical results

9 For α = 0, though hard to see in the plots, there is always a thin red line just above the x-axis.

51 in Fig. 2.13 also allow us to characterize the regions in which the flexibility allocation is of second-order importance. In region (I), flexibility does not notably increase the edge probability as α f /α ≈ 1; thus, neither the budget nor the allocation of flexibility has a sizable effect. In region (II), with large α and α f , almost all nodes are matched irrespective of the flexibility allocation. Thus, in (I) and (II), any allocation of a fixed flexibility budget results in a similar matching size. In contrast, in regions where flexibility cannibalization (moderate values of α and α f ) and flexibility asymmetry (small α, large α f , and B < 1) are most prominent, the surrogate function identifies a larger gap between the one-sided and the balanced allocation. This mirrors our observation in Fig. 2.5 that either of the two allocations can dominate the other by at least 8% in these regions.

2.6 Managerial Implications for Platform Experimentation

Flexibility cannibalization and asymmetry can have important managerial implications. To highlight them, we extend our model slightly to study the geometry of a platform profit function that incorporates both the benefit and the cost of flexibility. Formally, we assume that the flexibility decision (b l , b r ) incurs a linear cost of c · (b l + b r ) for some constant c > 0. That is, we focus on the optimization problem

b max µ (b l , b r ) − c · (b l + b r ) ∈ [0,1]2 

(2.2)

Such a linear cost model reflects a setting wherein the marginal cost of more agents becoming flexible is approximately constant. This simplicity allows us to underline our main point, but our high-level observations would likely translate to other cost structures. We use the notation g(b l , b ) := µ (b l , b r ) − c · (b l + b r ) to refer to this objective function and g KS (b l , b r ) to denote µ KS (b l , b r r ) − c · (b + b r ).

In Fig. 2.14 we plot l g KS (b l , b r ) for two different sets of parameters of α f , α and c. The plots reveal distinct convexity and concavity properties in the directions of (1, 0), (0, 1), and (−1, 1). In the directions of (1, 0) and (0, 1), we consistently observe a concave function gKS  regardless of the starting point, i.e., the value of flexibility in our matching model exhibits decreasing returns. A similar decrease in the marginal value of flexibility is present in those works that identify that a little flexibility is almost as valuable as full flexibility [32, 46]. However, we also observe interesting geometric effects in the direction of (1, −1); this direction captures the tradeoff between investing a fixed budget of flexibility on one side or the other. Depending on the values of α f and α, Fig. 2.4 and Fig. 2.14 show that µ KS (b l , b r ), respectively g KS (b l , b r ), can be convex, concave or neither in the direction (−1, 1). Both the concavity in directions (0, 1) and (1, 0) and the potential convexity in direction (1, −1) are supported by theoretical findings in Appendix A.2.

In the remainder of this section, we first discuss two serious practical ramifications of such geometric properties and then argue how an understanding of flexibility cannibalization and asymmetry can help avoid a potential pitfall of current platform experimentation designs. Many platforms today operate with separate teams dedicated to controlling flexibility incentives on the demand and supply sides. Through frequent experimentation, including

52 (a) α f = e/2, α = 0 and c = 0.4

(b) α f = 4e, α = e/2 and c = 0.03

Figure 2.14: The plots present the value of g KS (b l , b r ) for varying α f , α and c. We highlight the values of the function in the directions (1, 0) and (0, 1) in blue, and in the direction (−1, 1) in red.

continuous local improvement of algorithmic parameters, these teams aim to optimize the flexibility investment on each respective side of the market. For illustrative purposes, suppose the supply and demand teams iteratively vary the flexibility investment on their own side (bl  and b r ) by γ whenever doing so improves the objective. The teams would eventually settle at a point where neither has an incentive to further change its flexibility investment. In Fig. 2.15, we build upon g KS (b l , b r ) to illustrate the outcomes of such experiments, which yields the following two observations:

Figure 2.15: The colored lines illustrate the trajectory of experimentation on the surface of g KS (b l , b r ) for different choices of γ . The experiment terminates around a suboptimal balanced allocation in (a) when γ is too small, and around a suboptimal one-sided allocation in (b) when γ is too large.

Suboptimality due to the lack of joint experimentation. Teams may settle at a suboptimal flexibility design due to not experimenting jointly. In other words, they may find themselves at a point where neither team can unilaterally improve the joint objective even though a joint experiment in the direction of either (1, −1) or (−1, 1) would yield a strict

53 improvement. Fig. 2.15 (a) illustrates that this can arise, when γ is small, near a suboptimal balanced allocation. At this suboptimal allocation, each team faces a concave objective and optimally manages its own levers (i.e., g KS (b l , b r ) is locally optimal in the directions (1, 0) and (0, 1)), but the overall flexibility decision remains suboptimal for the platform. In Appendix A.2, we formalize this observation by modeling the flexibility optimization along two axes as a game between two verticals within an organization (see Section 2.1.2); even though the verticals have the same payoff functions, we show that the suboptimal allocation can emerge as a local Nash Equilibrium (see Appendix A.2). Though the suboptimal allocation in Fig. 2.15 (a) can be avoided by setting γ sufficiently large, Fig. 2.15 (b) illustrates that this does not generally address the suboptimality. Indeed, such large γ may cause an outcome wherein one team operates with more flexibility than is jointly optimal, leading the other team to not invest in flexibility at all. Thus, the platform becomes trapped in a one-sided flexibility allocation, even though adopting flexibility on both market sides would be more profitable.

Suboptimality due to the existence of saddle points. Surprisingly, joint experimentation is not enough to avoid suboptimal flexibility designs. When α and α f are small, the concavity of g KS (b l , b r ) in the direction (1, 0) and convexity in the direction (1, −1) give rise to a saddle point on the surface of g KS (b l , b r ), as illustrated in Fig. 2.15 (a). Near the saddle point, the gradient of g KS (b l , b r ) is close to 0 in all directions. As a result, when γ is too small, even with joint experimentation, the platform may fail to capture value in the (1, −1) direction. The profit at the saddle point can be vastly smaller than that at the globally optimal one-sided allocation: in Fig. 2.15 (a), the locally optimal balanced allocation achieves just 73% of the profit of the globally optimal one-sided allocation, and for other parameters the gap can be even larger, especially when the platform’s margins are small. For instance, with α f = 2e, α = 0 and c = 0.99, the profit of a locally optimal balanced allocation is less than 10% of that of the globally optimal allocation.

As any local experimentation scheme, joint or not, may face obstacles in exploring the complicated geometry of g KS , an understanding of the cannibalization and asymmetry effects can also help platforms design non-local experiments. Consider a digital matching market with high α f that operates with just one lever of flexibility at (B, 0); introducing a second lever on the opposite side of the market, one would usually invest in a little flexibility by experimenting with (B, ϵ). In contrast, our study shows that (B, 0) may be a local optimum of g KS (see Fig. 2.4) whereas (B/2, B/2) would yield a much greater profit. Similarly, a ride-hailing platform with small (α, α f ) may be locally stuck at a balanced allocation despite a one-sided one being much more profitable. To avoid both of these outcomes, our findings suggest that platforms may want to supplement local experimentation with experiments on qualitatively different flexibility designs, i.e., moving from one-sided to balanced or vice versa. Given the high cost of experimentation, it may make sense in practice to first leverage non-local simulation before then attempting experiments in significantly altered parameter regimes; nonetheless, our results emphasize the need to explore non-locally, which stands in contrast to common industry practices. Of course, another distinction in practice is that the impact of flexibility levers is likely to be less symmetric: costs may depend on the side of the market, the value of flexibility (α f − α) may vary across sides, and the edge formation process need not be independent (see next section). However, these additional features (i) are more likely to further complexify the geometry of g KS than to remove saddle points and local

54 optima, and (ii) do not eradicate the impact of flexibility cannibalization and asymmetry. As a result, the practical takeaway from our findings is that matching platforms ought to explore non-locally, in simulations or experiments, by leveraging a high-level understanding of the matching function’s geometry.

2.7 Robustness in Alternative Graph Models

In this section we show that the intuitions behind flexibility cannibalization and asymmetry effects extend to three alternative models of matching in random graphs. The goal of these models is to capture dependencies among the edges that realize, which is common in many platforms that solve matching problems in the physical world (e.g., when edges are proximitybased). We first consider a “local model” wherein nodes are only eligible to form edges with neighbors. Next, we consider a spatial model wherein the realization of edges is governed by the distances between supply and demand nodes. Finally, we use the spatial model to investigate imbalanced markets that allow an uneven number of supply and demand nodes. For all of these models we find that, even as different models create new effects, (i) flexibility cannibalization and asymmetry remain the crucial drivers of the optimal flexibility allocation and (ii) both effects remain dominant in the same parameter regime we previously identified.

2.7.1 Local Model

We now define and analyze the local model, which is the simplest model to capture dependencies among the edges that realize. As illustrated in Fig. 2.16, we assume that for any i ∈ [n], v i l ∈ V l is only eligible to connect to v i r , v (i+1) r mod n , ...v (i+k) r mod n in V r , where k is a constant that specifies the number of eligible neighbors of a node. In particular, in line with our previous model in Section 2.2, we assume that the probabilities associated with flexible and regular nodes now scale with k (rather than n), giving p f = α f /k and p = α/k for constant α f and α. We require that 0 ≤ p < p f ≤ 1/2 for the edge probabilities to remain in [0, 1] and obtain the following additive model of conditional edge generation:

2p + (F i l + F j r ) · (p f − p) if ((j − i) mod n) ≤ k − 1 P = 1 | Fi l ,Fj r  Rij  = [ ] 0 otherwise {

With a slight abuse of notation, we use M n (b l , b r ) to denote the size of a maximum matching in

the local model, as we did in previous sections, and µ (b l , b r ) to denote lim n→∞ E M n (b l n ,b r ) 10 . [ ] For small k, we find that flexibility asymmetry cannot be a significant effect in the local model. In particular, as in Section 2.4, the one-sided allocation yields expected degrees among regular nodes that are equal to B(α f − α) + 2α and 2α on the two sides respectively. The gap between these is small when α f f − α is small; however, under small k in the local model, α f must also be small to ensure α /k = p f ≤ 1/2. Thus, intuitively, we expect flexibility cannibalization to dominate in that regime. Indeed, when k = 2, the next result shows the dominance of the one-sided allocation across the entire feasible parameter space:

10 We show the existence of this limit in the proof of Theorem 5.

55 Figure 2.16: Illustration of local models with different values of k.

Theorem 5. When k = 2, µ (B, 0) > µ (B/2, B/2) for any B ∈ (0, 1] and p, p f with

0 ≤ p < p f ≤ 1/2.

(a) k = 2

(b) k = 5

(c) k = 10

Figure 2.17: The heatmaps present values of µ EMP µ EMP (B/2,B/2) (B,0) in the local model when B = 0.6 for varying k, α and α f − α. The parameter regimes that violate 0 ≤ p < p f ≤ 1/2 are left blank.

To prove Theorem 5, we derive a closed-form solution for µ (b l , b r ) through the combinatorial analysis of each possible local structure (see Appendix A.4.1). However, such an analysis becomes intractable for larger k. Our numerical results 11 in Fig. 2.17 indicate that as we increase k, the resulting plots begin to closely resemble Fig. 2.5 with a gradual emergence of the flexibility asymmetry effect. In the parameter regime where cannibalization previously dominated, which captures the entire parameter regime for small k, we observe that the

11 As before, we denote the empirical average matching probability by µ n,s EMP (b l , b r ). Across Section 2.7 we fix n = 100, s = 1000 and drop the dependency of µ n,s EMP (b l , b r ) on these two parameters.

56 one-sided allocation continues to dominate. In contrast, when k becomes large enough for α f − α to create significant asymmetry, we again observe the balanced allocation performing better.

2.7.2 Spatial Matching

In this subsection and the next, we focus on a model with spatial dependencies to better capture the matching problems faced by ride-hailing and food delivery platforms. In such platforms, the compatibility between pairs of agents is primarily governed by the distances between them. Thus, we start by considering a two-dimensional cell [0, 1] 2 with uniformly distributed drivers and riders. The n drivers are at locations denoted by vectors d 1 , d 2 , . . . , d n , and the n riders at r 1 , r 2 , . . . , r n . For a given flexibility allocation b = (b l , b r ), driver i is flexible if random variable F i l ∼ Bernoulli(b l ) takes the value of 1, otherwise the driver is regular. Similarly, each rider j is associated with F j r ∼ Bernoulli(b r ), and the rider is flexible if and only if F j r = 1. We take constants α f and α such that 0 ≤ α < α f and define p n f = α f / √ n, p n = α/ √ n, respectively. We assume that an edge exists between a driver i and a rider j if their distance is within a threshold decided by their respective flexibility types:

1 if ‖ ‖ d i − r j ‖ ‖ 2 ≤ 2p n + (F i l + F j r ) · (p n f − p n ) P = 1 | Fi l ,Fj r  Rij  = [ ] 0 otherwise {

In other words, r j has an edge with d i if their distance is within 2p n + (F i l + F j r ) · (p n f − p n ). The asymptotic set-up p n f , p n ∈ Θ(1/ √ n) ensures that the expected number of edges in the spatial graph is the same Θ(n) that we considered in our previous asymptotic regime.

The spatial model relaxes two assumptions common to the previous models we have examined: (1) the conditional independence assumption on edge realization R ij with respect to indices i and j, and (2) the equivalence of different flexibility allocations in expected edge counts. In particular, in the one-sided allocation the expected number of riders that connects to a random driver is12 

2 B + p n + (1 − B) (2p n ) 2 · π · n. pn f  ( ( ) )

This is smaller than the expected number of riders that connects to a random driver under the balanced allocation, which equals

2 2 B/2 ) 2 + 2 · B/2(1 − B/2) + p n + ( 1 − B/2 ) 2 (2p n ) 2 · π · n. 2pn f  pn f  ( ( ( ) ( ) )

As such, we expect the balanced allocation to have an advantage over the one-sided allocation in the spatial setting. Indeed, in Fig. 2.18 we find that in a parameter regime with small α f and α, the balanced allocation outperforms the one-sided allocation. This follows because the maximum matching size is close to the number of edges in this very sparse regime, and the latter is higher in expectation in the balanced allocation. In other parts of the heatmap, we

12 We assume for simplicity that the driver is at least 2p n away from the boundary of the [0, 1] 2 cell, an event that occurs with probability 1 as n → ∞.

57 (a) B = 0.6

(b) B = 1

Figure 2.18: The heatmaps present values of µ EMP µ EMP (B/2,B/2) (B,0) varying α and α f − α.

in the spatial matching model across

find consistency with the results in our main model: the one-sided allocation can outperform the balanced allocation by over 8% when B = 1 or when α f is moderate; moreover, it can be worse by more than 8% when α f is very large, α is a small positive number, and B < 1.

We highlight that α f and α capture the density of the spatial market: multiplying α f and α by a factor of η > 1 in a cell with side length 1 is equivalent to maintaining the number of uniformly distributed agents in the two-dimensional cell [0, 1/ η ] 2 but with the same compatibility as before, i.e., with α f and α kept constant. As a result, we can interpret the setting with very small α f and α as a spatial market in which (i) the density is very low, but (ii) drivers and riders nonetheless “expect” to be matched with agents that are very close. In contrast, as the market density increases, agents form more edges, which leads, at first, to flexibility cannibalization. With a further increase in density, we observe that when B < 1 flexibility asymmetry becomes a dominant effect and the balanced allocation yields a much larger matching size than the one-sided allocation. Therefore, a natural interpretation of our results is that the optimal flexibility allocation depends on the market density, the flexible/regular agents’ acceptable dispatch radius, and the flexibility penetration B.

2.7.3 Imbalanced Market

In this subsection we numerically investigate whether the structural insights we identified in fully symmetric settings are robust to imbalances in matching markets. Specifically, we extend the spatial model in the previous subsection by allowing λ · n rather than n riders, where λ ∈ (0, 1] (we ignore for symmetry the setting where the market has more demand than supply). We assume that, for a given flexibility allocation (b l , b r ), each driver is flexible with probability b l · λ and each rider is flexible with probability b r . This set-up ensures that the cost of incentivizing an equal number of riders and drivers remains the same. 13 We remark that the one-sided flexibility allocation (B, 0) is no longer equivalent to (0, B), as the latter generates more edges in expectation. This difference leads to (0, B) being a better allocation than (B, 0), and moreover it also weakens the flexibility asymmetry effect: in Fig. 2.19 (a) and (b) we show that the region in which the one-sided allocation is dominated by the balanced one almost vanishes. In contrast, the regions with the strongest advantage for the one-sided allocation are consistent with all of our previous findings.

13 In Appendix A.5 we consider an alternative model that assumes drivers and riders are flexible with probability b l and b r , respectively.

58 (a) B = 0.6

(b) B = 1

Figure 2.19: The heatmaps present values of µ EMP µ EMP (B/2,B/2) (B,0) varying α and α f − α when λ = 0.8.

2.8 Conclusion

in the imbalanced model across

In summary, our work initiates the study of two-sided flexibility. Our model is not meant to represent any specific platform accurately but to gather structural insights likely to generalize to realistic settings. In particular, we identify flexibility cannibalization and asymmetry, which are respective drawbacks of the balanced and one-sided allocations, showcasing that two-sided flexibility can interact in complex ways. We characterize the typical parameter regimes where each effect dominates and numerically evaluate their strength. Our main practical recommendation for platforms is that their various products affecting flexibility on both sides interact and should therefore not be considered independently. The teams in charge of these products should communicate and conduct experiments and simulations that jointly vary different levers to avoid suboptimal outcomes that can easily arise otherwise.

On the theoretical side, comparing the expected maximum matching sizes in graphs with different flexibility allocations is a challenge, and we leverage a coupling construction, employ concentration bounds, and generalize KS algorithm-based analyses with computer-aided proofs. Nonetheless, our work leaves many questions open. Firstly, our model intentionally focuses on a particular type of edge probability distribution, which keeps the expected number of edges invariant for a given budget B. However, different constructions (e.g., based on random geometric graphs) may be of practical interest. Secondly, though our effects seem to be robust under some such different constructions (see Section 2.7), all of our results are based on a central decision maker maximizing an unweighted matching, whereas many platforms in practice involve choice among agents on both sides; we know of no results in this direction and believe it to likely yield interesting findings. Finally, our work focuses on a matching model, but two-sided flexibility may also appear in queueing and manufacturing settings. All of these directions may be fruitful and, together, potentially reveal a general theory of two-sided flexibility.

59 60 
# Chapter 3 On the Supply of Autonomous Vehicles in Platforms

3.1 Introduction

The development of commercially viable autonomous vehicles (AVs) will, if successful, transform transportation. As early as August 2023, AVs have been deployed, either operationally or as pilots, in at least 18 U.S. cities [47]. This includes commercial deployments with no safety drivers in San Francisco and Phoenix [48, 49], and, more recently, in Los Angeles and Austin [50, 51]. The strong momentum is expected to continue, with some estimating the robotaxi market size to grow to up to 45 billion US dollars by 2030 [52].

One important obstacle in the path of widespread AV adoption is the high cost of AV hardware, which currently stands at $150,000 to $200,000 per vehicle [53]. John Krafcik, the CEO of Waymo, one of the firms leading the race to develop AV technology, is famously bearish on the question of whether AVs will be adopted in mass for private use any time soon due to the technology’s high cost [54]. Similarly, analysts widely expect that Level 5 (Full Driving Automation) AVs will not reach individual households before 2035 [55]. Instead, AVs are widely expected to first build a major presence in settings where they could be highly utilized, such as in ride-hailing and delivery, which are precisely the settings where they are already commercially deployed [55–57].

In line with such expectations, our work focuses on four potential operational models for the commercial deployment of AVs in the ride-hailing industry. We first consider (1) a model where AVs are adopted within the context of open platforms, which are platforms that allow third-parties such as human drivers and AV suppliers to bring their vehicles into the system. This is akin to the operational model currently adopted by Uber and Waymo (owned by Google parent company Alphabet Inc.) in Phoenix [58] and the planned partnership between Lyft and May Mobility in Atlanta [59], among others. We also consider variations of such an open platform wherein the platform is able to make contractual commitment to the AV supplier, e.g., with regard to utilization or prioritization. The second current operating model is (2) an AV-only platform that is operated independently by the AV supplier. In particular, Waymo operates AV-only platforms in San Francisco and Los Angeles [48, 50], though our results show that such deployments can face significant inefficiencies due to an

61 inability to access flexible human drivers to handle stochastic demand (see Section 3.5.1). We also analyze (3) a platform that sources AVs from a supplier through leasing contracts (either short- or long-term); this resembles the newly launched partnership between Uber and Waymo in Austin [51] and more closely follows the payment structure in a traditional supply chain, though it is subject to the well-studied risk of double marginalization and has worse theoretical guarantees than a well-contracted open platform model (see Section 3.5.2). Finally, we consider (4) a benchmark model where AVs and human drivers are integrated on a single ride-hailing platform. This operational model is akin to a “Waymo buys Lyft” model, and can in theory lead to an efficient supply chain design. However, due to regulatory risk and financial obstacles, AV technology companies such as Motional and Aurora Innovation, Inc. have openly expressed that they do not intend to build ride-hailing or carrier platforms themselves, but will instead build the driving technology to power those businesses [60, 61]. Likewise, in an effort to reign in costs, platforms like Uber and Lyft have mostly abandoned their plans to develop/build their own AV fleets, with Uber striving to become “a smart hub for Cruise, Waymo, Tesla and AV players to come” [62].

Operationally, most of our deployment models (except for AV-only platforms) enable hybrid fleets that rely on a combination of human drivers joining as independent contractors (ICs) and AVs [63, 64]. Intuitively, AVs, having lower variable costs, could serve base demand, while ICs, having lower fixed costs, could help cover peak demand. Thus, on a superficial level, the respective use of AVs and ICs to serve base and peak demand resembles classical ideas in operations management like dual-sourcing [65], where a firm sources inventory from two locations, a dedicated one that has long lead-times but is cheaper, and a flexible one that has shorter lead-times but is more expensive. A standard solution in dual sourcing is to use the cheap source for base demand while the flexible source handles random fluctuations. In our setting, the supply of AVs is similarly unresponsive and has a lower marginal operating cost whereas ICs react more quickly but at a larger marginal operating cost; thus, one might expect the same outcome. However, this analogy is imperfect. Using ICs to cover only peak demand is likely to be infeasible as it would require ICs to be left idle for large periods of time. An additional constraint that is not present in dual sourcing is that ICs need to be incentivized to participate, and this requires offering them a sufficient workload. Consider the following stylized example:

Example 1. Suppose a platform pays ICs $15 per request served, and ICs have a reservation earnings level of $15, i.e., they only join the platform if they are guaranteed to serve an order (with a probability of 100%). Suppose further that the platform has access to 20 AVs that operate at a marginal cost of $1 per unit of demand served. Demand is assumed to be equal to 20 or 30, each with probability of 1/2.

The platform would like to serve 20 units (base demand) via AVs and, when demand is high, 10 units via ICs. This however, is not feasible because it would leave ICs with a utilization of 50%. In order to have 10 ICs present in the system, 10 units must also be served via ICs when demand is low to maintain sufficient IC utilization. AVs end up unutilized some of the time despite operating at a very low marginal cost.1 

1 In this example we assume for simplicity that the IC pay is set exogenously. If it were endogenous, the platform could set the IC pay higher, and have ICs operate at lower utilization in this example; however, one can easily compute that the most cost-effective way for the platform to attract 10 ICs to join is by setting

62 The distinction to the dual sourcing setting is due to the ICs’ utilization constraints, i.e., ICs may only be available to serve high demand if they also get to serve some demand when demand is low. We refer to this phenomenon, in which AVs are available and have a lower operating cost but it is nonetheless optimal for the platform to not fully utilize them, as the AV underutilization effect. When supply decisions are made centrally this effect may be a mere curiosity. However, we will show that in the case of open platforms that do not own the AVs, but rather pay an independent outside supplier (e.g., a car rental company, an AV manufacturer, or an investment fund) for AV usage, the AV underutilization can propagate backwards in the supply chain and reduce the supplier’s incentive to invest in AV capacity.

A natural response to AV underutilization is to source AVs using leasing contracts instead of relying on usage payments. In our work, we consider two types of leasing contracts, including a long-term leasing contract, which is signed before any demand information is revealed, and a short-term leasing contract, which is signed after a demand scenario (but not the actual demand) realizes. We find that due to the need to manage stochasticity using ICs within a demand scenario, in either of these models, AV underutilization may still arise. Under leasing contracts, the platform partly shares the burden of AV underutilization, which can improve the supply chain performance relative to an uncontracted open platform model, but does not always do so. The long-term leasing contract, in particular, requires the platform to commit to an AV leasing quantity before any uncertainty is realized; the worst instance we find for this contract is not as bad as the one we identify for the short-term leasing contract. Nevertheless, neither of the leasing contracts is as effective as usage commitments: our study of potential contracting solutions demonstrates that employing simple contractual utilization guarantees through the open platform model leads to better theoretical guarantees and superior numerical performance.

In what follows, we start by modeling the deployment of AVs through an open platform as a supply chain game that involves an open platform, an AV supplier, and ICs. We describe the AV underutilization effect and show that it can have a significant impact on the supply chain profits. We then study the power of usage commitment to resolve this incentive misalignment. Finally, we contrast the performances of the open platform model with alternative operational models.

3.1.1 Contributions

Our work is, to the best of our knowledge, the first study of the strategic interaction between a platform and an AV supplier, and the implications of this interaction on the availability of AVs within platforms. In Section 2.2-3.4, we focus on an open platform operational model by defining a sequential game with the following events: at first the platform commits to how much it will pay the AV supplier for AV usage, then the AV supplier determines the AV capacity it provides, then a demand scenario realizes, followed by a number of ICs deciding whether to work in the realized scenario, and finally the actual demand realizes and the platform decides how to fulfill it given the ICs and the AVs at its disposal. We discuss some of the underlying model assumptions in Section 3.2.2.

their pay to $15 and fully utilizing them rather than increasing their pay and decreasing their utilization. In particular, this means that even with endogenous IC pay, AVs would end up unutilized some of the time.

63 Supply Chain (SC) Inefficiency. In Section 3.3, we investigate the subgame perfect equilibrium of the above-described game. We compare the combined supply chain profit, i.e., that of platform and supplier combined, in equilibrium with that of an integrated supply chain that controls both the capacity decision (how many AVs to order) and the dispatch decision (how much demand to fulfill through AVs and ICs, respectively). We find that the subgame perfect equilibrium can have an arbitrarily large efficiency loss (see Theorem 6), i.e., the Price of Anarchy (PoA) [66] is unbounded. This occurs because the AV underutilization effect may lead the supplier to supply no AVs at all, even when it would be near-optimal to operate with AVs only. Whereas the unbounded PoA arises in a family of pathological instances, we find in our numerical study in Section 3.7 that a significant efficiency loss also occurs in numerical simulations of plausible instances; for these, we rely on 2023 NYC Trip Record data [67] to create scenarios based on real-world demand. We find an average efficiency loss of 5.9% and a maximum loss of 9.9%. This unveils a curious pitfall of the open platform model wherein the platform’s optimal dispatch decision, via AV underutilization, may lead to market failures.

Comparisons of AV Deployment Contracts/Models. The possibility of a significant SC misalignment in the open platform model begs the questions of (1) whether supply chain contracts could help realign the incentives of a supplier and an open platform, and (2) how a contracted/uncontracted open platform model compares with other AV deployment models in terms of SC efficiency. In Section 3.4, we explore a range of different permissible contracts between an open platform and a supplier, including integration (Proposition 4), revenue-sharing (Proposition 5), and usage contracts. Our main focus is on usage contracts, as these are closest to the platforms’ current modus operandi. We find that when the platform can contractually commit to an AV utilization level under each demand realization in each scenario, then the AV underutilization effect cannot propagate backwards, and the supply chain can be as profitable as if it were integrated (Theorem 7). However, when scenarios are not contractible, perfect alignment is in general not possible without some degree of integration (Theorem 8). Nonetheless, we find that, even when scenarios are not contractible and integration is fully avoided, the open platform model can potentially become much more efficient through contracts with well-designed dispatch commitments. As a proof of concept, we show a guarantee of the following flavor for a simple prioritization contract: either the supply chain profit under the contract is at least half of that of an integrated supply chain or the supply chain can achieve half the profit of an integrated supply chain even without a contract (Theorem 9). Despite the inability to fully align the supply chain, this contract demonstrates the value of supply chain contracts when compared to the potentially unbounded efficiency loss in the absence of a contract. In our numerical results based on real demand data, we find significantly improved outcomes with an average loss of 0.4% and a maximum loss of just 1.9%. We further show numerically in Section 3.6, via a spatial closed queueing model, that this kind of dispatch prioritization can be implemented in a way that has a small effect on overall system efficiency.

We then proceed to use our modeling framework to evaluate deployment models beyond the open platform setting. In Section 3.5 we examine an AV-only platform and a platform that sources AVs through short- or long-term leasing contracts, providing bounds on the worst-case performance of each setting. In particular, we show that the worst-case bound

64 for each of these deployment models is worse than that of a well-contracted open platform (Propositions 6-8). This is also reflected in our numerical results with each of these deployment models experiencing a greater average/maximum loss than the prioritization contract. As ride-hailing platforms such as Uber and Lyft are currently working to set up partnerships with AV suppliers, such guidance on how these partnerships can be structured is critically needed, especially as platforms plan to operate with a combination of ICs and AVs for the foreseeable future.

3.1.2 Related Work

Our work lies at the intersection of supply chain contracting and platform operations, especially with a focus on (i) different worker types, (ii) self-scheduling workers, and (iii) the integration of autonomous vehicles. We highlight the most closely related papers in this section.

Supply chain management. Though our work has some similarities with dual sourcing [65], it is quite far from the significant literature on the optimal implementation of dual sourcing inventory systems [68, 69]. Rather, the main focus of our work is on the strategic interaction in a supply chain. In doing so our work centers on the hold-up problem [70], where a party underinvests due to uncertainty regarding future transactions. In particular, our model presents a novel hold-up problem that arises from both demand uncertainty and the platform’s access to a more flexible but utilization-driven supply source (the ICs). This novel effect goes hand-in-hand with a rather surprising optimal strategy: in traditional supply chain models with demand uncertainty the risk of low demand drives the inefficiency, as the supplier’s excess capacity is unused when demand is low [71–74]. In contrast, our model presents a case where high demand generates the risk for AV underutilization. This is due to the dual-sourcing that occurs downstream, wherein the platform may need to allocate higher utilization to ICs during high demand scenarios to keep them engaged, which in turn risks lower usage of AVs. We illustrate this point through a family of instances in which the demand is monotone increasing (in a stochastic dominance sense), but the equilibrium capacity decisions can be inverted, with the higher demand leading to lower capacity.

In addressing AV underutilization, our work connects to classical solutions to the hold-up problem, which rely on full contractibility of future states [75, 76]. While a similar solution applies to our setting when demand scenarios are contractible, we strengthen the robustness of usage contracts by showing that they can vastly improve the efficiency guarantee even when demand is not fully contractible. Our work also relates to double marginalization [77] and the contracting literature that aims to align supply chains in the face of it [78, 79]. Whereas revenue-sharing or buy-back contracts are the go-to solutions to align inventory decisions in that context, the dual-sourcing nature of the problem creates different dynamics. In Theorem 6 we show that the supply chain cannot be aligned when the platform only shares the revenue from AV-fulfilled trips. Rather, the revenue from both AV and IC-fulfilled trips has to be shared with the AV supplier for a revenue-sharing contract to align the supply chain (Proposition 5). Such a contract may intertwine two separate entities (i.e., the ride-hailing platform and the AV supplier) more than these entities may find desirable in light of antitrust and contractor payment regulations [80]. Thus, we study solutions beyond revenue-sharing as potential remedies for AV underutilization.

65 The issue of managing multiple sources of capacity with different degrees of flexibility also appears in other domains, such as in power systems. Renewable energy such as solar and wind power often has low fixed cost but is fairly unpredictable, while other energy sources have higher fixed cost but are more reliable. There is a literature on how to manage such systems [81, 82] and the risk of a capacity “death spiral.” But this connection is fairly loose: in transportation, the cost structure is different, and the less flexible resource (AVs) is the one with a higher fixed cost (yet lower marginal cost). More closely related to our work is the notion of supply retention in repeated split-reward auctions: [83] study the phenomenon that, rather than sourcing from only the cheapest supplier, a seller may buy some of its supply from other suppliers to maintain them as suppliers for the future. This notion has also been corroborated experimentally by [84] and variants thereof were studied by [85]. This line of works shares the interesting feature that a decision maker would take the costlier option to ensure (future) participation, with the notable distinction that in a traditional supply chain underutilized capacity can be managed as inventory, whereas in service systems such as ride-hailing, underutilized capacity is lost due to its time-sensitive nature.

Platform operations. Our work is part of a growing stream of work on platform operations, especially for platforms with self-scheduling capacity [86–88]. Within this stream of work, there are relatively few papers that consider different worker types, usually drawing the distinction between employees and ICs — our work is similar to these, but with AVs instead of employees [89–92]. Usually, these papers assume that the platform can hire some number of employees before the ICs join due to some equilibrium condition (often the same as ours, as motivated by [93] and [94]). The key distinction that arises in our setting is that the AV supply is set by an outside supplier as opposed to the platform itself, i.e., we assume that both types of supply join the platform based on strategic considerations. We also remark that the prioritization scheme we consider is more general than most in the literature, except for

[91], allowing for arbitrary prioritization of either supply type. At a high level, our paper is also connected to a nascent but growing literature exploring the connections between supply chain contracts and platform operations, in particular, in food delivery [95, 96].

Our work also naturally relates to some very recent studies on AV integration within platforms, though none of them consider the interaction between an AV supplier and the platform. [97] study four different possible market designs and investigate the prices that result in each of them for customers; the setting that is closest to our open platform is a common platform with monopoly AV, though they assume equal prioritization of ICs and AVs. [98] similarly investigate how platform profit and IC welfare changes when a platform gains access to AVs, and in particular how that is affected by the AV cost. Along this line,

[99] further examine a fluid model consisting of two locations with asymmetric demands and strategic drivers who can reposition, demonstrating the displacement and incentive effects of automation on driver welfare. In our study of the platform’s dispatch problem, our work relates to [100], in which the platform has access to an AV fleet of known size (exogenous), and needs to decide how many of these to deploy before demand realizes. Before that decision, the platform announces an IC wage (endogenous) and the ICs make a decision whether to join the platform; once demand realizes, it is assumed that the platform’s prioritization is so that AVs are always fully prioritized (see Section 3.3). Roughly speaking, they find that the platform should not deploy too many AVs, as a large AV deployment causes ICs to only

66 join at a high wage, i.e., the platform may price itself out of the market for ICs. In contrast, we consider the IC wage as exogenously given, while allowing for arbitrary prioritization. Crucially, our focus is on the strategic interaction between an AV supplier and the platform, which has not been previously considered.

Finally, we note that our model focuses on the strategic interaction of firms in the supply chain, not on details of operational implementation. Therefore, we do not focus on platform levers such as repositioning [101] and routing [102], which have been studied in the literature, but are abstracted away in our model. In contrast, following the literature that examines dynamic driver wages and rider pricing in ride-hailing platforms [103, 104], we verify the robustness of our results in Appendix B.1.3-B.1.6 by incorporating these additional operational levers.

3.2 The Model

We model the interaction between a platform and an AV supplier as a sequential game. At a high level, in the uncontracted open platform model, the following sequence of events takes place: (1) the platform determines the payment to the AV supplier per unit of demand served; (2) the AV supplier chooses its fleet size; (3) the demand scenario (but not the actual demand) is realized; (4) the platform decides its dispatch prioritization, i.e., how to allocate demand to AVs and ICs; (5) ICs make participation decisions; (6) the demand realizes and AVs/ICs are both dispatched according to the chosen prioritization. Fig. 3.1 below provides an illustration of the sequential game and indicates the key decisions. This timeline is based on the assumption that the AV fleet size is negotiated far in advance of its deployment, and the AV per-use payment is agreed upon upfront to avoid an unrealistic bad equilibrium where the AV fleet size is zero because the platform can choose to pay nothing for its use once it is deployed.

Figure 3.1: Illustration of stages of the sequential game.

Demand. Demand in our model is characterized by two levels of stochasticity. The first level of stochasticity comes from the realization of n potential states of the world, which we call scenarios, each occurring with probability α i , i ∈ { 1, ..., n } . Then, in a second level of stochasticity — in each scenario i — the demand realizes as a non-negative random variable D i with cumulative distribution function F i . The distinction between demand scenario and demand captures the fact that ICs have some information about the demand when they choose whether to participate, but they do not know the precise demand level. In contrast, the platform and the AV supplier know much less about demand when setting the AV fleet size and payment.

67 AV Supply. To secure its AV supply, the platform guarantees upfront the supplier a payment of c AV + c P per unit of demand served. The term c AV represents the AV supplier’s exogenous variable cost incurred whenever AVs serve a unit of demand, while c P represents the AV supplier’s profit per unit of demand served. 2 Since c AV is exogenous, we use c P to represent the platform’s first-period decision of how much to pay its AV supplier per unit of AV use. The AV supplier also faces an upfront fixed cost of c F per unit of AV capacity it provides. This fixed cost is incurred regardless of whether the AVs are eventually used to serve demand. As the supplier makes its AV investment in the second stage after observing c P , we denote the AV capacity by K (c P ). The amount of demand the platform serves through AVs in the third stage is given by the function A i ( · | c P , K (c P ) ) in each scenario i, a choice of notation that highlights the dependence on both c P and K (c P ). That is, the amount of demand the platform fulfills through AVs in scenario i is a random variable A i ( D i | c P , K (c P ) ) . We assume that each unit of supply capacity can serve up to one unit of demand, and therefore we must have A i ( D i | c P , K (c P ) ) ≤ min { D i , K (c P ) } for all c p and i.

IC Supply. We follow the common assumption that ICs self-schedule their work on the platform depending on their expected earnings on the platform and their own reservation earnings level. Denoting by H i ( · | c P , K (c P ) ) the amount of demand the platform serves through ICs in scenario i and by c I the platform pay per demand fulfilled, the ICs’ combined earnings evaluate to H i ( D i | c P , K (c P ) ) · c I . In the main body we focus on a setting where all ICs have a common reservation earnings level t > 0. 3 This reflects a perfectly elastic labor market motivated by the empirical findings of [93] and [94], who show that Uber’s supply pool is highly elastic. In such a setting, denoting by y i ( c P , K (c P ) ) the number of ICs that join in scenario i, the IC supply is based on the following equilibrium condition

ty i ( c P , K (c P ) ) = c I E D i ∼F i ( D i | c P , K (c P ) ) Hi  . [ ]

(3.1)

Similar to AVs, the IC supply bounds the amount of demand served through ICs, i.e., H i ( D i | c P , K (c P ) ) ≤ min , y i ( c P , K (c P ) ) Di  . We then refer to (A (·) , H (·)) as the plat{ } form’s dispatch policy.4 

Revenue. The platform earns a revenue of r per unit of fulfilled demand. In the main body of the paper we assume that c I and r are exogenous parameters with r ≥ c I ≥ t (with c I < t no ICs would ever join) and r is normalized to 1. In particular, in each scenario i, Di  corresponds to the demand when r = 1. 5 Given exogenous r = 1 and c I , we assume without loss of generality that c AV + c F < 1 and c I < 1, i.e., fulfilling demand, whether through AVs or ICs, is profitable. While c AV is generally expected to be lower than c I due to labor cost

2 We assume that c P is set by the platform for simplicity, but the choice of decision-maker for c P —be it the platform, the AV supplier, or a social planner—does not alter the main result of the model (see Theorem 6). 3 In contrast, in Appendix B.1.2 we consider a model wherein the number of ICs that join in scenario i

follows some general increasing function S

E D i ∼F i ( D i | c P , K (c P ) ) . Hi  · cI  ( [ ] )

4 One can view our dispatch policies as a generalization of existing notions in the literature that either consider a platform that does not actively prioritize either supply type [97] or a platform that fully prioritizes the supply type with lower marginal cost [100].

5 We show in Appendix B.1.3-B.1.5 that our main insights continue to hold when platform dynamically controls the supply of ICs and/or the demand for rides, generalized as D i ( D i , r i (D i ) ) , through endogenous decision variables c I i (D i ) and r i (D i ).

68 savings, for the generality of our model we do not impose additional assumptions on the relative costs of AVs and ICs unless explicitly stated otherwise. Finally, we define an instance of our model as a collection of all of the exogenous parameters.

Definition 2. An instance I = , t, c AV , cF  , of our model is specified by the exogenous α ( ) parameters α ⃗ , F, ⃗ c I , t, c AV , and c F . We denote by I the set of all instances.

F, ⃗ cI 

The sequential game. We formalize our model through a three-stage game and assume that all players in this game are rational, i.e., when the platform sets c P , it knows (i) the variable profit of serving demand with AVs and ICs are 1 − c AV − c P and 1 − c I respectively, (ii) the optimal response K(c P ) of the AV supplier in the second stage and (iii) its own resulting optimal dispatch policies A i ( D i | c P , K (c P ) ) and H i ( D i | c P , K (c P ) ) in the third stage. It thus sets c P by optimizing the following:

max ∑ α i E D i ∼F i − c P ) A i ( D i | c P , K (c P ) ) + (1 − c I ) H i ( D i | c P , K (c P ) ) (1 cAV  (3.2) c P [ ] i

In the second stage, given c P , the AV supplier optimizes K knowing that the resulting AV dispatch would be A i ( · | c P , K ) ∀i :

max ∑ α i E D i ∼F i A i ( D i | c P , K ) K cP  cF  K [ ] i

(3.3)

In the final decision stage, for any given c P and K, the platform decides its optimal dispatch policy A i ( D i | c P , K ) and H i ( D i | c P , K ) in each scenario i by solving:

max E D i ∼F i (1 − c AV − c P )A i (D i ) + (1 − c I )H i (D i ) ] y i ,A i ,H i [

(3.4)

s.t. 0 ≤ A i (D i ) ≤ min { D i , K }

0 ≤ H i (D i ) ≤ min { D i , y i }

(3.5) (3.6) (3.7)

A i (D i ) + H i (D i ) ≤ min { D i , K + y i }

(3.8)

ty i = c I E D i ∼F i [ H i (D i ) ]

Here Eq. (3.5), Eq. (3.6) and Eq. (3.7) represent the capacity constraints of available AVs and ICs, and Eq. (3.8) is the equilibrium condition for the participation of ICs. In particular, (3.4)-(3.8) also give rise to y i (c P , K), the optimal number of ICs participating in each scenario i given c P and K.

Equilibrium outcome. The standard solution concept in a dynamic game without private information is the pure-strategies subgame perfect equilibrium (SPE), which is the solution concept we consider. An SPE s requires that the action taken by a player in any stage of the game tree maximizes their forward-looking expected utility. In the context of the sequential game described before, an SPE dictates that the platform determines c P in the first stage knowing the optimal responses K(c P ), A i ( D i | c P , K (c P ) ) and H i ( D i | c P , K (c P ) ) from subsequent stages for any c P ; the AV supplier adopts the optimal response K(c P ) in the second stage, given c P and knowning the subsequent optimal response A i ( D i | c P , K ) and H i ( D i | c P , K ) of the platform for any K; and the platform adopts the optimal response A i ( D i | c P , K (c P ) )

69 and H i ( D i | c P , K (c P ) ) in the third stage given c P and K (c P ). We use the superscript s to denote an SPE outcome and let c P s , K(c P s ), A i s (D i ) := A i ( D i | c P s , K(c P s ) ) , H i s (D i ) :=

( D i | c P s , K(c P s ) ) and y i s := y i ( c P s , K(c P s ) ) ∀i denote the solution to the sequential game. An SPE can thus be solved through backward induction by sequentially optimizing (i) the third stage for any given K and c P , (ii) the second stage for any given c P , and (iii) the first stage. For any I ∈ I and an SPE s, we denote the resulting equilibrium profits of the platform and the AV supplier respectively by

Hi 

V P s (I) := ∑ α i E D i ∼F i [ (1 − c AV − c P s )A i s (D i ) + (1 − c I )H i s (D i ) ] , i V A s (I) := ∑ α i E D i ∼F i [ c P s A i s (D i ) ] − c F K s . i

Then, the aggregate supply chain profit for I in the equilibrium is given by

V s (I) := V P s (I) + V A s (I) = ∑ α i E D i ∼F i [ (1 − c AV )A i s (D i ) + (1 − c I )H i s (D i ) ] − c F K s . i

3.2.1 Other Deployment Models

We benchmark the performance of an SPE, and later of a contracted open platform, against a vertically integrated supply chain in which the platform and the supplier are just one entity. This serves as a natural upper bound for the profit in any deployment model. We then consider three alternatives to the above-described “open platform” model: an AV supplier operating an AV-only platform with no ICs or a platform that sources its AVs from a supplier through either short-term or long-term leasing contracts. We present the integrated benchmark here and defer the presentation of the other models and the corresponding results to Section 3.5. Centralized benchmark. In the centralized benchmark, the platform owns the AVs; thus, it does not need to pay c P to an outside supplier for the use of the AVs but instead incurs the fixed cost of c F per unit of AV capacity. This centralized problem and our model are two modeling variants known in the contracting literature respectively as the first-best and second-best solutions [105]. Mathematically, the goal of the platform is to optimize the AV fleet size K, IC quantity ⃗ y and dispatch policy A and H for an instance I ∈ I.

max α i E D i ∼F i (1 − c AV )A i (D i ) + (1 − c I )H i (D i ) ] − c F K s.t. (3.5) − (3.8) K,⃗y,A,H ∑ [ i

(3.9)

One may solve (3.9) sequentially by (i) optimizing ⃗ y, A, H under every K and then (ii) optimizing K. In particular, (i) can be equivalently solved as the third stage of the sequential game given K and c P = 0, which yields optimal dispatch policies A i ( D i | 0, K ) and H i ( D i | 0, K ) for AVs and ICs, respectively. We denote a centralized solution of instance I ∈ I by (K ⋆ ,⃗y ⋆ , A ⋆ , H ⋆ ) and write

V ⋆ (I) := ∑ α i E D i ∼F i [ (1 − c AV )A i ⋆ (D i ) + (1 − c I )H i ⋆ (D i ) ] − c F K⋆  i

for its supply chain profits. Throughout our work we are interested in the following questions: (1) How does the equilibrium supply chain profit compare to that of an integrated supply

70 chain? (2) If the gap between the two is large, are there practically implementable contracts to limit the efficiency loss? We provide answers to questions (1) and (2) in Sections 3.3 and 3.4, respectively.

3.2.2 Discussion of Model Assumptions

The goal of our model is to capture key features of the interaction between an AV supplier and an open platform. In this section we explain some of the modeling choices we make toward this goal.

Sequence of events. The platform and the AV supplier both face significant demand uncertainty when the former decides on the price to pay for AV usage and the latter makes their investment; this is captured by the uncertainty over different possible demand scenarios at the time of the capacity decision, which we assume occurs many months or perhaps even a year or two in advance of a prioritization decision. We follow the framework of [90] in assuming there is still some residual demand uncertainty when ICs make participation decisions. We assume the dispatch policy is decided before ICs choose to participate to represent in a reduced-form way that participation decisions are daily or weekly decisions, without having to formally model a repeated game. That is, there is no possibility of ICs being there as a sunk-cost decision despite a dispatch policy that is not in their favor (as could happen with AVs), as ICs would quickly leave the platform. The assumption that AVs are exclusively deployed through an open platform can be relaxed to accommodate the existence of outside options (as well as our alternate deployment models). In Appendix B.1.1 we show that, regardless of whether the outside option is offered to the supplier before the demand scenario realizes, in-between it realizing and the demand realizing, or after the demand realizing, the result in Theorem 6 continues to hold.

Demand scenarios. The scenario definitions can be used to capture (i) both observable and unobservable market conditions and (ii) frequencies of these market conditions. Moreover, they allow demand to remain stochastic even within a given scenario. Concretely, one may interpret this as follows: different scenarios encode both major events that affect demand (e.g., construction sites, concerts, weather, or strikes that affect demand) and different time windows (e.g., workday mornings during the summer, weekend evenings during the winter, etc.). Even with full knowledge of these conditions demand remains stochastic. We assume that all market participants (platform, AV supplier, and ICs) have accurate distributional information, i.e., the probability of a given scenario realizing (e.g., the frequency of major events, the fraction of time a given time window represents in a week, or the likelihood of major regulations that affect the market) and the probability that demand of a given magnitude realizes conditioned on the scenario are common knowledge. By weighing each scenario i by α i , we account for both the probability of major events and the frequency of each time window.

As we model the AV investment as a long-term decision, we assume that the investment is made before the realization of the scenario. In other words, the supplier cannot redeploy its AVs based on short-term market conditions (e.g., add vehicles for one evening to serve demand going to a concert, but then not incur the fixed cost for owning them between 3-6AM

71 when they would not be used). 6 ICs, on the other hand, know of the market conditions and can adapt accordingly. Specifically, ICs (i) observe the market conditions (e.g., they know of the concert in advance and can decide to drive during that time, without needing to incur a fixed cost between 3-6AM when they are sound asleep), and (ii) make rational decisions based on the conditions and the platform’s anticipated dispatch prioritization. Finally, we assume that the platform (i) adapts quickly to the market conditions, i.e., it has the ability to prioritize ICs in one scenario, and prioritize AVs in another, and (ii) does so in a way that ICs can anticipate, i.e., the ICs are able (potentially thanks to platform communication) to form rational expectations of the platform’s dispatch prioritization in a given scenario. Of course, with demand remaining stochastic, residual uncertainty remains for the ICs, i.e., though full knowledge of the platform’s dispatch decisions and the distribution of demand allows them to accurately predict their expected utilization, it does not guarantee perfect utilization (e.g., if too many drivers show up to serve demand coming from the concert, a driver may end up idle).

Vehicle Dispatch. Our model assumes that the platform has full operational control over AVs, i.e., it decides which rides AVs serve. This reflects current partnerships between Uber and Waymo [106], but it abstracts away two features of AV dispatch systems in the interest of model tractability: (1) AV launch time and (2) spatial friction.

In practice, there is often a distinction between (a) launching AVs and (b) serving demand through AVs. In a given demand scenario, the platform may first need to decide how many AVs to launch before observing and then fulfilling the realized demand with AVs. Our model simplifies this process by omitting the AV launching stage (this would be an accurate model in reality assuming that either AV depots are sufficiently close to enable near-instant deployment or that the cost of launching excess AVs is negligible so that the platform would launch all AVs in all scenarios, regardless of how they are used to serve demand). However, incorporating first-stage launching costs should not affect the incentive misalignment that we study in this paper, which arises from the second stage.

We also abstract away the spatial friction that exists in many service systems in which AVs would be deployed. Just like the service quality in these systems improves when more supply is available, e.g., because spatial density reduces pick-up times [30, 107–109], prioritizing one type of supply over another would worsen the service quality (as the platform dispatches a further-away vehicle). If the resulting spatial frictions are extremely strong, then any kind of dispatch prioritization is never a good idea and the platform should always dispatch the closest vehicle. In this case, without actively prioritizing either supply type, the platform dispatches proportionally from both ICs and AVs. As a result, the platform’s downstream prioritization decision can no longer propagate upwards in the supply chain and cause the supplier to underinvest in AVs. However, there is evidence that the effect of spatial friction is not that strong: in Section 3.6, we simulate a spatial system and show that supply prioritization is often achievable at a very low cost (0.1% of demand lost). Moreover, such prioritization already occurs in practice [110]. As such, we believe that our results remain insightful even without explicitly incorporating spatial friction; this also follows the approach of related papers [95, 98, 100] that study high-level strategic decisions and ignore similar congestion effects.

6 Though, in Appendix B.1.1, we consider an extension where the supplier can redeploy AVs at a cost.

72 Despite the above reasoning, there is one meaningful aspect of our results that changes in a spatial setting: whereas supply prioritization is very clearly defined in our model, it requires a more detailed specification in a spatial setting. Our simulation in Section 3.6 considers dispatch policies that prioritize AVs if there is an AV within a specified distance of a ride request, whereas otherwise the closest vehicle (AV or IC) is dispatched. When the specified distance is too large this can naturally become costly, e.g., when dispatching an AV from Brooklyn to the Bronx despite an IC being available locally in the Bronx. In that case, larger inefficiencies arise as (i) the rider may cancel leading to the request not being fulfilled or (ii) the AV may waste a lot of time on a very long pick-up. Our results show that this does not arise when the specified distance is reasonably small; as such, one should also interpret our full prioritization in a real system with spatial friction as a local concept, e.g., prioritization within a neighborhood, and not as a global concept.

3.3 The AV Underutilization Effect

At first sight, it might appear that the incentives of the platform and the AV supplier are fairly well-aligned. After all, we already assumed that c P is chosen upfront in order to encourage the AV supplier to build capacity. However, this is not the case, as there exists a more subtle source of inefficiency in this supply chain, which we call the AV underutilization effect. In this section, we explore this effect, its causes, and its consequences.

We first define AV prioritization: for given c P and K, the ratio

E D i ∼F i ( D i | c P , K ) / E D i ∼F i [ min { D i , K } ] Ai  [ ]

measures to what extent AVs are prioritized in scenario i. We say that the platform fully prioritizes AVs in scenario i if A i ( D i | c P , K ) = min { D i , K } , i.e., when AVs fulfill as much demand as possible. The supplier always prefers full AV prioritization, as their revenue is proportional to E D i ∼F i ( D i | c P , K ) Ai  . Intuitively, if AVs have lower marginal cost, i.e., [ ] c AV + c P < c I , one might expect that it is also in the platform’s interest to fully prioritize them. We show below that this is not the case. Indeed, the platform may even want to prioritize ICs fully by setting, for given y i in scenario i, H i ( D i | c P , K ) = min { D i , y i } . We refer to such a deviation from full AV prioritization as AV underutilization.

Definition 3. Given K, c AV , c I and c P , we say that AVs are underutilized in scenario i if c AV + c P < c I but A i ( D i | c P , K ) < min { D i , K } for some realization of D i . Furthermore, the

magnitude of AV underutilization in scenario i is measured by

1 − E D i ∼F i ( D i | c P , K ) [ min { D i , K } ] . Ai  ED i ∼F i  [ ] /

The possibility of AV underutilization raises two questions: (1) if AV capacity investment is set at a fixed K, how severe can AV underutilization be? (2) Given a supplier’s rational expectation of AV underutilization, how should they make their investment decision? In other words, can AV underutilization propagate backward to earlier stages of the game, and discourage the AV supplier from making the socially optimal AV investment, thus resulting in a source of supply chain inefficiency? In the rest of this section we aim to answer these questions.

73 3.3.1 Dispatch Prioritization

In this section we show that the platform may prefer a non-trivial dispatch prioritization with ICs sometimes having higher priority than AVs, and that this can occur both in an SPE and in an integrated supply chain. This is a consequence of the greater flexibility of ICs: while the AV capacity must be secured in advance of when the platform makes dispatch decisions, the number of ICs varies across scenarios based on how much demand they are assigned in expectation in that scenario. Thus, in peak demand scenarios it may even be in the platform’s interest to fully prioritize ICs in order to ensure sufficient IC capacity is available to meet demand. 7 In Proposition 2, we constructively show the occurrence of such a phenomenon through an instance of our model.

Proposition 2. There exists an instance I ∈ I with unique centralized solution (K ⋆ ,⃗y ⋆ , A ⋆ , H ⋆ ) and SPE ( K s ,⃗y s , A s , H s , c P s ) such that c AV < c AV + c P s < c I holds and

(i) y i ⋆ > 0, H i ⋆ (D i ) = min { D i , yi ⋆  tion D i ;

}

and A i ⋆ (D i ) < min { D i , K⋆ 

}

for scenario i and realiza-

(ii) y i s > 0, H i s (D i ) = min { D i , yi s  tion D i .

}

and A i s (D i ) < min { D i , Ks 

}

for scenario i and realiza-

The proposition shows that the AV underutilization effect occurs in both an integrated supply chain (part i) and in equilibrium (part ii). The AV underutilization effect arises from ICs being both more flexible, and constrained by their equilibrium participation condition holding in expectation. It occurs because, even though AVs might be cheaper to operate on the margin, they are less flexible and the need to incentivize ICs to participate can trump the marginal cost differences.8 

For a given value of K, the magnitude of the AV underutilization effect depends on c P : the higher the value of c P , the smaller the upside of using AVs and therefore the more likely the platform will be to prioritize ICs. We formalize this result in Proposition 3 and illustrate it in Fig. B.4 (Appendix B.3.3) through an instance of our model. Proposition 3 also states that, even with c P < c I − c AV , AV underutilization can be arbitrarily bad, i.e., AV prioritization can be arbitrarily close to 0.

Proposition 3. For any I, K, c P and c P ′ where c P < c P ′ , there exist optimal solutions to (3.4) with (3.10) (3.11) Moreover, for any ϵ > 0, there exist I ∈ I, c P and K where c AV + c P < c I and

E D i ∼F i [ A i (D i | c P , K) ] ≥ E D i ∼F i [ A i (D i | c P ′ , K) ] , ∀i,

E D i ∼F i [ H i (D i | c P , K) ] ≤ E D i ∼F i [ H i (D i | c P ′ , K) ] , ∀i.

∑ i α i E D i ∼F i [ A i (D i | c P , K) ] < ϵ. ∑ i α i E D i ∼F i [ min { D i , K } ] As discussed in Section 3.2.1, in an integrated supply chain the platform pays only cAV  per unit of AV usage which effectively sets c P = 0; in contrast, in a disintegrated supply chain the AV supplier needs c P > 0 for its AV investment to break even. It follows from Proposition 3 that, with a positive in a disintegrated supply chain, an AV supplier that supplies K ⋆ units of AVs would experience a stronger AV underutilization effect than an integrated supply chain would.

3.3.2 The Profit Ratio

A key question in our paper is whether the AV underutilization effect is a source of economic inefficiency and, if yes, how big a source it is. If the extent of AV underutilization is the same under first-best (an integrated supply chain) and second-best (a decentralized supply chain), perhaps we do not need to worry about its occurrence since, in this case, the AV utilization would be set at a level chosen by a social planner. Proposition 3 suggests that this is not the case: the AV underutilization effect is stronger under a decentralized supply chain than under an integrated one. This implies that the AV underutilization effect is likely a source of supply chain inefficiency. In this section, we explore the degree of inefficiency introduced by the AV underutilization effect in a decentralized supply chain. One of our key results is to prove that this inefficiency, as measured by the profit ratio we are defining next, can be arbitrarily large.

Definition 4. For any I ∈ I and SPE s, we define its profit ratio by PR s (I)

:= V ⋆ (I) /V s (I). We know that PR s (I) ≥ 1, ∀I ∈ I as a centralized solution always leads to higher supply chain profits than any SPE. When PR s (I) = 1, we say that the supply chain is aligned for I. This opens the question of how large the profit ratio can be. We show below that there is no constant bound on the profit ratio. Our result is actually a stronger one, demonstrating that the profit ratio can be arbitrarily large for any given c P in the first stage (not just the cP  from an SPE). For this purpose, we enhance the definition of profit ratio in Definition 5 to take into account an arbitrary c P ≥ 0. That is, we remove the first stage of the sequential game and only solve the second and third stages of the game with a given c P . We denote the corresponding supply chain profit by V s ( I | c P ) , which we then use to compare with V ⋆ (I).

Definition 5. For any I ∈ I, cP 

V ⋆ (I) . V s ( I | c P )

≥

0 we define the profit ratio given c P as PR s (I | c P )

:=

Equipped with this new definition, we are ready to show in Theorem 6 that there are instances with arbitrarily large profit ratio regardless of the choice of c P ≥ 0.

≥ 0, PR s (I | c P ) ≥ M. Intuitively, we construct a sequence of instances where, for any c P , the AV underutilization effect is so strong that the AV supplier responds by not investing in capacity at all. The platform then uses only ICs, whose variable cost is set so close to the revenue that the platform’s profit margin vanishes. In these instances, the profit ratio of an SPE increases when: (i) c I − c AV is large, and (ii) the profit margin is thin. This observation aligns with our numerical findings in Section 3.7, where we show that the performance of an SPE deteriorates when either (i) is true (see Fig. B.1) or when (ii) is true (Fig. B.2), and particularly when

Theorem 6. ∀M ∈ R : ∃I ∈ I such that for any SPE s and any cP 

75 both (i) and (ii) are true (Fig. B.5). We remark that inefficient SPEs can also occur when suppliers have outside options for their AVs (Appendix B.1.1) or the platform sets c I and/or r endogenously (Appendix B.1.3-B.1.5).

Moreover, while such efficiency loss is also partially driven by double marginalization — a supply chain distortion that results from successive markups by independent firms at different vertical levels of the supply chain [77] — we note that the key factor leading to the unbounded profit ratio is the AV underutilization effect. The difference between the AV underutilization effect and the double marginalization phenomenon is exhibited by Theorem 6: even if c P is chosen by a social planner (and thus there is no efficiency loss from pricing), the profit ratio can still be arbitrarily large. Finally, we observe an interesting contrast to many traditional supply chain models where inefficiency is driven by the risk of low demand. Due to the nature of the dual-sourcing that occurs downstream (wherein the platform may utilize ICs highly in a high demand scenario to keep them engaged), it may actually be high demand scenarios that generate the risk of low AV utilization. We illustrate this point through families of instances in Appendix B.3.2 where the equilibrium capacity decision decreases while expected demand monotonically increases.

In addition to our theoretical results showing potentially unbounded inefficiency for an equilibrium outcome, we examine in Section 3.7 the inefficiency of the AV underutilization effect under plausible parameter choices. Our instances show that misalignment of equilibrium outcomes are commonly observed among a wide range of instances.

3.4 Supply Chain Coordination Contracts

We have argued so far that the AV underutilization effect creates an incentive misalignment that can lead to an underprovision of AV capacity. A natural follow-up question is whether the use of supply chain contracts might be able to ameliorate or resolve this supply chain misalignment. The model considered so far can be viewed as a simple contract model where the platform promises a profit per use c P , and our previous section proves that this kind of contract is not powerful enough to resolve the misalignment. Indeed, it follows from the proof of Theorem 6 that a contract that stipulates the AV fleet size K as well as c P does not suffice to guarantee that the supply chain achieves a constant fraction of the first-best objective. Thus, in this section, we examine the power of alternative contracts in aligning the supply chain.

To allow for contracts in our formulation, we expand the game to add a stage-zero contracting phase. At stage 0, some contract π is offered to both the platform and the AV supplier. We do not focus on who chooses the contract under consideration, which could be chosen by one of the two parties or by a third-party moderator. Both parties have the option to accept or reject the contract. If both accept the contract, they play a subgame perfect equilibrium according to the contract rules. If either party rejects the contract, they play an SPE as defined in Section 3.2. 9 Therefore, a contract π is accepted if V P π (I) ≥ V P s (I)

9 This assumption means that, without an agreement on π, the supplier can still deploy its vehicles on an open platform. This mirrors the renegotiation option in the dynamic contracting literature [111] and contrasts with the stronger assumption from static settings, wherein all players leave with zero payoff when the contract is rejected. Assuming a zero outside option for the AV supplier would increases the platform’s

76 and V A π (I) ≥ V A s (I), where V P π (I) and V A π (I) denote the profits of the platform and the AV supplier under the contract. Moreover, we denote the supply chain profit for I given π by V π (I), so we have V π (I) = V P π (I) + V A π (I) when the contract is accepted. For a given contract π, we next describe how we measure the supply chain’s profit ratio.

Definition 6. The profit ratio for I given π is measured by PR π (I) := V ⋆ (I)/V π (I). In particular, we say that π aligns the supply chain for I if the contract is accepted and

PR π (I) = 1.

Integration-style contracts. We first note that one can always integrate the supply chain through a contract with a sufficiently large side payment c S . The side payment, independent of the later AV usage, allows the platform to incentivize the AV supplier to invest in AV capacity. In Proposition 4 below we define such an integration contract; this reflects standard results in the supply chain literature.

Proposition 4. For any I ∈ I with a centralized solution (K ⋆ ,⃗y ⋆ , A ⋆ , H ⋆ ), an integration contract π ⋆ (I) requires that (i) the platform pays the AV supplier a side payment of c S π = c F K ⋆ + V A s (I) and no usage payment of AVs, i.e., c P π = 0, and (ii) the supplier invests in K π = K ⋆ units of AVs. Then, π ⋆ (I) aligns the supply chain.

Since the side payment c S π required by an integration contract can be prohibitively large for asset-light platforms such as Uber and Lyft, a natural question is whether traditional revenue-sharing contracts, like integration contracts, can also align the platform’s and the supplier’s incentives and thus maximize the supply chain profit. Indeed, the parameter c P suggests that the platform and the supplier, even in the absence of a contract, already implement revenue-sharing for the demand served through AVs. However, as suggested by Theorem 6, such a scheme is not sufficient to align the supply chain. We thus consider a broader set of revenue-sharing contracts in Proposition 5. These pay the supplier both for demand served through ICs and for demand served through AVs, thus making the supplier indifferent to the platform’s dispatch policy and thereby aligning the supply chain. One can view this set of contracts as a natural extension of classical revenue-sharing contracts to a dual-sourcing setting.

Proposition 5. Denote by Π S the set of revenue-sharing contracts π which specify that (i) the platform must pay the AV supplier c P π for each unit of demand served by AVs and c R π for each unit of demand served by ICs, and (ii) the supplier must invest in K π units of AVs. Then, for every instance I ∈ I, there exists some contract π ∈ Π S that aligns the supply chain.

Usage contracts. In practice, in light of regulatory and antitrust concerns, a platform and a supplier may want to avoid intertwining their operation to the extent that revenue-sharing would require. Therefore, in the remainder of this section, we focus on the power of usage contracts to align the supply chain.

Definition 7. The set Π U contains all contracts π that specify:

bargaining power.

77 (i) The platform pays the AV supplier c P π for each unit of demand served by AVs;

(ii) The AV supplier provides K π units of AV capacity;

(iii) In each scenario i, the platform serves at least A i π (D i ) units of demand through AVs, where A i π (·) is a function that maps D i to a lower bound on AV-served demand.

Usage contracts address the practical limitations of integration and revenue-sharing contracts by excluding integration-style payments to the supplier that are not based on demand fulfillment (e.g., side payments or payments to the AV supplier for demand fulfilled by ICs); instead, they avoid excessive AV underutilization by imposing lower bounds on the AV dispatch. We first consider a general class of usage contracts that allow the utilization of the AVs to be contractible in each scenario, i.e., the mappings A i π (·) can be different across scenarios. In this case, we can guarantee that there exists a usage contract that aligns the supply chain. This solution echoes classical approaches to tackle hold-up problems, but requires (i) the ability to accurately predict the probability of each possible state of nature and (ii) the ability to contract based on the realized state of nature [75, 76]. As we discussed in Section 3.2.2, the realization of scenarios may not be contractible in practice; thus, we later consider a subset of Π U that restricts the mappings A i π to be equal across scenarios. Under this restriction, we show that even when allowing a side payment, this class of restricted usage contracts cannot guarantee to align the supply chain whenever it involves a positive usage payment. Nonetheless, even with this restriction, usage contracts remain valuable: we prove that, by committing the platform to fully prioritize AVs, usage contracts can guarantee to achieve half of the first-best supply chain profit, whenever an SPE fails to do so. Though this does not guarantee alignment, it demonstrates the value of utilization commitments in the AV supply chain.

Contractible Scenarios. Our next result shows that the contracts in Π U can align the supply chain.

Theorem 7. For every instance I ∈ I, there exists some π ∈ Π U that aligns the supply chain.

For an outcome to obtain the first-best objective, it must be the case that the AV fleet size K, the number of ICs ⃗y , and their respective utilization in each scenario are all equal to their respective values in a first-best solution. The contract constructed in the proof of Theorem 7 specifies K and the utilization for each realized demand accordingly, and thus allows the platform to attract ⃗ y ⋆ ICs to complement the AVs. This almost fully specifies an outcome with a supply chain profit that is greater than under the second-best; what remains open is how that larger profit is apportioned between the supplier and the platform. Given these fixed values, c P fully determines the share of the profit the supplier and the platform each receive; by setting it appropriately one can guarantee that both the platform and the supplier agree to the contract. In Appendix B.2 we show (Corollary 1) that the same outcome can be achieved when the platform’s dispatch commitment to the supplier is based on the IC dispatch, instead of on the realized demand, as long as it may be scenario-dependent; this may be of interest when demand served by ICs is more easily observed than total latent demand.10 

10 This only requires public ridership data which many cities provide (e.g., NYC at https://data.

78 Due to the additional notations needed to define such dispatch policies and contracts, we defer the formalization of this result to Appendix B.2.

Not contractible scenarios. Though the contracts covered by Theorem 7 align with classical solutions to the hold-up problem in the supply chain literature, they may not be a practical solution to AV underutilization. Given the high dimensionality of a ridehailing marketplace, the realization of a scenario may be an unobservable, or at least unverifiable, event (see Section 3.2.2). We now study the efficacy of usage contracts in a more challenging setting where we assume that scenarios are not contractible. In that case we are restricted to use contracts π with A i π (d) = A j π (d) for all d that are in the domain of i and j and ∀i, j (for simplification, we often denote this restriction by A i π = A j π ∀i, j).

We first state an impossibility result implying that even for arbitrarily small c P π > 0 in a contract π ∈ Π U with A i π = A j π ∀i, j, the platform may still underutilize AVs and thereby misalign the supply chain. In fact, we establish an even stronger result: supply chain alignment is not possible even with a contract π that provides side payment c S π , as long as the usage payment c P π is strictly positive.

Theorem 8. Let Π D denote the set of contracts π that require (i) the platform pays the AV supplier a side payment of c S π and c P π per demand unit served by AVs, (ii) the AV supplier provides K π units of AVs, and (iii) the platform serves at least A π units of demand through AVs, where A i π = A j π ∀i, j. Then, for any ϵ > 0, there exist c P ∈ (0, ϵ) and I ∈ I with cAV  and c I such that we have (i) c AV +c P < c I and (ii) PR π (I) > 1 for any π ∈ Π D with c P π ≥ c P .

Intuitively, Theorem 8 shows that no matter how small a value of c P is chosen, and despite AVs having lower variable cost (i.e., c AV + c P < c I ), it may still be in the interest of the platform to underutilize AVs in order to incentivize the ICs to participate in the high demand scenarios. Thus, the only contracting solution that guarantees supply chain alignment in this setting is to set c P = 0 and incentivize the supplier solely through side payments, i.e., full integration. The proof of the theorem is based on constructing an instance where the AV platform cannot tell whether AVs are being underutilized on purpose or because the scenario is one where less capacity is needed. The inability to contract on scenarios therefore causes a misalignment.

Nonetheless, contracting on commitment to AVs can have significant value: there exists a simple class of contracts that requires neither contracting on scenarios nor side payments and that guarantees that the supply chain obtains at least half of the profit of a first-best solution when an SPE fails to provide the same guarantee. Intuitively, full prioritization contracts allow the platform to commit to fully prioritize AVs, which prevents the AV underutilization effect, and thus ensures the AV supplier’s incentive to invest. Since AVs are fully prioritized regardless of the demand scenario, full prioritization contracts are a subset of contracts in Π U that satisfy A i π = A j π ∀i, j. In particular, they do not require side payments. We next establish that the better of “always prioritizing AVs” and an SPE (without resorting to contracts) leads to a profit ratio of 2.

cityofnewyork.us/Transportation/uber-Data/gre9-vvjv and Chicago at https://data.cityofchicago.org/ Transportation/Transportation-Network-Providers-Trips/m6dm-c72p)

79 Theorem 9. We denote by Π F ⊂ Π U the set of full prioritization contracts π that, given I ∈ I, requires that A i π (D i ) = min { D i , K π } , ∀i. Then, for any I ∈ I, at least one of the following two statements is true:

(i) The profit ratio of an SPE s satisfies PR s (I) ≤ 2;

(ii) Both the platform and the supplier agree to a π ∈ Π F that guarantees a profit ratio

PR π (I) ≤ 2.11 

The proof of this result is based on constructing two solutions, one that relies only on ICs and one that relies only on AVs, and showing that one of them must earn at least half the profit from an integrated supply chain. Since the solution that relies only on ICs can be enforced by the platform without resorting to the AV supplier, we know that any no-contract equilibrium s must do at least as well as the IC-only solution. Then, we argue that when the IC-only solution is bad (i.e., when it obtains less than a half of the integrated supply chain profit), we can find a contract from Π F that ensures both the platform and the supplier have incentives to adopt the AV-only solution, which then yields at least a half of the integrated supply chain profit. In Appendix B.4.2 we show that the factor of 2 in our guarantee is almost tight for this class of contracts.

The IC-only and AV-only solutions in our proof provide, respectively, lower bounds on V s (I) and max π∈Π F V π (I) for any instance I; however, in general, outcomes in SPEs and under a full prioritization contract almost always involve both ICs and AVs. Indeed, our numerical findings in Section 3.7 reveal that hybrid fleet solutions are common among our numerical instances: hybrid usage of both ICs and AVs occurs in 94.7% of our instances with full prioritization contracts, in 97.3% with centralized solutions, and in the SPE of every single instance — for the centralized and the full prioritization solutions, the remaining instances involve only AVs. This aligns with a structural result we derive on the relative use of ICs in the full prioritization, the centralized, and the SPE solution: for a given K, among those three, the use of ICs is lowest under full prioritization and highest in the SPE (Appendix B.3.6). In Appendix B.3.7, we additionally investigate the conditions under which IC-only and AV-only solutions respectively perform well or poorly. Finally, Theorem 9 suggests that either an SPE or a full prioritization contract can yield a greater supply chain profit; this is indeed the case as we discuss in Appendix B.3.8. There, we show that the SPE may yield larger supply chain profit in settings where c F is small but c AV is large; those would correspond to “low-quality” robotaxi markets, in which AVs are cheap to produce, but expensive to operate (e.g., due to frequent failures that require human intervention). In contrast, when AVs are expensive to produce but cheap to operate, full prioritization contracts tend to yield the better outcome. This regime is the focus of our numerical results (Section 3.7) which thus, consistently, display that full prioritization contracts yield the most robust performances out of all models/contracts considered. Nonetheless, Theorem 9 highlights the importance of usage commitments when demand scenarios are not contractible. Even a simple prioritization contract can substantially enhance the supply chain’s profit ratio guarantee by providing the platform and the supplier with the option to commit to full AV prioritization.

11 As in the case of Theorem 7, the reliance of Theorem 9 on the contractibility of the realized demand can be replaced with the contractibility of the dispatch of ICs (see Appendix B.2).

80 3.5 Alternative Deployment Models

In this section we consider the performance of three alternative deployment models: the AV-only model, the short-term leasing model and the long-term leasing model. Specifically, we identify lower bounds on the worst-case profit ratios in these models to compare them with those for an open platform model.

3.5.1 AV-only Model

We start with a model of an AV supplier that builds a ride-hailing platform using only AVs, which is akin to the current deployment of Waymo’s fleet in San Francisco [112]. Such a platform solves (3.9) subject to ⃗ y = 0, i.e.,

V AV (I) := max ∑ α i E D i ∼F i [ (1 − c AV )A i (D i ) ] − c F K s.t. K,A i

(3.12)

0 ≤ A i (D i ) ≤ min { D i , K } , ∀i.

⋆

We define the profit ratio for I in an AV-only platform as PR AV (I) := V VAV (I) (I) . Since AVs are the only source of supply, the AV-only platform avoids the risk of AV underutilization. However, the inability to dynamically adjust its fleet size in different demand scenarios can lead to significant inefficiency relative to an integrated platform. In particular, we prove that the profit of an AV-only platform can be arbitrarily worse than V ⋆ (I).12 

Proposition 6 (Inefficiency of AV-only). For any M > 0, there exists I with PR AV (I) ≥ M.

Despite recent commercial deployments, a comparison of this result to Theorem 9 suggests that an AV-only platform yields a less robust operational model to handle demand variability.

3.5.2 Leasing Models

In this section, we study two models in which a platform secures its AV supply through leasing contracts as opposed to making per-trip payments. We distinguish between short-and long-term leases: for short-term leases, the platform decides the AV leasing quantity after a demand scenario realizes, and the leasing quantity can thus be scenario-dependent; for long-term leases, the platform commits to an AV leasing quantity before any demand information is revealed. We find that AV underutilization may still arise in both of these models. 13 However, by requiring the platform to commit to fixed leasing quantities over a longer period, the leasing contracts force the platform to partly share the burden of AV underutilization, which alleviates the risk for the AV supplier. In this section, we show that both short- and long-term leasing contracts can be more efficient than an open platform SPE, but are not always so; however, the leasing contracts can have profit ratios greater than 2, which is the upper bound on the profit ratio in a well-contracted open platform.

12 A similar inefficiency was noted in [90], in a paper that compares employees and contractors, with the employee-only model having the same kind of rigidity as the AV-only model here.

13 Recall that, due to the need to manage stochasticity using ICs within a demand scenario, AV underutilization may even arise in an integrated supply chain.

81 Short-term Leasing

In our short-term leasing model, the AV supplier determines the fleet size K, and the platform leases κ i ≤ K AVs in scenario i and pays c P per AV leased. Thereafter, it only incurs the usage cost c AV for serving demand through AVs and no additional payment to the supplier. The model evolves as follows:

(1) A social planner sets c P to maximize supply chain profit, i.e., the platform’s profit from fulfilling demand minus the fixed cost of AVs. The social planner knows that for given c P the supplier responds with capacity investment K (c P ) and the platform responds with leasing quantity κ i (c P , K (c P )), dispatch policy A i ( D i | c P , K (c P ) ) and H i ( D i | c P , K (c P ) ) and solves:

max ∑ α i E D i ∼F i ) A i ( D i | c P , K (c P ) ) + (1 − c I ) H i ( D i | c P , K (c P ) ) F K (c P ) (1 cAV  −c c P [ ] i

(2) Anticipating the AV leasing quantities κ i (c P , K), ∀i, the supplier solves:

max ∑ α i E D i ∼F i [ c P κ i (c P , K) ] − c F K; K i

(3) Given c P and K, the platform sets ⃗ κ ,⃗y, A and H as follows:

max α i E D i ∼F i (1 − c AV )A i (D i ) + (1 − c I )H i (D i ) − c P κi  ⃗ κ ,⃗y,A,H ∑ [ ] i

s.t. (3.6), (3.8), 0 ≤ A i (D i ) ≤ min { D i , κ i } , A i (D i ) + H i (D i ) ≤ min { D i , κ i + y i } , κ i ≤ K, ∀i.

We denote the supply chain profit and profit ⋆ ratio of an SPE in an instance I of the above sequential game by V SL (I) and PR SL (I) := V VSL (I) (I) . The following bound is our main result on short-term leasing.

Proposition 7 (Inefficiency of Short-term Leasing). There exists I with PR SL (I) ≥ 100.

We prove this proposition in a similar way to Theorem 6: in one scenario demand can be high, and thus the platform wants to prioritize ICs to ensure their participation; in the other scenario, it would be beneficial for the supply chain if the platform was able to lease AVs. However, the supplier’s expected revenue from these intermittent leasing quantities does not justify an investment in AVs. The supply chain efficiency thus suffers from the resulting AV under-investment, with the bound of 100 being much worse than the guarantee for a well-contracted open platform.

Long-term Leasing

In the long-term leasing model the quantity of AVs leased by the platform is scenarioindependent. In this model the payment c P is made for each unit AV that the platform leases from the supplier before a scenario realizes, regardless of the actual AV usage. For given c P , it is trivially optimal for the supplier to invest in whatever AV quantity the platform

82 decides to lease, i.e., K is effectively chosen by the platform. Here, we assume that (1) the AV supplier sets c P = arg max(c P − c F )K(c P ) where K(c P ) denotes the resulting AV leasing quantity and (2) given c P , the platform sets K, ⃗ y, A and H so as to

max

K,⃗y,A,H

∑

i

α i ED i ∼F i 

[ (1 − cAV 

)A i (D i ) + (1 − c I )H i (D i ) ] − c P K

subject to

(3.5) − (3.8).

We denote the supply chain profit and profit ratio of an SPE in an instance I of the above ⋆ sequential game V LL (I) and PR LL (I) := V VLL (I) (I) . We show the following bound for the profit ratio.

Proposition 8 (Inefficiency of Long-term Leasing). There exists I with PR LL (I) ≥ 2.8.

The long-term leasing model requires the platform to commit to a fixed leasing quantity before any demand uncertainty realizes. Post-commitment, the AV supplier is indifferent to the usage of the leased vehicles, and therefore AV underutilization no longer reduces the supplier’s incentive to invest. However, with long-term leasing the supply chain suffers significantly under double marginalization — the AV supplier adds a profit-maximizing markup to the fixed cost c F , which drives the AV leasing quantity below the socially optimal level. Proposition 8 shows that due to the under-investment from double marginalization, a long-term leasing contract is no more efficient than a well-contracted open platform. Though our worst-case lower bound for the long-term leasing model is much smaller than that for short-term leasing, our numerical results suggest that the long-term leasing contract is usually more inefficient under plausible problem instances.

3.6 Prioritization Schemes in Spatial Matching Systems

In practice, spatial friction reduces the service efficiency of a platform that prioritizes one type of supply. As discussed in Section 3.2.2, prioritizing one type of supply over another leads to longer pick-up times (on average) and a fraction of ride requests may be lost as a result – both because customers cancel to avoid a long wait and because fulfilling a ride takes longer as pick-up times increase. Though our model disregards this type of spatial friction to ensure tractability, we now design a numerical framework to study its significance. In short, our results show that a dispatch scheme that prioritizes AVs within a distance threshold ¯d, chosen based on supply and demand density, allows for a significantly increased AV (or IC) utilization while only losing a small fraction of demand. In contrast, a full prioritization scheme, that dispatches to an AV whenever one is available (no matter the distance), may significantly decrease demand fulfillment and even decrease AV utilization.

Simulation model and parameters. We simulate a closed system with a fixed pool of vehicles and potential incoming ride requests. To model the density of demand, we bootstrap the 2023 NYC High Volume For-Hire Vehicle (HVFHV) trip record data [113] during weekday rush hours (7 AM - 10 AM and 5 PM - 8 PM on Monday to Friday), finding a per-minute average of around 180 rides in the 22.82 square mile Manhattan area. We simulate such spatial density by sampling potential riders uniformly at random in a 5 × 5 miles area with an inter-arrival time that follows an exponential distribution with rate parameter λ = 1/200 (minutes/request). Additionally, we find an empirical average pickup time of 4.5 minutes and

83 a trip duration of 16.3 minutes. Assuming vehicles are idle (neither traveling with riders nor picking up riders) for t I = 20 − 40% of the time, we estimate that such a closed system contains approximately (4.5 + 16.3)/(1 − t I )/λ ≈ 5000 − 7000 vehicles, composed of K AVs and y ICs. The platform assigns each incoming rider instantaneously to an idle vehicle in the system; to model potential loss in demand due to spatial friction, we assume that the conversion rate for an assignment linearly decreases from 1 to 0 for pickup times between 5 and 15 minutes. 14 With a travel speed of 0.125 miles per minute (i.e., 7.5 miles per hour) [114], this conversion rate as a function of the distance d (in miles) from the assigned vehicle to the rider becomes 1 − min { 1, (d − 0.125 · 5) + /(0.125 · 10) } . The ride request is lost if it is not converted successfully. When an assignment does convert, the pickup time is d/0.125, the trip duration follows an exponential distribution with parameter µ = 16.3, and the assigned vehicle becomes idle again, after completing the trip, at a randomly sampled location. Prioritization schemes. We consider a simple class of dispatch and prioritization policies parameterized by a threshold ¯d: each request is matched to the closest vehicle, except for when there is an AV within distance ¯d of the request, in which case the request is matched to the closest AV even when some IC would be closer. When ¯d = 0 we recover a no prioritization policy where the rider is always assigned to the nearest idle vehicle (regardless of the vehicle type). When ¯d = 10, the platform always prioritizes AVs over ICs, i.e., whenever at least one AV is idle, the platform dispatches to that AV rather than to an IC. We experiment with different values of the prioritization radius, varying ¯d ∈ { 0, 0.05, 0.1, 0.15, 0.2, 0.4, 0.8, 0.9, 1, 10 } , to visualize the tradeoffs between AV utilization and demand fulfillment.

Findings. We measure, for each threshold, the fraction of demand that is successfully fulfilled (y-axis) and the fraction of time that AVs travel with riders (x-axis) 15 over a 500 minute horizon. Fig. 3.2(a)-(c) illustrate the average performance of the policies in a simulated system with 5000 vehicles. We observe that the no prioritization policy (i.e., the policy with ¯d = 0) leads to the highest demand fulfillment rate out of all policies but suffers from the worst AV utilization. The other extreme involves policies with ¯d ≥ 0.8 which heavily prioritize AVs but suffer from a very low fulfillment rate. This is because these policies send AVs on long dispatches with low conversion rates. Moreover, even the AV utilization of these policies is lower than that of policies with smaller ¯d values because AVs spend more time picking up passengers rather than driving them to destinations. This holds particularly true when the number of AVs, K, is small. In contrast, policies with moderate ¯d can achieve both a high AV utilization and small losses in demand fulfillment; e.g., with ¯d = 0.4 we achieve the highest AV utilization with no more than 0.1% in demand fulfillment lost. As we increase the number of vehicles in the system from 5000 to 7000 in Fig. 3.2(d)-(f), we find that all policies experience lower AV utilization because more vehicles are idle. This reflects the situation in our analytical model where K > D i and even with full prioritization some AVs are idle. However, it is still the case that setting ¯d around 0.4 yields a high AV utilization at a negligible loss in demand. Finally, we highlight that intermediate utilization levels can also be attained through smaller values of ¯d; e.g., if one wants AVs to be only 75% utilized to

14 A similar conversion model has been applied by [91] in a related setting.

15 We measure AV utilization in this way to capture the status quo in which vehicles do not generate revenues when they are idle or on their way to passengers. It is noteworthy that in the spatial setting, a tradeoff between idle capacity and pickups implies that supply can never be 100% utilized [109, 115, 116].

84 ensure IC participation, then one could set ¯d = .1 in Fig. 3.2(b).

Figure 3.2: Each plot is based on a different combination (K, y), and illustrates the tradeoffs between AV utilization and demand fulfillment under different dispatch prioritization policies parameterized by ¯d.

Overall, our results in this section suggest that even simple prioritization schemes, parameterized by just a single well-tuned parameter, can meet prioritization goals at a very small cost in demand fulfillment. This may seem counter-intuitive at first sight, but it should not be too surprising: the regime in which AVs would have low utilization in the absence of prioritization is exactly the supply-rich regime wherein the cost of prioritizing is small. In contrast, when supply is scarce, the cost of prioritizing increases. However, when that is the case, significant prioritization is not required for AVs to be highly utilized.

3.7 Numerical Results

In this section, we complement our theoretical bounds through a numerical investigation of the AV underutilization effect and the supply chain inefficiencies caused by it. Specifically, we examine (i) PR AV (I) (ii) PR LL (I), (iii) PR SL (I), (iv) PR s (I) as well as (v) the profit ratio of a full prioritization contract π ∈ Π F in the open platform model, with K π = K ⋆ , A i π (D i ) = min { D i , K π } ∀i and

V A s (I) + c F K⋆  c P π = ∑ i α i E D i ∼F i [ min { D i , K ⋆ } ]

(set as in the proof of Theorem 9).

For the full prioritization contract, we use ⃗ y π and PR f (I) := V ⋆ (I)/ ( V P π (I) + V A π (I) ) to respectively denote the number of ICs and the profit ratio assuming that the contract π is accepted. Observe that we know from V A π (I) = V A s (I) that π is always accepted by the supplier, and it is accepted by the platform if and only if V P π (I) ≥ V P s (I), i.e., when

PR f (I) ≤ PR s (I).

85 We structure this section as follows. We first leverage empirical data to derive demand distributions and plausible cost parameters across which we evaluate each profit ratio. Next, we aggregate the results to illustrate the inefficiency faced by each of operational mode in Fig. 3.3. Finally, we explore in a more granular way how the inefficiency of each deployment mode depends on particular parameters in Figs. 3.4–B.2.

Parameters. Our results are based on the trip record data provided by the NYC Taxi and Limousine Commission [113]. We leverage the data for the Manhattan area in 2023, which contains more than 60 million trip records, to construct 12 demand scenarios. These are based on the historical hourly demand during particular intervals, e.g., the weekday morning rush hours, the weekend evening hours, etc. In our numerical results we assign each scenario a probability that corresponds to the fraction of hours in a week that the scenario represents, e.g., the weekend afternoon scenario (Saturday/Sunday from 2PM-5PM) occurs with probability 6/168 = 1/28. Within each scenario, the demand is drawn from the empirical hourly demand distribution that occurred during the corresponding hours in the data. We refer the reader to Appendix B.3.4 for more details.

We now provide some back-of-the-envelope motivation for the range of parameters we consider. For ICs, we rely on current platforms’ business practices. Uber and Lyft charge commissions that are typically in the 20 − 25% range but can go up to 40% [117]; on the other extreme, Juno, aimed to charge only 10% [118]. Given that the revenue r is normalized to 1, this motivates 0.6 to 0.9 as a natural range for c I ; for t, we follow empirically observed utilization values of around 60% [117] and set t = 0.60 · c I . Though the AV technology is still in development, with cost parameters changing as the business scales, AVs are generally expected to have higher fixed cost and lower marginal cost than ICs (indeed, given the reduced need of labor and the additional equipment necessary, one could view this as a defining distinction). In particular, current sources suggest that an AV operated by Cruise costs $150,000 to $200,000 [53], which is much higher than the approximate cost of $25,000 of an economy car operated through Uber’s platform [119]. To calculate c F , we consider $200, 000 as the cost of an AV, and assume a cost of capital of 10%; this gives an annual fixed cost of $20, 000 which translates into a per-minute fixed cost of ≈ $.04; with an average revenue of $0.4 per minute of demand being served, we can then approximate the normalized fixed cost as 0.1. In contrast, the marginal cost of AVs is expected to be lower than that of a conventional vehicle due to the savings in labor costs. To estimate a reasonable cost for c AV , we need to include the costs of fuel, wear and tear, insurance, and cleaning, i.e., all of the costs ICs currently face except for driver costs (which is replaced by compute cost). We consider a range for c AV between 0.1 and 0.5, i.e., between a tenth and a half of the revenue of a trip. Though these numbers are generally consistent with those reported in the media, e.g., by [120] and [121], we emphasize that they should only be interpreted as educated guesses; by numerically exploring a wide range with c F ∈ [0.025, 0.4] and c AV ∈ [0.1, 0.5] we aim to include realistic numbers. Across our experiments, we solve K to a precision level of 500, whereas the average hourly demand is on the order of tens of thousands, and c P to a precision level of (1 − c AV − c F ) /100.

Aggregate results. Fig. 3.3 shows the range of profit ratios for our different deployment modes. Whereas PR AV , PR SL , PR LL , and PR s can face significant inefficiencies, PR f displays a small profit ratio for almost all parameters. In particular, we find that PR f (I) < PR s (I) across our experiments, implying that the better-of-two in Theorem 9 always relies on the

86 Figure 3.3: Profit ratio of different deployment modes across all parameters.

Figure 3.4: Experiments that respectively scale up c AV and c F for fixed c I = 0.75.

full prioritization contract and not on the SPE; we discuss this phenomenon further in Appendix B.3.8 where we also highlight instances in which this ceases to be true. As our parameters are not chosen adversarially, we do not expect to see the unboundedly large inefficiencies we observed in our theoretical results; nonetheless we find the most significant inefficiencies in those modes (PR AV , PR SL , PR LL , and PR s ) for which our theoretical results suggest that they can occur. Our numerical results thus reflect our theoretical finding that a well-contracted open platform more effectively hedges against significant inefficiencies and provides a superior deployment model.

Varying costs for AVs. We next examine the effect of the AV cost parameters on the profit ratios of the different deployment models. In Fig. 3.4 (a) and (b) we fix c I and vary, respectively, c AV and c F . We find that the AV-only platform is most sensitive to increases in c AV and c F : While PR AV is close to 1 when c AV and c F are small, it quickly deteriorates as the cost parameters of AVs grow larger. In contrast, PR LL (I) tends to decrease in cAV  and c F , ultimately achieving a profit ratio of almost 1. PR s (I) largely follows the same trend. Intuitively, when c AV and c F are smaller, AVs have a larger advantage relative to ICs, and thus a misalignment causing too few AVs to be supplied creates a greater inefficiency. In contrast, for sufficiently large c AV and c F all operational models (except for AV-only), including the integrated benchmark, rely only on ICs, and AV underutilization no longer disrupts the supply chain. Moreover, while an AV-only platform suffers greatly from the lack of access to ICs for large c AV and c F , the full prioritization contract, though also requiring commitment to AVs, exhibits robust performance as costs of AVs scale up. This occurs because the full prioritization contract sets its AV investment to be K ⋆ , which is decreasing in c AV and c F .

Inefficient SPEs. We then focus on PR s (I) to investigate its dependence on c I and c AV .

87 As shown in Fig. B.1, we find that the misalignment tends to be worse when c I − c AV is large and particularly when c AV is also large. Intuitively, this occurs because when c I − cAV  is small, a platform may perform well by relying only on ICs, which bounds the effect of a misalignment with the supplier; in contrast, when c I − c AV is large, the benefit of AVs is significant, yet the supplier may undersupply to avoid underutilization. When c AV and c I are both large PR s (I) is particularly bad, as we examine next.

Scaling Up Costs. In our next set of numerical results we consider a setting where costs scale up proportionally, so profit margins shrink for both AVs and ICs. Specifically, we set initial values of c I , c AV , and c F , and then proportionately scale these three cost parameters by factors between 1 and 1.5. Fig. B.2 presents the outcomes of these experiments for different initial values of c AV and scaling factors. Fig. B.2 (a) shows that, for almost all initial values of c AV , the resulting misalignment of the SPE in the open platform model worsens as the cost parameters scale up. Intuitively, as costs scale large the profit margin of any solution is small, which magnifies the absolute loss in profit relative to the integrated benchmark. We find similar patterns for the long-term leasing contract in Fig. B.2 (b), with performances deteriorating even faster as the cost parameters grow large. In contrast, the full prioritization contract is more robust as we simultaneously increase the different cost parameters, with < 3% efficiency loss for all instances (see Fig. 3.3).

3.8 Conclusion

Our paper explores a new kind of supply chain misalignment that is likely to emerge as AVs move from being prototypes to being deployed technology. The misalignment is due to the fact that AVs will likely have to be supplemented with human-driven vehicles for managing stochastic demand, and since human drivers need to be engaged to ensure participation, the platform might need to reduce the prioritization of AVs. This is an unusual misalignment where the platform deviates from low-cost to high-cost to ensure sufficient capacity remains available for peak moments of demand.

We find that this, or a similar misalignment also arises when AVs are deployed through short- or long-term leasing contracts in which suppliers are not compensated on a per-ride basis. Though an AV-only platform does not suffer from misaligned incentives, it too may perform poorly due to its inability to adapt to scenarios with heterogeneous demand patterns. The supply chain management literature has solutions in place for aligning incentives, but they all have their challenges in a platform setting like this one. As usual, vertical integration is an option, though it requires merging two very different businesses, one of them being a capital-intensive one. A revenue-sharing contract aligns incentives but requires sharing profits from ICs which may deeply intertwine businesses to a greater degree than is desirable in this highly regulated environment. We show that usage commitments are an effective alternative to align the incentives in the AV supply chain: in the unlikely setting that demand scenarios are contractible, they fully align the supply chain; and even when that is not the case, the option to commit to full AV prioritization offers a strong profit ratio guarantee. In particular, with usage commitments, an open platform exhibits stronger theoretical guarantees and superior numerical performances compared to AV leasing or AV-only platforms.

88 Part II Optimizing Levers for Flexibility

89 
# Chapter 4 Overbooking with Bounded Loss

4.1 Introduction

We study the canonical (quantity-based) single-resource revenue management problem with no-shows (SRMNS). In this problem we consider a firm (e.g., airline, restaurant, hotel, rental car agency) selling multiple products/fares of a single resource (e.g., seats, tables, rooms, cars) over a known, finite, time horizon of T periods. The firm’s resource capacity B and the product prices are exogenously set, and the firm’s objective is to maximize the total profit earned by controlling the availability of the different products over time, i.e., in each period a customer arrives to purchase a particular product, and the firm decides whether or not to accept the customer. For each accepted customer it receives a product-dependent reward. At the end of the time horizon, each accepted customer is a no-show with some (product-dependent) probability, and thus does not consume any resources. The firm is allowed to overbook, i.e., it may accept more customers than it has capacity for, but it pays a fixed compensation (denied-service cost) for every customer that was accepted, shows up, and cannot be served due to a lack of capacity. We study the usual scaling for this problem in which the number of customer arrivals T (demand) and the firm’s supply B (supply) are scaled large while all other parameters remain constant. Our main result is the first algorithm that achieves a uniform additive loss guarantee relative to a clairvoyant optimal algorithm that knows the arrivals a priori (sometimes referred to as the hindsight optimum); uniform additive loss means that the loss is bounded independent of either B or T.1 

4.1.1 Motivation

SRMNS was originally motivated by yield management for airlines for which the single resource consists of seats in a given cabin on a plane [126]. [127] give an excellent overview of its history in the airline industry that also helps illustrate the mapping between the mathematical model and the real-world setting: up until the 1970s the airline industry was regulated, with commercial airlines offering only two service options: first-class and coach-class with fares set centrally across carriers by the regulator (Civil Aeronautics Board). After deregulation

1 Some papers [122–124] refer to this loss as regret, but we avoid that terminology to avoid confusion with other literatures, e.g., the bandit literature [125] that involve a different information/arrival structure.

91 airlines introduced new discounted fare classes with specific requirements/conditions, such as minimum-stay conditions, required round-trip travel, non-refundability, or the inclusion of a Saturday-night stay to segment demand into different categories. For example, a Saturdaynight stay requirement would tend to filter out business travelers while not affecting as many leisure travelers. In essence, these requirements and conditions create different products for the same resource, e.g., a seat in the coach cabin, such that (i) revenue yields vary by product, and (ii) demand for different products is roughly independent — the latter assumes, e.g., that leisure travelers are more price-sensitive and unwilling to pay the higher fare, whereas business travelers are price-insensitive and thus unwilling to fulfill the requirements to meet the lower fare. Having created such different products, the airlines’ real-time decision is whether or not to allow reservations for a particular product. In practice, when an airline closes a given product to reservations, even though seats remain available on a flight, then a customer for such products would be quoted a higher fare based on the products that remain open. As demand is assumed independent across products, such a customer would not make a reservation for the higher fare, and the request is effectively rejected. Notice that, assuming independence of demands across fares, the decision to accept (reject) demand for a specific product is mathematically equivalent to the decision to have that product be open (closed) to incoming reservation requests. While originating in the airline industry, overbooking has since been adopted much more widely, including for lodging [128, 129], rentals cars [130], the restaurant industry [131], and the nonprofit sector [132]. Moreover, the single-resource problem specifically is often not only used in isolation, but also sometimes appears as a subproblem when solving problems with more than one resource, i.e., in network revenue management [133]. Thus, SRMNS is one of the fundamental admission control problems in revenue management.

4.1.2 Technical challenges and algorithmic techniques

Without no-shows the quantity-based single-leg revenue management problem can be solved efficiently via dynamic programming: in each period, an optimal decision only requires knowledge of the remaining capacity and the remaining number of periods. More generally, when no-show probabilities are equal across products, an optimal decision requires knowing only the total count of admitted customers, not the respective product requested by each admitted customer. Thus, in this case as well there is no curse of dimensionality, and a dynamic program solves the problem efficiently to optimality, as was first shown by [126]. This reflects the requirements of Assumption 4.1 in [127]: (i) no-show probabilities are the same for all customers, (ii) no-shows are independent across customers, (iii) no-shows are independent of the time of the reservation, and (iv) denied-service costs are the same across customers. Though these assumptions help obtain a tractable problem, [127], and later [134] (see Chapter 3.3 therein), emphasize that (i) and (iv) are restrictive assumptions in practice. Our work shows how to relax (i) with bounded loss. However, we keep assumption (iv), i.e., we assume that the denied-service costs are the same across different products; obtaining bounded loss when loosening (iv) in addition to (i) remains an interesting avenue for future research.

Though the case with heterogeneous no-show probabilities has been studied extensively, there are few results with provable guarantees for this problem [11, 133]. This is in contrast

92 to the network revenue management problem without overbooking for which a number of algorithms with uniform loss guarantees have been developed over the past decade, and especially in the last few years [122, 124, 135, 136]. We fill this gap by adapting the compensated coupling technique of [122] (see proof of Theorem 11 and paragraph thereafter) to derive the first such uniform loss guarantee for a revenue management problem with overbooking, specifically for SRMNS with heterogeneous no-show probabilities.

Nonlinear objective

The key technical challenge in adapting the compensated coupling technique lies in the fact that the denied-service costs for the expected number of no-shows gives rise to a nonlinear objective. Existing results developing/applying the compensated coupling technique [122, 137, 138] rely on a property that [138] refer to as δ-insensitivity: intuitively, this means that the optimal solution is Lipschitz continuous in the number of arrivals of each type over the entire horizon; notice that this is a Lipschitz property about the optimal solution itself, not just its objective. For linear objectives, δ-insensitivity follows from standard results in linear perturbation analysis [139]. In contrast, establishing such a Lipschitz property directly for our setting is difficult due to the nonlinear objective.

Index policies

Leveraging compensated coupling requires us to take the following detour: instead of benchmarking directly against the complicated clairvoyant optimal solution, we define a suboptimal clairvoyant solution for which we show that it (i) is Lipschitz continuous in the number of arrivals of each type, and (ii) has bounded loss relative to the clairvoyant optimal solution. In order to define this solution we take inspiration from the greedy heuristic for the one-dimensional knapsack problem, which sorts items by their value/weight ratio and includes items in that order until no further items fit. As the expected “weight” of a customer is the probability that they will show up, we similarly sort customers by the ratio between their revenue and their probability of showing up (which we refer to as critical ratio), and accept customers in that order, i.e., there exists some threshold on the critical ratio such that all types with critical ratio higher than the threshold are accepted whereas all types with critical ratio lower than the threshold are rejected. We refer to such a solution as an index solution as the type indices are, without loss of generality, assumed to be ordered by critical ratios; for the index that has critical ratio equal to the index policy’s threshold there is no restriction on how many arrivals should be accepted and we refer to that type as having the threshold index. The main technical innovations to adapt compensated coupling then require us to establish that optimal index solutions fulfill (i) and (ii).

Lipschitz continuity and local optimality

For a given type, keeping the number of accepted arrivals constant for all other types, we can identify the optimal number of arrivals to accept through a marginal analysis. In particular, we should accept an additional request of that type if the expected compensation for that arrival (the compensation multiplied by the probability that they show up and the already accepted arrivals consume all of the capacity) is smaller-equal to the revenue of that type. The

93 optimal number of arrivals to accept for that type then follows a newsvendor-like condition — for the case of a single type, [134] show in their Proposition 3.1 that this locally optimal solution is indeed optimal. 2 With heterogeneous types with varying no-show probabilities, optimal solutions can be more complicated: accepting an additional customer of one type may require rejecting some number of customers of another type which in turn allows for more customers of a third type. . . . In a nutshell, the potential for such loops makes it hard to either find the globally optimal offline solution or prove δ-insensitivity. In a loal sense, however, matters are not as complicated: one of our main technical insights (Lemma 5) shows that the locally optimal number of accepted customers of one type is Lipschitz continuous in the number of accepted customers of a second type (keeping all other types fixed).

The reasoning above allows us to derive that index solutions fulfill (i) as, roughly speaking, an increase in the accepted arrivals of one type, only affects the number of arrivals at the threshold index (other types may be similarly affected in their local optimality, but for all other types we accept either all or none of the arrivals). To derive (ii) we first show that the optimal solution almost resembles an index solution (Lemma 8). In particular, the optimal solution, for all but one type (which would correspond to the threshold index in the index solution), either accepts all (but a constant number of) arrivals or rejects all (but a constant number of) arrivals. Combined with the local Lipschitz property applied to the threshold index, this guarantees that the difference in the number of accepted arrivals between the clairvoyant optimal and the clairvoyant index solution is bounded by a constant for every type, implying in particular that the clairvoyant index solution has bounded loss relative to the clairvoyant optimal.

Instance-dependence

The reasoning in the above paragraphs involve various instance-dependent constants, i.e., the Lipschitz continuity and the proximity between the clairvoyant index and the clairvoyant optimal solution. In particular, these depend on the magnitude of the no-show probabilities, and the ratio of value and no-show probability. This makes sense intuitively: if one type has a probability of ϵ of showing up, then a small decrease in accepted arrivals of another type (with constant probability of showing up) should intuitively cause the locally optimal number of the former type to increase by roughly 1/ϵ — this intuition is driven again by the greedy Knapsack heuristic that replaces probabilities by expectations. When arrival probabilities are allowed to be that small, our O(1)-guarantees break down and, in fact, we show formally in Appendix C.4 that any online policy must incur Ω( √ T) loss when no-show probabilities are allowed to be arbitrarily small. In that same appendix we also show a shortcoming of index policies specifically: we give an example to illustrate their inability to accurately account for the trade-off between risk and reward when the critical ratios of two types are close to each other (and getting closer as the horizon gets longer). We identify an example where a very simple online policy obtains O(1) loss, whereas even the clairvoyant index policy that knows the arrivals incurs Ω( √ T); intuitively, this is caused by the index policy preferring a type with infinitesimally larger critical ratio, even though that type introduces significant costs

2 Considering only the offline optimal index solution, an added benefit of the newsvendor-like condition is that it allows us to find the threshold index, as well as the locally optimal number of accepted customers for that index, through binary search.

94 due to higher variability. For a more detailed discussion of how our guarantees depend on the problem parameters we refer the reader to the paragraphs after Lemma 5 and Lemma 8.

4.1.3 Related work

Compensated coupling

As we alluded to above, our work is most closely related to the recently introduced compensated coupling technique for online stochastic decision-making problems [122, 137, 138]. The novelty of our work, relative to these, lies in (i) the structural results for SRMNS that bound the losses incurred in the detour to the index policy, (ii) the extension of the compensated coupling technique to a nonlinear objective, and (iii) the first uniform loss guarantees for a dynamic revenue management problem with overbooking. Our work also relates closely to the following recent results: [140, 141] prove logarithmic lower bounds on the optimal loss guarantee when types have values that come from continuous distributions, e.g., U[0, 1], rather than coming from a finite set. Similarly, [138] prove lower bounds on uniform loss guarantees that are based on the arrival probabilities of each type (when the latter are not iid). Both of these consider special cases of our setting with overbooking, and thus apply as well. [137, 142] prove uniform loss guarantees for settings where the arrival probabilities are unknown a priori (but iid), and need to be learned — we believe that this part of the analysis of [137] would extend to our setting in a straightforward manner. Finally, it is worth highlighting the work of [143], who introduced novel technical ideas when studying the multisecretary problem with known distribution (equivalent to our problem without no-shows/overbooking), and thereby initiated much of the recent work in this space.

Fluid, diffusion, and uniform loss

The OR literature often distinguishes between fluid and diffusion optimal solutions when proving asymptotic optimality for finite-horizon stochastic control. A solution is optimal on the fluid scale if its loss grows as o(T) over a horizon of length T, and optimal on the diffusion scale if its loss grows as o( √ T); of course, a uniform loss guarantees implies both. For network revenue management (no overbooking), [144] proved the fluid optimality of a static admission policy that is based on the optimization of a deterministic relaxation; [145] found that resolving that relaxation once at an appropriately selected time, to update the policy, gives the first diffusion optimal algorithm. This was strengthened by [135] who resolve in every period to obtain a uniform loss under a technical non-degeneracy assumptions, and further strengthened by [122, 124, 138] to hold in the absence of such an assumption, and without resolving in every period. For problems with overbooking, we know of no algorithms that are optimal on the diffusion scale, as we discuss next.

Overbooking

Our work adds to the literature on dynamic optimization problems in revenue management, and more specifically to the long line of literature on overbooking. [146] describe overbooking as having the “longest research history of any of the components of the revenue management problem” since most quantitative research in revenue management before 1972 focused on

95 admission controls for overbooking. Early models of overbooking include [126, 147, 148], which all focus on just a single leg. In contrast to most early works, [126] studied a dynamic problem, not a static one (in the language of [149]). The distinction, informally, lies in whether admission levels are statically set initially, or made continuously over time. The solution of [126] is an optimal dynamic program, but it considers only a single fare. For multiple fares, the Expected Marginal Seat Revenue heuristics (EMSRa and EMSRb), that are popular in practice to this day, were developed by [150]. Motivated by Littlewood’s rule [151], these heuristics are fundamentally static, yet they can be applied in a dynamic setting (however, they have no provable guarantees); our use of the critical ratio of value and no-show probability is motivated by the same ideas (see Section 4.2 and Lemma 4). Much more recently, [152] study the setting with multiple fares on a single-leg, and cancellations, but assume uniform no-show and cancellation probabilities; their policies do not have any performance guarantees. [153] study the network revenue management problem with only no-shows via a decomposition of the network by flight legs, before using state aggregation for the single-leg problem, i.e., while studying the problem with heterogeneous no-show probabilities, they approximate this problem through one with homogeneous no-show probabilities, without finding provable guarantees for this approach — in Appendix C.5 we prove that, for the single-leg case, their approximation of heterogeneous no-show probabilities with homogeneous ones causes a loss of Ω(T); crucially this is not a shortcoming of the specific method by which they approximate heterogeneous no-show probabilities with homogeneous ones, but rather a fundamental limitation of any such approximation (see Appendix C.5 for details). [133] allows for no-shows in a network setting, and finds an asymptotically optimal policy that is based on the randomized LP of [154]. While asymptotically optimal, this approach incurs Ω( √ T) loss over a time horizon of length T, whereas ours incurs O(1). Loss guarantees of that magnitude may also be obtainable using online convex optimization, e.g., as in [155]; notably they assume significantly less structure on the problem than we do, and therefore their problem is harder (in general, there is a significant body of work on online stochastic allocation problems without overbooking that aims to achieve sublinear regret with less problem structure, e.g., in the context of the AdWord problem [156, 157]). Finally, [11] study the network revenue management problem with no-shows and cancellations and prove a O( √ T) loss over a time horizon of length T; they explicitly state as an open question whether O(1) guarantees are achievable when overbooking is allowed, which we answer in the affirmative. We refer the interested reader to [158] for an overview of further recent work on overbooking.

Overview of remaining sections

In Section 4.2, we formally define our model and algorithm. In Section 4.3 we present our main result using a compensated coupling proof that requires three new auxiliary results. The main technical difficulties lie in obtaining these auxiliary results, which we prove in Section 4.4 and Appendix C.2. In Section 4.5, we complement our analytical results with numerical experiments.

96 4.2 Model

Arrivals

Consider a known finite time horizon of T periods. Every period begins with the arrival of a type j ∈ [k], where [k] denotes the set { 1, . . . , k } . Each arrival is of type j with probability λ j > 0, where ∑ j λ j = 1 and arrivals are independent. We denote the vector of arrivals A ⃗ where A t denotes the arrival type in period t, and ⃗ A[t, T] denotes the last (T −t+1) entries of A. ⃗ We use N j for the number of arrivals of type j over the entire time horizon and N j [t 1 , t 2 ] for the number of type j arrivals in periods t 1 , . . . , t 2 , where t 1 < t 2 . When future ~ arrivals N[t, T] need to be estimated in period t, we denote such an estimate by N f [t].

Objective

There is an initial capacity B. Upon the arrival of each customer, we need to make an irrevocable decision on whether to accept or reject them. Accepting a customer of type j generates revenue v j < 1. For an algorithm ALG we denote by x j ALG [t] the number of accepted customers of type j until the end of period t, i.e., in periods 1, . . . , t. Similarly, let ⃗x ALG [t] denote the k-dimensional vector of accepted customers of each type until the end of period t. At the end of the time-horizon each accepted customer of type j (independently) consumes one resource with probability p j ∈ Q , and is a no-show (does not consume any resources) with probability 1 − p j . The types are ordered such that v 1 /p 1 ≥ v /p 2 ≥ · · · ≥ v k /p k , where ties are broken in favor of greater value, i.e., if v j /p j = v j+1 /p j+1 ,2 then v j > v j+1 and p j > p j+1 . Since this ratio remains important throughout the paper, we define it as the critical ratio vj  vj j  q j = p j of customer type j, and define ¯q j = 1 − p .

In our asymptotic analysis, we assume that all parameters of the customer types are assumed to be fixed, whereas B and T grow large. The combined required resources (arrivals) at the end of the time horizon are distributed as ∑ j Bin(x j ALG [T], p j ), where Bin(x, p) denotes the binomial distribution with x trials and success probability p. When the arrivals require more than B resources, a type-independent compensation is paid for each overbooked customer. We normalize the compensation to 1 so the total compensation has cost ( ∑ j Bin(x j ALG [T], p j )B) + where (α) + := max { α, 0 } . Thus, the objective is to maximize

+   E  ∑ x j ALG [T]v j −  ∑ Bin(x j ALG [T], p j ) − B   . j j    

For any j ∈ [k], we denote by X j,x ALG [T] ∼ Bin(x j ALG [T], p j ) the binomial random variable j of accepted customers of type j who consume a resource. Moreover, we adopt a shorthand notation for expected compensation, with

+   V B (⃗x) := E   ∑ X j,x j − B   .   j  

97 Note that we may assume that the critical ratio q j < 1, i.e, ¯q j > 0. Customer types j with q j ≥ 1 should always be accepted even if we had 0 capacity (left) because the expected compensation is less than the guaranteed value from accepting, and this will indeed be the case for our policy too. Thus, we focus without loss of generality on types j with q j < 1.

4.2.1 Algorithm and benchmark policies

We now define four “policies”: the online index policy, the hybrid clairvoyant index objective, the clairvoyant index objective, and the clairvoyant general objective. The first is our algorithm, the others provide useful benchmarks in our analysis. All four are based on ~ deterministic optimization problems that take an estimate N f [t] of future arrivals in period t to solve

max

⃗x

∑

j

vj 

( xj 

[t − 1] + xj 

) + V B ( ⃗x[t − 1] + ⃗x ) subject to 0

≤

xj 

f ≤ N j [t], ∀j

(4.1)

~ In words, assuming future arrivals N f [t] in periods t, t + 1, . . . , T and past accepted arrivals ⃗x[t−1], optimization (4.1) finds the optimal number ⃗x to accept of each in periods t, t+1, . . . , T.

Index policies

The first three policies are all index policies, meaning intuitively that if j ′ > j, then they prioritize accepting arrivals of type j over arrivals of type j ′ . Since we are in an online setting, this holds only in a forward-looking manner, i.e., it is conditioned on the already accepted customers. Index solutions in period t, conditioned on past decisions ⃗x[t − 1], are defined as follows.

~ Definition 8. Suppose in period t the remaining arrivals are estimated to be N f [t]. A solution ⃗x to (4.1) is an index solution if it has a threshold index ~ j ∈ [k] such that for all j < ~ j all future arrivals of type j are accepted, i.e., x j = N j f [t], and for all j > ~ j no future arrivals of type j are accepted, i.e., x j = 0. As a convention, we always assume that when more than one index could be a threshold index, we uniquely define ~ j to be the smallest possible one, implying that x j > 0 (unless x 1 = 0).

Notice that the intuition for an index policy comes from the one-dimensional knapsack LP in which a customer of type j takes up exactly p j capacity, rather than Bin(1, p j ) capacity. In that case, the critical ratio v j /p j corresponds to the density of value of type j, and the optimal LP solution is to sort by density and pack users until the knapsack is filled. Similarly, our index policy in Definition 8 prioritizes customers with higher critical ratio over ones with lower critical ratios.

Online index policy

The online index policy is formally given in Algorithm 1. Initially, it samples an arrival vector A ⃗ ′ ; this is not the real arrival vector but stems from the same distribution. In period t, it observes an arrival j ′ , and uses A ⃗ ′ to estimate N j f [t]. It then solves the optimization

98 Algorithm 1 Online Index Policy

1: Initialize x j [0] = 0 ∀ j

2: Draw arrival vector λ j

3: for t = 1, . . . , T do benchmark, as was observed by [11]. Nevertheless, our much weaker clairvoyant, which knows the realization of the future arrivals, but not the realization of the no-show probabilities, still provides an upper bound on an optimal algorithm. Finally, it may seem counter-intuitive ~ for the algorithm to draw a sample A ⃗ ′ to estimate N f [t] rather than just using the expected ~ value thereof. However, this ensures that our estimates for N f [t] are integral, which simplifies the analysis in light of Bin(x j , p j ) not being well-defined for fractional x j .

4.2.2 Further notation

We often rely on the Poisson Binomial distribution

PBin(x 1 , p 1 ; ...; x k , p k ),

which consists of x j trials, each with success probability p j , for j ∈ [k]. Note that ∑ X j,x j ∼ PBin(x 1 , p 1 ; ...; x k , p k ) based on this definition. As a shorthand notation, for X j ∼ PBin(x 1 , p 1 ; ...; x k , p k ), we denote the compensation given X by W B (X) = (X − B) +

and the expected compensation by E[W B (X)] = E

(X − B) . [ ]

+

We denote the Cumulative Distribution Function (CDF) of any discrete random variable X at x by F X (x), the Probability Mass Function (PMF) by P[X = x], and the quantile function (i.e., the inverse of CDF) by F X −1 (q), where q ∈ [0, 1]. We use the notation P[E] for the probability of event E. And lastly, we use the standard notation N = 0, 1, 2, ... for natural numbers, and e j for the k-dimensional canonical unit vector with its j th coordinate equal to 1 and all other coordinates equal to 0.

4.3 Main result

Our goal is to prove that the expected additive loss between the online index policy and the ⌃ clairvoyant objective can be bounded by a constant M, i.e., E A ⃗ OPT A − OBJ A ⃗ To do ≤ M.3  [ ] so, we derive intermediate benchmarks and bound their expected loss relative to each other. The most important technical ingredients in our analysis use the following local optimality condition:

Definition 9. Consider a feasible solution ⃗x ⋆ to (4.1) with (estimated) future arrivals and past accepted arrivals ⃗x[t − 1]. We call ⃗x ⋆ locally optimal at j if

 xj v j − E     

 

      

+





∑

−B

x j ⋆ = max

arg max

Xj,x j [t−1]+x j +

X n,xn 

.

[t−1]+xn ⋆ 





f ≤ N j [t]

x j :0 ≤ xj 

n=j ̸

~ N

f

[t]

Intuitively, ⃗x ⋆ is locally optimal at j if x j ⋆ is the (maximum) optimal number of future type j customers to accept given acceptance of x n ⋆ future customers of type n for each n = j. ̸ Because this maximum optimal number of customers is uniquely defined, we observe the

3 Throughout this work, we refer to terms as constant if they do not depend on B or T.

100 irritating property that there may be global optima, i.e., solutions that yield the highest possible profit, that do not satisfy our local optimality condition for every type j. Fortunately, for our analysis, there always exists some global optimum that is locally optimal for every type j. This claim is formalized and proven in Appendix C.2.1, and it allows us to compare our solution to a global optimum that fulfills the local optimality condition for every type. Next, in Lemma 4 we provide an equivalent local optimality condition that is often easier to apply.

~ Lemma 4. For a solution ⃗x ⋆ to (4.1) with (estimated) future arrivals N f [t] and past accepted arrivals ⃗x[t − 1], let ⃗x = ⃗x[t − 1] + ⃗x ⋆ . Then, ⃗x ⋆ is locally optimal at j if and only if both of the following conditions are satisfied:

(i) x j ⋆ = N j f [t] or P [ ∑ n X n,x n n ≥ B ] > q j ; (ii) x j ⋆ = 0 or P X n,x + X j,x j −1 ≥ B . ≤ qj  [ ∑ n=j ]

As noted in the literature review, Lemma 4 bears resemblance to classical results in the field of revenue management like Littlewood’s rule [151], the ESMR heuristics [150], and most notably Proposition 3.1 in [134], which is equivalent for the case that k = 1.

In a nutshell, the main analytical advantage of local optimality over global optimality is that we can derive the following (local) Lipschitz bound on locally optimal solutions. We apply this repeatedly in our proofs to bound by how much solutions deviate from each other.

~ Lemma 5. There exists a constant δ ≥ 1 such that for any solution ⃗x ⋆ to (4.1) with N f [t] and ⃗x[t − 1], it is true that if ⃗x ⋆ is locally optimal at j, then ∃l ∈ { 0, 1, ..., δ } such that ⃗x ′ = ⃗x ⋆ + e i − le j is locally optimal at j.

We remark that δ is large only when (a) p j is small or (b) the critical ratio of any type is either close to 0 or close to 1. For (a), it makes sense that δ depends inversely on p j , e.g., when p j = 1/10, then for every unit of additional capacity one would want to accept (roughly) 10 more arrivals of type j. For (b), δ grows large at the boundary of the critical ratios due to us resorting to the standard normal distribution for a probability bound (see Section 4.4.1). The resulting bound we obtain is based on the inverse of the CDF of the standard normal, which has a large derivative (only) close to 0 and 1. In our context, assuming p j to be an actual constant, e.g., in (0.2, 1], this corresponds to types that either have very small value (so we may want to reject them regardless) or types that have very large value (so we may want to accept them regardless). Recall also that if the critical ratio was greater than 1 in our setting, then one should accept an arrival even if one is out of capacity as the revenue received is greater than the expected compensation to be paid (given the probability of the customer showing up).

The key motivation for our consideration of index solution and local optimality is that Lemma 5 provides a strong bound to capture how an optimal index solution changes when an additional arrival of some type is accepted. In contrast, for a globally optimal solution, we do not know how to prove such a bound. Next, armed with these lemmas, we can show the following two bounds.

101 Theorem 10. There exists a constant M 1 such that for every arrival vector

A ⃗

⌃ OPT A − H A ⃗ [1] ≤ M 1 ,

⌃ which implies in particular that E A ⃗ OPT A [

+E ≤ M ] 1 A [ Lemma 6. There exists a constant M 2 such that

HA ⃗ 

[1] ] .

T ∑ P [ H A ⃗ [t − 1] − H A ⃗ [t] > 0 ] ≤ M 2 . t=2

From these bounds we derive, using compensated coupling [122, 138], the result in Theorem

11.

⌃ Theorem 11. There exists a constant M such that E A ⃗ OPT A ⃗ − OBJA ⃗  [

≤ M. ]

Proof.

⌃ E A OPT A − OBJ A [ ] ≤ M 1 + E A [ H A ⃗ [1] − OBJ A ] T = M 1 + E A ⃗  ∑ H A ⃗ [t − 1] − H A ⃗ [t]   t=2 

T ≤ M 1 + ∑ P [ H A ⃗ [t − 1] − H A ⃗ [t] > 0 ] t=2

≤ M1 +M2 .

(Theorem 10)

(⋆)

(Lemma 6)

For the equality above, observe that we have a telescoping sum in which the first term is H A ⃗ [1], and the last term is H A ⃗ [T] = OBJ A ⃗ as (i) the hybrid clairvoyant in period T is bound to make the same decisions as the algorithm in periods 1, . . . , T − 1 and (ii) the online index policy makes an optimal decision in period T (when there is no uncertainty about future periods). The starred inequality holds because any action in one period affects the objective, through lost revenue or incurred compensation, by at most 1.

Notice that the proof is based on a sample path-wise coupling of the online index policy and the clairvoyant objective. Then, in each period, when the hybrid clairvoyant loses in objective due to a decision by the online policy, the technique “compensates” the clairvoyant for that loss. The expected loss of the online index policy can then be interpreted as the total compensation paid out to the clairvoyant; this, in turn, can be upper-bounded (using that the loss/compensation in any period is bounded by 1) by the sum of the probabilities of having to pay out a compensation.

4.4 Proofs of auxiliary results

This section is dedicated to proving the auxiliary results from Section 4.3, and is organized as follows: in Section 4.4.1 we prove Lemma 4 and Lemma 5 in order to characterize locally

102 optimal solutions and provide a Lipschitz bound for them. Then, in Section 4.4.2 we prove Theorem 10 through a series of lemmas: in Lemma 7 we show through an exchange argument that for i < j any feasible solution improves when a certain number of type j customers is replaced by a proportionate number of type-i customers (where the proportion is based on p i , p j ). Lemma 8 and 9 apply this result to show that globally optimal solutions are, in a sense, not too far from being index solutions. As the objective of optimization (4.1) is Lipschitz in its solution, Theorem 10 then follows from the globally optimal solution and the optimal index solution not being too different. Finally, in Section 4.4.3 we combine the Lipschitz bound on optimal index solutions with the compensated coupling technique to uniformly bound the loss of the online index policy relative to the optimal index solution.

4.4.1 Proof of Lemma 4 and Lemma 5

Proof of Lemma 4

We show both directions by contradiction. First, suppose ⃗x ⋆ fulfills Definition 9, but (i) is false. Recalling that the lemma defines ⃗x = ⃗x[t − 1] + ⃗x ⋆ , we find that

X n,x n B ∑ [ n ] Then ⃗x ⋆ +e j is feasible because x j ⋆ +1 ≤ N j f [t]; we shall argue that accepting x j ⋆ +1 customers of type j yields no less profit than accepting x j ⋆ , which contradicts that ⃗x ⋆ fulfills Definition 9.

P

≥

≤

q j and x j ⋆ <

~ N

f j

[t].

We first observe that the increase in revenue for accepting one more type j customer is v j . To quantify the increase in expected compensation from taking solution ⃗x ⋆ + e j rather than ⃗x ⋆ , let ∑ n X n,x n denote the Poisson Binomial random variable capturing the number of customers among ⃗x = ⃗x[t − 1] + ⃗x ⋆ who consume a resource (see definition in Section 4.2.2). Similarly, the random number of customers requiring resources under solution ⃗x + e j is ∑ n =j ̸ X n,x n +Xj,x j +1 .

To characterize the compensation paid, suppose first that ∑ n X n,x n < B, i.e., the number of accepted customers among ⃗x who show up is smaller than the capacity B. Then from X j,1 ≤ 1 we also find ∑ n =j ̸ X n,x n + X j,x j +1 = ∑ n X n,x n + X j,1 ≤ B, and no compensation is paid for the additional type j customer.

If instead ∑ n X n,x n ≥ B, then the additional type j customer decreases the objective by 1 if that customer shows up (with probability p j ). Thus, the increase in expected compensation from an additional type j customer is

V B ( x + e j ) − V B (⃗x) = P X n,x n < B · 0 + P X n,x n ≥ B · p j · 1 ≤ q j · p j = v j . ∑ ∑ [ n ] [ n ]

Notice that the inequality holds when Lemma 4 (i) is false. Thus, ⃗x ⋆ + e j yields at least the same objective value as ⃗x ⋆ does. Since the solution ⃗x ⋆ is locally optimal at j only if x j ⋆ is the largest number that achieves the highest objective value, ⃗x ⋆ is not locally optimal at j, which is a contradiction.

103 Next, we show that Definition 9 implies Lemma 4 (ii). We suppose for sake of contradiction that ⃗x ⋆ is locally optimal at j and (ii) is false. We then show that ⃗x ⋆ − e j must achieve a higher objective than ⃗x ⋆ to derive a contradiction. First, when (ii) is false, we have

P  ∑ X n,x n + X j,x j −1 ≥ B  > q j and x j ⋆ > 0. ̸  n=j 

Then, ⃗x ⋆ − e j is feasible because x j ⋆ − 1 ⋆ ≥ 0. As above, the increase in expected compensation from taking solution ⃗x ⋆ rather than ⃗x − e j is

V B (⃗x) − V B ( x − e j ) =P  ∑ X n,x n + X j,x j −1 < B  · 0 + P  ∑ X n,x n + X j,x j −1 ≥ B  · p j > v j , ̸ ̸  n=j   n=j 

where the inequality holds when (ii) is false. Since the increase in revenue from accepting x j ⋆ rather than x j ⋆ − 1 type j customers is v j , ⃗x ⋆ − e j yields a better objective value than ⃗x⋆  does, which contradicts that ⃗x ⋆ is locally optimal at j.

Next we show the other direction, i.e., that ⃗x ⋆ is locally optimal at j if both (i) and (ii) are satisfied. We again argue by contradiction, and show that if ⃗x ⋆ is not locally optimal at j, then at least one of (i) and (ii) must be false. Specifically, if ⃗x ⋆ is not locally optimal at j, then there exists some l = ̸ 0⋆ j such that ⃗x ⋆ + l · e j is locally optimal at j.

If l > 0, we must have x < N j f [t] since otherwise x j ⋆ + l > N j f [t] is infeasible. Since we showed that ⃗x ⋆ + l · e j being locally optimal at j requires ⃗x ⋆ + l · e j to fulfill condition (ii) of the lemma,

P  ∑ X n,x n + X j,x j +l−1 ≥ B  ≤ qj  ̸  n=j 

holds true. Then, since l ≥ 1,

k P  ∑ X n,x n ≥ B  ≤ P  ∑ X n,x n + X j,x j +l−1 ≥ B  ≤ q j . ̸  n=1   n=j 

f P n Thus, [ ∑ X n,x ≥ B ] ≤ q j and x j ⋆ < N j [t], which contradicts (i).

If l < 0, n we must have x j ⋆ > 0 since otherwise x j ⋆ + l < 0 is infeasible. Since we showed that ⃗x ⋆ + l · e j being locally optimal at j requires ⃗x ⋆ + l · e j to fulfills condition (i) of the lemma,

P  ∑ X n,x n + X j,x j +l ≥ B  > qj  ̸  n=j 

holds true. Then, since l ≤ −1,

P  ∑ X n,x n + X j,x j −1 ≥ B  ≥ P  ∑ X n,x n + X j,x j +l ≥ B  > q j . ̸ ̸  n=j   n=j 

104 X n,x n + X j,x j −1 ≥ B and x j ⋆ > 0, which contradicts (ii). > qj  [ ∑ n =j ̸ ] Thus, if ⃗x ⋆ is not locally optimal at j, then at least one of (i) and (ii) must be false.

Thus, P

Proof of Lemma 5

Let ⃗x = ⃗x[t − 1] + ⃗x ⋆ . Lemma 4 (i) guarantees that

P

∑ [ n

Xn,x n 

≥

B

]

> q j , or x j ⋆ =

~ N

f j

[t].

If x j ⋆ = l ≤ −1,

~ N

f j

[t], then no additional type j customers may be accepted; otherwise, for any

P









∑

n=i,j ̸

X n,x n +Xi,x i +1 +X j,x j + l || ≥

B

≥

P

∑ [ n

Xn,x n 

≥

B

]

>qj 

means that the objective value of ⃗x + e i + | l | · e j is smaller than that of ⃗x + e i + ( | l | − 1) · e j . Thus, l ≥ 0.

We show for each j that there is a constant δ j such that l ≤ δ j is guaranteed. Then, we set δ = max j δ j as a constant that fulfills the lemma. To determine δ j and prove the lemma, vj  we first take Claim 1 and Claim 2 below for granted. Recall that ¯q j = 1 − p j from Section 4.2. We denote for a given constant δ ⋆ ≥ 1 and solution ⃗x:

k Y = ∑ X n,x n + X j,x j +δ ⋆ , Z = ∑ X n,x n , and m = ∑ x n . n=j n n=1 ̸

Claim 1. There exist constants δ ⋆ j and m 0 ∈ Z + such that

F Y −1 (¯q j ) − F Z −1 (¯q j ) ≥ 1

(4.2)

holds whenever m ≥ m 0 .

Claim 2. If ⃗x − (δ j + 1)e j + e i is a feasible solution to the optimization problem (4.1), then

P  ∑ X n,x n + X j,x j −δ j −1 ≥ B − X i,x i +1  ≤ P  ∑ X n,x n + X j,x j −δ j −1 ≥ B − 1 − X i,x i  . ̸ ̸  n=i,j   n=i,j 

Now, take δ j = 1 + δ j ⋆ + m 0 with δ ⋆ j and m 0 from Claim 1. Observe that we only need to check cases where x j ⋆ > δ j , because x j ′ = x j ⋆ − l ≥ 0 guarantees l ≤ δ j when x j ⋆ ≤ δ j . Thus, we below assume that x j ⋆ > δ j , when showing l ≤ δ j .

For solution ⃗x with x j ⋆ > δ j , define

¯Y = ∑ X n,x n + X j,x j −1 and ¯Z = ∑ X n,x n + X j,x j −δ ⋆ −1 . n=j n=j ̸ ̸

105 In particular, ¯Y is the random variable Y from above, constructed for solution ⃗x − (δ ⋆ + 1)e j , which is guaranteed to be feasible when x j ⋆ > δ j > 1 + δ ⋆ . Similarly, ¯Z is the random variable Z from above, constructed for solution ⃗x − (δ ⋆ + 1)e j . Since

∑ x n − (δ ⋆ + 1) ≥ x j ⋆ − (δ ⋆ + 1) > m 0 , n

we can apply Claim 1 to ¯Y and ¯Z.

We will argue that ∀a ≥ 1 : P X n,x n + X i,x i +1 + X j,x j −δ ⋆ −a ≥ B to derive a ≥ qj  [ ∑ n =i,j ̸ ] contradiction from Lemma 4 (i). Lemma 4 (ii) guarantees that, with ⃗x ⋆ locally optimal at j,

x j ⋆ > 0,

P [ ¯Y ≥ B ] = P  ∑ X n,x n + X j,x j −1 ≥ B  ≤ q j , ̸  n=j 

so we know F ¯Y (B −1) ≥ ¯q j . By inverting the CDF into the quantile function, we equivalently find that F ¯Y −1 (¯q j ) ≤ B − 1. Then, Claim 1 implies that

F ¯Z −1 (¯q j ) ≤ F ¯Y −1 (¯q j ) − 1 ≤ B − 2.

By inverting the quantile function for ¯Z back into the CDF, we find that F ¯Z (B − 2) ≥ ¯q j . Thus,

P  ∑ X n,x n + X j,x j −δ ⋆ −1 ≥ B − 1  = P [ ¯Z ≥ B − 1 ] ≤ q j . ̸  n=j 

With Claim 2, we obtain

P  ∑ X n,x n + X j,x j −δ ⋆ −1 ≥ B − X i,x i +1  ≤ P  ∑ X n,x n + X j,x j −δ ⋆ −1 ≥ B − 1  ≤ q j , ̸ ̸  n=i,j   n=j  and thus

∀a ≥ 1 : P  ∑ X n,x n + X i,x i +1 + X j,x j −δ ⋆ −a ≥ B  ̸  n=i,j 

≤ P  ∑ X n,x n + X i,x i +1 + X j,x j −δ ⋆ −1 ≥ B  ̸  n=i,j 

=P  ∑ X n,x n + X j,x j −δ ⋆ −1 ≥ B − X i,x i +1  ≤ q j . ̸  n=i,j 

It follows from Lemma 4 (i) that ⃗x ′ = ⃗x ⋆ + e i − le j is not locally optimal at j when

x j ′ ≤ x j ⋆ − δ ⋆ − 1 < x j ⋆ − δ j − 1.

Thus, there exists l ≤ δ j such that ⃗x ⋆ + e i − le j is locally optimal at j.

We prove Claims 1 and 2 in Appendix C.2.2.

106 4.4.2 Proof of Theorem 10

The proof of Theorem 10 is based on Lemma 5 as well as a second bound. Informally, the second bound implies that, for large enough T, the optimal policy starts to resemble an index policy up to constant differences. We deduce that the optimal clairvoyant objective and the optimal clairvoyant index objective are based on solutions to (4.1) that have bounded distance in infinity-norm. Since the objective is Lipschitz, the theorem follows. We formalize this argument through three lemmas.

Lemma 7. For every i < j there exists a constant R ij such that, for any feasible solutions R ⃗x ⋆ + p i ij · e i and ⃗x ⋆ + ij j · e j to optimization problem (4.1) with N[t, T] and ⃗x[t − 1], the

R Rij  objective of ⃗x ⋆ + p ij i · ei R p is always greater than that of ⃗x ⋆ + p j · e j .

We prove Lemma 7 via an exchange argument.

Proof of Lemma 7. For any constant R ∈ Z + such that p i R and denote

R are both integers, pj 

R R X i ∼ Bin , p i , X j ∼ Bin , p j . ( p i ) ( p j )

Since we leave all customers among ⃗x = ⃗x ⋆ + ⃗x[t − 1] unchanged, we denote the number of unchanged customers who consume a resource by random variable

X ∼ PBin (x 1 , p 1 ; ...; x k , p k ) .

To prove the lemma we distinguish between the following cases for i < j. We prove the Lemma for the first case here, and the second (more complicated) case in Appendix C.2.3.

(i) q i > qj 

(ii) q i = q j and v i > vj 

is

In case (i), the difference in revenue between any feasible solutions ⃗x ⋆ + p R ·e i and ⃗x ⋆ + p R ·e j i j

R vi  R vj  v i − v j = − R, p i p j p i pj  ( )

which is positive and scales linearly with R. Thus, to show that a constant R exists such that the increase in revenue outweighs the increase in compensations, it suffices to verify that the difference in expected compensation is bounded by o(R).

Recall that, by definition, E[W B (X)] = E

(X − B) + for random variable X. We show [ ]

E [ (X i − X j )+ 

] ∈ O (

√ R log(R) ) to bound the difference in expected compensation as

E[W B (X + X i )] − E[W B (X + X j )] ≤ ∑ P [X = x] E [ (X i − X j ) + | X = x ] x

=E [ (X i − X j ) + ] ∈ O √ R log(R) ( )

107 Next, for E [ (X i − X j )+ 

] , we apply a Chernoff bound. Let κ = 2

√ R log(R). Since

E [ (X i − X j ) + ] ≤ P [ X i − X j < κ ] · κ + P [ X i − X j ≥ κ ] · E[ ( X i − X j ) | X i − X j ≥ κ] R ≤ P [ X i − X j < κ ] · κ + P [ X i − X j ≥ κ ] · , pi 

it suffices to show P [ X i − Xj 

≥

κ ] ∈ O

( √

log(R) R

)

to prove the required bound. For X i −

≥ κ to hold, observe that at least one of 1) E 1 = { Xi  must occur, so

Xj 

≥

κ/2 } ; or 2) E 2 = { Xj 

≤

κ/2 }

P [ X i − X j ≥ κ ] ≤ max ( P [E 1 ] , P [E 2 ] ) .

With ϵ =

√

log(R) R

a Chernoff bound gives

2 log(R) P [E 1 ] = P ≥ R + √ R log(R) = R − 2+ϵ 1 ∈ o , Xi  ≤ e− 2+ϵ ϵ R  [ ] R √ ( )

and a similar Chernoff bound works for P [E 2 ]. Thus, we find

E [ (X i − X j ) + ] ≤ O R log(R) . ( √ )

Rij  Therefore, there exists some R ij such that the increase in revenue from replacing p j type j

Rij  customers with p i type i customers outweighs the loss in additional compensation, i.e., ⃗x ⋆ +

Rij  p i ij · e i yields a better objective than ⃗x ⋆ + p j · e j does, and this completes the first part of the proof.

R

Lemma 8. Consider an optimal solution ⃗x ⋆ to the optimization problem (4.1) with future arrivals N[t, T], and past accepted arrivals ⃗x[t − 1]. Then for every i and j with i < j there exists a constant R ij such that at least one of the following two is true:

(i) x i ⋆ > N[t, T] − R ij /pi 

(ii) x j ⋆ < R ij /p j .

Notice that the constant R ij above is large when types have critical ratios that are close to each other. We highlight the intuition here and this limitation of the index policy is further explored in Appendix C.4.2. Intuitively, we find R ij as the smallest R such that

vi  vj  − R ≥ 2 √ R log(R), p i pj  ( )

where the left-hand side is the increase in revenue (from replacing p i R type i customers with p j R type j customers) and the right-hand side is an upper bound for the increase in

108 (

2

compensation. Thus, R ij roughly scales as 1/

vi  pi 

vj  − pj 

)

. Notice, though, that our upper

bound of 2 √ R log(R) for the increase in compensation is extremely loose as the expected number of customers who show up among p i R type i customers is in fact the same as that among p j R type j customers.

Proof of Lemma 8. We prove the lemma by constructing a contradiction. Take R ij as constructed in Lemma 7. For an optimal solution ⃗x ⋆ , if neither (i) nor (ii) is true, i.e.,

x i ⋆ ≤ N[t, T] − R ij /p i and x j ⋆ ≥ R ij /p j ,

R R then, ⃗x ⋆ − p j ij · e j + p ij i · e i is a feasible solution, and from Lemma 7, we know its objective is greater than that of ⃗x ⋆ , which contradicts the assumption that ⃗x ⋆ is an optimal solution to (4.1).

Now we formally compare a globally optimal solution x ⋆ with an optimal index solution x ′ . Based on Claim 13, we know that there exists a globally optimal solution x ⋆ that is locally optimal for every type j. For the optimal index solution x ′ , we only assume that it is locally optimal at its threshold index and it need not be locally optimal at any other index. Since the index policy is allowed to accept any number of requests at its threshold index, we are guaranteed that there exists an index solution that is locally optimal at the threshold index.

Lemma 9. Consider an optimal solution ⃗x ⋆ that is locally optimal for every type j, and an optimal index solution ⃗x ′ ~ boththatislocallyoptimalatitsthresholdindexj, for the optimization problem (4.1) with arrivals N. ⃗ 4 With δ as constructed in Lemma 5, we have

(i) ∑j 

xj ′  (

−xj ⋆ 

)

+

≤

kδ 1 + ∑j  [

xj ⋆  (

−xj ′ 

)

+

, ]

+ + (ii) ∑ j − x j ′ ≤ kδ ∑ j − x j ⋆ . xj ⋆  xj ′  ( ) ( )

Proof of Lemma 9 (i). Recall that we have x j ′ = N j for every j < ~ j, x j ′ = 0 for every ′ j > ~ j, and x ~ > 0. We start by showing that ⃗x ′ is locally optimal at every j > ~ j, and ⃗x ′ − e~ j  j is locally optimal at every j < ~ j. From Lemma 4 (i), since ⃗x ′ is locally optimal at ~ j, we find ′ ′ that either x ~ j = N j , in which case x ~ = 0, and j+1

P

∑ [ n

Xn,x 

′ n

≥

]

B > q j+1

≥

q j , ∀j >

~ j,

or P

∑ [ n

Xn,x 

′ n

≥

B

]

>q~ j 

≥

q j , ∀j >

~ j.

Thus, for every j >

~ j both conditions of Lemma 4 are fulfilled with

x j ′ = 0 and P

∑ [ n

Xn,x 

′ n

≥

B

]

>qj ,

which implies that ⃗x ′ is locally optimal at all such j.

4 We assume without loss of generality that N j > 0∀j as types j with N j = 0 cannot be accepted by either solution.

109 Moreover, applying Lemma 4 (ii) to

 P 

~ j, where x′ 

~ j

X n,x n ′ +X~ j,x ~ j −1 

> 0, we find for all j <

 B 

q~ j 

qj .

≥

≤

≤

~ j

∑



n= ̸

~ j



Thus, for every j <

~ j, we have x

′

j

= N j and P

̸ ~ [ ∑ n=j

X n,x n ′ + X j,x −1 ≥ B , so ⃗x ′ − e j ≤ q j j ] ~ j, and is thus locally optimal at each such j.

fulfills both conditions of Lemma 4 at every j < ′ Next, define ˆ j to be either ~ j or ~ j − 1 depending on whether x ~ ≥ x or not, to ensure j ′ ′ ⋆ ⋆ x j ≥ x j for all j ≤ ˆ j and x ≤ x j for all j > ˆ j — these follow for j < ~ j~ ⋆ j from x j = N j , for j > ~ j from x j ′ = 0, and for ′ j j = ~ from the definition of ˆ j. Then, to prove Lemma 9 (i), it j suffices to show for j ≤ ˆ j

k

≤ ∑ n=j+1 In particular, when this inequality holds true for j = { 1, ...,

x j ′ − xj ⋆ 

(x n ⋆ − x n ′ )).

δ(1 +

(4.3)

ˆ j

, we can sum over j ≤

}

ˆ j to

obtain ˆ j k + +   ′   xj  − x j ⋆ = x n ′ − x n ⋆ ≤ kδ  1 + (x n ⋆ − x n ′ )  = kδ 1 + − x j ′ . xj ⋆  ∑ ( ) ∑ ( ) + ∑ ∑ ( ) j n=1 n=j+1 j    

We prove Inequality (4.3) by contradiction. Specifically, suppose

k   x i ′ − x i ⋆ > δ  1 + ∑ (x n ⋆ − x n ′ )  n=j+1  

for some i ≤

ˆ j. Then xi ⋆ 

< N i and we prove that

P X n,x n ⋆ ≥ B ≤ qi , ∑ [ n ]

(4.4)

which contradicts ⃗x ⋆ fulfilling the local optimality conditions from Lemma 4 at i.

We consider two cases

(a) i < ˆ j ≤ ~ j or i ≤ ˆ j < ~ j (b) i = ˆ j = ~ j For Case (a), let m = ∑ n= k j+1 (x n ⋆ − x n ′ ). We construct a sequence of solutions

⃗x 1 ,⃗x 2 ,⃗x 3 , ...,⃗x m+1 ,

where ⃗x m+1 has the following properties:

110 • ⃗x m+1 is locally optimal at i,

• xi m+1 >xi ⋆ ,

• ̸ x j m+1 ≥ xj ⋆ x j ′ = N j for all j ≤ ˆ = j such that j = i, and

• x j m+1 = x j ⋆ for all j > ˆ j.

With x j m+1 ≥ x j ⋆ ∀j we have the first inequality, and with ⃗x m+1 locally optimal at i and x i m+1 > 0 we have (Lemma 4 (ii)) the second inequality in

P X n,x n ⋆ ≥ B ≤ P  ∑ X n,x n m+1 + X i,x i m+1 −1 ≥ B  ≤ q i . ∑ [ n ]  n=i  ̸

Thus, such ⃗x m+1 implies Inequality (4.4), i.e., a contradiction to ⃗x ⋆ being locally optimal at i. We now show how to derive ⃗x m+1 by inductively constructing ⃗x h from ⃗x h−1 where for every h ∈ { 1, 2, ..., m + 1 } , ⃗x h is locally optimal at i, x i h > x i ⋆ + δ(m + 1 − h), and ⃗x m+1 fulfills the last two properties above.

Recall that ⃗x ′ ~ so− e ~ j is locally optimal at i < j, by Lemma 5 there exists 0 ≤ l 1 ≤ δ such that ⃗x 1 = ⃗x ′ − e ~ j + e ~ j − l1 e i = ⃗x ′ − l 1 ei 

is locally optimal at i. Further, since l 1 ≤ δ, we know x 1 − x i ⋆ > δm. Now, for each i h ∈ { 1, 2, ..., m } , we repeat this procedure of adding one customer of type j > ˆ j: given a solution ⃗x h that is locally optimal at i, Lemma 5 allows us to find the l h+1 such that ⃗x h+1 = ⃗x h + e j − l h+1 e i is locally optimal at i. Moreover, Lemma 5 guarantees that l h+1 ≤ δ, i.e., x i h − x i h+1 ≤ δ. Thus, the first two properties are maintained throughout. Since we 1 ⋆ have x j ≥ x j for j ≤ ˆ j when j = i, and we never remove a customer from such j, the third ̸ property holds, and since we add customers until x j h = x j ⋆ for j > ˆ j the fourth property holds. This completes the proof of Case (a).

For Case (b) the sequence of solutions starts at ⃗x ′ , not ⃗x 1 , because ⃗x ′ is already locally optimal at i when i = ˆ j = ~ j. Then, we derive the same contradiction to x i ′ − x i ⋆ > δ ∑ n= k j+1 (x n ⋆ − x n ′ ) = δm by constructing ⃗x m+1 with the properties as above.

The proof of Lemma 9 (ii) is based on a similar argument and is included in Appendix C.2.4.

Proof of Theorem 10. Consider p min = min j p j < 1, R max = max i,j:i<j R ij ≥ 1 for R ij as constructed in Lemma 8, and δ ≥ 1 as constructed in Lemma 5. To prove the theorem we show ⌃ := R A, ⃗ OPT A − H A ⃗ [1] ≤ M 1 δk(k + 2) , ∀ pmin max  and observe that all terms on the right are independent of B and T.

Suppose the clairvoyant general solution, locally optimal at each j, given B and A, ⃗ is ⃗x⋆  and a clairvoyant index solution, that is locally optimal at its threshold index ~ j, is ⃗x ′ . Then

⌃ OPT A ⃗ − H A ⃗ [1] =

 

∑

j

 

v j x j ⋆ − V B (⃗x ⋆ )

−

 

∑

j

v j x j ′ − V B (⃗x ′ )

 

111 =  ∑ v j (x j ⋆ − x j ′ )  + ( V B (⃗x ′ ) − V B (⃗x ⋆ ) ) ≤  ∑ (x j ⋆ − x j ′ ) +  +  ∑ (x j ′ − x j ⋆ ) +  .  j   j   j 

Notice that the inequality is a seemingly loose bound: it ignores greater revenue for ⃗x ′ from types j with x j ′ > x j ⋆ , it compensates for every such customer, regardless of whether or not such compensation would be paid, it rounds up v j to 1 for j with x j ⋆ > x j ′ , and it ignores the compensation for these types. Nonetheless, it is sufficient for our purposes. We discuss two main cases based on the threshold index ~ j of ⃗x ′ , where we recall that x j ′ = N j ≥ x j ⋆ for j < ~ j, and x j ′ = 0 ≤ x j ⋆ for j > ~ j.

(i) x j ⋆ < R pmin max 

(a) x ′ ~ j

≥

, ∀j ≥

x ⋆ ~ j

(b) x ′ ~ < x ⋆ ~ j j

~ j. Then we consider

(ii) Find the largest index j ≥

(a) x ′ j

≥

x ⋆ j

(b) x ′ j < x ⋆ j

~ j such that xj ⋆ 

R ≥ pmin max 

, denoted by

ˆ j. Then we consider

~ We begin with Case (i.a). Since x j ′ j,= N j x j ⋆ for any j < ≥ k (x j ⋆ ~ +− x j ′ ) x j ⋆ (k − j 1) R max . ∑ ≤ ∑ ≤ p min j j=j Then we find that

k   ∑ (x j ′ − x j ⋆ ) + ≤ kδ  1 + ∑ (x j ⋆ − x j ′ )  j j=j+1  

(Lemma 9 (i))

R j) ≤ kδ 1 + (k − ~ [ p min max ] Rmax  δk 2 . ≤ pmin 

(Assumption of Case (i.a))

⌃ Thus, in Case (i.a): OPT A − H A ⃗ [1] ≤ (k −

~ j + 1) R pmin max 

R + δk(k + 1) pmin max 

≤

Rmax  δk(k + 2) .

pmin 

The arguments for Case (i.b) are similar to those for Case (i.a) and give

k   ~ j + 1) R Rmax  ∑ (x j ′ − x j ⋆ ) + ≤ kδ  1 + ∑ (x j ⋆ − x j ′ )  ≤ kδ [ 1 + (k − p min max ] ≤ δk(k + 1) p min . j j=j  

112 ⌃ Thus, in Case (i): OPT A − H A [1] ≤ (k −

~ j + 1) R max

p min

R max + δk(k + 1)

p min

≤

R δk(k + 2)

pmin max 

.

⋆ For Case (ii.a) we argue as follows. We know that x j ′ ~ so= 0 x , > j, for x ∀j ≤ j max R to hold we must have ˆ j = ~ j. Moreover, x ′ = N j x j ⋆ , ∀j < ˆ j = ~ j. Thus,

′ ˆ j

j ≥

p min

≥

x j ⋆ ˆ

≥

k

∑

ˆ j+1

j=

∑

j

(x j ⋆ − x j ′ ) +

≤

x j ⋆

≤

(k −

ˆ j) R max

p min

ˆ j k R Rmax    and ∑ (x j ′ −x ⋆ j ) + = ∑ (x j ′ −x ⋆ j ) ≤ kδ  1 + ∑ (x j ⋆ − x j ′ )  ≤ kδ 1 + (k − ˆ j) ≤ δk2  [ p min max ] pmin  j j=1 j=j+1  

⌃ imply OPT A − H A [1] ≤ (k −

ˆ j) R

pmin max 

Rmax 

pmin 

R ≥ pmin max 

+ δk2 

≤

Rmax  δk(k + 1) .

pmin 

In Case (ii.b), we know from Lemma 8 that, if x ⋆ j Thus, , < ˆ j, implying x j ′ −x j ⋆ ≤ R p min max ∀j

, then x j ⋆ > N j − R max p min ∀j <

ˆ j.

ˆ ˆ j−1 j−1 R max R ∑ (x j ′ − x j ⋆ ) + ≤ ∑ (x j ′ − x j ⋆ ) ≤ ∑ ≤ (j − 1) . p min pmin max  j j=1 j=1

Moreover, with Lemma 9 (ii) implying the second, and Lemma 8 (i) implying the third inequality in

j−1 k ˆ Rmax  ∑ (x j ⋆ − x j ′ ) + ≤ ∑ (x j ⋆ − x j ′ ) ≤ kδ ∑ (x j ′ − x j ⋆ ) ≤ δk 2 , pmin  j j=j j=1

⌃ we conclude OPT A ⃗ − H A ⃗ [1] ≤ δk2 

R

pmin max 

ˆ j − 1) R

pmin max 

+(

≤

δk(k

R + 1)

pmin max 

.

Thus, in any case, the loss is bounded by δk(k + 2) R p min max , independent of B, T and

4.4.3 Proof of Lemma 6

A. ⃗

The proof of the lemma follows ideas from [122, 138]. Suppose the arrival in period t − 1 is of type i, and the online index policy accepts the arrival — the proof is symmetric, but the notation is more cumbersome, when the arrival is rejected. We denote by ⃗x ⋆ the clairvoyant index solution in period t − 1 and by ⃗x ′ the solution found by Algorithm 1 in period t − 1, i.e., ⃗x ⋆ and ⃗x ′ are both optimal index solutions to (4.1) with past actions ⃗x[t − 2], but ⃗x ⋆ is based on the real arrivals, from A, ⃗ in periods t, t + 1, . . . , T whereas ⃗x ′ is based on the sampled arrivals from A ⃗ ′ .

113 Observe first that we must have x i ′ ≥ N i f [t − 1]/2 when we are in the case that the online index policy accepts i in period t − 1 (see Algorithm 1). Now, if x i ⋆ > 0, then the clairvoyant index policy (in period t−1) still accepts at least one arrival of type i in periods t−1, t, . . . , T. But that implies that the clairvoyant index policy objective in period t−1 is still achievable in period t. Thus, the online index policy does not incur any loss by accepting an arrival of type i in period t − 1, and we must have H A [t − 1] − H A [t] = 0. We derive that in order to incur a loss when accepting i in period t − 1 it must be the case that x i ⋆ = 0 and x i ′ ≥ N j f [t − 1]/2, i.e., P [ H A [t − 1] ′ − H A [t] > 0 ] ≤ P i ′ − x i ⋆ > N i f [t − 1]/2 − 1 (4.5) x . [ ]

At the same time, since ⃗x and ⃗x ⋆ are index policies, (i) x i ⋆ = 0 and N i [t − 1, T] ≥ 1 imply f f ′ ′ ⋆ that x j = 0 ∀ j ≥ i, and (ii) x i ≥ N i [t − 1]/2 > 0 implies x j = N j [t − 1] ∀ j < i. We make the following claim, which we prove in Appendix C.2.5.

Claim 3. With ⃗x ′ , ⃗x ⋆ as described we have

i−1 ′ xj ⋆  x i − x i ⋆ ≤ δ  ∑ − x j ′ ) +  . (  j=1 

The proof of Claim 3 is straightforward from Lemma 5 and included in Appendix C.2.5. Combining the claim with the reasoning above we obtain

i−1 ′ x i − x i ⋆ ≤ δ  ∑ x j ⋆ − x j ′ ) +  (  j=1 

i−1 +  f  N = δ ∑ ( x j ⋆ − j [t − 1] )  j=1  i−1 +  f  N ≤ δ ∑ ( N j [t − 1, T] − j [t − 1] ) .  j=1  Together with (4.5) this implies that

(Claim 3)

(ii)

(x j ⋆ ≤ N j [t − 1])

i−1 +    f  f N N P [ H A ⃗ [t − 1] − H A ⃗ [t] > 0 ] ≤ P  δ ∑ ( N j [t − 1, T] − j [t − 1] ) > i [t − 1]/2 − 1  .   j=1  

Let ¯t = T − t. Applying Chernoff bounds to that

~ ⃗ N[t − 1] and N

f

[t − 1] with ϵ = log(¯t) ¯t , we know λj 

√

1 with E 1 j = [t − 1] − λ j ¯t ≥ log(¯t)√¯t ∈ o , ∀j Nj  we have P E1 j  ≤ e− 2+ϵ ϵ 2 λ j ¯t  { } [ ] ( ¯t 2 )

1 With E 2 j = N j f [t − 1] − λ j ¯t ≤ − log(¯t)√¯t ∈ o , ∀j we have P E2 j  ≤ e− ϵ ϵ 2 λ j ¯t  { } [ ] ( ¯t 2 )

114 E1 j  , P E2 j  < for any ¯t ≥ t 1 . A [ ] [ ] c union bound over E 1 j E 2 j for all j implies that, for E = ∩ j ∪ E 2 j , we have E1 j  ( )

Thus, there exists some constant t1 

,

∈

Z + such that P

1 ¯t2 

2k P(E) > 1 − , ∀ ¯t ≥ t 1 . ¯t2 

Next, define t2 

∈

Z + as the smallest value such that for ¯t ≥ t2 

1 δk2√ ¯t log(¯t) ≤ λ i ¯t/2 − 1 − ¯t. √ 2

Then, conditioning on event E we find for ¯t ≥ t 2 that

  ∑ ( N j )  j=1  where the first inequality holds conditioned on E, and the second with ¯t ≥ t 2 . Let t 3 = max { t 1 , t 2 } ; then for T − t ≥ t 3 we have P [ H A ⃗ [t − 1] − H A ⃗ [t] > 0 ] < (T−t) 2k 2 . We conclude the proof with

i−1

δ

[t − 1, T] −

N j f

[t − 1]

+

≤

1 δk2√ ¯t log(¯t) ≤ λ i ¯t/2−1√ 2

T ∑ P [ H A ⃗ [t − 1] − H A ⃗ [t] > 0 ] t=2 T−t3  ≤ t 3 + ∑ P [ H A ⃗ [t − 1] − H A ⃗ [t] > 0 ] t=2

T−t 3 ∞ 2 2k 2k π ≤ t 3 + ∑ ≤ t 3 + ∑ = t 3 + 2k t=2 (T − t) 2 t=1 t 2 6

2

¯t log(¯t) ≤

~ N

f i

[t−1]/2−1,

giving a constant bound M2 

:= t3 

+ 2k 6 π as required.5 

4.5 Numerical results

Our numerical results consist of three parts. In the first part, we compare the optimal clairvoyant general solution and the optimal clairvoyant index solution for a few instances, i.e., we focus on the accepted customers rather than the objective. This serves to illustrate both that (i) index solutions are not optimal in general and (ii) as described in Lemma 8, asymptotically the clairvoyant general and the clairvoyant index policies look “similar”. Thereafter, in the second part, we focus on the relative performance gaps bounded in Theorem 10 and Lemma 6. Finally, in the third part we show how, for fixed B and T, the loss changes when we vary the parameters v i and p i . All figures from this section are included in the electronic companion of this paper.

5 Notice that different t 1 , t 2 may be needed to capture, through analogous arguments, the case where the online index policy rejects, rather than accepts, an arrival in period t.

115 Optimal solutions

We first observe that the clairvoyant optimal solution is not guaranteed to be an index solution in all settings, although it “switches” to an index policy as B scales up. This switching behavior can be intuitively explained by Lemma 8, which shows that, when i < j, accepting R ij /p i type i customers yields better objective than accepting R ij /p j types j customers does for some large constant R ij . Thus, when B and T are large, if R ij /p i type i customers are present, the clairvoyant general policy does not accept more than R ij /p j types j customers.

We capture this switching behavior in the example below, where we consider a single sample path based on the following parameters: k = 3, λ 1 = 0.3, λ 2 = 0.2, λ 3 = 0.5. Moreover, the values and no-show probabilities are v 1 = 0.044, v 2 = 0.1, v 3 = 0.06, p 1 = 0.2, p 2 = 0.5, p 3 = 0.3. We test for B ∈ { 1, ..., 15 } two settings, one in which demand is unconstrained (T is large), so any number of customers of each type can be accepted, and one in which T = 5B, so the number of customers accepted is constrained by both the capacity and the demand for each type. For each setting, we consider both the clairvoyant general and the clairvoyant index policy.

In the first setting, we observe a switch from type 2 customers to type 1 customers as B scales up. Figure C.1 shows this switch in the different types of customers accepted by the clairvoyant general policy. On the other hand, Figure C.2 shows that the clairvoyant index policy accepts only type 1 customers, since those have the highest critical ratio, and demand is unconstrained in this example.

The second setting captures a similar behavior when demand is constrained. In Figure C.3 we show both the demand and the accepted number of requests for each type, as we vary B. We observe that the clairvoyant general policy in Figure C.3 accepts more customers of type 2 and type 3 customers when B is small, while the clairvoyant index policy in Figure C.4, by definition, always accepts the types of customers in the order of their indices. As B grows larger, the clairvoyant general policy becomes more similar to an index policy, but sometimes, e.g., with B = 12, it still does not accept all arrivals of type 1 (in line with Lemma 8).

Performance loss of clairvoyant index policies

We next turn our attention to the performance loss of the clairvoyant index and the online index policy relative to the clairvoyant general policy. As our results show, both have uniformly bounded loss. We consider two experiments below, corresponding to the case with “switching” behavior (Experiment A) and the case without “switching” behavior (Experiment B). Throughout this part, we show results as a log-log plot, i.e., 1 minus the index policies’ objective divided by the objective of the clairvoyant general policy. On these plots, a slope of −1, i.e., relative loss scales asB 1 1/B, indicates a uniform loss guarantee. We include curves proportional to Θ( 1 B ) and Θ( ) to better visualize the different scalings. Further, given that √ finding the clairvoyant general solution is computationally expensive (even when knowing the arrivals) for a large time horizon, we only evaluate the loss relative to the general clairvoyant for T ≤ 250. However, since we find that the clairvoyant index solution seems to have (near-)zero loss anyway, we also include comparisons between the online index policy and the clairvoyant index policy over longer time-horizons.

In Experiment A we have the same parameters as in the first part. Figure C.5 displays the

116 relative loss of the two index policies for T ∈ { 25, 50, . . . , 250 } where B = T/5. We observe that the losses of the two policies are uniform as T and B scale up, i.e., the relative loss of the clairvoyant index policy decreases as 1/T (or even faster). We remark that the loss of the clairvoyant index solution is so small (indeed, zero after the “switch”, but positive before) that we need to artificially add a constant to it for it to appear on the log-log plot. In Figure C.6 we compare the clairvoyant index policy to the online index policy for a time horizon up

to T = 750.

In Experiment B we use a different set of parameters in which we have no switching behavior. We consider k = 3, λ 1 = 0.2, λ 2 = 0.3, λ 3 = 0.5, as well as v 1 = 0.6, v 2 = 0.4, v 3 = 0.3, p 1 = p 2 = p 3 = 0.8. Figure C.7 displays the relative loss. Without the switching behavior the clairvoyant index policy always incurs zero loss, so we add a constant to it for it to appear on the log-log plot. We evaluate both online and clairvoyant index policies for T ∈ { 15, 10, 15, . . . , 150 } , and B = T/3. In Figure C.8 we compare the clairvoyant index policy to the online index policy for a time horizon up to T = 900.

Varying parameters

Finally, we test how the loss bound changes with respect to the other parameters in our model. In Figure C.9 and C.10 we assume λ 1 = 0.2, λ 2 = 0.3, λ 3 = 0.5, B = 10, T = 20. Moreover, in Figure C.9 we let v 1 = p − 0.1, v 2 = p − 0.2, v 3 = p − 0.3, where p 1 = p 2 = p 3 = p for p ∈ [0.4, 0.9], and compute the absolute (not relative) loss of the index policies as a function of p. In Figure C.10, we instead assume v 1 = v 2 = v 3 = v and p 1 = v+0.1, p 2 = v+0.2, p 3 = v+0.3 for v ∈ [0.1, 0.6], so that we observe how the relative losses of index policies change with respect to the revenue per customer. While the experiments show varying loss for the online clairvoyant index policy as we change these parameters, it is always extremely small relative to the size of the budget and the overall objective for a maximum relative loss of about 1% when compared to the clairvoyant general policy.

4.6 Conclusion

In this work we developed a simple online algorithm for SRMNS with heterogeneous no-show probabilities. In contrast to previous results, that were only optimal on the fluid scale, our algorithm is the first that achieves a uniform loss guarantee. Our key technical innovation is the design of a set of policies, specifically ones based on index solutions, that (i) have bounded loss relative to the clairvoyant over the entire time horizon, and (ii) change in a tractable manner in each period. In doing so, we are able to leverage the novel compensated coupling technique of [122, 138] for a problem with overbooking.

Our results extend to capture customer requests with (i) product-dependent (heterogeneous) refunds for no-shows (see Appendix C.3.1), and (ii) different resource requirements (see Appendix C.3.2), or (iii) arrivals that are not iid. However, there are other ways in which we do not know how to extend our results. The most obvious among those would be to extend our results to a network problem with no-shows, i.e., one with different types of resources. In this case, one may be able to combine a decomposition approach with our technique for individual legs to obtain a uniform loss guarantee (potentially under a

117 non-degeneracy assumption à la [135]). Next, it would be interesting to extend our results to capture type-dependent compensation amounts. This complicates the problem, as it is then non-obvious that the clairvoyant general solution asymptotically resembles the clairvoyant index solution — however, again under some technical assumption, it may be possible to derive such a result.

Finally, the most well-studied extension would be to settings where there are cancellations in addition to no-shows; unfortunately, traditional models of cancellation do not seem to fit under the umbrella of compensated coupling techniques, as the objective is not only based on the action counts, i.e., how often were product requests of each type accepted, but also on the timing of those actions. Thus, this seems to be the least feasible extension of our techniques.

118 
# Chapter 5 On the Power of Delayed Flexibility

5.1 Introduction

A key question in operations is how to effectively address supply-demand imbalances in dynamic settings. When a decision-maker has access to different resources with which to satisfy demand, this question is often tackled through the lens of load balancing. The canonical model of load balancing is the balls-into-bins paradigm, in which balls (demand) are sequentially placed into bins (resources) according to an allocation scheme [159]. These models are used to understand how a decision-maker can maintain an approximately balanced load across bins over time, i.e., design policies that maintain an approximately equal number of balls in each bin throughout the decision-making horizon. In such settings, it has been established that a limited amount of flexibility goes a long way. Specifically, an algorithm that places each ball in the minimally loaded of two randomly chosen bins in each period ensures that the gap between the maximum and minimally loaded bins is independent of the number of thrown balls [160–162]. The power of these simple algorithms has been far-reaching, particularly in computing settings wherein (i) the decision-maker seeks to balance the load across throughout time, in order to minimize metrics such as average delay, and (ii) querying the load of all bins in each period can be costly.

This work is motivated by two important observations that apply to a number of load balancing settings. First, maintaining a balanced load across all resources over all time may be an unnecessarily stringent requirement. Instead, balance may only be required at the end of the decision-making horizon. Second, in many settings it is not the act of querying the loads of bins that is costly; rather, it is the act of placing of a ball (i.e., a demand unit) into a bin (i.e., a resource) that it was not destined for originally. Another way to view this is that each arriving ball has a preferred resource, and exerting flexibility by placing it in a lesser-preferred bin is costly to the decision-maker. Examples where this is the case include the following:

Online retail warehouse operations. In many e-commerce settings, the platform operator (e.g., Amazon) offers fulfillment services to third-party sellers [163]. Sellers bear the cost of shipping their goods (balls) into one of the warehouses operated by the platform (bins), and therefore prefer to send their shipments to the closest warehouse. The platform operator, on the other hand, maintains end-of-week shipment volume targets for each warehouse. These

119 fixed targets represent the ideal fraction of shipments each warehouse should receive to balance the load across the network, in line with pre-determined processing capacities and expected arrival volumes [164]. While these targets need not be respected throughout the week, it is important that they be respected approximately at the end of each week. In cases where the load across warehouses becomes so imbalanced that the operator may not achieve its targets, the platform operator can incentivize sellers to send their shipments to a different warehouse by compensating them for the difference in shipment costs.

Inventory management via opaque selling. Consider a retailer that sells a large number of a few different products (bins), and jointly restocks them all once the stock of any one product is depleted by customers (balls). For inventory costs to be minimized, the retailer wants all items to be close to depletion at the time restocking occurs; however, imbalances in remaining inventory do not affect the retailer’s supply costs at other points in time. In practice, to address these inventory imbalances many retailers offer opaque products to customers [32, 165]. These products give the retailer the right to choose which item is allocated to the customer (thereby giving the retailer more control over her inventory levels), at the cost of a discount (see Figure 5.1 for an example).

Within the context of the food industry, in recent years restaurants have partnered with online applications such as Too Good To Go to reduce food waste [166]. While restaurants can list any individual food item (bin) on these apps for purchase by a customer (ball), at the end of the day they begin offering heavily discounted surprise bags filled with surplus items, the content of which the customer has no control (see Figure 1 in [167] for an example ). These surprise bags allow restaurants to ensure that the remaining stock of food across all products is even by the end of the day; this however comes at the cost of a steep discount. Delivery windows in e-commerce fulfillment. Consider a setting in which customers living in the same zip code place orders on an e-commerce website. Each customer (ball) has a preferred delivery window (bin), but the e-commerce company prefers to have a similar number of orders associated with each delivery window, for efficiency purposes. If too many customers choose the same delivery window, the e-commerce company may choose to assign a lesser-loaded delivery window to customers placing orders closer to the delivery date. However, the company wants to do this as infrequently as possible, as it represents a costly inconvenience to the customer.

Dynamic workforce scheduling. In settings with flexible workforces (e.g., volunteers in nonprofit organizations [168], gig economy workers in online retail fulfillment [169]), workers (balls) may begin signing up for their preferred shifts (bins) well in advance of the shift date. As in the delivery window example, these organizations prefer to have a balanced supply of workers across shifts. Closer to the shift date, the organization may start to assign shifts to workers (or close off over-subscribed shifts). This however comes at the cost of a worse experiences for flexible workers, who assign a premium to the flexibility to choose their schedule.

While the style of load balancing algorithms described above would indeed achieve the desired balance across resources by the end of the horizon in all of these settings, the fact that these algorithms attempt to allocate a demand unit to a lesser-preferred resource in each period would come at a significant cost to the decision-maker. Moreover, this cost may be incurred unnecessarily, given that the decision-maker does not require balance throughout

120 the horizon. Against this backdrop, this work tackles the following questions:

What is the minimum amount of flexibility a decision-maker needs to exert to achieve end-of-horizon balance? Do there exist simple load balancing algorithms that achieve this lower bound?

5.1.1 Our Contributions

Late-stage flexibility in the canonical balls-into-bins model.

Toward answering this question, we first study the power of late-stage flexibility in the classical balls-into-bins model. We consider a discrete decision-making horizon of length T. In each period, a ball arrives; this ball has a preferred bin to which it wants to be allocated, drawn uniformly at random from N available bins. The ball is moreover flexible with known and constant probability. If the ball is flexible, the decision-maker may draw a subset of two bins uniformly at random and allocate the ball to the lesser-loaded of these two bins; we say that she exerts flexibility in this case. The decision-maker’s goal is to achieve approximate end-of-horizon balance — i.e., ensure that the expected gap between the maximum and average loads across all bins is a constant independent of T — in the minimum number of flexible throws.

We first establish a natural lower bound of Ω( √ T) on the minimum number of flexible actions required to achieve approximate balance, in expectation (Proposition 9). This intuitive result is a natural consequence of the Central Limit Theorem. In our first main contribution, we design a non-adaptive policy that starts exerting flexibility when Θ ( √ T log T ) periods remain in the time horizon. We prove that such a policy achieves approximate end-of-horizon balance, thereby achieving the lower bound up to a factor of Θ( √ log T) (Theorem 12). Importantly, the analysis of this policy is tight: we show that no policy that starts exerting flexibility at a deterministic point in time can close this gap to Θ( √ T) (Proposition 28). Motivated by this fact, we then design a semi-dynamic, “point-of-no-return” style policy that begins exerting flexibility the first time the maximum and average loads across bins exceeds a carefully designed time-varying threshold. This threshold is constructed to intuitively represent the expected number of opportunities remaining to rectify the current imbalance; if it is satisfied, this indicates that, unless flexibility is exerted immediately, approximate end-of-horizon balance may not be achieved, thereby justifying the use of a costly diversion. In our second main contribution, we demonstrate that this slightly more adaptive policy closes the gap of the non-adaptive policy: it achieves approximate balance in O( √ T) flex throws, in expectation (Theorems 13 and 14).

Our analysis of these algorithms is based on the following intuition: over the course of the entire time horizon, if the decision-maker never exerted flexibility, the imbalance between bins would scale as Θ √ T . If each time the decision-maker exerted flexibility that imbalance ( ) was reduced by 1, then she would only need to do so O √ T times in order to achieve ( ) approximate balance. The main issue with this intuition as a formal argument, however, is that though exerting flexibility always reduces the instantaneous imbalance among the bins, it does not always reduce the imbalance as measured in hindsight. To see this, consider the setting where N = 2. Consider moreover a sample path over which the decision-maker

121 decided to exert flexibility early on in the horizon by diverting a ball to bin 1, away from bin 2. If, later on in the horizon, more balls landed in bin 1 than in bin 2, exerting flexibility in this early period would have actually increased, rather than decreased, the imbalance at the end of the horizon. Proving that these “mistakes” are not too costly in hindsight is one of the main technical challenges overcome in the analysis of our two algorithms. This difficulty is further compounded in the analysis of our semi-dynamic policy, under which flexing begins at a random time. The key then is to show that the threshold defined for this policy is constructed carefully enough that the now-random number of rounds remaining suffices to control the accumulated imbalance across bins.

Application to inventory management via opaque selling.

We next leverage the algorithmic insights derived for the fundamental balls-into-bins model to address the more complex problem of designing dynamic opaque selling strategies for inventory management, a connection first made in [32]. In the model we consider, a retailer sells N horizontally differentiated products; customers are risk-neutral, and behave according to the Salop circle model [170]. The retailer sets a single price for each “traditional” product, sold individually; she may also offer the opaque product at a discount. In addition to the revenue generated from sales, the retailer incurs holding and replenishment costs associated with her inventory decisions.

While opaque selling has been an active area of research in operations in recent years, its appeal has been rooted in its ability to act as a market segment strategy, thereby generating higher revenues under certain behavioral models [171]. Our main insight here is that there exist a variety of horizontally differentiated settings for which there exists no revenue benefit from offering an opaque product; rather, the only benefit of opaque selling is in inventory cost savings due to the additional control the retailer has over which products she allocates to customers. This clear trade-off between the revenue loss due to opaque discounts and the resulting inventory cost savings then motivates the design of late-stage opaque selling policies that achieve a better revenue-inventory cost trade-off than a naive policy that offers the opaque product in each period. Indeed, in our main contribution for this section, we show that the semi-dynamic policy designed for the canonical balls-into-bins model achieves the optimal revenue-inventory cost trade-off in a large-inventory regime parameterized by a base-stock inventory level S: it achieves a revenue loss of O 1 S relative to the revenue( √ ) optimal policy that never offers the opaque discount, all the while incurring the minimum possible inventory costs of any opaque selling policy (Theorem 15). These results moreover imply that, from a profit perspective, late-stage opaque selling (i) always outperforms naive opaque selling, and (ii) is beneficial relative to traditional selling when inventory costs are substantial (Proposition 14).

From a technical perspective, the challenge presented by the opaque selling setting is that the effective “end-of-horizon” in this case corresponds to the time to replenishment, which is random and endogenous to the opaque selling policy. The introduction of this moving target then requires tighter probabilistic bounds on the first time that a product’s inventory is depleted, as compared to the bounds on imbalance of the system in the balls-into-bins model, which only are required to hold in expectation.

Finally, we demonstrate the robustness of our insights via extensive computational

122 (a) Opaque stapler sold on Amazon.com

(b) Opaque calf sleeves sold by PRO Compression

Figure 5.1: Examples of opaque selling in retailing platforms

experiments for a wide variety of choice models (including heterogeneous preferences across products, and risk-seeking / risk-averse behaviors relating to the opaque product). Our results illustrate that even when there are revenue gains to be made by opaque selling (and as a result, exerting flexibility is not as costly), late-stage opaque selling remain attractive, outperforming both traditional selling and “always-flexible” opaque selling policies.

5.1.2 Related work

Our work relates to three separate streams of literature: studies of balls-into-bins processes, literature studying the revenue and inventory implications of opaque selling practices, and more generally, the value of flexibility in operations. We survey the most closely related papers for each of these lines of work below.

Balls-into-bins processes. The balls-into-bins model represents one of the most fundamental models in applied probability. This paradigm gained traction early on as being well-suited for a variety of computing applications, such hashing, shared memory emulation, dynamic task assignment to servers, and virtual circuit routing [159]. We refer the reader to [159] for an exhaustive survey on this line of work, focusing our discussion on the most closely related technical results.

[172] analyze a basic model where m balls are sequentially and randomly assigned to n bins, and derive high-probability upper and lower bounds on the maximum load across bins,

. ( √ ) For the special case where m = n, [160] and [161] established the celebrated power of two choices, showing that the load balancing strategy that allocates each ball to the lesser-loaded of two randomly chosen bins yields an exponential decrease in the maximum load across all bins. [162] later generalized these results to the case where m ≫ n; they showed that if a ball is assigned to a random bin with probability q ∈ (0, 1], and to the lesser-loaded of two random bins with probability 1 − q, the expected gap is a constant independent of m (though dependent on n).

showing that the gap between the most-loaded bin and the average load is Θ

m log n n

At a high level, the underlying motivation behind the power of two choices framework is the idea that load balancing is costly in many applications, due to the diversion of jobs to

123 lesser-preferred resources. Our contribution to this line of work is to push this idea to its limit, by showing that to achieve an approximately balanced load at the end of the horizon, not only does it suffice for a decision-maker to load balance with two (as opposed to n) bins; the decision-maker need only do so a vanishingly small fraction of the time, at the very end of the horizon. In this sense, our work can be viewed as even further evidence of the power of two choices in balls-into-bins processes.

On the power of flexibility in opaque selling. The practice of offering opaque products has been widely studied in the operations literature. From a revenue perspective, opaque selling offers two key benefits: (i) it can boost overall demand, and (ii) it enables better capacity utilization when demand and supply are misaligned [173]. Much of the focus on opaque selling has been on its ability to effectively price discriminate between customers with different willingnesses-to-pay, thereby generating gains in revenue [171, 174–176]. The majority of these latter works focus on uncapacitated settings with horizontally differentiated products, with customers behaving according to the Hotelling or Salop circle models, as is the case in our model. [4] extend this line of work by identifying conditions under which opaque selling outperforms both discriminatory and uniform pricing for exchangeable valuation distributions. More recently, [177] study pricing and assortment optimization with opaque products under MNL choice.

Relative to this literature, our contribution is to show that even in settings where there are little to no revenue gains from opaque selling, this remains an appealing practice due to the inventory cost savings resulting from the retailer having the power to choose which good to allocate to the customer. A number of prior works have studied the inventory management aspect of opaque selling. For instance, [178] analyze a model wherein a retailer sells two products over a finite selling period, in addition to an opaque product. They propose a dynamic programming approach to compute the optimal opaque selling decision at each state, and moreover illustrate the positive effects of inventory pooling in their setting. [179] study a stylized model wherein the retailer selling two goods needs to time the opaque selling decision before or after observing demand, in addition to deciding how much of each good to order. More recently, [180] study a retailer’s finite-horizon dynamic pricing problem in the presence of opaque products. Less closely related to our work is [181], who propose a stylized, game-theoretic model of a retailer offering two vertically differentiated products over two periods, and using opaque selling as an inventory-clearance strategy in the second period. The goal of the retailer is to set optimal prices and inventory levels when customers strategically time their purchases.

We highlight two works upon which our work builds: [165] and [32]. In the model considered by [165], a retailer sells two products over an infinite horizon, with inventory dynamics as in our setting (and, in particular, in a large-market regime parameterized by order-up-to-level S). The authors show that when demand is symmetric across both products,

the inventory cost savings are on the order of Ω

(

1

√

S

as long as the per-period opaque )

. When demand follows a Hotelling model, they demonstrate ( √ S ) the existence of an opaque discount that induces q ∈ Θ 1 S and yields a revenue loss on ( √ ) 1 the order of O ( S ) . Since N = 2 is a special case of our setting, our work adds to their result by proposing an adaptive opaque selling policy with the same guarantees. [32] later extended

purchase probability q ∈ Ω

1

124 this first work by considering N ≥ 2 horizontally differentiated products. Focusing only on the inventory management problem in this case, they leverage an elegant connection to the balls-into-bins model to show that opaque selling yields relative cost savings of Θ 1 S when ( √ ) q ∈ Ω 1 , for > 0. They introduce revenue considerations in numerical experiments, δ ( √S 1−δ ) exhibiting a number of demand models under which opaque selling yields strong profit gains relative to traditional selling. 1 We bridge the theoretical gap between [165] and [32] by showing that even for demand models for which opaque selling yields no revenue gains, late-stage opaque selling strategies generate the same inventory savings as those that offer the opaque product in each period, all the while losing a limited amount in revenue due to opaque discounts.

General flexible processes. Finally, we note that the power of flexibility has been extensively studied in operations applications such as manufacturing [2], queuing systems [26, 183], workforce cross-training [15], bin packing [184], and warehouse operations [164]; all of these works demonstrate that a small amount of supply-side flexibility suffices to realize most of the benefits of full flexibility. We refer the reader to [185] for an excellent survey of more recent results on the power of flexibility in operations.

Moreover, our opaque selling contribution relates to broader research on how demand-side flexibility can improve supply utilization and reduce costs. For instance, [33] and [30] show that time-flexible demand improves utilization in scheduled services and ride-hailing, respectively. Relatedly, in the resource allocation setting, [186] show the value of demand flexibility when both time-flexible and time-inflexible customers seek a service with periodic replenishments. [187] study a flexible version of the classical network revenue management problem, where the service provider chooses which combination of resources to allocate to each customer. Finally, the trade-off between demand-side flexibility and cost minimization also relates to fairness-efficiency trade-offs that have been studied in various operational settings of late [188, 189].

5.2 Preliminaries

In this section we present the classical balls-into-bins model [162, 190]. exposition, we defer a description of the opaque selling model to Section 5.4.

The balls-into-bins process.

For clarity of

The vanilla balls-into-bins model evolves over a discrete, finite-time horizon in which T balls are sequentially allocated into N ≥ 2 bins. At the beginning of each period t ∈ { 1, 2, . . . , T } , a ball arrives; the ball has a preferred bin, drawn uniformly at random from { 1, 2, . . . , N } and denoted by P(t). In addition to this, the ball is a flexible, or flex, ball with probability q ∈ (0, 1]. We let f(t) = 1 be the indicator variable denoting whether the ball is flexible, with f(t) = 1 if it is, and f(t) = 0 otherwise. If the ball is not flexible, the decision-maker places it in its preferred bin. If it is flexible, on the other hand, the decision-maker has more control

1 These findings were later echoed in [182], who extend their results to non-uniform demand across products.

125 over the bin to which the ball will be allocated. In particular, the decision-maker may choose to draw a random subset of two bins, and may place the ball in any of these two random bins. We refer to this random subset of bins as the flex set, denoted by F(t), and refer to the act of choosing the bin amongst which to allocate the ball as exerting flexibility, or exercising a flex throw. If the decision-maker chooses not to exert flexibility, the ball is placed in its preferred bin. In this latter case, or if the ball is not a flex ball, we write F(t) = ϕ . For t ∈ { 1, 2, . . . , T } we let θ(t)= ( f(t), P(t), F(t) ) , and define the history of balls at time t to be σ(t) = (θ(1), . . . , θ(t − 1)). Finally, let Σ(t) be the set of all possible histories at time t.

Objective.

Let π denote a policy that maps the number of balls in each bin to the decision to exert flexibility, denoted by ω π (t) (with ω π (t) = 1 if exercised, and 0 otherwise). For i ∈ [N], we use x i π (t) to denote the number of balls in bin i at the end of period t under policy π, and henceforth refer to this quantity as the load of bin i. Unless otherwise specified, we assume that, if a ball is flexible, the decision-maker always places it in the bin with the smallest load in its flex set. Formally, letting A π (t) denote the bin to which the t-th ball is allocated, we have:

arg min j ∈F (t) x j π (t) A π (t) = { P(t)

if f(t)ω π (t) = 1,

if f(t)ω π (t) = 0,

where we define the arg min with a lexicographic tie-breaking rule that returns the smallest value i of all bins with the smallest number of balls. Finally, we let M π denote the number of times that the decision-maker chooses the bin that a flex ball goes into, i.e., M π = ∑ t=1 T f(t)ω π (t). The decision-maker’s goal is to ensure that the load across bins (i.e., the number of balls in each bin) is approximately balanced at the end of the time horizon, all the while minimally exerting flexibility. To formalize this two-fold objective, we define the gap of the system at the beginning of period t under π as the difference between the maximum load across all bins and the average load after the t-th ball arrives, given by t/N. Letting Gap π (t) denote this gap, we formally have:

t Gap π (t) = max x i π (t) − ∀ t ∈ { 1, 2, . . . , T } . i ∈ [N] N

We say that the system is approximately balanced under π if E [ Gap π (T) ] ∈ O(1), where the Big-O notation is with respect to the time horizon T.

In order to formalize the desideratum of achieving approximate balance in a minimal number of flex throws, we present two simple policies that have previously been analyzed in the literature. Consider first the no-flex policy, denoted by superscript nf, that never exerts flexibility (i.e., M nf = 0 almost surely). It is known that under this policy, the load

across bins is imbalanced by the end of the horizon, with E [ Gap nf ] ∈ Θ √ T [172]. On the ( ) other hand, the always-flex policy, denoted by superscript a, always exerts flexibility, letting ω a (t) = 1 for all t ∈ { 1, 2, . . . , T } . Such a policy has been shown to achieve an approximately balanced load at the end of the horizon, with E [Gap a ] ∈ O(1) in E [M a ] = Tq ∈ Θ(T) flex throws in expectation [162]. Given these benchmarks, our goal will be to design policies that

126 achieve two desiderata: (i) ensuring the load is balanced at the end of the horizon, with E[Gap π (T)] ∈ O(1), and (ii) doing this with o(T) flexes, in expectation.

Discussion of modeling assumptions.

We conclude this section with a discussion of the modeling assumptions upon which the classical balls-into-bins model relies. Specifically, the model we consider here is most appropriate for settings endowed with the following features: (i) demand for resources is approximately homogeneous, and (ii) the cost of diverting a demand unit from its preferred resource is approximately the same across all lesser-preferred resources (otherwise, the number of flexes M π ceases to be a meaningful metric of costly flexibility). The first assumption is not critical to our results; namely, at the end of Section 5.3 we discuss how our results easily extend to settings in which demand is non-uniform across resources. It therefore remains to justify the assumption of uniform costly diversion. We highlight instances of the examples provided in Section 5.1 for which this assumption is well-justified below.

For the warehouse operations example, this model is most appropriate for “regionalized” networks that have ex-ante been partitioned into warehouses within the same geographic region [191]. For these smaller regions, it is sensible to assume that sellers’ shipping costs do not vary wildly across warehouses that are at a slightly further distance. For the opaque selling examples, the uniform cost of diversion follows from the practice of offering a discount for the opaque product. Finally, within the context of delivery windows and dynamic workforce scheduling, one can assume that the decision-maker partitions windows / shifts according ex-ante (e.g., according to peak and non-peak hours). As in the regionalization example, for all intents and purposes these partitions form different load balancing systems, and diversions within these systems are similarly inconvenient to customers / workers.

We underscore that the trade-off between balance and flexibility we consider in this work can be tackled by formulating an appropriate stochastic optimization problem tailored to each of the aforementioned applications. However, the popularity of the balls-into-bins model lies in its generality, and the fact that it is able to parsimoniously capture this fundamental trade-off. We will see that this parsimony gives rise to intuitive and easy-to-implement algorithms, a further testament to the power of the balls-into-bins paradigm.

Technical notations.

Throughout the paper we use Ber(p) to denote a Bernoulli random variable with probability p, B(n, p) to denote a Binomial random variable with probability p and n trials, and U(a, b) to denote a uniform random variable with support [a, b]. Finally, Φ(·) denotes the CDF of the standard normal distribution N (0, 1).

5.3 Optimality of Late-Stage Flexing for Balls-into-Bins

In this section, we tackle the task of designing policies that achieve the two desiderata described above. We first study the question of how many flex throws are required to achieve approximate balance at the end of the horizon in order to build intuition as to the structure of optimal policies. We leverage this lower bound to design an approximately optimal policy

127 that balances the system up to a factor of Θ( √ log T) of the minimum number of flexes. We then use the analysis of this policy to derive a simple optimal policy that closes this gap.

5.3.1 Warm-Up: Approximate Optimality of Non-Adaptive LateStage Flexing

Proposition 9 below establishes that, in order to achieve an approximately balanced load, a policy must exert flexibility Ω( √ T) times, in expectation.

Proposition 9. Consider any policy π such that E [ Gap π (T) ] ∈ O(1). Then, E [M π ] ∈

Ω √ T . ( )

This lower bound is quite intuitive: every time the decision-maker exerts flexibility, the gap at time T decreases by at most 1. Since the expected gap when balls are randomly thrown into the bins is well-known to scale as Θ T , closing this gap to would require the O(1) √ ( ) decision-maker to exert flexibility at least Θ √ T times. We defer a full proof to Appendix ( ) D.1.2.

We next design two policies that strive to achieve this lower bound. Both leverage the fact that, without any flexing, the load in each bin at the end of the time horizon is, with high probability, within Θ √ T of the expected load T/N. Thus, it should suffice to begin ( ) ~ exercising the flex option with O T periods remaining. Thus motivated, the first policy √ ( ) we consider, referred to as the static policy π s , is non-adaptive, and starts exerting flexibility ⌃ when Θ ( √ T log T ) periods remain. Specifically, π s fixes a time T = ⌊ T − a s √ T log T ⌋ , where ⌃ a s > 0 is a constant tuning parameter. This simple policy exerts flexibility for all t ≥ T (i.e., it places flex balls in the minimally loaded bin within the flex set), but not before. Throughout the section, we use superscript s to refer to all quantities induced by this static policy.

Theorem 12 establishes that the intuition underlying the design of this naive policy is correct: exerting flexibility Θ( √ T log T) times suffices to achieve a balanced load by the end of the horizon.

Theorem 12. For any constant as  O (1) .

N 2 √ 2 ( 2 ) ≥ q

, the static policy π s achieves E [ Gap s (T) ] ∈

We will build on the analysis of the static policy to analyze the optimal semi-dynamic policy in Section 5.3.2. Hence, we provide a detailed proof sketch below, deferring a complete proof of Theorem 12 to Appendix D.1.3.

Proof sketch. The sample paths where Gap s (T) > 0 can be partitioned into two events: (i) the event E 1 , under which the maximally and minimally loaded bins in period T never ⌃ had the same load between T and T, and (ii) the event E 2 , under which these two bins had ⌃ the same load at some “intersection time” τ ∈ { T, . . . , T − 1 } . Noting that the gap of the system can trivially be bounded by T under event E 1 , and by T − τ under event E 2 (which

128 would occur if all T − τ balls when into the maximally loaded bin between τ + 1 and T), we obtain the following bound on E[Gap s (T)]:

E[Gap s (T)] ≤ TP(E 1 ) + E [ T − τ | E 2 ] P(E 2 ).

(5.1)

+ e−Ω(T−  , and ( ) (ii) given the last intersection time τ, P(E 2 | τ) ∈ e −Ω(T−τ) . To prove each of these two facts, we let i and j respectively denote the maximally and minimally loaded bins at time T.

The key steps of the proof then lie in showing that (i) P(E 1 ) ∈ O

⌃−1  T

⌃ T)

⌃ By definition, x i s (t) > x j s (t) for all t ∈ { T, . . . , T } under event E 1 . Intuitively, E 1 would ⌃ occur if the flex balls thrown into bin j between T + 1 and T do not sufficiently correct the imbalances created by the random balls thrown into bin i throughout the entire time horizon. We formalize this intuition via a union bound over two bad events: (i) that the number of random balls thrown into bin i over all T periods exceeds those thrown into bin j j ⌃ ⌃ by 2 q T), where q T) represents the expected number of times { i, j } is chosen

(T − (T ( N ) ( N ) 2 2 ⌃ as the flex set, and (ii) that the number of flex balls allocated to bin j between T + 1 and T, ⌃ ⌃ denoted by Y (T − T), exceeds the number of flex balls allocated to bin i between T + 1 and ⌃ ⌃ T, denoted by Y i (T − T), by no more than 2 q T). (T ( N ) 2

Noting that the number of random balls allocated to bins i and j are binomially distributed, the bound on the former event follows from a standard application of Hoeffding’s inequality. ⌃ ⌃−1  Using the fact that T − T ≥ a √ T log T, this gives rise to the O( T ) term in (i), for large enough a s . The main challenges lies in bounding the second event, due to the state-dependent nature of our allocation rule. In particular, characterizing the excess of flex balls placed into bin j over bin i requires not only keeping track of the loads of these two bins, but also the loads of all other bins with which j and i could have been included in a flex set. Keeping track of the loads of these other bins is important, given that bin i may have a smaller load than some bin k ∈ ̸ { i, j } at some point in the flexing horizon, in which case the policy would place a flex ball in bin i and have further contributed to the imbalance between i and j.

We overcome this challenge by showing that, under event E 1 , our policy makes the same decisions as a “lazy” allocation rule that is biased toward bin j, and is conceptually easier to analyze. For this policy, we show that the difference between the number of flex balls allocated to bin j and those allocated to bin i form a submartingale, since the lazy allocation rule is biased toward bin j. This then allows us to leverage Azuma-Hoeffding’s inequality ⌃ ⌃ ⌃ to show that the probability that Y j (T − T) − Y i (T − T) ≤ 2 q T) is exponentially (T ( N ) 2 ⌃ decreasing in T − T.

The exponential bound on P(E 2 | τ) follows similar lines. The key difference is that, given ⌃ that the loads of bins i and j intersected in some period τ ≥ T, any imbalance between bins i and j would be caused by the random balls thrown between τ + 1 and T, as opposed to all random balls thrown throughout the horizon, as was the case above. A Hoeffding’s bound over this source of imbalance yields a term that is exponentially decreasing it T − τ. We then similarly leverage the “lazy” allocation rule to show that the probability that the imbalance caused by incorrect flex throws is linear in T − τ is also exponentially decreasing in T − τ. Applying the bounds on P(E 1 ) and P(E 2 | τ) to (5.1), we obtain the theorem.

129 5.3.2 Optimality of a Semi-Dynamic Threshold Policy

Notice that our static policy does not exactly meet the lower bound from Proposition 9 due to the additional O ( √ log T ) factor in the number of flexes. This is not an artifact of our analysis, nor is it due to our definition of a s . Instead, it is a general fact about non-adaptive policies: we show in Appendix D.1.2 that no non-adaptive policy can achieve O(1) gap at

T while exerting flexibility O √ T times. At a high level, this follows from the fact that ( ) static policies ignore that not all sample paths are created equal: while the loads under certain sample paths require a larger number of flexes to achieve balance, on others, a smaller number of flexes suffices. This naturally leads us to the idea that, while no static policy can achieve an approximately balanced load with O √ T flexes, it may be that an adaptive policy can. ( ) Thus motivated, we consider an adaptive modification of our static policy, referred to as the semi-dynamic policy π d , which begins flexing the first time the gap of the system exceeds a pre-specified threshold, and keeps flexing from then onwards. Specifically, the threshold (also referred to as the flexing) condition that our policy verifies is given by:

ad  (T − t)q Gap d (t) ≥ , N

(5.2)

where the superscript d is used for all quantities induced by the semi-dynamic policy, and : a d ∈ (0, 1] is a constant tuning parameter. We let T ⋆ = inf (t) ≥ a d (T−t)q t Gapd  be the { N } period in which the flexing condition is triggered; that is, the first period in which the semi-dynamic policy flexes is T ⋆ + 1. We provide a complete description of the semi-dynamic policy in Algorithm 2.

The threshold condition specified in Equation (5.2) can be interpreted as verifying whether the system has attained a “point of no return,” at each time t. Namely, the quantity a d (T−t)q N represents, for any bin i, a lower bound on the number of remaining opportunities to flex a ball that prefers i into another bin. If the gap of the system exceeds this estimate, since exerting a flex throw in any given period reduces the gap of the system by at most one, the semi-dynamic policy assumes that the only way it can balance the system by the end of the horizon is if it starts load balancing immediately. Having established that it is at a point of no return, our policy flexes from then onwards. Figure 5.2 illustrates the difference between the times at which the static and semi-dynamic policies begin flexing for two sample paths, and gives intuition as to the challenge in analyzing the random time at which the semi-dynamic policy begins flexing. In particular, while we observe in Figure 5.2b over ⌃ ⌃ some sample paths it indeed avoids unnecessary flexing, with T ⋆ > T if the gap at T is low, ⌃ Figure 5.2a also illustrates that it may begin flexing well before T. The main concern would then be that the threshold condition chosen in Equation (5.2) was chosen too conservatively, resulting in early starts happening more frequently than late starts, as depicted in Figure 5.2. Theorem 13 below establishes that our threshold condition in fact guarantees that late starts occur frequently enough, and moreover are within O( √ T) of the end of the horizon, in expectation.

Theorem 13. For any constant a d ∈ (0, 1], the semi-dynamic policy flexes O( √ T) times in expectation, i.e., E [ M d ] ∈ O √ T . ( )

130 Algorithm 2 Semi-Dynamic Policy π d

Initialize: x i d (0) = 0 ∀ i ∈ [N], ω(t) = 0 ∀ t, constant a d > 0 1: for t ∈ [T] do

2: 3: 4: 5: 6: 7: 8:

if

ω(t)f(t)

=

1

then

Sample flex set F(t).

Allocate ball to least-loaded bin in F(t), i.e., set A d (t) = arg min i ∈F (t) x i d (t − 1). else Allocate ball to preferred bin, i.e., set A d (t) = P(t).

end if

for

i

∈

[N]

do

Update load of each bin:

x i d (t − 1) + 1 x i d (t) = d { x i (t − 1)

if i = A d (t)

otherwise.

9: end for ad  (T−t)q 10: if Gap d (t) ≥ N then 11: Exercise the flex option from t + 1 onwards, i.e., set ω(t ′ ) = 1 ∀ t ′ > t. 12: end if 13: end for

To prove Theorem 13, we use the threshold condition to show that bounding E[T − T ⋆ ] reduces to obtaining tight bounds on the gap of the never-flex at any time t. We provide a proof sketch of our approach below, deferring a complete proof to Appendix D.1.4.

Proof sketch.

Algebraic arguments yield the following useful bound on E[T − T ⋆ ]:

⌈ √ T ⌉ E[T − T ⋆ ] ≤ √ T ∑ P(T − T ⋆ ≥ (k − 1) √ T). k=1

(5.3)

Namely, it suffices to show that the probability T − T ⋆ exceeds (k − 1) √ T, for some k ∈ { 1, . . . , ⌈ √ T ⌉} , is upper bounded by a constant.

ad  (k−1) √ Tq Since the threshold condition is satisfied at T ⋆ ≥ (k−1), T−T ⋆ √ T implies Gap d (T ⋆ ) ≥ N Noting that Gap d (t) = Gap nf (t) for all t ≤ T ⋆ , since the policy only begins flexing after T⋆ 

by construction, it then suffices to bound P (T ⋆ ) ≥ c(k − 1) √ T ⋆ q/N. Gapnf  , where c = ad  ( ) The result then follows by applying the Berry-Esseen theorem to bound the load of each bin under the no-flex policy, for all k ∈ { 1, . . . , ⌈ √ T ⌉} , allowing us to bound the probability of interest by the tail of a standard normal distribution. Summing over all k completes the proof of the result.

It remains to argue that beginning to exert flexibility only when absolutely necessary suffices to recoup the imbalance accumulated before T ⋆ . Theorem 14 establishes this fact below.

1

[ Gapd 

(T) ] ∈ O(1).

Theorem 14. For any ad 

, the semi-dynamic policy achieves E 5 ( N ) 2

≤

ad  ≥

(k−1 N

131 40

30

20

10

0

π s π d

40

30

20

10

0

0

2000

4000

6000

8000

10000

0

2000

4000

6000

8000 10000

t

t

⌃ T

⌃ T

(a) Early start: T ⋆ <

(b) Late start: T ⋆ >

Figure 5.2: Gap(t) versus t, under the static and semi-dynamic policies, for N = 3, q = 1,

a s = 2 √ 2 ( N 2 ) , a d = 5 1 . ( N ) 2

We defer the formal proof of Theorem 14 to Appendix D.1.4, and provide a proof sketch below.

Proof sketch. The proof follows similar lines as that of Theorem 12. Namely, we analyze the gap under events: (i) the event E 1 , under which the maximally and minimally loaded bins in period T, respectively denoted by i and j, never had the same load between T ⋆ and T, and (ii) the event E 2 , under which these two bins had the same load for some τ ∈ { T ⋆ , . . . , T − 1 } . We then have the following bound on E[Gap d (T)]:

E (T) (T) | E 1 ) + E [ T − τ | E 2 ] P(E 2 ). Gapd  ≤ E Gap d P(E1  [ ] [ ]

While our analysis of the second term is identical to that of the static policy, with the likelihood that E 2 occurs being exponentially decreasing in T − τ, the main challenge in this setting is bounding the first term, since the time at which the semi-dynamic policy begins flexing is random, with no explicit characterization. We tackle this obstacle by leveraging the threshold condition to first upper bound Gap d (T). In particular, we use the fact that Gap d (T) ≤ Gap d (T ⋆ − 1) + 1 + T − T ⋆ , since no more than T − T ⋆ + 1 balls can go into any ⋆ bin between T ⋆ and T. Moreover, it must be that Gap d (T ⋆ − 1) < a d (T−T +1)q , by definition N of T ⋆ . Putting these two facts together, we have that Gap d (T) ≤ (1 + T − T ⋆ ) ( 1 + a N d q ) . Not only is this fact useful to bound the expected gap at time T, given E 1 , but it will also be useful to bound the likelihood that E 1 occurs.

To bound this latter probability, we use the threshold condition to observe that E 1 occurs if the total number of balls that land in bin j during the flexing horizon cannot correct an already accumulated imbalance of a d q(T − T ⋆ ) + a with respect to bin i, for some constant a > 0. We bound this via two “bad” events: (i) that the number of random balls thrown into bin i during the flexing horizon exceeds those thrown into bin j by a d q(T − T ⋆ ) + a, and (ii) the number of flexible balls thrown into bin j exceeds those thrown into bin i by no more than 2a d q(T − T ⋆ ) + a.

As before, the analysis of the random throws is a simple application of Hoeffding’s inequality. To analyze the flexible throws, we rely on the useful “lazy” allocation rule from the

Gap(t)

Gap(t)

132 proof of Theorem 12, and show that there exists a constant t 0 > 0 for which the probability that event (ii) occurs is exponentially decreasing in T − T ⋆ , as long as T − T ⋆ ≥ t 0 , for small enough a d > 0. For values of T ⋆ such that T − T ⋆ < t 0 , Gap d (T) is trivially upper bounded by a constant, thereby completing the proof of the theorem.

Remark 1. In order to illustrate the fundamental insights of the power of late-stage flexibility, for simplicity we focus on the setting where the preferred bin of each arriving ball is drawn uniformly at random (i.e., with probability 1/N). This models settings where, e.g., resources preferences or requirements are homogeneous. With that said, our algorithms and analyses easily extend to the heterogeneous setting, wherein each random ball is placed into bin i ∈ [N] with constant probability p i ∈ (0, 1). In this setting, the appropriate notion of balance is one in which each bin i receives exactly Tp i balls by the end of the horizon 2 Then, in order to map this setting to the homogeneous setting, we would define the normalized load of a bin xi π  (t) under any policy π to be ¯x i π (t) = Np i , and the gap of the system under this policy to be π Gap (t) = max i ∈ [N] ¯x i π (t) − N t . (Note that by letting p i = 1/N for all i ∈ [N], we exactly π recover that ¯x i π (t) = x i π (t) and Gap (t) = Gap π (t) in the homogeneous setting.) We can moreover adapt our semi-dynamic policy by placing any flexible ball into a randomly chosen π bin with the smallest normalized load, and let the threshold condition be Gap (t) ≥ ¯a d (T−t)q N for an appropriately defined tuning parameter ¯a d depending on (p 1 , . . . , p N ). Leveraging our analysis for the homogeneous setting, it is easy to show that for heterogeneous p i all results would continue to hold. We omit this analysis for brevity.

5.4 Application: Late-Stage Opaque Selling for Inventory Management

In this section we extend the insights derived in Section 5.3 to the problem of inventory control. In particular, recent work leveraged the balls-into-bins paradigm to identify potential inventory benefits from retailers offering opaque products to their customers [32, 165]. In settings where opaque selling also improves a retailer’s revenue through price discrimination, offering opaque products is a no-brainer. In this section, however, we show that there exist a number of settings in which opaque selling may on the contrary be detrimental to a retailer from a revenue perspective. We use this as motivation to build upon our contributions for the balls-into-bins model to design simple opaque selling strategies that yield strong savings in inventory costs, all the while losing a small amount in revenue.

5.4.1 Basic Setup

Choice model.

We consider a retailer offering N ≥ 2 horizontally differentiated (also referred to as homogeneous) product types to customers over an infinite horizon. For instance, these products

2 This models the practical reality that, in settings where certain resources are known to be much preferred over others, their capacities are scaled in accordance to the demand that they are expected to receive. For instance, within the context of .

133 Figure 5.3: Illustration of the Salop Circle Model. A customer with X = 4N 3 will always purchase product i = 1 at revenue-maximizing price pˆ. Moreover, she will purchase the 1 opaque option for any δ ≥ γ 4 ( 1 − N ) .

may differ in color or style but are not inherently quality-differentiated (e.g., differently colored staplers or socks, as in Figure 5.1). A customer arrives in each period and evaluates the products offered to her by the retailer. Generalizing the Hotelling model considered in [165], we assume that customers value all products according to the Salop circle model [170], a standard framework for modeling customer choice amongst horizontally differentiated products. Specifically, each product i ∈ [N − 1] is defined by a numerical characteristic x i = i/N; we use the convention that x N = 0 for the Nth product. Each arriving customer has (i) a deterministic baseline value for obtaining any product, denoted by ¯v, and (ii) an idiosyncratic preferred product characteristic X ∼ U[0, 1]. Her valuation for product i ∈ [N] is then given by V i = ¯v − γ · d(X, x i ), where d(X, x i ) = min { | X − x i | , 1 − | X − x i | } denotes the arc distance between the customer’s preferred product characteristic and that of product i and γ ∈ [0, ¯v · N] is a known constant. 3 Given that products are homogeneous, we assume the retailer sets a single revenue-maximizing price pˆ for each individual product i ∈ [N]; we derive pˆ later on in Proposition 10. Finally, without loss of generality we assume that the marginal cost of selling each unit is zero.4 

Beyond selling the products individually, the retailer may offer an opaque product (also referred to as an opaque option) to customers, as shown in Figure 5.1. The opaque product gives the retailer the freedom to allocate any of the N products to the customer; in exchange for this uncertainty (in particular, the likelihood that they may receive a product whose characteristics are far from their preferred characteristics), customers purchase the product at a discounted price. Let p o = pˆ − δ denote the price of the opaque option, where δ ∈ (0, pˆ] is chosen by the retailer. We assume customers are risk-neutral, as in [165, 171, 174, 175,

3 The upper bound on γ ensures that v − γ /N ≥ 0, i.e., the products are sufficiently attractive that a customer may be incentivized to purchase at least one non-preferred product. [165] similarly make such an assumption on the corresponding Hotelling model, for N = 2.

4 This assumption is without loss of generality for our theoretical results, as we will see that customers purchase any product with probability one in this setting. While marginal costs may impact the effectiveness of our policies when the demand lift from the opaque discount also increases production costs, in our numerical experiments we find that our insights continue to hold for a wide variety of choice models.

134 179, 192], and that they value the opaque option as the average of all non-opaque products. Formally, letting V o denote a customer’s random valuation for the opaque product, we have 1 V o = N ∑ i=0 N−1 V i . 5

In the absence of the opaque option, customers purchase a product that maximizes their utility, given by V i − pˆ for i ∈ [N], breaking ties lexicographically. If all products generate negative utility for the customer, she purchases nothing. Since ¯v, γ , and pˆ are common to all products, this is equivalent to each customer choosing the the product whose characteristics are closest to her preferred characteristics (i.e., the product that minimizes the arc-distance d(X, x i )). In the presence of the opaque product, the customer compares the utility generated by each individual product to that of the opaque option, given by V o − p o . If V o − p o > max i ∈ [N] V i − pˆ ≥ 0, the customer purchases the opaque option. We illustrate the purchase decision for a customer with preferred product characteristic X = 4N 3 in Figure 5.3.

Finally, for expositional simplicity, we assume N is even in the remainder of this work. This restriction is due to the fact that the revenue-maximizing price under the Salop model differs based on whether or not N is even. All of our analysis and insights go through with N odd.

Inventory model.

In addition to the revenue generated from product sales, the retailer incurs costs for managing product inventories. Specifically, in each period, the retailer incurs a holding cost h > 0 per unit of on-hand inventory. Additionally, as in [32, 165, 193, 194], we assume that the retailer jointly replenishes her stock of all products whenever the inventory of any product is depleted to 0, incurring a fixed replenishment cost of K > 0. We refer to the time between consecutive replenishments as a replenishment cycle, and let S ∈ N + be the inventory level of each product at the beginning of each replenishment cycle.

Performance metrics and trade-offs.

The goal of the retailer is to design simple opaque selling strategies that (i) achieve high long-run average revenue, and (ii) incur low long-run average inventory costs. (The meanings of “high” and “low” will be made in precise in Section 5.4.2, when we introduce our benchmark policies.) To formalize these metrics, we introduce some additional notation. We define a policy π to be a mapping from the current state of the system (i.e., the inventory levels of all products) to the decision of whether or not to offer the opaque product. For t ∈ N + , let ω π (t) denote this decision, with ω π (t) = 1 if the product is offered, and ω π (t) = 0 otherwise. We moreover let q i π (t) be the probability that a customer arriving in period t purchases individual product i ∈ [N], and denote by q o π (t) the probability that the opaque product is purchased by the customer. (For ease of notation, we omit the dependence of these quantities on δ and pˆ.) We assume that, if the customer purchases the opaque product in period t, the retailer samples two products uniformly at random, denoted F(t), and allocates the product in F(t) with higher remaining inventory.

5 Note that this is equivalent to saying that customers assume they will receive each product uniformly at random.

135 1.00

0.75

0.50

0.25

0.00

1.0

N

2

0.8

5

10

0.6

15

20

0.4

0.0

0.1

0.2

0.3

(a) q o π (t) vs. δ

0.4

0.5

0.0

0.2

0.4

δ

δ

(b) R π (t) vs. δ

Figure 5.4: Dependence of q o π (t) and R π (t) on δ and N, for ¯v = γ = 1.

Finally, we use R π (t) to denote the expected revenue in period t induced by the decision made by π. Notice that, absent inventory considerations, it is a priori unclear why the retailer would want to offer an opaque product, given the revenue loss associated with the incentivizing discount δ. We formalize the intuition that offering the opaque product is costly to the retailer via Propositions 10 and 11 below.

Proposition 10. The revenue-maximizing price in each period is given by pˆ = ¯v Moreover, (i) in periods where the opaque product is not offered,

γ 2N

.

1 q i π (t) = i [N] ∀ ∈ N

and

γ

−

(t)

=

¯v

Rπ  2N

(ii) in periods where the opaque product is offered:

   0 if δ ∈ − 1 1  [ 0, ( 4 2N ) γ ] q o π (t) = 1 − N + 2Nδ if δ ∈ 1 − 1 γ , 1 4 γ    2 γ ( ( 4 2N ) )  1 if δ ≥ 1  4 γ γ with R π (t) = v − 2N − δ · q o π (t).

and

−

(t) qi π  N

1

qo π 

(t)

=

We illustrate Part (ii) of Proposition 10 in Figure 5.4, deferring the proof of the fact to Appendix D.2.1. In Figure 5.4a we observe that, as N increases, the threshold past which customers begin purchasing the opaque product with non-trivial probability increases; moreover, for δ ∈ ( 1 4 − 2N 1 ) γ , 4 1 γ (t) is linearly increasing in δ. , the purchase probability qo π  ( ) These two facts together imply that, as N grows large, q o π (t) approaches a step function: for any δ ≤ γ /4, no one chooses the opaque product; past this point however, everyone chooses the opaque product. Figure 5.4b illustrates the implications of these factors for the retailer’s revenue. In particular, note that the retailer’s maximum possible revenue is achieved when no one purchases the opaque product (i.e., δ ≤ ( 4 1 − 2N 1 ) γ ). Between this point and γ /4, her loss is quadratic in δ; finally, past γ /4 her revenue is linearly decreasing, since everyone

R π (t)

q o π (t)

136 purchases the opaque product. This also highlights that there is no incentive for the retailer to ever offer a discount higher than γ /4. As a result, in the remainder of this section we

γ ∈ 1 1 assume δ ( ( 4 − 2N ) γ , min { 1 4 γ , pˆ } ] , with ¯v > 4 in order to ensure that this interval is non-empty. Finally, throughout the section we abuse notation and define q o := 1 − N 2 + 2Nδ . γ

Having established the retailer’s per-period revenues with and without the opaque option, Proposition 11 provides a closed-form expression for the long-run average revenue of any opaque selling policy π, denoted by Rev π . We denote by R π the random variable representing the length of a replenishment cycle under π, and by M π the number of times the opaque product is purchased in a replenishment cycle.

Proposition 11. For a fixed policy π, the retailer’s long-run average revenue is given by

E [Mπ  ] Rev π = pˆ − δ · . E[R π ]

(5.4)

We defer the straightforward proof of Proposition 11 to Appendix D.2.1. Noting that Rev π attains its maximum when M π = 0, Proposition 11 underscores that the retailer should never offer the opaque product if her only goal is to maximize revenue. With that said, the loss in revenue from offering the opaque option may be justified if the opaque selling strategy results in inventory costs savings, as observed in [32, 165]. To see why this would be the case, notice that exercising the opaque option gives the retailer additional control over product inventories, since she has the freedom to allocate any of the N products to the current customer under this option. By allocating products with higher inventory levels, the retailer can delay the time to replenishment (since each individual product’s inventory level will deplete more slowly), yielding lower replenishment costs overall. Equation (5.5) below (derived in [32], Equations (1) and (2)) provides a closed-form expression for the retailer’s long-run average inventory costs, denoted by Inv π , thereby helping to formalize this intuition:

K h )2 ] E[(Rπ  Inv π = 2NS + 1 − . + E[R π ] 2 E[R π ] ( )

(5.5)

For ease of notation, we let K π =

2NS + 1 − . ( )

E[(R π ) 2 ] E[R π ]

and H π =

Equations (5.4) and (5.5) together recover theh 2 intuition that a “good” policy trades off between exercising the opaque option frequently enough to keep inventory levels approximately balanced, thus ensuring long replenishment cycles in expectation, but not so frequently as to incurs large revenue losses. In what follows, we will evaluate the performance of various opaque selling strategies in a “large-inventory” limit in which N is fixed and S grows large. It 1 will moreover be useful to interpret K ∈ Θ(S) and h ∈ Θ ( S ) for our theoretical results, so that the replenishment cost per unit and the total holding cost per period are constants.6 

K E[R π ]

Discussion of modeling assumptions.

Before presenting our results, we discuss our most important modeling assumptions for this section.

6 One can alternatively view this as a regime in which the holding cost per period h is small relative to the replenishment cost K, as is expected in practice.

137 On the Salop circle model. As alluded to above, the Salop circle model is a common modeling framework in settings where the retailer offers horizontally differentiated products, such as differently-colored shirts. Moreover, not only does it generalize the Hotelling model considered in the majority of existing works on opaque selling when N = 2 [165, 171, 174, 175], but, joint with the assumption that customers are risk-neutral, it also is one of the simplest models for which there are no revenue gains from opaque selling. As a result, the clear-cut trade-off between revenue and inventory costs makes it a prime candidate to illustrate the relevance of our insights, i.e., that (i) there exist settings in which exerting flexibility is costly, and (ii) judiciously exerting flexibility in load balancing settings can generate almost all of the benefits of a perfectly balanced load, at small cost to the decision-maker. With that said, we highlight that our results themselves rely fairly minimally on the Salop circle model. In particular, in Remark 4 at the end of this section we highlight the minimal assumptions on the customer choice model required for our results to hold. Moreover, in Section 5.5.2 we demonstrate via extensive numerical experiments the robustness of our algorithmic contributions to the choice model, for a wide variety of models, including the multinomial logit choice model, as well as risk-averse and risk-seeking customer behavior.

On the control levers. An important assumption in our setting is that the retailer can only influence customer choice by offering the opaque product. Specifically, all products share the same price; moreover, this price and the opaque discount are fixed at the beginning of time. While the fact that all products share the same price is without loss of generality for our analytical results, since products are homogeneous, in our numerical experiments we show that our insights are robust to settings in which products are heterogeneous and the decision-maker implements a discriminatory pricing (DP) policy, which fixes different prices for different products.

We highlight that a common and well-studied practice to address supply-demand imbalances in retail setting is dynamic pricing, wherein the retailer adaptively varies the prices of products as a function of their inventory levels. Here, we focus on separate class of policies that address this issue, i.e., policies that set a static price for all products, and begin offering an opaque option at some point in time. While we do not seek to argue that implementing dynamic pricing is always unreasonable, in many settings (especially when products are homogeneous), frequent price changes may be viewed unfavorably by customers. The addition of a discount product, however, is less likely to be contentious. Additionally, [165] numerically showed that policies that fix a static price and offer an opaque option in each period frequently outperform dynamic pricing strategies. Thus motivated, we restrict our benchmarks to opaque selling strategies that fix a single price through time.

We also note that we do not study the joint optimization of the fixed price pˆ and the opaque discount δ. Given that we study an asymptotic regime in which S grows large and δ is constant, our bounds hide potentially important dependencies on δ that would be required for this joint optimization. In light of the fact that we assume that pˆ and δ are set separately, letting pˆ be the revenue-maximizing price is the natural choice. Moreover, our numerical experiments provide guidance for choices of δ that generate high profits for the retailer, given pˆ.

Finally, recall that we restrict the retailer to allocate from two products chosen uniformly

138 at random if the customer purchases the opaque product. This restriction is for expositional purposes, in order to maintain consistency with the balls-into-bins strategies presented in Section 5.3; we formalize this connection in Section 5.4.3. While sampling two products at random may be computationally efficient in settings where N is large (as motivated by the power-of-two-choices paradigm in balls-into-bins), in many settings it may be more desirable to allocate the product with the highest remaining ttory across all N products, henceforth referred to as the N-sample setting. The algorithm we propose in Section 5.4.3 can be directly adapted to such a setting. Moreover, it is easy to see that the two-sample setting constitutes a lower bound on the performance of our policies for the N-sample setting. Since our results will show that the two-sample algorithm is asymptotically optimal in the large-inventory regime we consider, extending to N-sampling only strengthens the insight that late-stage semi-adaptive opaque selling can yield gains for the retailer.

On the metrics. In line with our results for the vanilla balls-into-bins model, our main focus is on characterizing the trade-off between revenue and inventory costs for various opaque selling strategies, as opposed to a single objective, such as profit. The reason for this is two-fold. From a technical perspective, obtaining a closed-form expression for the profit of any given policy proves to be a challenge analytically, given the asymptotic regime in which we situate ourselves. Moreover, analyzing revenue and inventory costs separately allow us to obtain finer-grained insights into the value a retailer derives from exercising the opaque option. While we obtain sufficient conditions on regimes for which the semi-dynamic policy outperforms all benchmark policies in theory, our computational experiments moreover show its strong performance over a wide variety of randomly generated instances.

5.4.2 Benchmark Policies

Having described the model, we now analyze two policies against which we will benchmark our algorithm: (i) the no-flex policy π nf , which never offers the opaque option to customers, and (ii) the always-flex policy π a , which offers it in each period. 7 As before, we use the superscripts nf and a to refer to metrics under the no-flex and always-flex policy, respectively.

Intuitively, the no-flex and always-flex policies lie on opposite extremes of the revenueinventory costs trade-off curve: while the no-flex policy achieves the maximum possible revenue, it exerts no control over inventory levels; the always-flex policy, on the other hand, suffers substantial revenue losses by offering the opaque option in each period, but should incur low inventory costs due to balanced inventory levels throughout the horizon (and consequently long replenishment cycles). The impact of these two policies on replenishment cycle length is illustrated in Figure 5.5, which plots a sample path of the minimum inventory level under the always-flex and never-flex policies (the “flex- √ S” policy π f is later discussed in Remark 2). In particular, we observe that π nf leads to replenishment cycles that are on average much shorter than those under π a , with periods in which the minimum inventory level decreases steeply, as customers’ random purchases deplete the product with the lowest inventory. The minimum inventory level under the always-flex policy, on the other hand, looks staircase-like, as the only time the product with the minimum inventory level is allocated to

7 The always-flex policy is equivalent to the N-opaque selling strategy considered in [32].

139 40

20

0

π nf π a

π f

0

100

200

300

400

500

t

1

Figure 5.5: Minimum inventory level, denoted by min i ∈ [N] z i π (t), under π nf , π a and the

of the ( √ S ) periods (see Remark 2). Here, S = 40, N = 3 and q o = 1. Periods in which the minimum inventory level increases to 40 signify the start of a new replenishment cycle.

“flex- √ S" policy π f which offers the opaque product uniformly at random in Θ

1

a customer is when inventory levels are perfectly balanced, thereby yielding replenishment cycles that are on average 10 periods longer.

Propositions 12 and 13 formalize this intuition. We defer their proofs to Appendix D.2.2.

Proposition 12. Under the no-flex policy π nf , the following holds:

(i) E[M nf ] = 0 and E[R nf ] = NS − θ nf , where θ nf ∈ Ω( √ S).

(ii) Rev nf = pˆ and Inv nf = NS K + h 2 · NS + ξ nf , where ξ nf ∈ Ω 1 S . ( √ )

Proposition 13. Under the always-flex policy π a with δ ∈ Θ(1) 8 , the following holds:

(i) E[M a ] ∈ Θ(S) and E[R a ] = NS − θ a , where θ a ∈ O(1).

1 (ii) Rev a = pˆ − δ ( 1 − N/2 + 2Nδ/ γ ) and Inv a = NS K + h 2 · NS + ξ a , where ξ a ∈ O ( S ) .

Since the retailer stocks exactly NS products at the beginning of each replenishment cycle, NS is a loose upper bound on the maximum possible length of a replenishment cycle, which we refer to as the ideal replenishment cycle length. As a result, the constant NS K + h · NS can 2 be thought of as a theoretical lower bound on the retailer’s inventory costs. We henceforth refer to this quantity as the ideal inventory cost. Using this interpretation, Proposition 12 establishes that the stochasticity in customers’ purchase decisions without the opaque option results in a decrease in expected cycle length of Ω( √ S) relative to the ideal replenishment

cycle, leading to an inventory cost increase of Ω 1 S relative to this theoretical lower bound. ( √ ) Proposition 13, on the other hand, establishes that exerting the opaque option in each period results in a cycle length that is within O(1) of the ideal replenishment cycle length, with 1 inventory costs within O ( S ) of the ideal inventory cost. However, this comes at a constant per-period revenue loss. Notice that this latter loss far outweighs the inventory cost savings from offering the opaque option in each period; as a result, from a profit perspective it is

8 Since δ > ( 4 1 − 2N 1 ) · γ , the condition that δ ∈ Θ(1) is naturally satisfied when N > 2.

π i (t)

min z

i∈[N]

140 clear that in this homogeneous setting, the retailer should not adopt a policy of offering the opaque product to customers in each period, for any value of δ ∈ Θ(1).

Motivated by these extremes, we seek to design policies that achieve a two-fold objective, as it relates to the revenue-inventory cost tradeoff: (i) incurring o(1) loss relative to the revenue-maximizing solution that never offers the opaque option, and (ii) incurring order-wise identical inventory savings as the always-flex policy that has the most control over inventory 1 levels, i.e., O ( S ) loss relative to the ideal inventory costs.

Remark 2. A natural idea to reduce the revenue loss incurred from offering the opaque product would be to set δ ∈ O 1 S , so that a customer only purchases the opaque product ( √ ) with probability O 1 S , as suggested in Proposition 4 of [165] for the special case of N = 2. ( √ ) This idea, however, does not achieve the desired trade-off in our model, for two reasons. First of all, when N > 2, Proposition 10 establishes that δ > ( 4 1 − 2N 1 ) γ ∈ Θ(1) is required for the opaque product to be chosen with strictly positive probability. Moreover, independent of the customer choice model, a “flex- √ S" policy π f that exerts flexibility uniformly at random in 1 Θ √ S

of the periods will not guarantee that the expected replenishment cycle length is a ( ) constant away from the ideal cycle length NS; as a result, it will not be able to achieve the inventory costs savings of the same order as Inv a , our second desideratum. Intuitively, this is due to the fact that, for any constant a > 0, a policy that exerts flexibility randomly in

a

fraction of periods will not be able to approximately balance the system if its gap ever S

√

exceeds (a + 1) √ S; this event occurs with constant probability for any a. We illustrate this phenomenon in Figure 5.5, which shows that while replenishment cycles under π f are longer than those under the no-flex policy, they still fall short of those under π a . We provide a more comprehensive inventory cost and revenue analysis of this policy in Section 5.5.2.

5.4.3 Leveraging Balls-Into-Bins for Effective Late-Stage Opaque Selling Strategies

In this section we leverage the insights from Section 5.3 to design opaque selling strategies that appropriately trade off between revenue and inventory costs. To do so, we first specify the analogy to the balls-into-bins framework, first identified in [32]. Here, bins correspond to product types, and balls correspond to customers. Every time a customer purchases a product (thereby depleting its inventory by one), a ball is allocated to a bin (thereby increasing the bin’s load by one); a customer purchasing an opaque product is analogous to allocating a flexible ball. Moreover, keeping inventory levels balanced in the opaque selling model is analogous to the goal of maintaining a balanced load across bins. In the opaque selling model, we are similarly penalized for flexing too frequently given the dependence of the long-run average revenue on the expected number of flexes, E[M π ] (see Equation (5.4)).

Despite this fairly straightforward analogy, there exist important distinctions between the two settings. First of all, while the balls-into-bins setting has a fixed horizon of length T, the horizon in the opaque selling model is the replenishment cycle, whose length is not only unknown, but more importantly endogenous to (i) the random fluctuations in customers’ purchases, and (ii) the retailer’s opaque selling decisions. As a result, naively adapting the

141 dynamic policy designed for the balls-into-bins setting (see Algorithm 2) to this setting first would require the algorithm to maintain a prediction of the time at which the replenishment cycle ends. More fundamentally, however, this endogeneity issue makes it a priori unclear that such “point of no return”-style policies, which exercise the opaque option extremely infrequently, suffice to induce long replenishment cycles. Finally, we highlight the subtle difference in the way in which flexing is penalized in the opaque selling model, relative to the vanilla balls-into-bins setting. In particular, Equation (5.4) establishes that the retailer’s long-run average revenue is decreasing in the expected number of opaque purchases, for a fixed expected replenishment cycle length. However, as M π increases, so does R π . On the one hand, this renders the exact dependence of the revenue loss on the number of opaque purchases less straightforward; on the other, it makes clear the importance of policies that efficiently exercise the opaque selling option (i.e., in a way that maximizes the bang-per-buck of the cost of an opaque discount per increase in replenishment cycle length). As we saw in Proposition 13, the always-flex policy fails this litmus test, given that it offers the opaque product to customers in each period, even when inventory levels are approximately balanced.

The semi-dynamic policy.

In our main result for this section, we propose a variant of the dynamic policy designed for the balls-into-bins setting that addresses these subtleties. Specifically, we consider an analogous notion of system balancedness for product inventories, similarly referred to as the gap of the system and defined as:

t Gap I π (t) = S − z i π (t), ∀ t ∈ [R π ], −i  min N ∈ [N]

(5.6)

where z i π (t) ∈ [1, S] denotes the remaining inventory of product i in period t under policy π, and t is re-initialized at the beginning of each replenishment cycle. Intuitively, the term S − t/N captures the remaining inventory for each product if the previous realized demand had been split equally across products. Thus, Gap I π (t) captures the deviation between the current inventory level for product i, z i π (t), and a perfectly balanced state of the system.

As in Algorithm 2, the semi-dynamic policy triggers the opaque option the first time the system imbalance, as measured by Gap I π (t), reaches a “point of no return.” To formalize this point of no return, we define a fictitious end of horizon, denoted by T := N(S − 1) + 1, corresponding to the length of the replenishment cycle if the retailer balanced inventory in each period. The quantity T is a tight upper bound on the maximum cycle length; we henceforth refer to it as the achievable-ideal cycle length. 9 Under the semi-dynamic policy, the retailer verifies the following threshold condition in each period:

cd  (T − t)qo  Gap I d (t) ≥ , N

(5.7)

where c d > 0 is a tuning parameter. If this condition is satisfied, the opaque option is offered to customers until the end of the replenishment cycle. Notice that this policy is entirely

9 To see this, note that it takes N(S − 1) periods for all products to reach an inventory level of one. In the next period, no matter which product is purchased, its inventory level will then drop to 0 and a replenishment will occur.

142 π nf

π a

π d

π nf

π a

π d

E[M π ]

S Θ(S) √ ( )

O

0

NS − E[R π ] Ω O (1) √ S ( )

O

Rev ∗ 1 S ( √ ) Inv π 1 S O S ) S ) ( √

0 Ω O

− ( )

Revπ  Inv ∗ 1

Θ(1) (

O 1

(1)

Table 5.1: Discount Frequency-Cycle Length Trade-off

Table 5.2: Revenue-Inventory Cost Tradeoff

analogous to Algorithm 2, save for the fact that the opaque option allocates the product with the lowest inventory level, as compared to the balls-into-bins policy which throws a flexible ball into the highest-loaded bin. For completeness, however, we include a formal description of the semi-dynamic policy within this context in Appendix D.2.3.

Theorem 15 establishes that the semi-dynamic policy achieves a “best-of-both-worlds” as it relates to the revenue-inventory cost trade-off faced by the retailer: its long-run average revenue is within o(1) of the revenue-maximizing policy that never offers any opaque discounts, all the while achieving all of the inventory cost savings of the policy that seeks to perfectly balance inventory levels at all times.

Theorem 15. Under the semi-dynamic policy, the following holds, for any cd 

≤

1

and ( N ) 2

δ ∈ Θ(1):

10

(i) E[M d ] ∈ O( √ S) and E[R d ] = NS − θ d , where θ d ∈ O(1).

1 (ii) Rev d = pˆ ( 1 N/2 + 2Nδ/ γ ) ξ d 1 and Inv d = + 2 NS + ξ d 2 , where ξd 1  −δ − · NS K h · ∈ O √ S ( ) 1 and ξ d 2 ∈ O ( S ) . Hence, it suffices to establish that ∑ t=S N(S−1)+1 P ( Gap d (t) ≥ S − t/N ) ∈ O(1).

Herein lies the main technical challenge as compared to the vanilla balls-into-bins model. While this latter model only required a bound on the expected gap at the end of the horizon, since the horizon is random in the opaque selling model, we must now bound the tail of the ~ gap in each period. We do so by splitting the flexing horizon into two, letting T denote the midpoint between T ⋆ and T, for any realization of T ⋆ .

Case 1: t ∈ { T ⋆ , . . . , T } . In this region, S − t/N is large, so we should naturally expect P ( Gap d (t) d ≥ S − t/N ) to be small. The main challenge in obtaining tight bounds on the tail of Gap (t) lies in the fact that there exists an accumulated imbalance at T ⋆ on which we would need to condition. The follow key fact, however, allows us to eschew this obstacle.

Lemma 10 (Informal Lemma). Let Gap a (t − T ⋆ ) denote the gap induced by the always-flex policy for a system initialized with empty bins at T ⋆ . Then,

P (t) ≥ S − t/N | Gap d (T ⋆ ) ≤ a, T ⋆ ( Gap a (t − T ⋆ ) ≥ S − t/N − a | T ⋆ ) . Gapd  ≤ P ( )

With this fact in hand, we leverage the threshold condition to provide an upper bound of ⋆ ⋆ Gap d (T ⋆ ) < c d q(T−T N +1) + 1. We then argue that, for S − t/N − c d q(T−T N +1) + 1

(

> 0, )

c d q(T −T ⋆ +1) cd  q(T − T ⋆ + 1) −Ω S−t/N− ( N +1 ) P (t ) + 1 Gap a − T ⋆ ≥ S − t/N − | T ⋆ ∈ e ( ) . ( N )

Summing over all t in this interval, we obtain the first part of our constant upper bound.

~ Case 2: t ∈ { T + 1, . . . , T } . Unfortunately, in this region the same arguments fail to

+1 ≤ 0, ( N ) preventing us from applying the tail bound on Gap a (t − T ⋆ )). We first consider the “easy” ~ scenario in which the loads of the maximally and minimally loaded bins at T intersected for some τ ∈ { T ⋆ , . . . , T } . In this scenario, we leverage our analysis from the proof of ~ Theorem 12 to show that the likelihood the gap is nonzero at T if the loads of the maximally ~ ~ and minimally loaded bins at T intersected for some τ ∈ { T ⋆ , . . . , T − 1 } is exponentially ~ ~ ~ decreasing in T − τ. If it is indeed non-zero, in the worst case, Gap d (T) ≤ T − τ, since at ~ ~ most T − τ could have been placed in any one bin between τ + 1 and T. We can again then apply Lemma 10 to bound the tail of the gap. Summing over all t in this region, we again obtain a constant bound for the easy scenario.

apply given that S − t/N is now small (and in particular, S − t/N −

c d q(T−T ⋆ +1)

The remaining scenario to consider is when the loads of maximally and minimally loaded ~ ~ bins at T never intersected before T. ⋆ Let E 1 denote this event. Here is where we leverage the ~ definition of T as the midpoint of T and T. In particular, the threshold condition bounds the difference between the loads of the maximally and minimally bins as a linear function ~ of T − T ⋆ ; this then immediately implies that this bound is linear in T − T. We can then leverage the analysis from the proof of Theorem 12 to show that there exists a constant t 0 > 0 ~ such that the likelihood that E 1 occurs is exponentially decreasing in T − T. Summing this ~ over all t ∈ { T + 1, . . . , T } , we obtain our final constant bound.

Note that an immediate corollary of Theorem 15 is that the semi-dynamic policy is a strict improvement on the always-flex policy with respect to profit, for any δ ∈ Θ(1). The

144 comparison between the no-flex and semi-dynamic policies, however, is more subtle, and will in general be instance-dependent. In Proposition 14 below we identify a wide regime of parameters for which the semi-dynamic policy generates higher profits than the no-flex policy.

Proposition 14. Let Pr a , Pr d , and Pr nf respectively denote the long-run average profits 1N 2  under the always-flex, the semi-dynamic, and the no-flex policies. For c d = 10 , the ( )10  following holds:

(i) Pr d − Pr a ∈ Ω(1) for any δ ∈ Θ(1).

(ii) Fix δ ∈ Θ(1) and suppose K = ψ · NS and h = ψ /(NS) for some constant ψ > 0.

Then, there exists a constant C > 0 such that Pr d − Prnf 

∈

Ω

(

1 √ S

for all > Cδ. ) ψ

We defer the proof of Proposition 14 to Appendix D.2.3. At a high level, this result formalizes the intuition that, if the replenishment and holding costs are high enough relative to the disutility a customer incurs from the opaque product, then it is worthwhile for the retailer to implement the semi-dynamic policy. The threshold at which this occurs naturally has a dependence on N and γ , since the discount required to incentivize customers to choose the opaque option increases with these two parameters, as established in Proposition 10. In our computational experiments, we additionally show that the semi-dynamic policy outperforms the no-flex policy over a wide range of randomly generated instances.

Remark 3. Though of less practical interest, one can also adapt the static policy in the balls-into-bins model to the opaque selling model. Using similar arguments as those used in Theorem 15, it is easy to show that this static policy asymptotically leads to the same expected replenishment cycle length, at the cost of a higher number of opaque discounts given. We omit this analysis for brevity.

Remark 4. We conclude the section with a brief discussion on the minimal assumptions on the choice model required for our theoretical results. In particular, for Proposition 12, Proposition 13, and Theorem 15 to hold, we only require that (i) a purchase is made in each period, and (ii) each individual product is equally likely to be purchased. As discussed in Section 5.4.1, we require (i) to hold as we are interested in settings in which there is a clear trade-off between exercising the flexible option and load balancing. With respect to (ii), we conjecture that our results can be extended in a fairly straightforward manner to settings in which the purchase probability across products is heterogeneous. Moreover, the simplicity of the Salop circle model allows us to obtain a closed-form expression of q o as a function of δ, as a results allowing for the profit comparison in Proposition 14. Finally, we underscore that while these two minimal assumptions allow us to formalize the main managerial insight of this section — that strategically timed, late-stage opaque selling achieves optimal revenue and inventory cost trade-offs — our numerical experiments demonstrate that this insight continues to hold for a wide variety of choice models in which neither condition holds.

10 The assumption that c d =

1

is for simplicity. The result would still hold given any constant lower 10 ( N ) 2

bound on c d , with the only modification being a change in the constant C in Part (ii).

145 160

140

120

100

80

60

40

20

0

8000

6000

4000

2000

0

π nf π a

π s π d

π dyn

T

T

(a) E[Gap π (T)] vs. T

(b)

E[Mπ 

]

vs.

T

Figure 5.6: Comparison of the no-flex, always-flex, static, semi-dynamic, and dynamic policies.

5.5 Computational Experiments

In this section we complement our theoretical results via extensive computational experiments for both the vanilla balls-into-bins and the opaque selling setups.

5.5.1 Balls-into-Bins

We begin with a numerical investigation of the balls-into-bins model. Throughout our experiments, we fix N = 5 and q = 0.1, a s = 20 and a d = 0.5, except when specified. All results are averaged across 500 replications.

Benchmark comparison. In Figure 5.6 we validate our theoretical results by comparing E [ Gap π (T) ] and E [M π ] under the no-flex, always-flex, static, and semi-dynamic policies, for T ∈ { 10 4 , 2 · 10 4 , . . . , 9 · 10 4 } . Additionally, we investigate the performance of a practical, fully dynamic variant of the semi-dynamic policy, termed the dynamic policy π dyn . Rather than flexing in all periods after threshold condition (5.2) is met, this policy takes the point of no return philosophy even further, allowing for the idea that the gap of the system may naturally self-correct even after T ⋆ ; as a result, it keeps checking the threshold condition in each period after T ⋆ , only ever flexing in the period immediately after the condition is met.

Our results corroborate Theorems 12-14. In particular, in contrast to the no-flex policy, all flexing policies maintain a constant gap as T scales large. We moreover observe that the static, semi-dynamic, and dynamic policies exert flexibility in a sublinear number of periods, with the dynamic policy exerting half as many flexible throws as the static policy, for T = 9 · 10 4 . This comes at the cost of a slightly higher gap.

Impact of N and q. We next study the impact of the number of bins N and the flex probability q on the performance of the semi-dynamic policy. Across all experiments we let

T = 10 5 .

Figures 5.7a and 5.7b respectively plot E[Gap d (T)] and E[M d ] versus N, for q = 0.1. We observe that both of these quantities are increasing in the number of bins. This phenomenon

E

E

π [Gap (T)]

π [M ]

146 14

2000

12

10

8

6

4

2

1750

1500

1250

1000

750

500

250

2

4

6

8

10

12

2

4

6

8

10

12

N

N

(a) E[Gap d (T)] vs. N

(b)

E[Md 

]

vs.

N

Fig 9

1200

8

1175

7

1150

6

1125

5

1100

4

3

2

1

1075

1050

1025

0.1 0.2

0.3 0.4

0.5 0.6

0.7 0.8

0.9

0.1 0.2

0.3 0.4

0.5 0.6

0.7 0.8

0.9

q

q

(a) E[Gap d (T)] vs. q

(b)

E[Md 

]

vs.

q

Figure 5.8: Impact of q on semi-dynamic policy performance, for T = 10 5 , N = 5.

customers’ aggregate purchase probability (and as a result, there is less of a clear trade-off between revenue gains and inventory cost savings), strategically timing opaque offerings can strongly outperform the no-flex and always-flex policies. Moreover, these insights continue to hold when customers exhibit risk-averse and risk-seeking behaviors as it relates to the opaque option.

Numerical setup.

We first specify the behavioral and inventory models used in our experiments. Throughout, we use the notation { o } to denote the product corresponding to the opaque option.

Choice model. We consider a setting in which the retailer sells N = 3 types of products, and assume that each product has a marginal production cost of c = 0. There are L = 3 types of customers. In each period, a type-l customer arrives with probability α l ∈ (0, 1). A l type-l customer has valuation V i l = v + V i for product i ∈ [N], where v represents customers’ l intrinsic value for obtaining any product, and V i ∼ U(0, 1 − v) is an idiosyncratic term unique to each type, product pair. For our main set of experiments, we assume customers 1 are risk-neutral, and value the opaque option at V o l = N ∑ i=1 N V i l .

To model idiosyncrasies across customers of the same type, we assume customers make their purchase decisions according to the multinomial logit choice model (MNL) [195]. Formally, when the opaque product is not offered, we let q l,i be the probability that a type-l customer purchases product i. Then,

exp ( (V i l − p i )/ µ ) ql,i = , 1 + ∑ j ∈ [N] exp − p j )/ µ (Vj l  ( )

where p j is the price of product j ∈ [N] ∪ { o } , and µ is a scale parameter.

When the opaque option is offered, we denote the purchase probabilities by ql,i o  [N] ∪ { o } , with:

exp ( (V i l − p i )/ µ ) ql,i o = . 1 + ∑ j ∈ [N]∪ { o } exp − p j )/ µ (Vj l  ( ) As in our analytical results, we assume the prices of all products are fixed across time; however, we allow the retailer to vary prices across products. Specifically, the retailer sets p ˆ = (p 1 , . . . , p N ) to be a revenue-maximizing price vector absent the opaque option, i.e., p ˆ ∈ arg max p ∑ i ∈ [N] (p i − c)q i , where q12 i = ∑ l ∈ [N] α l q l,i is the aggregate purchase probability of product i across all customer types. Given p ˆ , we set p o = ∑ i ∈ [N] p i q i − δ, i.e., we apply the opaque selling discount δ > 0 to the weighted average price of a product in the absence of the opaque option. Finally, across all experiments, we let v = 0.6, c = 0, µ = 0.1 and δ = 0.05. We defer sensitivity analyses of our results to various values of v and c to Appendix D.3.

Inventory model. We assume the retailer sets the aggregate initial inventory level across all products according to the classical Economic Order Quantity (EOQ) formula [196]. Letting S ˆ denote this total inventory level, we have S ˆ := 2DK , where D represents √ h an estimate of aggregate demand across all products. Notice that, under this general model, offering the opaque option may boost product sales, thereby potentially significantly impacting the aggregate demand D if offered frequently. As a result, we consider different values of D depending on the opaque selling policy. For the always-flex policy, we let D= ∑ l ∈ [L] α l ql,i o  , since the opaque option is offered in each period. For all ( ∑ i ∈ [N]∪ { o } ) other policies, we let D = ∑ l ∈ [L] α l ql,i  be the aggregate expected demand absent ( ∑ i ∈ [N] ) the opaque option. 13 To adjust for the heterogeneous purchase probabilities across products, ˆ we set the order-up-to level S i for each product i ∈ [N] by normalizing S by the market share for product i. For instance, under the always-flex policy:

α l ql,i o  ˆ ∑l ∈ [L]  S i S= · . ∑ l ∈ [L] α l ( ∑ i ∈ [N] q l,i o )

(5.9)

For all other policies, we set S i by replacing q l,i o in Equation (5.9) above with q l,i .

Policies. Throughout our experiments we compare the performance of the semi-dynamic policy to that of the no-flex and always-flex policies. Recall, in the homogeneous setting considered in Section 5.4, the retailer allocates the product with the highest remaining inventory to customers purchasing the opaque product. While this naturally balances inventory levels across time for homogeneous products, the notion of system balancedness changes in the heterogeneous product setting we consider here. Specifically, in order to account for the different purchase rates (and stocking levels) of products in this setting, we zi π  (t) now reason with respect to the normalized inventory levels of products, defined as ¯z i π (t) = Si  for all i ∈ [N], t ≥ 0. System balancedness, then, naturally corresponds to the normalized

ˆ ˆ 12 In general, solving for p exactly is computationally intractable; we instead approximate p via grid search, enumerating over p ∈ { 0.01, 0.02, . . . , 1 } N .

13 This estimate of D is exact for the no-flex policy. However, for all other tested policies that offer the opaque option, this will underestimate the expected demand only slightly, given that these policies exercise the opaque option very infrequently. While the retailer will stock suboptimally in these cases, for this value ˆ of S, the profit induced by these policies can then be viewed as a conservative estimate of the profit under the “optimal” order-up-to levels.

149 inventory levels being equal across all products, achieved by allocating the product with the highest normalized inventory level to a customer purchasing the opaque option. In line with this reasoning, we re-define the gap of the system to take in the normalized inventory levels of all products, i.e.,

z i π (t) d ∑i ∈ [N]  Gap I (t) := −i min z i π (t), ∀ t ∈ [R π ]. N ∈ [N]

(5.10)

The heterogeneous analog of the threshold condition in Algorithm 8 is then:

a · (S i − 1) + 1 t ( ∑ i ∈ [N] ) ] d Gap I (t) ≥ [ ,

(5.11)

ˆ S

where a ∈ (0, 1] is a tuning parameter. In our experiments, we let a = 0.5.

Remark 5 (Equivalence of the semi-dynamic policies in Sections 5.4 and 5.5.2). For the special case of the Salop circle model, the above semi-dynamic policy and the semi-dynamic policy specified in Algorithm 8 are equivalent. To see this, observe that since S i is identical across products under the Salop model, allocating the product with the highest normalized inventory level is equivalent to allocating the product with the highest actual inventory level. Moreover, since exactly one product is purchased in each period, under the Salop model we have that ∑ i ∈ [N] ¯z i d (t) = NS−t S . Letting a = c d q o in Equation (5.11), we have that the threshold condition is satisfied if and only if:

S − t/N z i d (t) c d q o N(S − 1) + 1 − t q o (T − t) mini ∈ [N]  cd  − ≥ ( ) ⇐⇒ S − t/N −i min z i d (t) ≥ , S S NS ∈ [N] N

which is precisely the threshold condition used in Algorithm 8.

Results.

Across all experiments, we run 100 replications over 10 4 periods for each random instance, specified by choice model and inventory parameters. All reported metrics are averaged over these 10 4 periods and 100 replications.

Before presenting our results, we note that for these instantiations, whenever the opaque product is offered, the aggregate purchase probability across all offerings is on average 6.5% higher than periods in which the opaque product is not offered. However, since the opaque product is sold at a discount, opaque selling results in an expected revenue loss of 3.8% in periods in which it is offered. As a result, we observe a revenue-inventory cost trade-off over a wide variety of instances, even in the heterogeneous product setting.

Benchmark comparison in large-inventory regime. We first numerically validate our ˆ theoretical results by studying the performance of π d in the large-inventory regime, as S scales large. In order to do so, we fix a scaling parameter λ > 0, and let K = λ, h = 0.05/λ, ˆ so that S scales linearly with respect to λ. We moreover assume that the three types are perfectly balanced, with α = (1/3, 1/3, 1/3).

150 Θ (

1/

√

λ

)

0.030

0.020

Inv − Invd  Inv nf a − Inv d

0.025

1/ Θ √ λ ( )

0.020

Rev 0.12

0.10

0.08

0.06

0.04

0.02

0.00

0.12

0.10

0.08

0.06

0.04

0.02

0.00

−20

−10

0

10

20

30

40

50

−20

−10

0

10

20

30

40

50

(a) Relative profit improvement (%) over π nf (b) Relative profit improvement (%) over π a

0.14

0.12

0.10

0.08

0.06

0.04

0.02

0.00

−20

−10

0

10

20

(c) Relative profit improvement (%) over max { π nf , πa 

}

Figure 5.10: Distribution of the relative profit improvement of π d over π nf , π a , and

max { π nf , π a } .

a wide variety of instances. Specifically, we let K ∈ { 1, 2, · · · , 5 } , h ∈ { 0.004, 0.008, · · · , 0.02 } and α ∈ ( 1/3, 1/3, 1/3 ) , ( 2/5, 3/10, 3/10 ) , ( 1/2, 1/4, 1/4 ) . We run 100 replications for { } each (K, h, α) tuple, and plot the distribution of relative profit improvement of the semidynamic policy over the no-flex, always-flex policies in Figure 5.10. We abuse notation and refer to the better of the no-flex and always-flex policies from a profit perspective as

max { π nf , π a } .

These results strengthen our analytical results by demonstrating that strategically timing opaque selling can lead to significant value for the retailer. In particular, Figure 5.10a shows that the semi-dynamic policy generates higher profits than the no-flex policy in over 87% of instances, with an average relative profit improvement of 5.9%. In Figure 5.10b, we observe that it generates higher profits than the always-flex policy in over 88% of instances, with an average relative profit improvement of 8.4%. Finally, this policy generates higher profits than the better of these two policies in over 76% of instances, as seen in Figure 5.10c.

We provide a detailed cost breakdown of the different sources of loss of each policy in Table 5.3. Table 5.3a reports all revenue-related metrics. Specifically, the first column of the table reports the fraction of periods each policy offers the opaque product; the second column reports the fraction of periods the opaque product was purchased; the final two columns report the average revenue loss of all policies relative to the no-flex policy. The always-flex policy yields 3.8% less revenue than the no-flex policy; the semi-dynamic policy, on the other hand, offers the opaque product approximately 35% of the time, with customers purchasing it almost 20% of the time. This results in a revenue loss of 1.4% relative to the no-flex policy.

Table 5.3b then breaks down the sources of inventory costs. In particular, we observe that the cycle lengths across all policies are between 19 and 21 periods, on average. The second column of this table reports this quantity relative to the maximum possible cycle length

Density

Density

Density

152 Opaque product offered (%)

0

100

35.4

Opaque product purchased (%)

0

47.9

17.0

Abs. loss

0

0.025

0.016

Rel. loss (%)

27.8

21.5

18.4

Rel. loss (%)

π nf π a

π d

0

3.8

1.4

(a) Revenue comparison

Cycle length

19.2

21.2

21.1

Cycle completion (%)

83.4

91.4

91.4

Abs. loss

π nf π a

π d

0.064

0.048

0.042

(b) Inventory cost comparison

Table 5.3: Revenue and inventory comparisons of π nf , π a and π d over all randomly generated instances.

of ∑ i ∈ [N] S i − 1; in a relative sense, we see that customers purchasing the opaque option 17% of the time yields cycles that are 8 percentage points higher. The final two columns of this table compare all policies’ inventory costs to that of the “ideal” inventory cost, as described in Section 5.4. We observe that the inventory loss of the semi-dynamic policy is almost 10 percentage points lower than that of the no-flex policy, due to the gains in cycle length. Overall, these inventory gains outweigh the revenue loss, as can be seen from the absolute losses reported in both tables, which helps to explain the overall profit improvement of the semi-dynamic policy.

Importance of strategically timing the opaque offering. In order to illustrate the value of strategically timing the opaque selling offering, we also consider a policy termed the “flex- √ S” policy π f , which offers the opaque option with the same probability as the semi-dynamic policy, but does so in an i.i.d., state-independent fashion in each period.14  Specifically, for each sample path, we instantiate the flex- √ S policy by first simulating the semi-dynamic policy π d , and using the probability with which this latter policy offers the opaque product in each period as the flexing probability for π f .

We plot the distribution of inventory costs and profit of the semi-dynamic policy relative to the flex- √ S policy in Figure 5.11. (Note that, by construction, these two policies lead to the same revenue in expectation.) As demonstrated in Figure 5.11a, the semi-dynamic policy yields significantly lower inventory costs, with an average inventory cost saving of 4.7% relative to π f . This result is intuitive, since the decision to offer the opaque product is uncorrelated with the inventory state under the flex- √ S policy, meaning that it may offer the opaque product when inventory levels are approximately balanced, and fail to offer the opaque product in periods when the gap is large, leading to an average of 6.6% shorter

14 The flex- √ S policy can be viewed as the N-opaque selling strategy in [32], where customers purchase

the opaque product with probability Θ

(

1 √ S

. )

153 0.30

0.25

0.20

0.15

0.10

0.05

0.00

0.175

0.150

0.125

0.100

0.075

0.050

0.025

0.000

−20

−15

−10

−5

0

−5

0

5

10

15

20

(a) Inventory cost relative to π d (%)

(b) Profit improvement relative to π f (%)

Figure 5.11: Histograms for the performance of π d relative to π f .

Revenue-Inventory Cost Trade-off

Relative Profit Improvement (%)

Revd 

Invd 

0.28

δ

0.025 0.65

0.050 0.64

0.075 0.64

0.100 0.63

πnf 

πa 

max }

{

,

0.37 3 2 1 0 −1 −2

Risk-neutral Risk-averse Risk-seeking

0.02

0.04

0.06

0.08

0.10

0.12

δ

Figure 5.12: Relative profit improvement of π d over max { π nf , πa  risk models and opaque discount δ.

}

under different customer

Robustness to customer risk preferences. Finally, we test the robustness of the semidynamic policy to risk-averse and risk-seeking behavior. Specifically, we model risk-seeking customers by letting V o l = max i ∈ [N] V i l , ∀ l ∈ [L]; on the other hand, we model risk-averse customers by letting V o l = min i ∈ [N] V i l , ∀ l ∈ [L]. We plot the relative profit improvement of the semi-dynamic policy over the better of π nf and π a in Figure 5.12 as a function of δ.

These results illustrate that the semi-dynamic policy exhibits profit gains for a wide range of values δ. Moreover, the optimal opaque discount is the smallest under the risk-seeking model, followed by the risk-neutral and risk-average models, respectively. This makes sense, intuitively, as a lower value of δ is required to incentivize to risk-seeking customers to purchase the opaque option. In contrast, larger discounts are required to incentivize risk-averse customers to purchase the opaque option. Overall, these results also hint at the idea that “middling” values of δ (around 7.5% of the maximum possible price, in our setting) are robust to customers’ risk preferences.

5.6 Conclusion

In this work we studied a variation of typical load balancing problems, in which the load needs to be balanced only at a specific, potentially random, point in time. We began by demonstrating the power of late-stage flexibility in the canonical balls-into-bins setting, introducing an algorithm that achieves approximate end-of-horizon balance using a tight Θ( √ T) number of flexible throws. Building on these algorithmic insights, we then designed opaque selling strategies for inventory management. We show that the semi-dynamic policy, by maximizing the inventory cost savings with the minimum possible order of revenue loss, can dominate classical benchmarks in the opaque selling literature that blindly offer or withhold the opaque product in each period.

This work opens several avenues for future exploration. Though our findings point to our heuristics’ broad applicability in load-balancing applications where imbalance predominantly stems from stochastic fluctuations, it would be interesting to explore similar ideas in settings with first-order supply-demand imbalances. Second, tighter analyses could yield stronger

Relative Proﬁt

Improvement (%)

155 guarantees for other parameters of interest (e.g., the number of bins/products) or in nonasymptotic regimes. The latter would be particularly beneficial in problems with short or fluctuating time horizons and may require new models to better capture these regimes. Lastly, extending the notion of late-stage flexibility to other revenue management contexts — such as those involving learning or reusable products — could present new opportunities.

156 Chapter 

# 6 Conclusion

In this thesis, we have examined how modern service platforms leverage agent flexibility to enhance operational efficiency. Across the five chapters, our analysis is structured into two distinct but interrelated parts. In Part I, we have explored the interactions and implications of flexibility decisions within platform ecosystems. Chapter 2 delves into the horizontal interactions between demand-side and supply-side flexibility incentives, uncovering two crucial effects – flexibility cannibalization and flexibility asymmetry – that dictate the optimal two-sided flexibility design. Chapter 3 investigates the vertical implications of flexibility decisions in the context of technology adoption, particularly focusing on how operational decisions affect supply chain incentives for autonomous vehicle deployment in hybrid fleets involving flexible human drivers.

In Part II, we have focused on algorithmic innovations for optimizing flexibility. Chapter 4 proposes an online admission-control policy tailored for real-time decision-making in platforms managing heterogeneous customer no-show probabilities, significantly improving performance guarantees on the literature. Chapter 5 explores the power of “opaque selling” as a flexibility lever in e-commerce, introducing dynamic inventory-balancing algorithms that strategically time discounts to manage inventory effectively and minimize fulfillment costs.

Moving forward, my long-term objective is to advance our understanding of flexibility incentives and their role in improving platform operations. One promising research direction lies in examining the value of flexibility in stable matching contexts, such as student-school or employee-firm matchings, to show that minimal flexibility from agents can drastically improve matching outcomes. Specifically, I aim to show how even slight relaxation of one pair of agents’ stability constraints can significantly improve the efficiency of a student-optimal stable matching without harming the flexible student’s welfare. This result would establish foundational insights into “the value of a little flexibility” in stable matching.

Additionally, expanding the concept of flexibility into broader settings beyond the retail context addressed in Chapter 5 holds significant potential. The opaque selling strategy, prevalent in hospitality, car rentals, and similar industries where products are reusable, merits further study. Investigating how the timing and structure of opaque products influence operational metrics in these domains could yield impactful insights into inventory and revenue management strategies, significantly broadening our understanding of demand-side flexibility.

Finally, exploring the welfare implications of operational decisions by platforms remains a critical and underexamined area. Platforms’ flexibility mechanisms, while improving efficiency,

157 may inadvertently create adverse market outcomes. For instance, the Priority Dispatch program at Uber incentivizes driver commitment by offering higher-earning trips to those with high trip completion rates and low cancellation rates. However, in a physical matching market like Uber, spatial friction can limit the efficiency of such dispatch prioritization schemes. In particular, prioritizing a subset of drivers may lead to long-distance pick-ups, which can negatively impact user experiences. I aim to assess the operational value of priority dispatch and compare its efficiency with other incentive mechanisms, such as cash bonuses.

Collectively, these avenues underscore the profound implications and rich opportunities associated with flexibility in platform operations. By deepening our theoretical understanding and refining practical algorithmic strategies, we can better harness flexibility to optimize performance, enhance market outcomes, and ultimately contribute to more effective and responsive platform ecosystems.