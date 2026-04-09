# PPT


## Page 1

# FinTech Co – Technology Architecture Strategy

Contacts: Jeff Tijssen, Adam Davis, Ryan Garner, Marc Hochar, Reina Tabbara

May 2022


## Page 2

# Bain Approach

## POVs and Market Overviews

- Consumer Preferences towards Financial Services Needs POV (KSA, 2022)
- Consumer Preferences towards Financial Services Needs POV (UAE, 2022)
- SME Banking Needs POV (KSA, 2022)
- Digital Attacker Benchmarks and Financial Services Market Trends POV (KSA and UAE, 2021)
- Retail and SME Banking Overview (KSA, 2020)

## Case examples

- FinTech Co – Roadmap to build a Digital Attacker
- FinTech Co – Technology Architecture Strategy
- Fintech Co – Regulatory Considerations and building BaaS Agreement with Bank Co
- Fintech Co – Building a Digital Attacker Operating Model


## Page 3

# Technical strategy have catalyzed the economics of digital attackers and neobanks globally

- Modern technology stacks have **changed the economics** relating to **set up and run costs** that it has catalyzed new Neobanks and Fintech’s globally
- A digital attacker **underpinned by cutting edge technology** could have a cost base **60-70% lower than a mid-tier traditional** bank
- From a servicing perspective, attackers serve **2-3x as many customers per employee as legacy core platform based technology stacks**

[Figure: Left-side content diagram/chart area]

Annual cost per retail customer ($)

[Figure: Bar chart comparing legacy core platform and next-generation platform annual cost per retail customer, showing $300–$400 vs $100–$150 and 60%–70% reduction]

Source: Bain & Company benchmark data and experience, Thought Machine experience with contributions from Personetics, Onfido TruNarrative and Form3


## Page 4

# There are 6 potential architectural principles we need to follow to build the digital attacker

## Microservice Architecture

- Design your services as microservice architectures - small modular services
  - Allows different parts of the system to be scaled in and out based on demand
  - Allows parts of the system to be upgraded in isolation

## Automated and Immutable

- Put in place full automation around the build and deployment, creating artefacts that are versioned and immutable through to Production
  - Allows you to perform Production changes and release new features rapidly, and with confidence.

## Event Driven

- Model your system as a stream of immutable events
  - Valuable for fault-finding, audit and scaling

## API First

- All services should be built with well-defined APIs
  - All data changes should be made through these APIs, with standard controls to ensure both security and scaling

## Cloud Native

- Applications designed to take full advantage of container orchestration and modern cloud platforms, whilst remaining agnostic towards hosting vendors

## SaaS

- Don’t look to build standard functions when they’re readily-available, instead look to favour paying for support licences where necessary (rather than enterprise product licences which can tie you in)

### Design for KSA - The design of the technical stack should be based on the core market, taking into consideration the data rules and requirements of SAMA, and how we might replicate the architecture in other markets


## Page 5

# A typical best in-class digital attacker application architecture has 6 main components

/EXAMPLE

## Comments application architecture

[Figure: Architecture diagram showing a comments application stack with customer interaction, integration, core services, messaging, supporting functions, systems of record, specific payments integrations, and cloud/infrastructure solution. It includes callouts a–f.]

a Front end to be built and owned by Fintech to ensure flexibility, ownership, and speed of change

b ESB - Enterprise Service Bus implements a communication system between mutually interacting software applications in a service-oriented architecture

c Core services with a ‘plug and play’ capability allowing for integrations to 3rd parties and best of breed providers

d Microservices are recommended to ensure modularity of the stack, isolation of issues and ability to change providers easily

e Core banking vendor chosen will depend on the final product roadmap

f Services typically hosted on the cloud as it is more flexible and cost effective


## Page 6

# The choice of licensing option and its impact on technology

## The license structure

[Figure: Diagram showing Bank Co parent entity above Bank Co KSA Branch Architecture, connected to New Fintech (FinTech Co) and Customer, with API’s and BaaS between Bank Co KSA Branch Architecture and New Fintech, plus Strategic partners shown inside the New Fintech box.]

## The wider implications

- Responsible for provision of banking license
- Owner of balance sheet
- BaaS agreement with new Fintech
- Owns KYC / AML

- Separate SAMA Fintech license required
- Owner of customer data / UI & UX interfaces / Data and Analytics / brand and products / customer support and relationships
- New Fintech cannot be deposit taking directly or cannot underwrite loans

## Key technology considerations

- Bank Co KSA Branch architecture needs to be customized to adopt the product suite of the Fintech
- Back end will be owned by Bank Co KSA Branch and thus will require enhancements:
  - New core banking systems will be required to fulfill product requirements (current core banking services corporate customers only)
  - Regulated product enhancements that sit on Branch BS (loans / deposits) need to be built and exposed as a service
  - Regulated KYC, AML feeds will need to be built to supply the fintech ‘as a service’
  - ‘Systems of record’ layer will need to be enabled to accept a RT feed from the fintech

- New front end stack needs to be created to own customer interactions and acquisition
  - API enabled to integrate back into Bank Co KSA branch architecture for reporting and monitoring purposes
  - System of record layer should be replicated in the Fintech to capture customer data for analytics and customer insights
  - Separate reporting line to be created to SAMA
  - 3rd party providers who provide services will have contracts with Fintech (sometimes tripartite agreements will be needed)


## Page 7

# Bank Co KSA: For the Bank Co KSA stack, there are three potential options

[Figure: Comparison of three options for the Bank Co KSA stack, with columns for: 1) Use existing TCS with enhancement, 2) Overlay back-end on top of existing TCS, and 3) Build new core for entire Bank Co KSA. The figure includes Overview, Pros, and Cons sections with bullet points.]


## Page 8

# New Fintech: To implement the front-end (mobile app) there are two options either to buy or to build

[Figure: Comparison graphic showing “Buy and customize” versus “Build” for a fintech mobile app, with pros and cons for each option, plus a recommended option marker under Buy and customize.]


## Page 9

# Potential Architecture Diagram for FinTech Co

[Figure: Main architecture diagram. Caption text: "/ TO BE REFINED DURING BUILD PHASE / DIRECTIONAL"]


## Page 10

# The product capabilities can be translated into 12 technical capabilities with limited level of re-use from Existing Bank Co KSA Branch

[Figure: Large technical capability diagram showing 12 capability areas, reuse legend, and labeled boxes for channels, customer relationship management, access management gateway, customer centric platform, API gateway, product processing, external gateways access, modern data architecture, robust support functions, security, and infrastructure.]

Note: ODS - operational data store  
Source: Bain analysis


## Page 11

# At the beginning of the build phase, we will need to run vendor selection across the stack

[Figure: Provider landscape showing example providers by layer, including front-end, digital onboarding/KYC, PFM, loyalty, real-time marketing, AI chatbots, product config, CRM providers, core banking, and cloud providers, plus a right-side panel of development vendors.]


## Page 12


