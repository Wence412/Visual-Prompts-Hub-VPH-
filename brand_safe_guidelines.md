# Brand Safety Guidelines

All VPH prompts must be brand-safe. This is not optional.

---

## What Brand Safety Means in This Repo

Brand safety means the generated output:

1. Contains no identifiable real-world trademarks, logos, or brand marks
2. Contains no copyrighted characters, mascots, or intellectual property
3. Contains no identifiable real people (living or deceased)
4. Contains no text, watermarks, or type elements unless the prompt explicitly intends this (Ideogram use case only)
5. Produces imagery appropriate for commercial and editorial use

---

## Required Negatives

Every prompt file must include these three negatives at minimum:

```yaml
negatives:
  - logos
  - text
  - watermark
```

For product prompts, also add:
```yaml
  - brand names
  - copyrighted elements
```

For portrait prompts, also add:
```yaml
  - identifiable real person
  - celebrity likeness
```

For fashion and apparel prompts, also add:
```yaml
  - visible branding
  - trademark patterns
```

---

## High-Risk Elements to Avoid

These elements frequently trigger brand safety issues. Do not include them in prompt fields:

| Element | Risk | Alternative |
|---|---|---|
| Specific luxury brand names | Trademark | Describe the category: "luxury Swiss watchmaker" |
| Distinctive product shapes (e.g. specific phone silhouette) | Trade dress | Describe the form: "slim rectangular device with rounded corners" |
| Color combinations associated with specific brands | Some are trademarked | Use material descriptions instead of color codes |
| Character costumes, uniforms | Copyright | Generic equivalents: "structured dark uniform" |
| Real athlete poses | Likeness rights | "Athletic figure, dynamic pose" |
| Building exteriors of famous landmarks | Copyright/IP | "Industrial concrete tower, modernist facade" |

---

## Fiction vs. Reference

**Permitted:** Prompts that describe fictional subjects with generic descriptors.
**Not permitted:** Prompts that reference specific real-world IP by name or obvious description.

Borderline case example:
- Not OK: "Apple AirPods in their charging case"
- OK: "Slim matte black wireless earbuds in their charging case, no visible branding"

---

## Reporting a Brand Safety Violation

If a prompt in this repo generates output that includes real trademarks, logos, or identifiable IP:

1. Open an issue using the `bug-report.md` template
2. Tag the issue `brand-safety`
3. Include the prompt YAML file path and a description of the violation
4. Do not include the generated image in the public issue

---

## Note on Engine Behavior

Some engines (particularly DALL-E 3 and ChatGPT Image 2.0) have internal safety filters that further reduce trademark generation. These filters are not a substitute for writing brand-safe prompts. Write safe prompts first. Rely on engine filters second.

VPH is designed for commercial and editorial use cases. Every prompt in this library must be safe for commercial use with no IP risk.
