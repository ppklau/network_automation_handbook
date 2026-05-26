---
title: "What Good Looks Like"
description: "The destination in concrete terms — what a well-automated network looks like for every stakeholder in a financial services organisation."
---

# What Good Looks Like

The case for network automation is often made in percentages: a 70% reduction in change-related incidents, 40% less operational overhead, compliance evidence available in minutes rather than days. These numbers are real. They are in the chapters that follow. But percentages do not make people want to embark on a difficult transformation.

What makes people want to start is a clear picture of the destination — what the working day looks like when it is done, what conversations become possible, what stops consuming energy. This chapter provides that picture. It is written for every person who needs to understand what they are working toward: the Head of Networks, the engineering and operations teams who will build and run the automated platform, and the business leaders who are being asked to support, fund, or adapt to the change.

---

## The Head of Networks

The Head of Networks occupies a structurally difficult position in most financial services firms. They sit between a business that wants things delivered faster and more reliably, and a team that is running at capacity keeping the current environment stable. Every commitment to the business involves a private calculation: who is available, what is in the change window, what could go wrong, how confident can I be. The honest answer to "can we have this by Thursday?" is often "probably not" — and explaining why to a CTO or Head of Trading Technology requires either going technical, which does not land, or saying "we're busy," which does not inspire confidence.

Compounding this, much of the knowledge the team needs to function reliably lives in the heads of two or three senior engineers. The Head of Networks knows this. They know what happens when those people go on holiday, when they are headhunted, when they are simultaneously managing two incidents and a change. The resilience of the operation is more fragile than anyone outside the team realises.

### Commitments become keepable

In a well-automated environment, delivery reliability is a property of the platform, not a function of individual availability. Standard connectivity requests flow through the pipeline with predictable timelines. Non-standard requests have a clear assessment path. The Head of Networks can give a firm answer to "can we have this by Thursday?" — and mean it.

### The leadership conversation changes

When the Head of Networks walks into a quarterly review with the CTO and CISO, they can speak in the same register as their peers: change success rate, lead time trend, incident frequency, pipeline adoption. These are not metrics assembled manually the night before — they are live on a dashboard. The conversation shifts from managing expectations to discussing strategy.

### The on-call burden lightens

The automated monitoring layer detects most fault categories before they become incidents. Self-healing handles a defined set of known fault patterns without human intervention. When the Head of Networks is called at 2am, it is because something genuinely novel has occurred and a decision is needed — not because a process needs executing.

### Good engineers stay when the work is interesting

Engineers whose days are spent on interesting problems stay. Engineers who spend their days executing the same CLI commands do not. When the work shifts from routine execution to design, automation development, and platform improvement, the job becomes one that technically strong engineers want to do — and the talent retention picture changes accordingly.

### Compliance stops being a crisis

The audit evidence is in the pipeline, complete and on demand. The quarterly review with the CISO becomes a fifteen-minute conversation rather than a three-day preparation exercise. The question "can you demonstrate that this change was properly authorised and tested?" has an immediate, complete answer.

The sections that follow describe what this transformation looks like from the perspective of each stakeholder the Head of Networks needs to bring along. The language in those sections is the vocabulary for those conversations.

---

## Network Engineering

The engineers who carry deep expertise in routing, switching, and security architecture spend a disproportionate share of their time on work that does not use that expertise. Configuration generation, change execution, manual verification — these tasks require care and discipline, but not the advanced technical judgment that senior network engineers were hired to provide. The mismatch between capability and daily activity is a persistent source of frustration for the engineers and waste for the organisation.

There is a second, less visible problem. Much of the knowledge that underpins good network design lives inside the heads of the engineers who built it. The routing policy exists because of a specific regulatory requirement. The VLAN architecture reflects a design decision made five years ago in response to a segmentation incident. The BGP timer was set non-standard for a reason that was significant at the time. None of this is written down in a form that survives the turnover of the people who knew it. Every time an engineer leaves, the organisation loses not just a person but a body of reasoning that is not recoverable. Their replacement inherits configurations, not the understanding behind them.

### The design becomes the deployment

When an engineer defines an intent model, updates a routing policy template, or encodes a new security zone standard, they are not writing documentation to be filed alongside the device configuration. They are writing the mechanism by which the network will be configured. The design and the implementation are the same artefact. There is no gap between what the architect specified and what was deployed, because the configuration was not written by an operator — it was rendered by the platform from the engineer's specification.

### Standards are enforced by the platform, not by memory

The pipeline checks every proposed change against the design standards before any device is touched. If a change violates the routing policy, assigns a device to the wrong security zone, or misses a mandatory configuration element, the pipeline rejects it. The engineer's standards are not a document that operators are expected to have read and memorised — they are encoded in the test suite that every change must pass. This changes the nature of the engineering role: from "I have to check whether operations followed my design" to "the platform ensures my design is followed."

### Intent survives churn

