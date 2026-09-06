---
type: distillate
source-type: data
representation: "[[10_markdown/documents/note]]"
topics: ["[[Broken]]"]
status: grounded
checked: {}
created: 2026-09-06
updated: 2026-09-06
---

# Distillate: Computations the validator must not run

Fixture: the first computation passes an argument the schema does not allow, and
the second names a script outside `tools/analysis/`, which a run would execute
from the vault root (defect: computation declaration).

## Core statements

- This statement hands its script an argument. ^s1
  - computation: `python tools/analysis/reduction.py --year 2025` → `31.4`
- This statement names a script beside the vault. ^s2
  - computation: `python ../outside.py` → `7`
