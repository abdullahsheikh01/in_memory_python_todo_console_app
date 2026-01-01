---
id: 1
title: Create Todo App Constitution
stage: constitution
date: 2026-01-01
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: user
command: /sp.constitution
labels: [constitution, todo, python]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

Write constitution for this In-Memory Python Todo Console App and you can use Context7 MCP if you have any confusion.
## Core principles:
- Functionality through modular code design
- Readability for developers (Python programming background)
- Testability (all features unit-tested with Pytest)
- Interactivity (enhanced user experience via prompt library)

## Key standards:
- All code must adhere to PEP 8 style guidelines
- Documentation format: Inline comments and a README.md file
- Dependency types: Use InquirerPy for command line prompts; install via UV package manager
- Code quality: Easy to Understand
- Interface clarity: Intuitive console interactions using InquirerPy prompts with help menu

## Constraints:
- Minimum 5 core features (add, list, delete, mark as done, search)
- Format: Python script with separate test file

## Success criteria:
- All features functional in console execution
- Zero runtime errors in standard use cases
- Passes unit test suite with 80%+ coverage
## Core principles:
- UV as Package Manager
- InquirerPy Package for command line prompts
- Type Hinting
- Proper README.md
- Project can easily start with uv start

## Response snapshot

Created a comprehensive constitution for the In-Memory Python Todo Console App that incorporates all specified principles and requirements. The constitution includes:

- Core principles for modular design, readability, testability, interactivity, and PEP 8 compliance
- Additional constraints section outlining the 5 required features
- Development workflow section with TDD approach and quality standards
- Governance section with compliance requirements

The constitution replaces the template placeholders with specific guidance for the todo console application, emphasizing modular code design, Pytest for testing, InquirerPy for CLI interactions, and proper documentation practices.

## Outcome

- ✅ Impact: Constitution created with all specified principles incorporated
- 🧪 Tests: No tests created yet, constitution phase
- 📁 Files: Updated .specify/memory/constitution.md with project-specific guidance
- 🔁 Next prompts: Ready to proceed with project implementation based on constitution
- 🧠 Reflection: Constitution provides clear governance framework for project

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): Not applicable at this stage
- Prompt variant (if applicable): Standard constitution creation
- Next experiment (smallest change to try): Begin implementing the todo app based on constitution