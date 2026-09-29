---
type: assertion
topics: ["[[ODD and Customization]]"]
status: grounded
checked: {}
grounding:
  - "[[20_distillates/documents/practice-v1-dracor-odd-c2f9e814#^s2]]"
  - "[[20_distillates/documents/practice-v1-epidoc-odd-e5b68eb8#^s4]]"
  - "[[20_distillates/documents/practice-v1-cmif-odd-d171133e#^s2]]"
contested-with: []
related: []
created: 2026-09-11
updated: 2026-09-11
---

# The sampled ODDs select P5 modules with different moduleRef strategies: mostly whole modules, except lists, or include lists

## Statement

The DraCor ODD references eight of its twelve modules whole, restricts one module with an `except` list and three with `include` lists. The EpiDoc ODD references three modules whole and restricts fourteen with `except` lists, using no `include` list. The CMIF ODD references `tei` whole and takes only listed elements from its four other modules. These are declared selection mechanisms at the pinned commits; the resulting element sets were not compiled.

## Support

- [[20_distillates/documents/practice-v1-dracor-odd-c2f9e814#^s2]] — DraCor's twelve `moduleRef` declarations: eight unrestricted, one `except`, three `include`.
- [[20_distillates/documents/practice-v1-epidoc-odd-e5b68eb8#^s4]] — EpiDoc's three unrestricted modules, fourteen `except` lists and no `include` list.
- [[20_distillates/documents/practice-v1-cmif-odd-d171133e#^s2]] — CMIF's unrestricted `tei` module and `include` lists on the other four modules.

## Related

- [[30_assertions/practice-v1-sampled-odds-name-their-tei-source-differently]]
