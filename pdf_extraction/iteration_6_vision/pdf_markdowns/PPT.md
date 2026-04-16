## Start of Page 1

## FinTech Co – Technology Architecture Strategy

Contacts: Jeff Tijssen, Adam Davis, Ryan Garner, Marc Hochar, Reina Tabbara

May 2022

---

All logos, trademarks, and brand names used belong to their respective owners.  
This information is confidential and was prepared by Bain & Company solely for the use of our client. It is not to be relied on by any 3rd party without Bain’s prior written consent.

![Figure: Bain & Company Logo]

## Start of Page 2

```markdown
## Bain Approach

![Figure: Description of the image](#)

> This deck is a part of a larger compendium. To have a look at more IPs from this case, search for the below case titles on Iris

### POVs and Market Overviews

- Consumer Preferences towards Financial Services Needs POV (KSA, 2022)
- Consumer Preferences towards Financial Services Needs POV (UAE, 2022)
- SME Banking Needs POV (KSA, 2022)
- Digital Attacker Benchmarks and Financial Services Market Trends POV (KSA and UAE, 2021)
- Retail and SME Banking Overview (KSA, 2020)

### Case examples

- FinTech Co – Roadmap to build a Digital Attacker
- **FinTech Co – Technology Architecture Strategy**
- Fintech Co – Regulatory Considerations and building BaaS Agreement with Bank Co
- Fintech Co – Building a Digital Attacker Operating Model

---

This information is confidential and was prepared by Bain & Company solely for the use of our client. It is not to be relied on by any 3rd party without Bain's prior written consent
```

## Start of Page 3

## Technical Strategy Have Catalyzed the Economics of Digital Attackers and Neobanks Globally

- Modern technology stacks have **changed the economics** relating to set up and run costs that it has catalyzed new Neobanks and Fintech’s globally
- A digital attacker **underpinned by cutting edge technology** could have a cost base **60-70% lower than a mid-tier traditional** bank
- From a servicing perspective, attackers serve **2-3x as many customers per employee as legacy** core platform based technology stacks

### Technology Platform
- **Lower unit cost** from microservices architecture and rationalized single core
- **Software as a service** vendors take on upgrades and API based open architectures to simplify the ‘plug-in’ and update processes

### Distribution
- Transition to **digital self-service and digital sales function**
- Branchless futures

### Operations
- **Know your customer and fraud** solutions that **reduce manual intervention**

### Central Functions
- Rationalized product portfolio
- Automation tools
- Clean **general ledger connections, single core, real-time** data for reconciliations

![Figure: Annual cost per retail customer ($)] 

- **60%—70%**
  - $300—$400
  - Technology platform
- **$100—$150**
  - Distribution
  - Operations
  - Central functions
  - Legacy core platform
  - Next-generation platform

---

_Sources:_ Bain & Company benchmark data and experience, Thought Machine experience with contributions from Personetics, Onfido TruNarrative and Form3

>This information is confidential and was prepared by Bain & Company solely for the use of our client. It is not to be relied on by any 3rd party without Bain’s prior written consent.

## Start of Page 4

## There are 6 potential architectural principles we need to follow to build the digital attacker

### Microservice Architecture

- Design your services as microservice architectures - small modular services
  - Allows different parts of the system to be scaled in and out based on demand
  - Allows parts of the system to be upgraded in isolation

### Event Driven

- Model your system as a stream of immutable events
  - Valuable for fault-finding, audit, and scaling

### Cloud Native

- Applications designed to take full advantage of container orchestration and modern cloud platforms, whilst remaining agnostic towards hosting vendors

### Automated and Immutable

- Put in place full automation around the build and deployment, creating artefacts that are versioned and immutable through to Production
  - Allows you to perform Production changes and release new features rapidly, and with confidence

### API First

- All services should be built with well-defined APIs
  - All data changes should be made through these APIs, with standard controls to ensure both security and scaling

### SaaS

- Don't look to build standard functions when they’re readily-available, instead look to favour paying for support licences where necessary (rather than enterprise product licences which can tie you in)

---

**Design for KSA - The design of the technical stack should be based on the core market, taking into consideration the data rules and requirements of SAMA, and how we might replicate the architecture in other markets**

---

*Note: API – Application Programming Interface, SAMA - Saudi Arabian Monetary Authority, KSA – Kingdom of Saudi Arabia*

*This information is confidential and was prepared by Bain & Company solely for the use of our client. It is not to be relied on by any 3rd party without Bain’s prior written consent.*