The engineer who designed the BGP policy writes the reasoning into the intent model: the business requirement, the regulatory driver, the design decision, the constraints it places on future changes. Three years later, a new engineer inherits that model. They do not find an opaque configuration and have to reconstruct the reasoning — they find an explicit statement of intent that tells them what the configuration is doing, why it exists, and what would break if it changed. Large organisations have constant churn. A well-structured intent model means the reasoning survives that churn. The knowledge that previously walked out of the door with departing engineers now stays in the codebase.

---

## Network Operations

Operations teams feel the weight of manual network management most directly. They are the people executing changes in production, working carefully through CLI commands in the early hours of Saturday morning, carrying the anxiety that a single mistyped command on the wrong device can take trading systems offline. They are also, paradoxically, the group who most clearly understand the patterns — the recurring fault types, the repetitive change procedures, the known-good configurations applied again and again across identical device types.

That pattern knowledge is the foundation of something important, and in most operations teams it is completely untapped.

### Solve every problem once

In a manual environment, when a fault occurs, the reflex is to fix it: diagnose the issue, apply the fix, document it, close the ticket. In an automated operations environment, the reflex is different: fix it, and then automate the fix so that no engineer ever has to manually resolve this category of problem again. This discipline is not imposed from outside — it becomes the natural way of working once engineers have experienced what it feels like when a recurring problem permanently disappears from the workload.

### The workload compounds downward

Each automated problem category is an incident type, a routine change procedure, a compliance check that no longer requires a human to execute. The on-call burden does not stay constant — it falls each year as automation coverage expands. The engineers who have been through this trajectory describe it consistently: the job in year four is genuinely different from the job in year one, and it is better.

### Changes become oversight, not execution

A change enters the pipeline as a structured request. The pipeline generates the configuration, validates it against design standards and the topology model, and presents it for review. Operations confirms the intent is correct and approves deployment. The pipeline executes. Operations monitors the outcome. The anxiety of live CLI execution in production does not disappear entirely — break-glass access for genuine emergencies remains available — but it is no longer the standard mode of operation.

### Projects arrive as specifications, not instructions

Under the current model, a project to provision a new branch site produces a detailed change document — dozens of pages — that operations must execute across multiple devices over several days, managing dependencies and verifying intermediate states manually. In a mature automated environment, the project produces a structured specification: site name, location, connectivity parameters, security zone assignment, approved design pattern. The pipeline generates the complete configuration, validates it, and deploys it. Operations reviews the specification and the pipeline output, approves, and monitors. The expertise shifts from "I can execute this correctly" to "I can assess whether this is right" — a higher-value application of the same knowledge.

---

## The Head of Trading Technology

Trading infrastructure operates under a specific commercial constraint: the speed at which new connectivity can be established is a competitive variable. Venues, dark pools, exchanges, data feeds — the ability to bring new connections live faster than a competitor is directly linked to business outcomes. Under a manual operations model, new venue connectivity is a project: scoped, scheduled, implemented, and reviewed over two to three weeks.

### Venue connectivity in hours, not weeks

In a well-automated environment, venue connectivity follows a templated pattern. A structured specification — the venue's BGP parameters, the required firewall policy rules, the VLAN allocation — is submitted to the provisioning workflow. The pipeline generates the complete configuration, validates it against the existing topology model, runs the policy compliance checks, and presents the result for review. A network engineer reviews the intent — not two hundred lines of CLI, but a clear description of what is being connected and how. Commercial agreement on Monday, live on Tuesday.

### Infrastructure leaves the critical path

The Head of Trading Technology's conversation with the business development team changes permanently. The question "how long does it take to bring new venue connectivity live?" has a different answer. Infrastructure lead time stops being a variable in commercial planning. New market opportunities are no longer constrained by network project timelines.

### The network exits the incident timeline

Network configuration errors stop appearing as contributing factors in trading infrastructure post-incident reviews. The configuration that reaches production has been validated before deployment. The possibility of a manual error during a high-pressure change causing a trading outage during market hours — a real and recurring source of operational risk — is dramatically reduced. The network team stops being a feature of the incident timeline.

---

## The CISO and Head of Information Security

Two things define the security posture of a financial firm's network: how reliably policy is enforced, and how completely changes can be evidenced. In a manual change environment, both are structurally compromised. Policy enforcement depends on people remembering the standards and applying them correctly under pressure. Evidence depends on someone assembling it retrospectively from change tickets and configuration snapshots. Neither is reliable at scale.

### Policy violations are caught before deployment

Every proposed change is checked against the security policy model before any device is touched. A misconfiguration that would allow traffic across zone boundaries is caught before deployment, not discovered in a quarterly audit. The CISO's exposure is the gap between when a new policy requirement is defined and when it is encoded in the pipeline — a gap measured in days, and a conscious, manageable decision. This is categorically different from the alternative: a gap measured in months, driven by the probability that someone notices a violation in a periodic review.

### Audit evidence is ready on demand

