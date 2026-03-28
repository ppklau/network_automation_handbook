# A-Team: Roles, Responsibilities and Gap Assessment

A transformation programme requires four aligned functions: Leadership, Product Management, Architecture, and Engineering. Use this template to map current people to those functions, identify gaps, and plan how gaps will be filled.

**Organisation:**
**Date:**

---

## Role Definitions

### Leadership

**Purpose:** Provides mandate, removes obstacles, sustains commitment, and connects the transformation programme to business strategy.

**Responsibilities:**
- Defines the target state in business terms and secures investment
- Removes structural obstacles (change management constraints, procurement delays, organisational boundaries)
- Sustains commitment through execution — particularly during Phase 1 when ROI is not yet visible
- Holds the programme accountable to business outcomes, not just technical deliverables
- Represents the programme in senior forums and business conversations

**What good looks like:** A sponsor who attends programme reviews, escalates blockers personally, and can articulate the business case without engineering support.

**What failure looks like:** A sponsor who champions the programme in presentations but is unavailable when blockers need to be resolved. A leader who has delegated the business case to the engineering team.

---

### Product Management

**Purpose:** Owns the relationship between the automation platform and its consumers. Ensures the platform delivers value to the business, not just technical capability to the team.

**Responsibilities:**
- Maintains the product backlog, prioritised by business value
- Manages stakeholder relationships with consuming teams (application, security, compliance, operations)
- Measures and reports adoption — not just deployment, but actual use
- Translates consumer feedback into backlog items
- Communicates programme progress in business terms to leadership and stakeholders

**What good looks like:** Someone who can tell you, at any point: what is in the backlog, what feedback has been received from consuming teams, and what the adoption rate is for the last released capability.

**What failure looks like:** No one with this function. Engineering team decides what to build based on technical interest. Adoption is low. Nobody knows why. No feedback loop exists.

---

### Architecture

**Purpose:** Ensures technical decisions are made with a complete view of the landscape. Prevents expensive mistakes. Makes build-versus-buy decisions explicit.

**Responsibilities:**
- Owns the technical vision for the automation platform and its evolution
- Makes and records build-versus-buy decisions (documented as ADRs)
- Ensures integration with existing systems is safe and well-understood
- Guards against over-engineering — the right amount of complexity is what the problem requires
- Identifies and surfaces technical debt accumulation before it becomes a constraint

**What good looks like:** An architect who has read the source of truth data model, understands why each decision was made, and can explain the trade-offs without referring to documentation.

**What failure looks like:** Architecture decisions made by whoever is loudest in the design meeting. No ADR register. Source of truth data model has to be redesigned after twelve months because it cannot accommodate multi-vendor environments.

---

### Engineering

**Purpose:** Builds and operates the automation platform with quality. Closes the feedback loop between technical execution and business outcome.

**Responsibilities:**
- Builds automation capabilities to the quality required for a platform, not a proof of concept
- Maintains the platform — updates, fixes, extension for new use cases
- Tests changes before deployment, including automation changes themselves
- Provides honest feedback to architecture and product management about what is and is not working
- Builds automation literacy across the broader team

**What good looks like:** Engineers who understand *why* they are building each capability, not just *what* they have been asked to build. A team where the automation platform is treated as a product they take pride in.

**What failure looks like:** Engineers who build excellent automation but have no visibility of whether it is being used. Automation that works perfectly in lab but fails in production because real-world complexity was not tested.

---

## Current State Assessment

Map current individuals or roles to each function. Note gaps and how they will be addressed.

| Function | Current Owner | Time Available | Gaps | How Gap Will Be Filled |
|---|---|---|---|---|
| **Leadership** | | | | |
| **Product Management** | | None (typical) | Full function missing | Assign to senior engineer or project manager with mandate |
| **Architecture** | | | | |
| **Engineering** | | | | |

---

## Gap Analysis

### Is the product management function covered?

- [ ] Yes — named individual with explicit mandate and allocated time
- [ ] Partially — covered by another role without dedicated time
- [ ] No — this function is absent

**If no or partial:** This is the highest-risk gap for automation adoption. Before Phase 2 begins, assign this function explicitly. It does not require a full-time hire — a senior engineer with 20–30% dedicated to stakeholder management and backlog ownership can fulfil it in most organisations.

---

### Does leadership have sufficient visibility?

- [ ] Yes — sponsor attends monthly programme reviews and can articulate the business case
- [ ] Partially — sponsor is aware but not actively engaged
- [ ] No — no named senior sponsor

**If no or partial:** Escalate before Phase 1 begins. A programme without an active sponsor will not survive the first budget review.

---

### Are architecture decisions being recorded?

- [ ] Yes — ADR register maintained, all significant decisions documented
- [ ] Partially — some decisions documented, inconsistently
- [ ] No — no ADR register

**If no or partial:** Establish the ADR register at programme initiation. The first ADR should cover source of truth platform selection.

---

### Is the engineering team resourced to maintain the platform, not just build it?

- [ ] Yes — platform maintenance is explicitly in the team's remit with allocated capacity
- [ ] Partially — maintenance is expected to happen around delivery work
- [ ] No — team is sized for build only

**If no or partial:** Size the engineering team for 20–30% maintenance and support overhead from Phase 2 onward. Failing to do so guarantees platform quality degradation as coverage expands.

---

## Team Structure Options

### Small Organisation (1–5 network engineers)

One engineer carries architecture and product management alongside their engineering responsibilities. Leadership function falls to the Head of Network or IT Director. This is viable if the product management responsibilities are made explicit — even a small programme needs someone tracking adoption and managing the backlog.

```
Head of Network (Leadership)
    └── Senior Engineer (Architecture + Product Management + Engineering)
            └── Engineer(s) (Engineering)
```

### Mid-Size Organisation (5–20 network engineers)

Dedicated architecture and product management functions become viable. Engineering team is large enough to have a platform sub-team and a delivery sub-team.

```
VP / Head of Infrastructure (Leadership)
    ├── Network Architect (Architecture)
    ├── Automation Programme Lead (Product Management)
    └── Engineering Team
            ├── Platform engineers (2–3)
            └── Automation delivery engineers (2–4)
```

### Large Organisation (20+ network engineers)

Full function separation. Platform team operates as an internal product team with its own backlog, release cadence, and stakeholder management.

```
VP of Infrastructure (Leadership)
    ├── Chief Architect (Architecture oversight)
    ├── Automation Platform Product Manager (Product Management)
    └── Platform Engineering Team
            ├── Platform lead
            ├── Senior automation engineers
            └── Automation engineers
```
