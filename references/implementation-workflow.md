# Reference: Structured Implementation & Verification Workflow

## Purpose

Turn a design or development request into a controlled, verifiable change. The agent must work like a product designer, frontend engineer and QA reviewer, not like a code generator that makes broad edits and declares success.

Use this workflow for meaningful UI, UX, responsive, accessibility, form or frontend changes. Scale the depth to the task. A small copy edit does not need a full audit.

## The Core Sequence

**Audit → Plan → Implement → Test → Verify → Report**

Do not skip directly from a vague request to a large rewrite.

### 1. Audit the Existing Experience

Inspect the running application and relevant source before editing.

Review:
- Visual hierarchy: what is noticed first, second and third?
- Density: are sections, forms, tables or navigation crowded?
- Typography: scale, line length, wrapping, consistency and readability.
- Spacing and alignment: repeated gaps, container widths and rhythm.
- Interaction: hover, focus, active, disabled, loading, empty and error states.
- Responsive behavior: overflow, stacking, touch ergonomics and content priority.
- Accessibility: contrast, semantic structure, labels, keyboard operation and focus visibility.
- Existing implementation: components, styles, routes, data flow, API calls and tests.

Prioritize the **five highest-impact problems first** when the scope is broad. Do not create a long list of cosmetic nits before identifying the issues that materially harm comprehension, task completion or trust.

For each finding, record:

| Field | Required detail |
| --- | --- |
| Issue | What is wrong, stated specifically |
| Evidence | Screenshot, viewport, code path or reproducible behavior |
| Impact | Why it matters to a real user |
| Priority | Critical, high, medium or low |
| Proposed fix | The smallest effective correction |

Do not invent findings. If browser access or a required test environment is unavailable, say what could not be inspected.

### 2. Define the Plan and Guardrails

Before implementation, establish:

- **Goal:** the user or business outcome the change should improve.
- **Scope:** the pages, components, states and viewport sizes affected.
- **Constraints:** what must not change.
- **Design decisions:** hierarchy, layout, spacing, typography, color and interaction behavior.
- **Acceptance criteria:** observable conditions that determine whether the work is complete.

For visual refinement, define a compact system before styling:
- A consistent spacing scale. Reuse existing project tokens when sound; do not invent a second system.
- A clear type scale with defined roles for display, heading, body, label and supporting text.
- A restrained palette. For a focused refinement, use no more than five core color tokens unless the existing brand system requires more.
- Shared rules for borders, radii, shadows, containers and focus states.

Do not force arbitrary tokens onto a project whose established design system is already coherent. Document intentional exceptions.

### 3. Implement in Focused Changes

Work in small, logically related areas. Avoid replacing entire pages or components when targeted changes will achieve the result.

Preservation rules:
- Preserve existing routes, business logic, data models, API contracts, authentication and integrations.
- Do not change form field order, names, validation rules or submission behavior unless explicitly requested.
- Do not remove functionality to make a visual test pass.
- Reuse existing components and tokens where appropriate.
- Avoid new dependencies unless they solve a real need that existing tools cannot address.
- Keep responsive behavior and accessibility in the implementation, not as a later decoration.
- Keep code maintainable. Do not add duplicate CSS, conflicting breakpoints or one-off overrides without a reason.

When requirements are ambiguous but implementation can safely proceed, state the assumption and choose the least disruptive option. Ask only when a missing decision materially changes the solution or risks irreversible work.

### 4. Test the Actual Application

Run the application using its documented commands. Use the project's existing test, lint, type-check and build commands where available.

At minimum, test the affected experience at:

| Viewport | What to verify |
| --- | --- |
| 390px | Mobile layout, readable text, touch targets, no unintended horizontal scrolling |
| 768px | Tablet layout, breakpoint transitions, stacked content and table behavior |
| 1440px | Desktop hierarchy, spacing, alignment and preservation of the established layout |

Add project-specific widths when a reported defect or supported device requires them. Capture screenshots at each relevant breakpoint. Do not claim responsive verification from CSS inspection alone.

