
<start_of_page_1>
# FinTech Co – Technology Architecture Strategy

Contacts: Jeff Tijssen, Adam Davis, Ryan Garner, Marc Hochar, Reina Tabbara

May 2022

BAIN &amp; COMPANY

All logos, trademarks, and brand names used belong to their respective owners

This information is confidential and was prepared by Bain &amp; Company solely for the use of our client; it is not to be relied on by any 3rd party without Bain's prior written consent
<end_of_page_1>

<start_of_page_2>
Bain Approach

This deck is a part of a larger compendium. To have a look at more IPs from this case, search for the below case titles on Iris

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

This information is confidential and was prepared by Bain &amp; Company solely for the use of our client; it is not to be relied on by any 3rd party without Bain's prior written consent

BAIN &amp; COMPANY
<end_of_page_2>

<start_of_page_3>
# Technical strategy have catalyzed the economics of digital attackers and neobanks globally

- Modern technology stacks have changed the economics relating to set up and run costs that it has catalyzed new Neobanks and Fintech's globally
- A digital attacker underpinned by cutting edge technology could have a cost base 60-70% lower than a mid-tier traditional bank
- From a servicing perspective, attackers serve 2-3x as many customers per employee as legacy core platform based technology stacks


IMAGE 1 begins...
Sure, here's the extracted text:

---

**Technology Platform**
- Lower unit cost from microservices architecture and rationalized single core
- Software as a service vendors take on upgrades and API based open architectures to simplify the ‘plug-in’ and update processes

**Distribution**
- Transition to digital self-service and digital sales function
- Branchless futures

**Operations**
- Know your customer and fraud solutions that reduce manual intervention

**Central functions**
- Rationalized product portfolio
- Automation tools
- Clean general ledger connections, single core, real-time data for reconciliations
IMAGE 1 ends...



IMAGE 2 begins...
Sure, here is the extracted text from the image:

- $300–$400
- Technology platform
- Distribution
- Operations
- Central functions
- $100–$150
- 60%–70%
- Legacy core platform
- Next-generation platform
IMAGE 2 ends...

Annual cost per retail customer ($)

Source: Bain &amp; Company benchmark data and experience, Thought Machine experience with contributions from Personetics, Onfido TruNarrative and Form3

This information is confidential and was prepared by Bain &amp; Company solely for the use of our client; it is not to be relied on by any 3rd party without Bain's prior written consent

BAIN &amp; COMPANY
<end_of_page_3>

<start_of_page_4>
There are 6 potential architectural principles we need to follow to build the digital attacker

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

- Don't look to build standard functions when they're readily-available, instead look to favour paying for support licences where necessary (rather than enterprise product licences which can tie you in)

Design for KSA - The design of the technical stack should be based on the core market, taking into consideration the data rules and requirements of SAMA, and how we might replicate the architecture in other markets

Note: API – Application Programming Interface, SAMA - Saudi Arabian Monetary Authority, KSA – Kingdom of Saudi Arabia

This information is confidential and was prepared by Bain &amp; Company solely for the use of our client; it is not to be relied on by any 3rd party without Bain's prior written consent

BAIN &amp; COMPANY
<end_of_page_4>

<start_of_page_5>
# A typical best in-class digital attacker application architecture has 6 main components

/EXAMPLE


IMAGE 3 begins...
Certainly! Here's the text extracted from the image:

---

Customer Interaction
- Android
- iOS
- Web
- React / React Native (suggested)

Integration
- Enterprise Service Bus (ESB)

Core services (as microservices) – (supporting SaaS infra - Docker / Kubernetes)
- Identity management
- Onboarding
- Scheme rails integrations
- Non scheme rails integrations
- Account provisioning
- Wallets (tokenisation)
- Fraud / Financial Crime
- Analytics
- Product config
- Rec’s
- Data visualisation
- Messaging / alerts

Messaging - Kafka
- Transactions
- Logging
- Notifications

Supporting functions
- Legal
- Risk
- Treasury
- Marketing
- Consumer / tech ops

Systems of record – 3rd party service
- Ledger
- Regulatory reporting

Specific payments integrations (exposed)
- Swift
- Domestic rails

Cloud / infrastructure solution

---
IMAGE 3 ends...


## Comments application architecture

a Front end to be built and owned by Fintech to ensure flexibility, ownership, and speed of change

b ESB - Enterprise Service Bus implements a communication system between mutually interacting software applications in a service-oriented architecture

c Core services with a ‘plug and play’ capability allowing for integrations to 3rd parties and best of breed providers

d Microservices are recommended to ensure modularity of the stack, isolation of issues and ability to change providers easily

e Core banking vendor chosen will depend on the final product roadmap

f Services typically hosted on the cloud as it is more flexible and cost effective

This information is confidential and was prepared by Bain &amp; Company solely for the use of our client; it is not to be relied on by any 3rd party without Bain's prior written consent

BAIN &amp; COMPANY
<end_of_page_5>

<start_of_page_6>
# The choice of licensing option and its impact on technology

