# Changelog

## 2026-10-22. Visual tests and prompt revisions

- Added thirteen reviewed image runs: eight initial tests and five retests.
- Revised portrait lighting, facade illumination, earbud lid geometry, paper texture, and watch clasp instructions.
- Added exact prompt snapshots, dimensions, hashes, and per-image caveats under tested/.

## 2026-10-22. Repository repair

- Replaced the proposed directory map and unavailable pack counts with links to eight actual examples and four templates.
- Added a file contract and executable validator, activated CI and GitHub contribution templates.
- Clarified historical engine settings, output review, and imported-library sync limits.
- Kept root YAML paths and legacy engine keys compatible with existing importers.

Earlier entries below describe the original release plan. Some listed paths were not present in the repository at review time.



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
