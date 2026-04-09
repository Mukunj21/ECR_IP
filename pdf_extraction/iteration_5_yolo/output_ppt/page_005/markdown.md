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