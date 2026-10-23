"""Validate VPH examples and template shapes without calling image services."""
from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {"products", "fashion", "portraits", "architecture", "abstract", "branding"}
APAE = ("appearance", "place", "action", "emotion")
TEMPLATES = {"prompt_template.yaml", "batch_template.yaml", "brand_pack_template.yaml", "campaign_template.yaml"}

class UniqueLoader(yaml.SafeLoader):
    pass

def mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result

UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)

def text(value):
    return isinstance(value, str) and bool(value.strip())

def validate(data, name):
    errors = []
    def check(ok, message):
        if not ok:
            errors.append(message)
    if not isinstance(data, dict):
        return ["file must be a mapping"]
    check(data.get("license") == "WenceStudio Library License 1.0", "license must be WenceStudio Library License 1.0")
    if name in TEMPLATES:
        if name == "prompt_template.yaml":
            check(isinstance(data.get("apae"), dict) and all(k in data["apae"] for k in APAE), "template needs four APAE fields")
            check(isinstance(data.get("variants"), list) and len(data["variants"]) >= 2, "template needs two variants")
        else:
            key = {"batch_template.yaml": "batch", "brand_pack_template.yaml": "brand_pack", "campaign_template.yaml": "campaign"}[name]
            section = data.get(key)
            check(isinstance(section, dict), f"template needs {key} mapping")
            if isinstance(section, dict):
                required = {"batch": ("prompts", "shared_settings"), "brand_pack": ("visual_identity", "hero", "editorial", "lifestyle", "abstract"), "campaign": ("brand_context", "launch_hero", "social", "editorial", "detail", "variants")}[key]
                check(all(k in section for k in required), "template is missing required sections")
        return errors
    for key in ("title", "version", "category", "engine_primary"):
        check(text(data.get(key)), f"{key} must be nonempty text")
    check(bool(re.fullmatch(r"\d+\.\d+\.\d+", str(data.get("version", "")))), "version must be major.minor.patch")
    check(data.get("category") in CATEGORIES, "unknown category")
    apae = data.get("apae")
    check(isinstance(apae, dict) and all(text(apae.get(k)) for k in APAE), "four nonempty APAE fields required")
    engine = data.get(data.get("engine_primary", ""))
    check(isinstance(engine, dict) and text(engine.get("prompt")), "primary engine needs a prompt")
    negatives = data.get("negatives")
    check(isinstance(negatives, list) and all(text(x) for x in negatives) and len(set(negatives)) >= 3, "need three distinct negatives")
    variants = data.get("variants")
    check(isinstance(variants, list) and len(variants) >= 2, "need two variants")
    if isinstance(variants, list):
        ids = []
        for variant in variants:
            valid = isinstance(variant, dict) and all(text(variant.get(k)) for k in ("id", "label", "change"))
            check(valid, "variant needs id, label, change")
            if valid:
                ids.append(variant["id"])
        check(len(ids) == len(set(ids)), "variant IDs must be unique")
    return errors

def main():
    files = sorted(ROOT.glob("*.yaml"))
    errors = []
    examples = 0
    for path in files:
        try:
            data = yaml.load(path.read_text(), Loader=UniqueLoader)
            errors.extend(f"{path.name}: {e}" for e in validate(data, path.name))
            examples += path.name not in TEMPLATES
        except (yaml.YAMLError, ValueError, TypeError) as exc:
            errors.append(f"{path.name}: {exc}")
    if examples < 8 or not TEMPLATES.issubset({p.name for p in files}):
        errors.append("expected at least eight examples and all four templates")
    for error in errors:
        print("FAIL:", error)
    if errors:
        return 1
    print(f"PASS: {examples} complete examples and {len(TEMPLATES)} template structures")
    return 0

if __name__ == "__main__":
    sys.exit(main())
