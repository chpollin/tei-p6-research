---
type: distillate
source-type: publication
reference: teic-tei-issue-2739
topics: ["[[Metadata and Entities]]", "[[Elements and Classes]]"]
status: validated
checked:
  machine-review: 2026-09-06
  validation: 2026-09-06
  quote: 2026-09-06
created: 2026-09-06
updated: 2026-09-06
---

# Distillate: TEIC/TEI GitHub issue 2739

This distillate extracts what one thread of the TEIC/TEI issue tracker reports
about the attribute classes `att.personal`, `att.naming` and `att.canonical`
and what its comments state about their membership.

## Core statements

- The issue author writes that the technical declaration of elements such as `persName` lists the attribute classes. ^s1
  > "The technical declaration of elements such as persName list the attribute classes" (https://github.com/TEIC/TEI/issues/2739, issue body, 2025-08-04)
- The issue author writes that `att.personal`, `att.naming` and `att.canonical` are listed as if they were subclasses of the previous one, which is not the case. ^s2
  > "list the attribute classes att.personal, att.naming, and att.canonical as if they were subclasses of the previous one, which is not the case." (https://github.com/TEIC/TEI/issues/2739, issue body, 2025-08-04)
- The issue author asks whether this results from an error in the ODD. ^s3
  > "Maybe this results from an error in the ODD?" (https://github.com/TEIC/TEI/issues/2739, issue body, 2025-08-04)
- A commenter states that `att.personal` is a member of `att.naming` and that `att.naming` is a member of `att.canonical`. ^s4
  > "att.personal is a member of att.naming, and att.naming is a member of att.canonical" (https://github.com/TEIC/TEI/issues/2739, first comment, 2025-08-05)
- A commenter writes that it can be seen from their spec files. ^s5
  > "as can be seen from their spec files" (https://github.com/TEIC/TEI/issues/2739, first comment, 2025-08-05)
- A commenter gives the URL of the `att.personal` specification file on the repository's `dev` branch. ^s6
  > "https://github.com/TEIC/TEI/blob/dev/P5/Source/Specs/att.personal.xml" (https://github.com/TEIC/TEI/issues/2739, first comment, 2025-08-05)
- A commenter asks whether, if that were true, the hierarchy would have to be reverse. ^s7
  > "If that were true, wouldn't the hierarchy have to be reverse?" (https://github.com/TEIC/TEI/issues/2739, second comment, 2025-08-06)
- A commenter writes that right now the display suggests that `att.naming` is a member of `att.personal`. ^s8
  > "Right now the display suggests that att.naming is a member of att.personal" (https://github.com/TEIC/TEI/issues/2739, second comment, 2025-08-06)
- A commenter asks whether `att.naming` should really be called `att.personal.naming` and `att.canonical` `att.personal.naming.canonical`. ^s9
  > "Shouldn't att.naming really be called att.personal.naming then and att.canonical att.personal.naming.canonical?" (https://github.com/TEIC/TEI/issues/2739, second comment, 2025-08-06)
- A commenter writes that attribute classes do not behave in quite the same way as model classes. ^s10
  > "Attribute classes dont behave in quite the same way as model classes" (https://github.com/TEIC/TEI/issues/2739, third comment, 2025-08-06)
- A commenter writes that in neither case is the naming as systematic as proposed. ^s11
  > "in neither case is the naming as systematic as you propose here" (https://github.com/TEIC/TEI/issues/2739, third comment, 2025-08-06)
- A commenter writes that it would be a fairly major upheaval to make all class names reflect the hierarchy. ^s12
  > "It would be a fairly major upheaval to make all class names reflect the hierarchy" (https://github.com/TEIC/TEI/issues/2739, third comment, 2025-08-06)
- A commenter suspects that there are some cases where a class inherits from more than one other class. ^s13
  > "And i suspect there are some cases where a class inherits from more than one other class" (https://github.com/TEIC/TEI/issues/2739, third comment, 2025-08-06)
- A commenter writes that it is not a simple hierarchy anyway. ^s14
  > "so it's not a simple hierarchy anyway" (https://github.com/TEIC/TEI/issues/2739, third comment, 2025-08-06)
- A commenter writes that they obviously still have problems understanding the attribute class hierarchy correctly. ^s15
  > "I obviously still have problems understanding the attribute class hierarchy correctly" (https://github.com/TEIC/TEI/issues/2739, fourth comment, 2025-08-06)
- A commenter writes that they do not want to overdo the harmonisation of the class names. ^s16
  > "don't want to overdo the harmonisation of the class names" (https://github.com/TEIC/TEI/issues/2739, fourth comment, 2025-08-06)

## Terms

No additional term definition is extracted in this bounded intake.

## Open questions

- Which rendering of the element declaration produces the reported nesting of the three attribute classes, which no body in the thread exhibits?
- Does the membership chain the thread names hold at the pinned TEI P5 4.12.0 release, given that the linked specification files are addressed on the moving `dev` branch?
- Which attribute classes declare more than one other class, which the thread leaves as a suspicion?
- Was the reported presentation an error in the ODD, which no comment in the thread answers?
- Did a governance decision, a pull request or a release follow from the thread?

## Appraisal

The thread establishes what participants stated in August 2025 about the class
chain of the naming elements and about the systematics of attribute class
names. It establishes neither the declared membership at a release nor a defect
in the ODD. Both are read in the admitted class specifications at the pinned
commit `113e933e21f016e2655518321e9d10214b8d9fcb`. The specification files the
first comment links are addressed on the moving `dev` branch, so they carry no
release state.

The recorded outcome comes from the work-item record of the admission run
`sources/manifests/2026-09-06-entities-run2-citations.yaml`. The issue is
closed with the reason `completed` on 2025-08-06, at the timestamp of the last
comment. It carries no label and no milestone, and the snapshot names no pull
request. Closure records closure alone; acceptance and a released effect would
need a governance record and a release.

Full discussion prose stays in local raw storage because repository licensing
does not license participant discussion text. Participant logins and names are
absent from this distillate under the same rule, so positions are attributed by
role and comment position.

## Related

- [[20_distillates/documents/tei-p5-att.personal-4.12.0]]
- [[20_distillates/documents/tei-p5-att.naming-4.12.0]]
- [[20_distillates/documents/tei-p5-att.canonical-4.12.0]]
