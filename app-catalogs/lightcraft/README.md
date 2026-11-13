# LightCraft native catalogs

These are LightCraft’s original JSON catalogs and Rust format-template maps.
The source and licence are recorded in the repository’s ATTRIBUTION.md.
They share the craft-i18n revision with the TSV catalogs, while retaining the grammar that LightCraft’s build checks with the Rust compiler.

LightCraft selects `app-catalogs/lightcraft/locales` below CRAFT_I18N_DIR.
Each `<locale>.json` is a string-to-string map of labels and messages; its `<locale>-formats.json` holds Rust format! templates.
Do not rewrite positional selectors or string precision as named placeholders: they can reorder arguments or omit an English plural suffix without dropping its argument.
An empty translation retains LightCraft’s existing English fallback.
The native app’s complete receiving gate must compile every selected translated format template; the data gate checks JSON shape and file pairing.

The initial import has 17 non-English locales and English remains the source language.
Korean is absent, as it is in the source registry; this import adds no language.
Future translation changes keep their own attribution and run the receiving compiler checks.
