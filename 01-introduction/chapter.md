---
title: "Introduction"
description: "Why automation is a strategic capability, not an infrastructure project, and how this handbook is structured."
---

# Chapter 1: Introduction

## The Problem This Handbook Solves

There is no shortage of resources on network automation tooling. Ansible documentation is exhaustive. Nornir has tutorials. Terraform providers for network devices are well-documented. YouTube has thousands of hours of lab walkthroughs.

And yet, most network automation programmes fail — not because organisations cannot find engineers who know the tools, but because nobody has successfully answered the harder questions:

- Where do we start, given where we actually are today?
- How do we get leadership to fund this and stay committed through the messy middle?
- What do we tackle first — source of truth, scripting, CI/CD, or something else?
- How do we carry the operations team along without creating a two-speed organisation?
- When do we buy a platform versus build our own tooling?
- How do we know if it's working?

These are transformation questions. They sit at the intersection of engineering, organisational design, stakeholder management, and business strategy. No tool tutorial answers them. Most conference talks skip them entirely.

This handbook exists to answer them.

---

## What This Handbook Is

The Network Automation Handbook is a practitioner's guide to network automation transformation — written from the perspective of someone who has run these programmes in a large, regulated financial institution, not from the perspective of a vendor or consultant with a methodology to sell.

It covers the full journey: from assessing where your organisation stands today, through designing and executing a phased transformation, to operating a mature automation platform and progressing toward intent-based, adaptive networking. Each stage is grounded in business outcomes — cost, risk, agility, and resilience — because transformation programmes that cannot articulate their business value do not survive long enough to deliver it.

The handbook is structured so that executives, architects, and transformation leads can all find what they need without reading sections that are not relevant to their role. It is designed to be used, not just read.

---

## What This Handbook Is Not

**It is not a tool tutorial.** Specific tools are discussed in the context of the decisions they inform — categories, trade-offs, and selection criteria. Step-by-step configuration guides and command references are not here. Those resources exist and are easy to find. What is harder to find is guidance on which category of tool to adopt, at which stage of maturity, and why.

**It is not a vendor recommendation.** No tool in this handbook is endorsed. Where specific tools are named — and some are, because abstraction has limits — they are named as illustrations of a pattern or category, not as the answer.

**It is not an academic framework.** There are no proprietary models, no certification levels, and no consulting engagement hidden behind the content. Every framework, template, and example in this handbook is designed to be immediately usable by a practitioner with the authority to act on it.

**It is not a comprehensive engineering reference.** Engineers looking for deep implementation detail on specific toolchains will find the architecture and design thinking here useful, but they will need to combine it with tool-specific documentation. The handbook focuses on what to build and why — not every detail of how to build it.

---

## Who This Is Written For

### Network Infrastructure Leaders and Senior Managers

Directors, Heads of Network Engineering, VPs of Infrastructure, and their equivalents — people who are responsible for the direction of the network function and who must justify investment, manage organisational change, and deliver against business commitments.

For this audience, the handbook provides a strategic framework: how to assess current state, build a phased roadmap, make the business case, and track progress in terms that the rest of the organisation understands. The technical depth is there when you need it, but every chapter leads with the strategic picture.

**Recommended starting points:** [Chapter 2 — Business Alignment](../02-business-alignment/), [Chapter 3 — Maturity Model](../03-maturity-model/), [Chapter 4 — Transformation Roadmap](../04-transformation-roadmap/)

### Automation Architects and Network Architects

Architects responsible for designing the automation platform, the source of truth, the pipeline architecture, and the intent model. People who need to make build-versus-buy decisions, choose between competing patterns, and design systems that will be maintainable by a team that does not yet fully exist.

For this audience, the handbook provides reference architectures, decision frameworks, and the design principles behind each pattern. The ACME Investments worked example runs throughout, providing a consistent, realistic context for every architectural decision.

**Recommended starting points:** [Chapter 5 — Tooling Strategy](../05-tooling-strategy/), [Chapter 6 — Architecture Patterns](../06-architecture-patterns/), [Chapter 11 — Advanced Topics](../11-advanced-topics/)

### Transformation Leads and Programme Managers

The people responsible for actually executing the transformation — managing the backlog, coordinating across teams, running the governance, and keeping the programme moving when organisational friction slows it down.

For this audience, the handbook provides the templates and frameworks that make the transformation manageable: the maturity assessment workshop, the roadmap planning canvas, the stakeholder communication templates, and the metrics framework.

**Recommended starting points:** [Chapter 3 — Maturity Model](../03-maturity-model/), [Chapter 4 — Transformation Roadmap](../04-transformation-roadmap/), [Chapter 10 — People and Skills](../10-people-and-skills/)

