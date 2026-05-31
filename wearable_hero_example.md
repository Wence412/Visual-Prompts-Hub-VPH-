# Annotated Example: Luxury Watch Hero Shot

This end-to-end example walks through how the VPH system produces a production-ready prompt from an APAE brief. Use this as a reference when authoring new prompts.

---

## The Brief

**Client need:** A hero product shot for a luxury smartwatch campaign. Dark, editorial, premium. Used as a newsletter hero and LinkedIn banner.

**Engine:** ChatGPT Image 2.0 (primary), Midjourney (variant)

---

## Step 1: APAE Construction

Start with the four fields. Be specific at every layer.

```yaml
apae:
  appearance: "titanium smartwatch, matte charcoal case, sapphire glass face, brushed steel band with deployant clasp"
  place: "dark concrete studio with a single overhead spotlight, smoke-effect background haze"
  action: "floating at 30-degree angle, slight clockwise rotation, band curving naturally downward"
  emotion: "premium, precise, futuristic, confident"
```

**Why these choices:**
- `appearance`: Names every material (titanium, sapphire glass) and finish (matte charcoal). "Deployant clasp" signals high-end watches to the model.
- `place`: "Smoke-effect" is a specific backdrop technique that adds depth without distraction. "Single overhead spotlight" gives the engine one clear light source.
- `action`: "30-degree angle" and "clockwise rotation" are precise. "Band curving naturally downward" prevents a rigid, unnatural look.
- `emotion`: Four words. Each adds a distinct tonal dimension.

---

## Step 2: Engine Prompt Construction

Translate the APAE fields into a coherent engine prompt. Do not just concatenate the fields. Write a sentence that flows.

**Weak version (just concatenating fields):**
> Titanium smartwatch, matte charcoal case, dark concrete studio, floating, premium.

**Strong version (VPH standard):**
> Titanium smartwatch with matte charcoal case, sapphire glass face, and brushed steel band with deployant clasp. Floating at a 30-degree angle with slight clockwise rotation, band curving naturally downward. Dark concrete studio setting with a single overhead spotlight casting a sharp pool of light, smoke-effect background haze creating depth. Premium product photography. Dramatic shadows. High-contrast lighting. Razor-sharp focus on the watch face. Editorial quality.

**What changed:** The subject noun leads. The physical arrangement is a separate sentence. The environment is a separate sentence. Photography style direction closes the prompt.

---

## Step 3: Add Style Preset and Background

```yaml
chatgpt_image_2:
  style_preset: product_photo
  background: cinematic
  ar: "1:1"
  quality: hd
```

`product_photo` preset + `cinematic` background = sharp subject + moody environment. Correct pairing for a dark editorial hero.

---

## Step 4: Add Negatives

```yaml
negatives:
  - logos
  - text
  - watermark
  - fingerprints
  - reflections on glass
  - hands
  - people
  - blurry
```

Note: `reflections on glass` and `fingerprints` are product-specific negatives that prevent common failure modes for watch photography.

---

## Step 5: Run and Evaluate

Paste the `chatgpt_image_2.prompt` string into ChatGPT Image 2.0.

**Evaluation checklist:**
- [ ] Matte charcoal case visible (not glossy)
- [ ] Sapphire glass face catching light correctly
- [ ] 30-degree float angle achieved
- [ ] Band curving naturally, not rigid
- [ ] Single overhead spotlight visible in composition
- [ ] Smoke-effect background present
- [ ] No logos, text, or watermarks
- [ ] Razor-sharp focus on watch face

If any item fails: identify which APAE field it maps to and refine that field.

---

## Step 6: Midjourney Adaptation

Take the same APAE brief and rewrite for Midjourney syntax:

```
titanium smartwatch matte charcoal case sapphire glass deployant clasp,
floating 30-degree angle clockwise rotation, dark concrete studio single overhead spotlight smoke haze,
premium product photography dramatic shadows high contrast, editorial quality
--ar 1:1 --style raw --v 6 --q 2
```

Note the difference: shorter, no full sentences, flags appended at end.

---

## Step 7: Variants

The base prompt serves the 1:1 hero. For the LinkedIn 16:9 banner:

```yaml
- id: v_linkedin
  label: "LinkedIn Banner"
  change: "Reframe to 16:9. Move watch to left third. Negative space right side for text overlay. Same lighting."
  ar: "16:9"
```

This is a Format Variant (Strategy 4 in `variants/variant_strategies.md`).

---

## Output

The full production-ready YAML file is at:
```
prompt_library/products/wearable_pack/watch_dark_studio_premium.yaml
```