## The license structure


IMAGE 4 begins...
Sure, here is the extracted text from the image:

- Bank Co parent entity
- Bank Co KSA Branch Architecture
- API's
- BaaS
- New Fintech (FinTech Co)
- Strategic partners
- Customer
IMAGE 4 ends...


## The wider implications

- Responsible for provision of banking license
- Owner of balance sheet
- BaaS agreement with new Fintech
- Owns KYC / AML

- Separate SAMA Fintech license required
- Owner of customer data / UI &amp; UX interfaces / Data and Analytics / brand and products / customer support and relationships
- New Fintech cannot be deposit taking directly or cannot underwrite loans

## Key technology considerations

- Bank Co KSA Branch architecture needs to be customized to adopt the product suite of the Fintech
- Back end will be owned by Bank Co KSA Branch and thus will require enhancements:
- New core banking systems will be required to fulfill product requirements (current core banking services corporate customers only)
- Regulated product enhancements that sit on Branch BS (loans / deposits) need to be built and exposed as a service
- Regulated KYC, AML feeds will need to be built to supply the fintech 'as a service'
- 'Systems of record' layer will need to be enabled to accept a RT feed from the fintech

- New front end stack needs to be created to own customer interactions and acquisition
- API enabled to integrate back into Bank Co KSA branch architecture for reporting and monitoring purposes
- System of record layer should be replicated in the Fintech to capture customer data for analytics and customer insights
- Separate reporting line to be created to SAMA
- 3rd party providers who provide services will have contracts with Fintech (sometimes tripartite agreements will be needed)

This information is confidential and was prepared by Bain &amp; Company solely for the use of our client; it is not to be relied on by any 3rd party without Bain's prior written consent

BAIN &amp; COMPANY
<end_of_page_6>

<start_of_page_7>
# Bank Co KSA: For the Bank Co KSA stack, there are three potential options

|   | 1 Use existing TCS with enhancement | 2 Overlay back-end on top of existing TCS | 3 Build new core for entire Bank Co KSA  |
| --- | --- | --- | --- |
|  Overview | TCS is currently used in Bank Co KSA
Re-use elements of TCS where applicable and buy missing functionalities required for the digital attacker from TCS | Re-use elements of TCS where applicable
Buy missing functionalities that are required for the digital attacker from a different vendor e.g. Mambu and connect to existing stack | Build new core banking system for entire Bank Co KSA and migrate the legacy corporate bank to the new system as well  |
|  Pros | Quick time to market
Fit for purpose if product suite is limited and roadmap is traditional | Fit for purpose in supporting innovative CVPs
Allows Bank Co KSA to have a separate system for the Fintech and do BaaS with other entities in the future
No impact on existing activities / customers
Higher agility (with new vendor specialized in digital banks)
Allows for Opex costs (SaaS) vs. Capex for TCS configuration
Maintenance to be provided by the SaaS vendor | Fit for purpose in supporting innovative CVPs
Allows Bank Co KSA to do BaaS with other entities in the future
Higher agility (with new vendor specialized in digital banks)
Allows for Opex costs (SaaS) vs. Capex for TCS configuration  |
|  Cons | Requires Capex for configuration and to sustain volumes for retail banking
Basic product configurations & limited cutting-edge digital technologies (e.g.: BNPL)
Lacks API enabled back-end infrastructure (modern front-end will be difficult to integrate)
Requires in-house maintenance | Integration can get complex and require time | Additional time to market required
Migration is complex and will interrupt current business
Requires significant capital  |

Final decision to be made once detailed architecture design is completed

This information is confidential and was prepared by Bain &amp; Company solely for the use of our client; it is not to be relied on by any 3rd party without Bain's prior written consent

BAIN &amp; COMPANY
<end_of_page_7>

<start_of_page_8>
# New Fintech: To implement the front-end (mobile app) there are two options either to buy or to build

|   | Buy and customize | Build  |
| --- | --- | --- |
|  Pros | + Faster time to market
+ Easier to maintain due to vendor maintenance support
+ Solutions offered have been tried and tested | + Added differentiation and flexibility as the front-end is built from scratch
+ Team capabilities can grow by working closely with vendors, thereby retaining knowledge through build and run  |
|  Cons | + Significant upfront capital spend
- Might require multiple customizations to fit the features that are required for FinTech Co
Recommended Option | + Will take significant time to build from scratch
- Limited development talent in the market and in-house (not an internal core competency)
- Difficult to maintain as maintenance activities will need to be done by in-house resources  |

This information is confidential and was prepared by Bain &amp; Company solely for the use of our client; it is not to be relied on by any 3rd party without Bain's prior written consent

BAIN &amp; COMPANY
<end_of_page_8>

<start_of_page_9>
# Potential Architecture Diagram for FinTech Co

/ TO BE REFINED DURING BUILD PHASE / DIRECTIONAL

Reuse/enhance Buy


IMAGE 5 begins...
Sure! Here is the extracted text from the image:

- Mobile App
- Mobile App Server
- Onboarding
- Payments
- Accounts
- Cards
- Loans
- PFM
- SMS
- ...
- Fintech
- Customer Relationship Mgmt.
- Digital marketing
- Data
- Cust. 360 view
- Behavior analytics
- Support functions
- Finance
- Procurement
- HR
- Fraud
- Risk mgmt.
- ...
- ESB (Enterprise Service Bus)
- Back End
- Overlay new back-end on top of existing TCS
- Deposit
- Loan servicing
- Card mgmt. (TBC)
- Data architecture
- Warehouse (TBC)
- Real-time stream
- Big data datalakes
- ETL (TBC)
- ODS
- Dashboard
- External gateway integrations
- E-payments
- POS/ ATM
- TCS Bancs (Existing)
- Reporting
- Ledger
- Payment
- Bank Co KSA Branch
- Support functions
- Finance
- Procurement
- Audit & compliance
- Treasury
- Risk mgmt.
- ...
IMAGE 5 ends...


This information is confidential and was prepared by Bain &amp; Company solely for the use of our client; it is not to be relied on by any 3rd party without Bain's prior written consent

BAIN &amp; COMPANY
<end_of_page_9>

<start_of_page_10>
# The product capabilities can be translated into 12 technical capabilities with limited level of re-use from Existing Bank Co KSA Branch

/ TO BE REFINED DURING BUILD PHASE / DIRECTIONAL

1. Innovative customer-facing channels

Digital (mobile, web, tablet, etc.)

Remote (call center, self service, etc.)

Ecosystem partners access (Open API, monetization API)

|  Digital Marketing | Campaign mgmt. | Customer 360 view | Forward looking insights | Customer feedbacks | Real-time marketing | Customer data & loyalty | User behavior analytics  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  3. Access management gateway | 4. Customer centric platform | 5. API gateway | 6. Highly automated product processing | 7. External gateways access  |
| --- | --- | --- | --- | --- |
|  Customer IDM | Omni channel business rule engine | Micro-services | Central product processing Business rule engine | POS/ATM  |
|  API security | Document management |  | Product processing | PPS/ATM  |
|  2FA/ OTP capability | Enterprise workflow engine |  | Deposit | E-payments  |
|  Biometrics / E-KYC | Digital Signature |  | Payment | Payment network  |
|   |  |  | Card mgmt. | Card scheme  |
|   |  |  | Loan servicing/admin. | SMS/ Push notification  |
|   |  |  | Loyalty | Social media  |
|   |  |  | PFM |   |
|   |  |  | E-statement solution |   |
|  8. Modern data architecture  |   |   |
| --- | --- | --- |
|  Real-time stream analytics | Big data datalakes | Reporting  |
|  ODS | Data warehouse | ETL  |
|   |  | Dashboard  |
|  9. Robust support functions  |   |   |
| --- | --- | --- |
|  Legal | Audit & Compliance | Finance Treasury  |
|  Risk mgmt | HR | Enterprise Scheduler  |
|   |  | Finance  |
|  10. Security  |   |   |
| --- | --- | --- |
|  API security | SIEM |   |
|  FIM | PAM |   |
|  Security Testing / Assessment |   |   |
|  11. Infrastructure  |   |
| --- | --- |
|   | Data center  |
|  Network | Other  |

Note: ODS - operational data store
Source: Bain analysis

This information is confidential and was prepared by Bain &amp; Company solely for the use of our client; it is not to be relied on by any 3rd party without Bain's prior written consent

BAIN &amp; COMPANY
<end_of_page_10>

<start_of_page_11>
At the beginning of the build phase, we will need to run vendor selection across the stack


IMAGE 6 begins...
```plaintext
EXAMPLE PROVIDERS

Front-end
BACKBASE

Digital onboarding / KYC providers
aion
e&, ShuftiPro, hooyu, JUMIO, Kastle, IDEMIA, onfido, Daon

PFM
STRANDS, meniga, MX, CSI, Geezeo

Loyalty
ICC fintech, AIMIA, BRAND LOYALTY, COLLINS, EPSILON

Real time marketing
evergage, BOXEVER, epl, W.UP

AI Chatbots
ACTIVE.Ai, Finn AI, Kasisto

Product Config
ZAFIN

CRM Providers
salesforce, Microsoft Dynamics

Core Banking
MAMBU, TCS BANCS, TEMENOS, ORACLE

Cloud providers
mobily, STC, DETASAD, ORACLE

Existing Bank Co vendors (checkbox)

Development vendors
FINANTEQ
Front-end developers

software AG
API developers

vacuumlabs
E2E development capability

endava
E2E development capability
```
IMAGE 6 ends...


This information is confidential and was prepared by Bain &amp; Company solely for the use of our client; it is not to be relied on by any 3rd party without Bain's prior written consent

BAIN &amp; COMPANY
<end_of_page_11>

<start_of_page_12>
BAIN &amp; COMPANY
4
<end_of_page_12>