---


## Start of Page 5

```markdown
## A typical best in-class digital attacker application architecture has 6 main components

![Figure: Diagram of application architecture components]  

### Comments application architecture

#### a
- **Front end to be built and owned by Fintech**  
  to ensure flexibility, ownership, and speed of change

#### b
- **ESB - Enterprise Service Bus** implements a  
  communication system between mutually interacting  
  software applications in a service-oriented architecture

#### c
- Core services with a **‘plug and play’ capability**  
  allowing for **integrations to 3rd parties** and best of breed providers

#### d
- **Microservices** are recommended to ensure  
  **modularity of the stack, isolation of issues**  
  and ability to **change providers** easily

#### e
- **Core banking vendor** chosen will depend on  
  the **final product roadmap**

#### f
- **Services typically hosted on the cloud** as it is  
  more flexible and cost effective

---

### Architecture Components

#### Customer Interaction
|     |     |     |
|-----|-----|-----|
| Android | iOS | Web |
| | **React / React Native (suggested)** | |

#### Integration
|---------------------------|
| Enterprise Service Bus (ESB) |

#### Core services (as microservices) – (supporting SaaS infra - Docker / Kubernetes)
|                    |                         |
|--------------------|-------------------------|
| Identity management | Onboarding             |
| Scheme rails integrations | Non scheme rails integrations |
| Account provisioning | Wallets (tokenisation) |
| Fraud / Financial Crime | Analytics            |
| Product config | Rec’s                    |
| Data visualisation | Messaging / alerts      |

#### Messaging - Kafka
|                 |
|-----------------|
| Transactions    |
| Logging         |
| Notifications   |

#### Systems of record – 3rd party service
|        |                     |
|--------|---------------------|
| Ledger | Regulatory reporting|

#### Supporting functions
|       |            |          |
|-------|------------|----------|
| Legal | Risk       | Treasury |
| Marketing | Consumer / tech ops | 

#### Specific payments integrations (exposed)
|       |                  |
|-------|------------------|
| Swift | Domestic rails   |

#### Cloud / infrastructure solution

---

This information is confidential and was prepared by Bain & Company solely for the use of our client. It is not to be relied on by any 3rd party without Bain’s prior written consent.
```


## Start of Page 6

```markdown
## The choice of licensing option and its impact on technology

### The license structure

![Figure: The license structure diagram](#)

- **Bank Co parent entity**

- **Bank Co KSA Branch Architecture**

  - APIs
  - BaaS

- **New Fintech (FinTech Co)**

  - Strategic partners

  - Customer

### The wider implications

- Responsible for provision of banking license
- Owner of balance sheet
- BaaS agreement with new Fintech
- Owns KYC / AML

---

- Separate SAMA Fintech license required
- Owner of customer data / UI & UX interfaces / Data and Analytics / brand and products / customer support and relationships
- New Fintech cannot be deposit taking directly or cannot underwrite loans

### Key technology considerations

- Bank Co KSA Branch architecture needs to be customized to adopt the product suite of the Fintech

- **Back end will be owned by Bank Co KSA Branch** and thus will require enhancements:
  - New core banking systems will be required to fulfill product requirements (current core banking services corporate customers only)
  - Regulated product enhancements that sit on Branch BS (loans / deposits) need to be built and exposed as a service
  - Regulated KYC, AML feeds will need to be built to supply the fintech ‘as a service’
  - ‘Systems of record’ layer will need to be enabled to accept a RT feed from the fintech

---

- **New front end stack needs to be created to own customer interactions and acquisition**
  - API enabled to integrate back into Bank Co KSA branch architecture for reporting and monitoring purposes
  - System of record layer should be replicated in the Fintech to capture customer data for analytics and customer insights
  - Separate reporting line to be created to SAMA
  - 3rd party providers who provide services will have contracts with Fintech (sometimes tripartite agreements will be needed)

---
```


## Start of Page 7

