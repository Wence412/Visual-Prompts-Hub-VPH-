# Changelog

All notable changes to Visual Prompts Hub (VPH) are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
Versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Planned
- Scene library: 20+ curated environment descriptions
- CLI validator script for local schema checking
- Prompt scoring rubric (coherence, brand-safety, engine compatibility)

---

## [1.1.0] — 2026-05-30

### Added
- Full prompt library: fashion, branding, portraits, architecture, abstract categories
- `templates/batch_template.yaml` for multi-prompt batch workflows
- `templates/brand_pack_template.yaml` for brand visual suite production
- `templates/campaign_template.yaml` for campaign-level prompt sets
- `variants/variant_strategies.md` with systematic variant generation methods
- `engines/engine_comparison.md` with cross-engine adaptation notes
- `docs/getting_started.md`, `docs/advanced_prompting.md`, `docs/brand_safe_guidelines.md`
- `prompt_system/engine_notes.md` with engine-specific override tips
- GitHub Actions CI workflow for YAML schema validation
- GitHub Issue templates: new prompt pack, bug report
- GitHub PR template
- CHANGELOG.md (this file)

### Improved
- README fully rewritten: badges, table of contents, quick start, featured packs table, engine support table
- CONTRIBUTING.md expanded with validation checklist, naming conventions, and review criteria
- Prompt schema extended with `engine_overrides` and `brand_pack` optional keys

---

## [1.0.0] — 2026-05-01

### Added
- Initial repository structure
- APAE specification (`prompt_system/apae_spec.md`)
- BMB background system (`prompt_system/bmb_backgrounds.md`)
- Core prompt schema (`prompt_system/prompt_schema.md`)
- Luxury wearables prompt pack (`prompt_library/products/wearable_pack/`)
- Base prompt template (`templates/prompt_template.yaml`)
- Variants reference (`variants/variants.yaml`)
- MIT License, CONTRIBUTING.md, README.md
- `.gitignore`
