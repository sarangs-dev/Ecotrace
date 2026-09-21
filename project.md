# Step 1 — Define What You Want to Build

## Project

**Personal Carbon Footprint Calculator**

**SDG:** SDG 13 — Climate Action

### Project Vision

A lightweight Python application that helps an individual estimate their approximate carbon footprint from selected everyday activities and understand which areas contribute most to their emissions.

The application is intentionally being built as a **learning project first**. The initial version will run locally and remain simple, but the design should not prevent it from being expanded into a public-facing project later.

The project will be useful for practising:

- Python programming
- Data handling and calculations
- Git/GitHub workflows
- API/AI integration
- Basic software architecture
- Building and iterating on an MVP

The application is an **educational estimator**, not a professional greenhouse-gas accounting tool. Established carbon calculators also use activity information such as electricity use, transportation, and waste, and note that estimates depend on location, habits, and assumptions. citeturn0search0turn0search2

---

# 1. What problem are you solving?

Individuals make many everyday decisions that contribute to greenhouse-gas emissions, such as how they travel, how much electricity they consume, and what they eat. However, the connection between those activities and their approximate carbon impact is not always easy to understand.

Existing carbon-footprint calculators demonstrate that personal or household footprints can be estimated using information about activities such as energy use and transportation. The EPA, for example, uses household energy, transportation, and waste as major areas in its household calculator. citeturn0search0turn0search2

### Problem

> **People may know that their lifestyle has an environmental impact, but they may not know the approximate size of that impact, which activities contribute most to it, or what practical changes they could make to reduce it.**

### How this project addresses the problem

The application will:

1. Collect simple information about the user's lifestyle.
2. Estimate emissions for selected categories.
3. Show a category-wise breakdown.
4. Calculate an approximate overall footprint.
5. Use AI to interpret the results and generate personalized suggestions.

The numerical calculation will primarily use predefined emission factors and activity data. This follows the general calculation approach used in greenhouse-gas accounting, where activity data is combined with an appropriate emission factor. citeturn0search3turn0search36

### Important limitation

The application will communicate that its result is an **estimate**.

Carbon-footprint estimates depend on factors such as location, data quality, assumptions, and the emission factors used. For example, electricity emissions can vary according to the electricity-generation mix in a region. citeturn0search1turn0search2

---

# 2. Who is the user?

## Primary target user

The primary target user is an **individual who wants to understand and reduce their personal carbon footprint**.

The user does not need specialized environmental knowledge. They should be able to provide relatively simple information such as:

- Approximate travel distance
- Mode of transportation
- Electricity consumption
- General food habits
- Other selected lifestyle information

The application should then convert this information into an understandable estimate.

## Potential future users

Although the first version will be used locally for learning and personal experimentation, the concept can later be extended to:

- Students
- Environment-conscious individuals
- People learning about sustainable lifestyles
- Households
- Educational institutions
- Users interested in tracking changes in their lifestyle over time

The application should therefore avoid being designed around only one person's data or habits.

### Target-user principle

> **Build the MVP for one individual user, but design the concept so that it can eventually be used by other individuals without fundamentally changing the core calculation system.**

This is different from saying that the project is only for the developer.

---

# 3. What is the main outcome?

The main outcome is:

> **Help users understand their approximate personal carbon footprint, identify the major sources of their emissions, and receive practical suggestions for reducing those emissions.**

The application should answer three questions:

### 1. How much am I emitting?

Example:

```text
Estimated monthly footprint:
95 kg CO₂e
```

### 2. Where are most of my emissions coming from?

Example:

```text
Transportation:  42 kg CO₂e
Electricity:     28 kg CO₂e
Food:             18 kg CO₂e
Other:             7 kg CO₂e
```

### 3. What can I change?

Example:

```text
Your transportation emissions are currently your
largest estimated category.

Possible actions:
- Reduce unnecessary short vehicle trips.
- Walk or use public transport when practical.
- Combine multiple errands into one trip.
```

The AI component should primarily help with **interpretation and recommendations**, rather than being responsible for inventing the numerical footprint.

---

# 4. What is the MVP?

The MVP should be the **smallest complete version of the product that successfully solves the core problem**.

For this project, the MVP will be a local Python application with the following functionality.

## 4.1 User Input

The application will collect a limited set of lifestyle inputs.

### Initial categories

- Transportation
- Electricity
- Food

The number of questions should remain relatively small so that the project stays manageable.

---

