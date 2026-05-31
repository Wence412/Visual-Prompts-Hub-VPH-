# Pull Request

## Type of Change

- [ ] New prompt pack
- [ ] New variant for existing prompt
- [ ] Engine adaptation (Midjourney / DALL-E 3 / SDXL / Firefly / Ideogram)
- [ ] Documentation improvement
- [ ] Bug fix (schema violation, broken YAML, incorrect flag)
- [ ] Other

---

## What This PR Does

Describe what you've added or changed and why.

---

## Affected Files

List all new or modified files:

```
prompt_library/[category]/new_file.yaml
templates/...
docs/...
```

---

## Prompt Pack Details (if applicable)

| Field | Value |
|---|---|
| Category | |
| Number of new prompts | |
| Primary engine | |
| Variants per prompt | |

---

## Validation Checklist

- [ ] All YAML files parse without errors
- [ ] All required APAE fields are present and specific (not generic placeholders)
- [ ] All prompts have `negatives` array with minimum 3 items including logos, text, watermark
- [ ] All prompts have minimum 2 variants
- [ ] File names follow `subject_setting_mood.yaml` convention
- [ ] No copyrighted characters, logos, or real people in prompt content
- [ ] Engine flags match the engine's actual syntax (see `engines/engine_comparison.md`)
- [ ] README Featured Packs table updated (if adding a new category or pack)
- [ ] CHANGELOG.md updated with a brief entry under `[Unreleased]`

---

## Testing

Which engine(s) did you test these prompts on?

- [ ] ChatGPT Image 2.0
- [ ] Midjourney
- [ ] DALL-E 3
- [ ] SDXL
- [ ] Adobe Firefly
- [ ] Ideogram

Describe the output quality briefly. Was the APAE intent accurately reflected?

---

## Additional Notes

Any context the reviewer needs to evaluate this PR.