---

## How to Use This Handbook

### It Is Modular

Chapters are written to be self-contained. You can start with the maturity model without reading the business alignment chapter. You can read the tooling strategy without having read the architecture patterns chapter. Cross-references are provided throughout so you can follow threads that are relevant to your context without being forced through material that is not.

### It Is Progressive

Within each chapter, content is layered from strategic overview to implementation detail. The opening sections of each chapter give you the picture and the reasoning. Later sections give you the specifics. If you are a senior leader who wants the strategic view without the implementation depth, you can stop reading each chapter when the detail level exceeds what you need.

### Templates Are Meant to Be Used

Every template and checklist in this handbook is designed to be taken into a real organisation and used without modification — or with minor adaptation. They are not illustrative examples of what a template might look like; they are working tools. Each chapter's template set is listed at the end of the chapter and available in the `templates/` directory.

### The ACME Investments Example Is a Thread, Not an Appendix

The worked example — ACME Investments, a fictional but realistic financial services firm — runs throughout the entire handbook. It appears in every chapter that benefits from a concrete example. Rather than introducing a new context each time, the handbook builds ACME's situation progressively so that by the time you reach the advanced topics, you have a detailed, coherent picture of an organisation navigating the transformation journey from Level 1 to Level 5.

---

## Introducing ACME Investments

ACME Investments is a fictional but deliberately realistic financial services firm. It is used throughout this handbook as the running example because network automation in financial services involves a combination of technical complexity, regulatory constraint, and organisational politics that makes it a useful test case for almost any principle.

### The Environment

ACME operates two primary infrastructure environments:

**London datacentre (lon-dc1):** An Arista EOS spine-leaf fabric, built on VXLAN with MLAG and eBGP-EVPN. This is the most mature part of the estate — well-structured, well-understood, and the natural starting point for automation. It runs three security zones: Trading, Corporate, and DMZ, each with distinct policy requirements.

**Branch offices:** A network of regional offices running Cisco IOS, connected via dual WAN with OSPF Area 0 and 802.1Q trunking. The branch network is more heterogeneous and historically less well-documented than the datacentre. It is where automation delivers some of its most visible business value — particularly around provisioning speed.

### The Regulatory Context

ACME is subject to MiFID II, FCA SYSC requirements, and PCI-DSS. These are not background detail — they shape real design decisions throughout the handbook. Audit trails, change authorisation, and policy enforcement are not optional in this environment. One of the recurring themes in the ACME example is how a well-designed automation platform makes compliance easier and cheaper, rather than harder and more expensive.

### The Starting Point

When we first encounter ACME, the network team is transitioning from Level 1 to Level 2 on the maturity model. They have a few engineers who have started scripting. They have no source of truth. Configuration knowledge is unevenly distributed across a team under sustained operational pressure. The Head of Network Engineering has a mandate to modernise the function but limited budget and a sceptical operations organisation.

This is where most real organisations begin. ACME is not a greenfield environment with unlimited budget and a greenfield team — it is a realistic starting point with real constraints.

### Where ACME Gets To

By the end of the handbook, ACME has:
- A YAML-based source of truth (`nodes.yml`, `inventory.yml`) as the single authoritative record of intended network state
- Jinja2 templates rendering device configuration from that source of truth
- A GitLab CI pipeline that validates every change through yamllint, intent verification, Batfish model analysis, and a human approval gate before deployment
- An intent model (`requirements.yml` → `design_intents.yml`) that traces business requirements to design decisions to device configuration
- `generate_branch.py` — a branch provisioning generator that creates a complete, validated configuration set for a new office from a structured specification, with no manual engineering steps

None of this was built in a single phase. The ACME journey through the handbook shows how each capability was built on the foundation of the previous one — and what decisions were made along the way.

---

## The Principles Behind This Handbook

Seven principles run through every chapter. They are worth stating explicitly here, because they represent opinions — not universally agreed positions, but the considered views of someone who has tried the alternatives and found them wanting.

### Configuration is an output, not an input

Engineers should not write device configuration. They should define intent — what the network is supposed to do, what the service requires, what the policy demands — and the automation platform should generate configuration from that intent. This principle shapes every architecture decision in the handbook, from source of truth design to pipeline structure to the role of templates.

Organisations that automate the *writing of configuration* have improved their efficiency. Organisations that automate the *translation of intent into configuration* have changed their operating model. The difference matters.

### Automation is a product, not a project

Automation programmes that are treated as projects — with a scope, a delivery date, and a handover — reliably fail. The tooling is delivered, the team disperses, the automation gradually stops working as the environment evolves, and the organisation concludes that automation doesn't work.

