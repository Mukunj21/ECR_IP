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