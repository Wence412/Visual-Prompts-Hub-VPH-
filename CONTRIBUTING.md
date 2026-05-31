# Contributing to Visual Prompts Hub (VPH)

Thank you for contributing. VPH is a structured prompt system — quality and consistency matter more than volume. Read this before opening a PR.

---

## What We Accept

- New prompt packs (minimum 4 prompts per pack, following APAE schema)
- Variants for existing prompts
- Engine-specific adaptations (Midjourney, DALL-E 3, SDXL, Firefly, Ideogram)
- Documentation improvements (engine notes, brand-safe guidelines, examples)
- Bug reports (schema violations, broken YAML, incorrect engine flags)

## What We Do Not Accept

- Prompts containing copyrighted characters, logos, or trademarked designs without rights
- Prompts that generate explicit, violent, or harmful content
- YAML files that do not validate against `prompt_system/prompt_schema.md`
- Prompts with no negatives array (brand-safety is required)
- Single prompts submitted without at least 2 variants

---

## Prompt File Requirements

Every prompt YAML file must include these fields:

```yaml
title: string                  # Required. Descriptive. Format: "Subject — Setting"
version: string                # Required. Semantic version, e.g. "1.0.0"
category: string               # Required. products | fashion | portraits | architecture | abstract | branding
engine_primary: string         # Required. chatgpt_image_2 | midjourney | dalle3 | sdxl | firefly | ideogram

apae:
  appearance: string           # Required. Subject, materials, finish, color.
  place: string                # Required. Environment, backdrop, set.
  action: string               # Required. Pose, motion, arrangement.
  emotion: string              # Required. Mood, brand feeling.

chatgpt_image_2:
  prompt: string               # Required. Full prompt string.
  style_preset: string         # Optional. product_photo | editorial | illustration | etc.
  background: string           # Optional. BMB type: gradient | clean | cinematic | practical | environment
  ar: string                   # Optional. e.g. "16:9" or "1:1"

negatives:                     # Required. Minimum 3 items.
  - logos
  - text
  - watermark

variants:                      # Required. Minimum 2 entries.
  - id: v1
    label: string
    change: string

authors:                       # Optional but encouraged.
  - name: string
    github: string

license: MIT                   # Required. Must be MIT for inclusion in main repo.
```

---

## Naming Convention

**Files:** `subject_setting_mood.yaml`
Examples:
- `watch_dark_studio_premium.yaml`
- `jacket_editorial_contrast.yaml`
- `facade_brutalist_dusk.yaml`

**Folders:** New categories go under `prompt_library/[category]/`. New product packs go under `prompt_library/products/[pack_name]/`.

---

## Submitting a PR

1. Fork the repository and create a topic branch from `main`.
   ```bash
   git checkout -b prompts/your-pack-name
   ```

2. Add your prompt YAML files following the schema and naming convention.

3. If adding a new category, update the `README.md` Featured Prompt Packs table.

4. Run local validation (if available):
   ```bash
   python docs/validate_schema.py prompt_library/your-new-file.yaml
   ```

5. Fill out the PR template completely. PRs with empty templates will be closed without review.

6. Keep each PR scoped to one prompt pack or one documentation change. Mixed PRs slow review.

---

## Review Criteria

Maintainers review against these criteria:

| Criterion | Pass Condition |
|---|---|
| Schema validity | All required fields present and correctly typed |
| APAE completeness | All four fields are specific, not generic |
| Negatives present | Minimum 3 negatives |
| Variants present | Minimum 2 variants with meaningful differentiation |
| Naming convention | File and folder names follow the convention above |
| Brand safety | No copyrighted elements, no harmful content |
| Engine accuracy | Engine-specific flags match that engine's actual syntax |

---

## Questions

Open a [Discussion](https://github.com/Wence412/Visual-Prompts-Hub-VPH-/discussions) rather than an issue for general questions about the APAE system or prompt strategy.
