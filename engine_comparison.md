# Engine Comparison and Adaptation Guide

This document covers key behavioral differences across supported engines and how to adapt VPH prompts for each.

---

## Supported Engines

| Engine | Version | Notes |
|---|---|---|
| ChatGPT Image 2.0 | Current | Primary engine. Native `style_preset` support. |
| Midjourney | v6.1+ | `--style raw` required for realism. |
| DALL-E 3 | API / ChatGPT | Verbatim prompts. Strong instruction following. |
| Stable Diffusion XL | 1.0 | Negative prompts separate field. CFG scale matters. |
| Adobe Firefly | 3+ | Good at surface textures. Mood and style via reference. |
| Ideogram | 2.0 | Best text rendering of all engines. |

---

## ChatGPT Image 2.0

**Strengths:** Style presets, composition control, consistent color grading.
**Weaknesses:** Occasionally softens hard lighting requests. May add unwanted bokeh.

**Tips:**
- Use `style_preset: product_photo` for crisp product shots.
- Include "no softening filters" explicitly if portrait is requested.
- `quality: hd` adds generation time but significantly improves texture detail.
- Specify `ar` explicitly. Default is 1:1.

**Style presets available:**
- `product_photo` — Clean, sharp, commercial
- `editorial` — Magazine, cinematic, storytelling
- `illustration` — Stylized, graphic
- `portrait` — Face-forward, lighting-aware
- `cinematic` — Film-grade, moody

---

## Midjourney v6.1+

**Strengths:** Aesthetic quality, lighting mood, painterly textures.
**Weaknesses:** Literal instruction-following is weaker than GPT Image or DALL-E 3.

**Required flags for VPH prompts:**
```
--style raw     # Disables Midjourney's aesthetic filtering. More literal output.
--v 6           # Use v6 or higher.
--q 2           # Higher quality. Slower.
--ar [ratio]    # Always specify. e.g. --ar 1:1 or --ar 16:9
```

**Negatives in Midjourney:**
```
[prompt] --no logos, text, watermark, blurry
```

**Tips:**
- Keep prompts shorter than ChatGPT Image 2.0 prompts. MJ handles dense prompts less well.
- Use adjective-heavy APAE fields directly in the prompt. MJ responds well to adjective stacking.
- Camera and lens references (e.g. "shot on Hasselblad 907X") reliably improve MJ output quality.

---

## DALL-E 3

**Strengths:** Exact instruction following, composition control, text rendering.
**Weaknesses:** Stylistic range narrower than MJ. Sometimes over-saturates.

**Tips:**
- Write in full sentences. DALL-E 3 follows verbatim instructions more faithfully than any other engine.
- Explicitly state what NOT to do: "no text visible," "no logos," "do not add bokeh."
- Include color temperature language: "cool blue-white light," "warm amber tones."
- DALL-E 3 handles negative space well when explicitly requested.

---

## Stable Diffusion XL

**Strengths:** Highly customizable via CFG scale, samplers, and LoRAs.
**Weaknesses:** Requires more technical prompt discipline. Consistency harder to achieve.

**Recommended settings:**
```yaml
cfg_scale: 7       # Higher = more literal. Lower = more creative. 6–9 for VPH prompts.
steps: 30          # 25–40 for quality. Higher steps slow generation.
sampler: "DPM++ 2M Karras"   # Best balance of speed and quality.
```

**Negative prompt field (SDXL uses this as a separate field):**
```
ugly, blurry, low quality, watermark, text, logo, deformed, overexposed, flat
```

**Tips:**
- Add quality boosters to positive prompt: `masterpiece, best quality, ultra-detailed, 8K`
- Use LoRA for specific styles (product photography, editorial, etc.)
- Keep negative prompt comprehensive. SDXL responds strongly to negatives.

---

## Adobe Firefly

**Strengths:** Excellent at surface textures, materials, and brand-safe outputs.
**Weaknesses:** Limited compositional control. Weaker at cinematic mood.

**Tips:**
- Use the Style and Mood references rather than trying to engineer composition in the prompt.
- Best used for texture and material shots (abstract, product surface detail).
- Reference visual styles from Firefly's built-in style library where possible.
- Not recommended as primary engine for portrait or editorial campaign shots.

---

## Ideogram 2.0

**Strengths:** Best text rendering in any image engine. Good product shots.
**Weaknesses:** Less cinematic than MJ. Limited on complex environments.

**Tips:**
- Primary use case in VPH: prompts that need text or typographic elements embedded in images.
- For all VPH prompts with `negatives: [text]`, Ideogram still respects this if explicitly stated.
- Use for: packaging mockups, product labels, branded environmental scenes.
- Aspect ratio: Ideogram supports 1:1, 16:9, 9:16 natively.

---

## Cross-Engine Adaptation Rule

When adapting a VPH YAML prompt to a different engine than `engine_primary`:

1. Use the APAE fields as your source of truth.
2. Rewrite the prompt string for that engine's behavior (do not copy-paste).
3. Add the engine-specific flags or settings from this guide.
4. Adjust negatives to that engine's format (separate field for SDXL, `--no` for MJ).
5. Store the adaptation in the `engine_overrides` key of the YAML file.
