# V16 Codex Execution Instruction

## Objective
Modify the Abaqus model according to engineering correspondence requirements before calculation.

## Execution order

1. Read V16_MODEL_AUDIT_REPORT.md
2. Read V16_MODEL_CORRESPONDENCE_FIX_PLAN.md
3. Complete missing engineering structures
4. Complete material and permeability mapping
5. Generate V16.1 model
6. Run geometry/material/boundary audit
7. Only after passing audit, run S01 baseline seepage analysis

## Restrictions

- Do not directly calculate the current V16.0 test model as the final engineering model.
- Do not remove traceability between engineering geology and Abaqus regions.
- Keep modification records in GitHub.
