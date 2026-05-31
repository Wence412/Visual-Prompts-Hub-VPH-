# Getting Started with VPH

This guide takes you from zero to your first production-ready prompt in under 10 minutes.

---

## Prerequisites

- A text editor that supports YAML syntax highlighting (VS Code recommended)
- Access to at least one supported image engine (ChatGPT Image 2.0, Midjourney, DALL-E 3)
- Basic familiarity with YAML format (key: value pairs, indentation matters)

---

## Step 1: Understand APAE

Before writing a single prompt, understand the four-layer APAE framework. Every prompt in this repo is built on it.

| Layer | Question it answers | Example |
|---|---|---|
| Appearance | What does the subject look like? | `matte black titanium smartwatch, sapphire glass` |
| Place | Where is it? | `dark concrete studio with overhead spotlight` |
| Action | What is it doing? | `floating at 30-degree angle, slight rotation` |
| Emotion | What should the viewer feel? | `premium, futuristic, precise` |

If any one of these four layers is vague, the output will be inconsistent. Specificity is the only lever you have.

---

## Step 2: Copy a Template

Start from a template, not a blank file.

```bash
cp templates/prompt_template.yaml my_first_prompt.yaml
```

Open `my_first_prompt.yaml` in your editor.

---

## Step 3: Fill the Required Fields

Fields marked `[REQUIRED]` must be completed before running any prompt. Do not skip them.

**Minimum viable prompt:**

```yaml
title: "Leather Wallet — Dark Oak Surface — Premium"
version: "1.0.0"
category: products
engine_primary: chatgpt_image_2

apae:
  appearance: "slim bifold wallet, full-grain dark brown leather, hand-burnished edges, card slot visible"
  place: "dark oak wooden surface, single overhead warm spotlight, soft shadow cast left"
  action: "wallet slightly open, angled 45 degrees toward camera, left panel facing forward"
  emotion: "craft, premium, warm, grounded"

chatgpt_image_2:
  prompt: >
    Slim bifold wallet in full-grain dark brown leather with hand-burnished edges and a
    visible card slot. Slightly open, angled 45 degrees toward camera, left panel facing
    forward. Dark oak wooden surface with a single overhead warm spotlight casting a soft
    shadow to the left. Premium product photography. Warm light enhancing leather texture.
    Sharp focus on the burnished edge detail.
  style_preset: product_photo
  background: practical
  ar: "1:1"

negatives:
  - logos
  - text
  - watermark
  - hands
  - blurry

variants:
  - id: v1
    label: "Black Leather"
    change: "Replace dark brown with matte black leather. Cool-toned studio light. Darker background."

  - id: v2
    label: "Lifestyle Desk"
    change: "Add desk context: open notebook, pen, keys alongside wallet. Natural window light."
    background: practical_with_props
```

---

## Step 4: Run the Prompt

Copy the `chatgpt_image_2.prompt` field text and paste it into ChatGPT Image 2.0 (or your chosen engine).

For other engines, use the guidance in `engines/engine_comparison.md` to adapt the prompt format.

---

## Step 5: Review and Iterate

Ask these questions before accepting an output:

1. Does the subject match `apae.appearance` exactly?
2. Is the environment correct per `apae.place`?
3. Does the composition match `apae.action`?
4. Does the mood match `apae.emotion`?
5. Are any negatives visible (logos, watermarks, blur)?

If any answer is no: refine the specific APAE field that failed and re-run.

---

## Step 6: Add Variants

Once the base prompt works, run your variants. See `variants/variant_strategies.md` for the four main strategies.

---

## Step 7: Contribute Back

If your prompt is polished and schema-compliant, consider submitting it to the library. See `CONTRIBUTING.md` for guidelines.

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Vague appearance field | Name the material, finish, color, and key visual detail explicitly |
| Generic emotion | Replace "nice, modern" with specific brand feelings: "architectural, precise, cold authority" |
| Missing negatives | Always include at minimum: logos, text, watermark |
| No variants | Every production prompt needs at least 2. One variant protects against a single-engine failure. |
| Copying the ChatGPT prompt directly to MJ | Adapt using `engines/engine_comparison.md`. Different engines have different prompt grammars. |
