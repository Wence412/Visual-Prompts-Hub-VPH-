# 🎨 Visual Prompts Hub (VPH)

> A production-grade Visual Prompt System (VPS) for ChatGPT Image 2.0 and cross-engine image generation. Turn prompts into repeatable, brand-safe visual pipelines.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Maintained](https://img.shields.io/badge/maintained-yes-green.svg)]()
[![Prompt Schema](https://img.shields.io/badge/schema-APAE%20v1-blue.svg)](prompt_system/apae_spec.md)

---

## What This Is

VPH is a structured, engine-agnostic prompt library built on the **APAE architecture** (Appearance, Place, Action, Emotion). It is not a collection of one-off prompts. It is a repeatable system for producing consistent, brand-safe visual outputs across ChatGPT Image 2.0, Midjourney, DALL-E 3, Stable Diffusion, Firefly, and Ideogram.

Every prompt in this repo is a structured YAML file. Every file follows the same schema. Every category has variants. The system is designed to scale.

---

## Core Architecture

### APAE Framework

| Layer | Purpose | Example |
|---|---|---|
| **Appearance** | Subject, materials, finish, color | `matte black titanium smartwatch, sapphire glass` |
| **Place** | Environment, backdrop, set | `neon-lit concrete studio` |
| **Action** | Pose, motion, arrangement | `floating at 30-degree angle, slight rotation` |
| **Emotion** | Mood, brand feeling | `premium, minimal, futuristic` |

### BMB Background System

| Type | Use Case |
|---|---|
| `practical` | Plinths, pedestals, product stands |
| `gradient` | Clean product shots, studio gradient |
| `clean` | White seamless |
| `cinematic` | Textured backdrops, mood lighting |
| `environment` | Real-world: stone arcade, mountain terrain |
| `practical_with_props` | Lifestyle context with minimal props |

---

## Repo Structure

```
visual-prompts-hub/
│
├── .github/
│   ├── workflows/
│   │   └── validate-prompts.yml       # CI: schema validation on PRs
│   ├── ISSUE_TEMPLATE/
│   │   ├── new-prompt-pack.md
│   │   └── bug-report.md
│   └── pull_request_template.md
│
├── prompt_system/
│   ├── apae_spec.md                   # Core APAE architecture spec
│   ├── bmb_backgrounds.md             # Background system reference
│   ├── prompt_schema.md               # YAML schema definition
│   └── engine_notes.md                # Engine-specific tips and overrides
│
├── prompt_library/
│   ├── products/
│   │   └── wearable_pack/             # Luxury wearables: watches, jewelry
│   ├── fashion/                       # Editorial fashion and apparel
│   ├── portraits/                     # Character and portrait prompts
│   ├── architecture/                  # Architectural and spatial prompts
│   ├── abstract/                      # Abstract, texture, and pattern prompts
│   └── branding/                      # Brand identity and product hero shots
│
├── templates/
│   ├── prompt_template.yaml           # Blank APAE prompt template
│   ├── batch_template.yaml            # Multi-prompt batch file template
│   ├── brand_pack_template.yaml       # Full brand visual suite template
│   └── campaign_template.yaml         # Campaign-level prompt set template
│
├── variants/
│   ├── variants.yaml                  # Variant system reference
│   └── variant_strategies.md          # How to build systematic variants
│
├── examples/
│   └── wearable_hero_example.md       # Annotated end-to-end example
│
├── engines/
│   └── engine_comparison.md           # Cross-engine behavior notes
│
├── docs/
│   ├── getting_started.md
│   ├── advanced_prompting.md
│   └── brand_safe_guidelines.md
│
├── README.md
├── CONTRIBUTING.md
├── CHANGELOG.md
└── LICENSE
```

---

## Quick Start

**1. Choose a template**

```bash
# Copy the base template
cp templates/prompt_template.yaml my_prompt.yaml
```

**2. Fill APAE fields**

```yaml
title: "My Product — Dark Studio"
apae:
  appearance: "brushed aluminum espresso machine, industrial finish"
  place: "dark concrete studio, single spotlight"
  action: "centered, slightly angled left"
  emotion: "artisan, serious, premium"
```

**3. Add your engine prompt**

```yaml
chatgpt_image_2:
  prompt: >
    Brushed aluminum espresso machine, centered and angled left,
    dark concrete studio with a single spotlight above,
    artisan mood, dramatic shadows, product photography
  style_preset: "product_photo"
  background: "cinematic"
negatives: [logos, text, watermark, people, hands]
```

**4. Run in your engine of choice.** See `engines/engine_comparison.md` for engine-specific tips.

**5. Add variants.** See `variants/variant_strategies.md` to generate systematic color, lighting, and mood variants.

---

## Featured Prompt Packs

| Pack | Category | Prompts | Status |
|---|---|---|---|
| [Luxury Wearables](prompt_library/products/wearable_pack/) | Products | 6 | ✅ Active |
| [Editorial Fashion](prompt_library/fashion/) | Fashion | 8 | ✅ Active |
| [Brand Hero Shots](prompt_library/branding/) | Branding | 5 | ✅ Active |
| [Architectural Forms](prompt_library/architecture/) | Architecture | 4 | ✅ Active |
| [Abstract Textures](prompt_library/abstract/) | Abstract | 4 | ✅ Active |
| [Portraits — Editorial](prompt_library/portraits/) | Portraits | 4 | ✅ Active |

---

## Supported Engines

| Engine | Support Level | Notes |
|---|---|---|
| ChatGPT Image 2.0 | ✅ Primary | Native `style_preset` support |
| Midjourney v6+ | ✅ Full | Use `--ar`, `--style raw` flags |
| DALL-E 3 | ✅ Full | Verbatim prompt support |
| Stable Diffusion XL | ✅ Full | Add CFG scale notes in variants |
| Adobe Firefly | ⚡ Partial | Style reference via `mood` field |
| Ideogram | ⚡ Partial | Strong text rendering support |

See `engines/engine_comparison.md` for detailed adaptation notes.

---

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting. Every prompt must follow the APAE schema. PRs without a valid YAML file will not be merged.

---

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.

---

## License

MIT. See [LICENSE](LICENSE).

---

*Built [WenceStudio by SmartDesign](https://github.com/Wence412). Prompt systems that scale.*