```markdown
## Bank Co KSA: For the Bank Co KSA stack, there are three potential options

### Overview

1. **Use existing TCS with enhancement**
2. **Overlay back-end on top of existing TCS**
3. **Build new core for entire Bank Co KSA**

### Pros

- **Use existing TCS with enhancement**
  - TCS is currently used in Bank Co KSA
  - **Re-use elements of TCS** where applicable and **buy missing functionalities** required for the digital attacker from TCS
  - ➕ Quick time to market
  - ➕ Fit for purpose if product suite is limited and roadmap is traditional

- **Overlay back-end on top of existing TCS**
  - **Re-use elements of TCS where applicable**
  - **Buy missing functionalities** that are required for the digital attacker from a different vendor e.g. Mambu and connect to existing stack
  - ➕ Fit for purpose in supporting innovative CVPs
  - ➕ Allows Bank Co KSA to have a **separate system for the Fintech** and do BaaS with other entities in the future
  - ➕ No impact on existing activities / customers
  - ➕ Higher agility (with new vendor specialized in digital banks)
  - ➕ Allows for **Opex costs (SaaS) vs. Capex for TCS configuration**
  - ➕ Maintenance to be provided by the SaaS vendor

- **Build new core for entire Bank Co KSA**
  - Build new core banking system for entire Bank Co KSA and migrate the legacy corporate bank to the new system as well
  - ➕ Fit for purpose in supporting innovative CVPs
  - ➕ Allows Bank Co KSA to do BaaS with other entities in the future
  - ➕ Higher agility (with new vendor specialized in digital banks)
  - ➕ Allows for Opex costs (SaaS) vs. Capex for TCS configuration

### Cons

- **Use existing TCS with enhancement**
  - 🔴 Requires Capex for configuration and to sustain volumes for retail banking
  - 🔴 Basic product configurations & limited cutting-edge digital technologies (e.g.: BNPL)
  - 🔴 Lacks API enabled back-end infrastructure (modern front-end will be difficult to integrate)
  - 🔴 Requires in-house maintenance

- **Overlay back-end on top of existing TCS**
  - 🔴 Integration can get complex and require time

- **Build new core for entire Bank Co KSA**
  - 🔴 Additional time to market required
  - 🔴 Migration is complex and will interrupt current business
  - 🔴 Requires significant capital

---

**Final decision to be made once detailed architecture design is completed**
```

## Start of Page 8

```markdown
## New Fintech: To implement the front-end (mobile app) there are two options either to buy or to build

| Buy and customize                                                                     | Build                                                                                   |
|---------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| ![Figure: Image of document signing]                                                  | ![Figure: Image of coding on screens]                                                   |

### Pros
- **Faster time to market**
- **Easier to maintain** due to vendor maintenance support
- **Solutions offered have been tried and tested**

### Cons
- **Significant upfront capital spend**
- Might require **multiple customizations** to fit the features that are required for FinTech Co

#### Recommended Option

#### Pros
- **Added differentiation and flexibility** as the front-end is built from scratch
- **Team capabilities can grow by working closely with vendors**, thereby retaining knowledge through build and run

#### Cons
- Will take **significant time to build** from scratch
- **Limited development talent** in the market and **in-house** (not an internal core competency)
- **Difficult to maintain** as maintenance activities will need to be done by in-house resources

---

*This information is confidential and was prepared by Bain & Company solely for the use of our client. It is not to be relied on by any 3rd party without Bain's prior written consent.*

![Bain & Company Logo]
```


## Start of Page 9

```markdown
## Potential Architecture Diagram for FinTech Co

*To Be Refined During Build Phase / Directional*

### Fintech

- **Mobile App**

### Mobile App Server

| Onboarding | Payments | Accounts | Cards | Loans | PFM | SMS | ... |
|------------|----------|----------|-------|-------|-----|-----|-----|

### Customer Relationship Mgmt.

| Digital marketing | Data |  
|-------------------|------|
| Cust. 360 view    | Behavior analytics |

### Support functions

| Finance | Procurement |
|---------|-------------|
| HR      | Fraud       |
| Risk mgmt. | ...      |

---

### ESB (Enterprise Service Bus)

---

### Back End

- **Overlay new back-end on top of existing TCS**

| Deposit   | Loan servicing | Card mgmt.(TBC) |
|-----------|----------------|-----------------|

#### Data architecture

| Warehouse (TBC) | Real-time stream  |
|-----------------|-------------------|
| Big data datalakes | ETL (TBC)      |
| ODS              | Dashboard        |

#### External gateway integrations

| E-payments  | POS/ATM |
|-------------|---------|

#### TCS Bancs (Existing)

| Ledger | Payment |
|--------|---------|

### Support functions

| Finance | Procurement |
|---------|-------------|
| Audit & compliance | Treasury |
| Risk mgmt. | ...      |

---

![Figure: Potential Architecture Diagram for FinTech Co]

---

*This information is confidential and was prepared by Bain & Company solely for the use of our client. It is not to be relied on by any 3rd party without Bain's prior written consent.*

Bain & Company

Page 9
```