An auditor arrives for an FCA review. Under the current model, the network team spends two to three days assembling evidence: configuration snapshots cross-referenced against change management records, annotated to explain the gaps. In the target state, the auditor's question is answered from the pipeline record: the original request, the approval chain, the validation results, the configuration diff, the deployment timestamp, the post-deployment verification. Every element is present, immutable, and instantly accessible. Audit preparation time falls not because the team gets faster, but because the evidence is generated automatically by the system that delivered the change.

### Drift is detected, not discovered

When a device's running configuration diverges from the intended state — a manual change made outside the pipeline, an error introduced during an emergency — it is detected and flagged immediately. The CISO's view of the network's security posture is current and objective, not a periodic inference drawn from audit activity.

---

## The Chief Risk Officer

Operational resilience has become a board-level concern in financial services, driven by regulatory requirements that demand demonstrable capability rather than asserted compliance. In a manual operations environment, change risk is difficult to quantify: incidents happen, some are change-related, and the controls are largely procedural — they depend on engineers following checklists, and checklists fail under pressure.

### Controls that enforce themselves

In a well-automated environment, the controls are technical rather than procedural. It is not that engineers must validate their changes before deployment — it is that no change can reach production without passing automated validation. The distinction matters for regulatory purposes: a technical control that enforces itself is categorically more defensible than a procedural control that relies on individual compliance.

### Risk becomes measurable, not estimated

Change-related incidents become trackable. The pipeline success rate, the change-related incident count per quarter, the mean time to recovery — these are real numbers, tracked from the start of the programme, available in a dashboard. When the CRO asks about change risk posture, the answer is a trend chart, not an estimate.

### Blast radius is contained

When a change fails in production, the automated rollback executes immediately. The duration of the impact is a fraction of what it would be if rollback required manual diagnosis and execution. For operational resilience purposes, this measurably reduces the severity of the incidents that do occur, even where it cannot prevent them entirely.

---

## The CFO

### Senior engineers are doing junior work

In a typical enterprise financial services firm, a significant share of senior network engineering capacity is consumed by routine execution: configuration generation, change implementation, manual compliance checks, audit evidence assembly. These tasks require care but not the advanced expertise that senior engineers cost. The fully-loaded cost of deploying that expertise on routine execution is the addressable cost of automation. This is not a headcount reduction story — it is a redeployment story. Once automation handles the execution layer, those engineers are available for the work they were actually hired for: design, resilience improvement, and platform development.

### Compliance overhead drops and stays down

The annual compliance cycle, in a manual environment, requires weeks of engineering time to assemble audit evidence, respond to regulatory requests, and run periodic configuration reviews. This cost accumulates every year and tends to grow as the regulatory environment becomes more demanding. In a mature automated environment, this overhead largely disappears. Evidence is a by-product of the operational workflow. Regulatory requests are answered in hours. The cost falls materially and stays down.

### The return is tracked from day one

Manual operations produce a category of spend that is structurally hard to budget: the specialist contractor brought in when a complex incident requires expertise the team cannot provide fast enough; the revenue impact of a change-related outage during market hours; the regulatory notification cost when a misconfiguration causes a reportable breach. A mature automated environment dramatically reduces the frequency of the category most amenable to prevention: the change-related incident caused by human execution error. Equally important, the return is visible from the start. The metrics captured at baseline — engineering hours on routine execution, change lead time, incident frequency, audit preparation effort — become the numerator of the return calculation. The transformation tracks actuals against baseline from day one, not projected benefits from year three.

---

## What Doesn't Change

It would be convenient if this were a story about technology making a complex domain simpler. It is not.

### The network is still complex

The network in a well-automated financial services firm is not less complex than it was before. BGP is still BGP. VXLAN, EVPN, and security zone architecture do not become straightforward because they are rendered by a template rather than typed by an engineer. If anything, good automation reveals complexity that was previously obscured: the implicit assumptions encoded in manual configuration, the undocumented dependencies, the design decisions that had never been made explicit because nobody was required to write them down.

### Expertise remains the foundation

An automation platform operated by engineers who do not understand what the network is doing is a liability. Automation amplifies technical judgment — it does not replace it. Novel problems — new hardware behaviour, unexpected interactions, unfamiliar failure modes — still require a skilled engineer making a decision in a complex environment. What changes is the proportion of time spent on the known versus the unknown. In a manual environment, the known consumes most of it. In a mature automated environment, the known is handled by the platform, and human attention is available for the work that actually requires it.

### The decisions that matter stay with people

Whether to proceed with a critical change during a volatile market session. Whether a design deviation is justified by operational necessity. Whether an automated remediation should be trusted in an unfamiliar scenario. These judgments cannot be automated and should not be. The goal of network automation is not to remove people from the operation of the network — it is to ensure that the people in that operation are spending their time on work that genuinely requires them.

---

*Next: [Business Alignment](../02-business-alignment/chapter) — the frameworks and language for building the case for this transformation and keeping it anchored to business outcomes throughout.*
