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