## Start of Page 10

## Product Capabilities

The product capabilities can be translated into 12 technical capabilities with limited level of re-use from Existing Bank Co KSA Branch.

---

### Legend

- Reuse and enhance ![#d3e9e0](https://via.placeholder.com/15/d3e9e0?text=+) 
- Bank Co KSA Branch ![#e3e1c1](https://via.placeholder.com/15/e3e1c1?text=+) 
- Non Available ![#ffffff](https://via.placeholder.com/15/ffffff?text=+)
- Fintech ![#ff6060](https://via.placeholder.com/15/ff6060?text=+) 
- Cannot be re-used ![#ff6060](https://via.placeholder.com/15/ff6060?text=+) 
- TBC ![#ffaaaa](https://via.placeholder.com/15/ffaaaa?text=+) 

---

### 1. Innovative customer-facing channels

- Digital (mobile, web, tablet, etc.)
- Remote (call center, self service, etc.)
- Ecosystem partners access (Open API, monetization API)

### 2. Customer relationship management

- Digital Marketing
- Campaign mgmt.
- Customer 360 view
- Forward looking insights
- Customer feedbacks
- Real-time marketing
- Customer data & loyalty
- User behavior analytics

### 3. Access management gateway

- Customer IDM
- API security
- 2FA/ OTP capability
- Biometrics / E-KYC

### 4. Customer centric platform

- Omni channel business rule engine
- Document management
- Enterprise workflow engine
- Digital Signature

### 5. API gateway

- Microservices

### 6. Highly automated product processing

#### Central product processing

- Business rule engine

#### Product processing

- Deposit
- Payment
- Card mgmt.
- Loan servicing/admin.
- Loyalty
- PFM
- E-statement solution

### 7. External gateways access

- POS/ ATM
- E-payments
- Payment network
- Card scheme
- SMS/ Push notification
- Social media

### 8. Modern data architecture

- Real-time stream analytics
- Big data datalakes
- ODS
- Data warehouse
- Reporting
- SAMA reporting
- ETL
- Dashboard

### 9. Robust support functions

- Legal
- Audit & Compliance
- Risk mgmt
- Finance Treasury
- Enterprise Scheduler
- Procurement
- HR

### 10. Security

- API security
- SIEM
- FIM
- PAM
- Security Testing / Assessment

### 11. Infrastructure

- Data center
- Network
- Other

### 12. Modern integration layer

---

![Figure: Diagram of technical capabilities and external integrations]

---

**Note:** ODS - operational data store  
**Source:** Bain analysis

---

_This information is confidential and was prepared by Bain & Company solely for the use of our client. It is not to be relied on by any 3rd party without Bain's prior written consent._  
**Bain & Company**

## Start of Page 11

## Vendor Selection at the Build Phase

At the beginning of the build phase, we will need to run vendor selection across the stack.

![Figure: Example Providers Table]

### Example Providers

|                                       |                                               |
|---------------------------------------|-----------------------------------------------|
| **Front-end**                         | BACKBASE                                      |
| **Digital onboarding / KYC providers**| Daon, Onfido, IDEMIA, Jumio, ShuftiPro, Eyeon |
| **PFM**                               | STRANDS, Meniga, MX, CSI, Geezeo              |
| **Loyalty**                           | Fintech, AIMIA, BOND, Collinson, EPSILON      |
| **Real time marketing**               | EVERGAGE, Boxever, Epi, W.UP                  |
| **AI Chatbots**                       | ACTIVE.AI, Finn AI, Kasisto                   |
| **Product Config**                    | ZAFIN                                        |
| **CRM Providers**                     | Salesforce, Microsoft Dynamics                |
| **Core Banking**                      | Mambu, TCS, BOCNS, Temenos, Oracle            |
| **Cloud providers**                   | Mobily, STC, Detsad, Oracle                   |

### Development Vendors

- **FINANTEQ**
  - Front-end developers
- **Software AG**
  - API developers
- **Vacuumlabs**
  - E2E development capability
- **Endava**
  - E2E development capability

_This information is confidential and was prepared by Bain & Company solely for the use of our client; it is not to be relied on by any 3rd party without Bain's prior written consent._

## Start of Page 12

The page appears to only contain the logo, "BAIN & COMPANY," without additional text, tables, or images to convert into Markdown content.

