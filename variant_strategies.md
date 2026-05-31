# Variant Strategies

A prompt without variants is a one-off. A prompt with variants is a system.

This document covers the four primary variant strategies used in VPH and how to apply each.

---

## Why Variants Matter

A single APAE prompt produces one visual interpretation. Variants let you:

- Test multiple aesthetics before committing to production
- Build cohesive visual suites across platforms (hero, social, lifestyle)
- Create A/B sets for campaign testing
- Generate seasonal or contextual adaptations without re-authoring from scratch

---

## Strategy 1: Lighting Variant

**What changes:** Lighting setup and mood. Everything else stays the same.
**Use case:** A/B testing. Day vs. night. Studio vs. natural.

**Examples:**

| Label | Change |
|---|---|
| Hard light | Replace soft diffusion with single hard key. Deep shadows. High contrast. |
| Soft light | Large soft box overhead. Wrap-around light. Minimal shadows. |
| Golden hour | Warm amber directional light from 45-degree angle. Warm shadows. |
| Night studio | Dark environment. Single spotlight. Background fully black. |
| Backlight | Light source behind subject. Rim-lit edges. Subject slightly silhouetted. |

**YAML pattern:**
```yaml
- id: v1
  label: "Hard Light"
  change: "Replace soft diffusion with a single hard key light from upper left. Deep cast shadows. No fill."
```

---

## Strategy 2: Background / Environment Variant

**What changes:** The BMB background type.
**Use case:** Platform-specific needs. Commercial vs. editorial.

| Background | Tone |
|---|---|
| `clean` | Commercial, catalog, e-commerce |
| `gradient` | Launch, announcement, modern |
| `cinematic` | Editorial, campaign, magazine |
| `practical` | Grounded, product-in-context |
| `environment` | Lifestyle, real-world, aspirational |
| `practical_with_props` | Curated lifestyle, curated context |

**YAML pattern:**
```yaml
- id: v2
  label: "Lifestyle Environment"
  change: "Move from studio gradient to a real-world environment. Add relevant contextual props."
  background: environment
```

---

## Strategy 3: Color / Finish Variant

**What changes:** Color palette or surface finish of the subject.
**Use case:** Colorway launches. Season-specific variations. SKU differentiation.

**Examples:**

| Label | Change |
|---|---|
| Bone White | Replace dark material with bone white or ivory finish. |
| Navy Edition | Deep navy colorway. Silver hardware. |
| Warm Rose | Rose gold or warm blush tone. Matching environment warmth. |
| Raw Natural | Unfinished material. Natural linen, unvarnished wood, raw concrete. |
| Chrome | High-gloss chrome or mirror finish. Adjusted lighting for reflection management. |

**YAML pattern:**
```yaml
- id: v3
  label: "Bone White Edition"
  change: "Change subject colorway to bone white. Adjust lighting to preserve detail on light surface. White or ivory gradient background."
```

---

## Strategy 4: Format / Composition Variant

**What changes:** Aspect ratio, framing, or compositional approach.
**Use case:** Cross-platform deployment. Instagram (4:5) vs. LinkedIn (16:9) vs. hero (1:1).

| Format | Platform Use |
|---|---|
| `1:1` | Instagram square, hero |
| `4:5` | Instagram portrait, Pinterest |
| `16:9` | LinkedIn, banner, newsletter |
| `9:16` | Stories, Reels, TikTok |
| `3:2` | Editorial, photography print |

**YAML pattern:**
```yaml
- id: v4
  label: "Story Format"
  change: "Reframe for 9:16 vertical. Move subject to lower two-thirds. Open sky or negative space above for text overlay."
  ar: "9:16"
```

---

## Combining Strategies

For a full campaign suite, combine all four:

| Shot | Strategy | Format |
|---|---|---|
| Hero | Cinematic background + hard light | 1:1 |
| Social feed | Same subject, lifestyle environment | 4:5 |
| Story | Same subject, vertical reframe | 9:16 |
| Banner | Wide editorial, soft light, negative space | 16:9 |
| Detail | Macro close-up, raking light | 1:1 |

This five-shot suite covers every major platform from a single APAE prompt source. Use `templates/campaign_template.yaml` to structure this workflow.

---

## Variant Naming Convention

```
v[number]_[strategy]_[label]
```

Examples:
- `v1_light_hard_key`
- `v2_bg_lifestyle`
- `v3_color_bone_white`
- `v4_format_story_9x16`