For forms, test the complete interaction lifecycle:
- Initial and filled states.
- Required and invalid input.
- Inline validation and useful error messages.
- Keyboard focus and tab order.
- Disabled and loading states.
- Successful submission and failure behavior.
- Preservation of existing field order and API behavior.

For interactive components, test keyboard and pointer/touch operation, including empty, active, selected, expanded and error states where applicable.

Record actual command output and browser observations. Distinguish a test that passed from one that was not run.

### 5. Verify Accessibility and Usability

Use WCAG 2.2 AA as the target where applicable.

Check:
- Text contrast: at least 4.5:1 for normal text and 3:1 for large text.
- Meaningful non-text controls and visual indicators: at least 3:1 contrast against adjacent colors where WCAG requires it.
- Visible keyboard focus that is not hidden behind sticky UI.
- Logical keyboard order and no keyboard traps.
- Programmatic labels and instructions for form controls.
- Accessible names for icon-only buttons and controls.
- Semantic headings, landmarks, buttons and links.
- Errors identified in text, not by color alone.
- Reduced-motion preferences respected.
- Touch controls comfortably usable. Aim for 44 × 44 CSS pixels where practical; apply the WCAG target-size criteria and exceptions accurately rather than treating 44px as a universal conformance threshold.

Prefer native HTML semantics. Add ARIA only when native elements do not provide the required meaning or behavior. Never use ARIA to disguise a broken interaction.

Automated scans are useful but do not replace keyboard, screen-reader and visual inspection.

### 6. Verify the Final Result

After implementation:
1. Revisit every original high-priority finding.
2. Compare before/after screenshots at the same viewport sizes.
3. Confirm the fix did not introduce regressions in adjacent components or layouts.
4. Check browser console and relevant network failures.
5. Run the relevant test, lint, type-check and build commands.
6. Confirm the final diff contains only intended changes.

If something cannot be tested, report it as unverified. Never describe a test as passed unless it was actually executed and passed.

## Focused Prompt Patterns

Use one focused task at a time. Adapt these prompts to the current repository and preserve the user's constraints.

### A. Audit Prompt

> Audit the current [page/component] before changing code. Inspect the rendered experience and relevant implementation. List the five highest-impact hierarchy, density, usability and visual problems first. For each, include evidence, user impact, priority and a specific proposed fix. Then define the smallest coherent spacing scale, type scale and color-token set needed for this work. Do not implement yet. Do not invent issues or replace a working design system without evidence.

### B. Plan Prompt

> Based on the audit, propose an implementation plan for [scope]. State the goal, affected files/components, design decisions, constraints, risks and measurable acceptance criteria. Preserve existing routes, API calls, data contracts and business logic. Do not change anything outside the stated scope. Flag any assumption that could materially affect the result.

### C. Implementation Prompt

> Implement the approved changes in the actual project. Inspect existing components and reuse working patterns. Keep the change focused. Preserve [explicit constraints]. Include responsive, keyboard, focus, loading, disabled and error states where relevant. Do not claim completion based on code changes alone. Run the application and relevant checks after implementation.

### D. Verification Prompt

> Verify the implementation in the running application. Capture screenshots at [required viewport widths]. Test the actual interactions and affected edge cases. Report each acceptance criterion as passed, failed or not tested, with evidence. List regressions and remaining issues. Fix verified defects within scope, then rerun the affected checks. Do not claim tests passed unless they were executed.

## Completion Report

Every substantial implementation task ends with a concise report:

1. **Changed:** files, components and user-visible outcomes.
2. **Verified:** viewport sizes, interactions and commands actually tested.
3. **Results:** pass/fail status against acceptance criteria.
4. **Not verified:** unavailable tools, blocked environments or untested cases.
5. **Remaining:** defects, risks or follow-up work.

A successful build is not proof of a successful interface. A polished screenshot is not proof that the interactions work. Report both visual and functional evidence.

## Working Principle

**Be precise about the problem, disciplined about the change, and honest about the evidence.**