## 4.2 Carbon Calculation Engine

Python will calculate estimated emissions from the user's activity data.

The basic concept will be:

```text
Activity Data × Emission Factor
                ↓
       Estimated Emissions
```

For example:

```text
Distance travelled × transport emission factor
```

or:

```text
Electricity consumed × electricity emission factor
```

This approach is consistent with established GHG calculation methodology. citeturn0search3turn0search36

The emission factors should be stored separately from the calculation logic so that they can be updated later without rewriting the entire application.

---

## 4.3 Category-wise Footprint

The application should show the estimated contribution of each category.

```text
Transportation → XX kg CO₂e
Electricity    → XX kg CO₂e
Food           → XX kg CO₂e
```

This makes the result more useful than showing only one total number.

---

## 4.4 Total Footprint

The application should calculate and display an overall estimate.

```text
Estimated monthly footprint:
XX kg CO₂e
```

The application should clearly label this as an **estimate**.

---

## 4.5 Basic AI Integration

AI will be used after the calculation stage.

```text
User Inputs
     ↓
Python Calculation Engine
     ↓
Carbon Footprint
     ↓
Category Analysis
     ↓
AI
     ↓
Personalized Recommendations
```

For example, if transportation represents the largest estimated category, the AI could suggest practical ways to reduce transportation-related emissions based on the user's stated habits.

This gives the project a meaningful AI component without turning it into an unnecessarily complex AI system.

---

## 4.6 Basic Input Validation

The application should handle common input problems such as:

- Empty input
- Invalid numbers
- Negative values where inappropriate
- Incorrect menu selections
- Unexpected user input

This is part of making the MVP usable rather than simply making the calculation work for perfect input.

---

# 5. What is NOT part of the first version?

The following features are intentionally outside the MVP.

## Product Features Out of Scope

- Mobile application
- User authentication/login
- User accounts
- Cloud synchronization
- Social/community features
- Social feed
- Leaderboards
- Gamification
- Payment system
- Carbon-credit purchasing
- Public profiles
- Multi-user administration
- Real-time tracking
- GPS/location tracking
- IoT integration
- Smart-home integration
- Professional carbon-accounting reports
- Carbon-offset marketplace

## Technical Features Out of Scope

- Microservices
- Docker/Kubernetes
- Cloud infrastructure
- Complex database architecture
- Machine-learning model training
- Custom ML prediction models
- Complex frontend frameworks
- Complex data pipelines
- Large-scale deployment
- Production-grade authentication/security infrastructure

## AI Features Out of Scope

AI is part of the MVP, but its responsibility will remain limited.

The first version will **not** attempt to build:

- A full AI chatbot
- An AI personal assistant
- A custom-trained LLM
- An autonomous AI agent
- Complex predictive ML models
- AI-generated carbon calculations without defined calculation rules

The AI's initial role is:

```text
Calculated Results
       ↓
AI interprets the results
       ↓
Personalized recommendations
```

---

# Final MVP Definition

The first version is complete when a user can perform this entire flow:

```text
┌───────────────────────┐
│ Enter lifestyle data  │
└───────────┬───────────┘
            ↓
┌───────────────────────┐
│ Calculate emissions   │
│ using Python          │
└───────────┬───────────┘
            ↓
┌───────────────────────┐
│ Show category-wise    │
│ footprint             │
└───────────┬───────────┘
            ↓
┌───────────────────────┐
│ Show total estimated  │
│ carbon footprint      │
└───────────┬───────────┘
            ↓
┌───────────────────────┐
│ Send relevant results │
│ to AI                 │
└───────────┬───────────┘
            ↓
┌───────────────────────┐
│ Show personalized     │
│ recommendations       │
└───────────────────────┘
```

If this workflow works reliably, **the MVP is finished**.

Everything beyond this should be treated as a future iteration rather than something that must be included before the first version is complete.

---

# Scope Rule

> **Build the smallest useful version first. Add a feature only when it either improves the core carbon-footprint workflow or provides a deliberate learning opportunity.**

The project can later evolve into a public application, but the first milestone is a functioning local MVP.

---

## Sources Used for Initial Research

- US EPA — Household Carbon Footprint Calculator citeturn0search0turn0search2
- US EPA — Assumptions and References for Household Carbon Footprint Calculator citeturn0search1
- GHG Protocol — Calculation Tools FAQ citeturn0search3
- GHG Protocol — Calculation methods and activity data/emission factors citeturn0search36
