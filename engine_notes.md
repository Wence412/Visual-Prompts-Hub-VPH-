# Engine Notes — APAE Override Tips

These are per-engine notes for adjusting APAE fields when authoring `engine_overrides` entries. Reference before writing any engine-specific prompt string.

---

## ChatGPT Image 2.0

**APAE → Prompt translation:** Full sentences. Combine all four fields into a flowing paragraph. Add lighting, composition, and photography style as additional sentences.

**Key tips:**
- Front-load the subject noun from `appearance`. Engine parses subject first.
- State lighting explicitly in a separate sentence after scene setup.
- Add `"Product photography"` or `"Editorial photography"` as a quality anchor phrase.
- End with a quality statement: `"Razor-sharp focus. No motion blur. 4K resolution."` (optional but helps for hd quality setting)

**What to watch:**
- Engine sometimes adds unwanted bokeh on background. Add `"flat background with no bokeh"` if gradient or clean backgrounds require sharp backgrounds.
- May soften skin textures on portrait prompts. Add `"No beauty filter. Skin texture visible."` for editorial portraits.

---

## Midjourney v6+

**APAE → Prompt translation:** Dense adjective list, then subject noun, then location, then lighting. No full sentences. Comma-separated descriptors work better than paragraphs.

**Key tips:**
- `appearance` → Extract material + finish + key adjectives. List them first.
- `place` → Describe in 3–5 words.
- `action` → Keep to 1–2 short phrases. MJ handles explicit action direction less literally than ChatGPT.
- `emotion` → Append to end of prompt as single descriptive words. MJ reads these as style direction.
- Always add `--style raw` for photorealistic outputs.
- Camera and lens references reliably improve MJ quality: `shot on Hasselblad 907X, Zeiss 85mm`.

**What to watch:**
- Prompt length over 200 words degrades MJ output. Keep it tight.
- MJ may add aesthetic elements not in the prompt when `--style raw` is omitted.

---

## DALL-E 3

**APAE → Prompt translation:** Verbatim instructions in complete sentences. Most literal engine. What you write is what you get.

**Key tips:**
- Use `appearance` to write a full descriptive sentence about the subject.
- Use `place` as a standalone sentence: `"The setting is a dark concrete studio..."`
- Use `action` explicitly: `"The subject is positioned at..."`
- Use `emotion` as a closing direction: `"The overall mood is premium and cinematic."`
- State negatives explicitly in the prompt body, not just in the YAML `negatives` array: `"No logos, text, or brand marks are visible."`

**What to watch:**
- DALL-E 3 may refuse some prompts that MJ or ChatGPT Image handle without issue. Use more neutral language for edgy editorial content.
- Can over-saturate colors. Add `"muted, natural color grading"` if needed.

---

## SDXL

**APAE → Prompt translation:** Positive prompt is keyword and adjective-heavy. Separate negative prompt field handles negatives.

**Positive prompt construction:**
```
[quality tokens], [appearance adjectives], [subject noun], [place], [action], [emotion/style]
```

**Quality tokens to prepend:**
```
masterpiece, best quality, ultra-detailed, 8K,
```

**Negative prompt (use this as your baseline):**
```
ugly, blurry, low quality, watermark, text, logo, deformed, overexposed, flat, amateur, jpeg artifacts
```

**Key tips:**
- `emotion` field → Translate to style tokens: `cinematic lighting, dramatic shadows, editorial photography`
- CFG scale controls literalness. Increase to 8–9 for very specific prompts. Drop to 5–6 for more creative variance.
- SDXL handles material textures well when `appearance` descriptions are specific.

---

## Adobe Firefly

**APAE → Prompt translation:** Shorter, more natural language. Firefly responds well to style and mood direction.

**Key tips:**
- Use `emotion` field as your primary style direction. Firefly's style controls amplify this.
- `appearance` → Focus on material and surface. Firefly handles texture particularly well.
- Avoid long action sequences. Keep `action` to a simple positional description.
- Use Firefly's Content Type and Style controls alongside the prompt for best results.

**Best for:** Texture and material shots (abstract, surface detail). Not ideal for complex compositional prompts.

---

## Ideogram 2.0

**APAE → Prompt translation:** Standard sentence-based prompt. Primary advantage over other engines is text rendering.

**Key tips:**
- For VPH prompts where negatives include `text`: explicitly state `"No text or typography visible in the image."` Ideogram defaults to adding text if the prompt includes a brand or product name.
- For packaging or branding prompts that need text: Ideogram is the recommended engine. Remove text from negatives and specify exact text in the `action` or a new `text_element` field.
- Aspect ratio: Specify in prompt as `"horizontal 16:9 composition"` or use platform's built-in ratio selector.