Automation is a platform. Platforms require continuous investment: maintenance, improvement, adoption support, and a team with a backlog. Organisations that treat their automation capability as an internal product — with stakeholders, release cadences, and adoption metrics — are the ones that sustain progress beyond the initial deployment.

### Every line of code you build becomes a product you must support

Every internally built component requires ongoing maintenance. The more you build, the more you must maintain. The right question before building anything is not "can we build this?" but "should we build this, given what it will cost to maintain it?"

Buy or adopt commodity capabilities — source control, CI/CD platforms, telemetry tools. Build only where doing so creates genuine competitive advantage that a commercial product cannot provide. The automation platform's job is to deliver network outcomes, not to demonstrate engineering creativity.

### Do not lose networking expertise while chasing automation

This risk is real and underappreciated. Organisations pursuing automation sometimes deprioritise deep networking knowledge — either by neglecting to retain experienced network engineers, or by allowing automation abstractions to erode the team's understanding of what the network is actually doing.

Automation amplifies engineering expertise. It does not replace it. An automated platform operated by engineers who do not understand BGP, VXLAN, or spanning tree is a liability, not an asset. The transformation should build automation capability alongside networking depth, not in place of it.

### One-touch deployment enables business scalability

When adding a new site requires weeks of engineering effort, the business's ability to act on strategic decisions — enter a new market, open a new office, onboard a new trading venue — is constrained by infrastructure lead time. When adding a new site is a business decision that triggers an automated provisioning workflow, that constraint disappears.

One-touch deployment is not a technical achievement. It is a business capability. The chapter on transformation roadmap ([Chapter 4](../04-transformation-roadmap/)) treats it as such.

### In production, the bottleneck is coordination, not automation

Once automation is mature enough to handle individual change types reliably, the bottleneck shifts. It is no longer the time to execute a change — it is the time to coordinate across the teams that need to approve, review, or act on it.

A network change that requires sign-off from network engineering, security, change management, and an application owner will not be delivered in under an hour regardless of how fast the pipeline runs, if those approvals take 48 hours to obtain. Workflow orchestration — addressed in [Chapter 5](../05-tooling-strategy/) — exists to solve this coordination problem. It is the capability that separates organisations operating at Level 3 from those operating at Level 4.

### Compliance is a by-product of good automation, not a separate workstream

In organisations with manual change processes, compliance is expensive. Evidence has to be assembled, often manually, from change tickets, emails, and engineer recollections. Regulatory reviews consume weeks of engineering time. Controls are enforced through procedure rather than technology — which means they fail whenever the procedure is not followed.

In organisations with mature automation, compliance is largely free. Every change has an audit trail. Every deployment has a diff. Every policy violation is caught in the pipeline before it reaches production. Regulatory evidence is available on demand, generated automatically by the system that delivered the change.

This is not a coincidence. It is the direct result of designing automation with compliance traceability as a first-class requirement, not an afterthought.

---

## A Note on Scope and Bias

This handbook reflects the experience of running network automation programmes in large, regulated financial institutions. This context shapes some of the framing — particularly around compliance, change management, and organisational politics.

The principles and patterns are broadly applicable. The examples are specific to a particular type of enterprise environment. If your organisation is a cloud-native startup, a managed service provider, or a hyperscaler, some of the framing will not map directly to your context. Adapt accordingly.

The handbook is also opinionated. Where there are genuine trade-offs with no universally correct answer, a position is taken and the reasoning is explained. That does not mean the position is always right for your organisation — it means that vague, hedge-everything guidance is less useful than a clear recommendation that you can evaluate and override with full context.

---

## Where to Go Next

The handbook is best entered at the point most relevant to your immediate need. If you are not sure where that is:

- **You need to make a business case for investment:** Start with [Chapter 2 — Business Alignment](../02-business-alignment/)
- **You need to understand where your organisation stands:** Start with [Chapter 3 — Maturity Model](../03-maturity-model/)
- **You need a plan:** Start with [Chapter 4 — Transformation Roadmap](../04-transformation-roadmap/)
- **You need to understand the tool landscape:** Start with [Chapter 5 — Tooling Strategy](../05-tooling-strategy/)
- **You need to understand the architecture:** Start with [Chapter 6 — Architecture Patterns](../06-architecture-patterns/)
- **You need to think about the human side:** Start with [Chapter 10 — People and Skills](../10-people-and-skills/)

If you are starting from the beginning and want the full picture, the chapter order is the intended reading sequence — but even then, feel free to skip ahead when a chapter covers ground you have already navigated in your own organisation.

---

*Next: [What Good Looks Like](../02-what-good-looks-like/chapter) — the destination in concrete terms, from every stakeholder's perspective.*
