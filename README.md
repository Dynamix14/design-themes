# Frontend Theme Gallery

89 web design themes, each rendered as a complete sample page (nav, hero,
feature cards, metrics, pricing, CTA, footer). Built to be browsed, compared, and
mined for tokens.

**Live gallery:** https://dynamix14.github.io/design-themes/

Gallery features: search, dark/light + brand/archetype filters, `★` save to a local
shortlist (persists in your browser), `⧉ tokens` to copy a theme's `:root` CSS.

## Structure

```
index.html          generated gallery + live previews
themes/<slug>.html  one full sample page per theme
themes_data.py      the only file you edit
build.py            regenerates everything (python build.py)
themes.json         machine-readable token export
```

## Using a theme

Fastest path: hover a tile in the gallery and hit **⧉ tokens** — it copies that
theme's full `:root` block to your clipboard.

Or open a sample and copy its `:root` block from the page source:

- `--bg / --surface / --line` — surfaces
- `--text / --muted` — ink
- `--accent / --accent-2` — brand pair, `--on-accent` is the contrast-safe text colour
- `--r`, `--r-btn` — radii
- `--fh / --fb` — heading / body stacks
- surface treatment: `flat` (hairlines, no shadow), `soft` (border + soft shadow),
  `hard` (2px border + offset shadow), `glow` (dark, accent bloom)

## Adding a theme

Append one line to `themes_data.py`:

```python
T("my-theme", "My Theme", "Archetype", LIGHT,
  ("#FFFFFF", "#F7F7F7", "#E5E5E5", "#111111", "#666666", "#2563EB", "#111111"),
  "Inter|sans", "Inter|sans", 12, "soft", "split", ("grad",),
  "One line about the vibe.")
```

then `python build.py`.

## Theme list

| Theme | Mode | Type | Vibe |
|---|---|---|---|
| [Claude / Anthropic warm editorial](themes/claude.html) | light | Brand | Warm paper, terracotta accent, large editorial serif. |
| [Cohere data-vivid](themes/cohere.html) | light | Brand | Restrained green with a coral counter-accent. |
| [ElevenLabs cinematic dark](themes/elevenlabs.html) | dark | Brand | Near-black stage, waveform-style detail, single violet spark. |
| [Minimax neon bold](themes/minimax.html) | dark | Brand | Big type, saturated dual-neon accent, dark product surfaces. |
| [Mistral orange minimal](themes/mistral.html) | light | Brand | Cream ground, single hot-orange accent, tight uppercase labels. |
| [Ollama terminal mono](themes/ollama.html) | light | Brand | Pure monochrome, zero radius, everything monospaced. |
| [OpenCode dev mono](themes/opencode.html) | dark | Brand | Dark IDE feel, amber caret accent, compact rows. |
| [Replicate code-forward](themes/replicate.html) | light | Brand | White canvas, mono body copy, one hot red accent. |
| [Runway cinematic black](themes/runwayml.html) | dark | Brand | Full black, huge white type, media-first composition. |
| [Together AI blueprint](themes/together.html) | dark | Brand | Blueprint grid, technical labels, cyan/indigo pair. |
| [VoltAgent void emerald](themes/voltagent.html) | dark | Brand | Void black, terminal blocks, emerald signal. |
| [xAI stark mono](themes/xai.html) | dark | Brand | Absolute monochrome, hairline rules, all caps. |
| [Cursor gradient dark](themes/cursor.html) | dark | Brand | Charcoal panels with a violet-to-blue sweep. |
| [Expo tight code](themes/expo.html) | dark | Brand | Compressed tracking, product-UI density, expo indigo. |
| [Linear precise dark](themes/linear.html) | dark | Brand | Near-black, hairline borders, one refined indigo accent. |
| [Lovable playful gradient](themes/lovable.html) | light | Brand | Peach wash, pink-to-amber gradient, friendly round shapes. |
| [Mintlify reading green](themes/mintlify.html) | light | Brand | Documentation calm: generous line height, green links. |
| [PostHog playful data](themes/posthog.html) | light | Brand | Warm off-white, orange primary, unexpectedly bright blue. |
| [Raycast chrome glow](themes/raycast.html) | dark | Brand | Command-palette chrome, red-to-violet glow. |
| [Resend minimal mono](themes/resend.html) | dark | Brand | Black, white, monospace labels, no decoration. |
| [Sentry data dense](themes/sentry.html) | dark | Brand | Purple-dark dashboard, pink signal, dense stat rows. |
| [Supabase emerald dark](themes/supabase.html) | dark | Brand | Developer dark with a single emerald accent. |
| [Superhuman premium glow](themes/superhuman.html) | dark | Brand | Keyboard-first premium dark with violet halo. |
| [Vercel black and white](themes/vercel.html) | light | Brand | Geist system, hairline borders, geometric precision. |
| [Warp block terminal](themes/warp.html) | dark | Brand | Command blocks, blue focus ring, IDE density. |
| [Zapier warm friendly](themes/zapier.html) | light | Brand | Warm cream, illustration-friendly, generous rounding. |
| [ClickHouse yellow technical](themes/clickhouse.html) | light | Brand | Documentation-first, yellow highlight blocks, mono data. |
| [Composio integration dark](themes/composio.html) | dark | Brand | Dark canvas with colourful integration chips. |
| [HashiCorp enterprise B/W](themes/hashicorp.html) | light | Brand | Enterprise neutral, black rules, minimal flourish. |
| [MongoDB leaf green](themes/mongodb.html) | light | Brand | Developer docs posture, bright leaf green. |
| [Sanity red content-first](themes/sanity.html) | light | Brand | Editorial content blocks, red accent, flat surfaces. |
| [Stripe gradient elegance](themes/stripe.html) | light | Brand | Weight-300 elegance, signature violet gradient. |
| [Airtable structured colour](themes/airtable.html) | light | Brand | Structured data blocks, warm yellow + blue pairing. |
| [Cal.com neutral simple](themes/cal.html) | light | Brand | Quiet neutral UI, developer honesty, no ornament. |
| [Clay organic art direction](themes/clay.html) | light | Brand | Cream ground, soft organic shapes, muted violet. |
| [Figma multicolour playful](themes/figma.html) | light | Brand | Multi-hue accents, playful yet professional. |
| [Framer motion bold](themes/framer.html) | dark | Brand | Black + electric blue, motion-first framing. |
| [Intercom conversational blue](themes/intercom.html) | light | Brand | Friendly blue, chat-shaped surfaces, generous padding. |
| [Miro canvas yellow](themes/miro.html) | light | Brand | Sunny yellow accent on a bright white canvas. |
| [Notion warm minimal](themes/notion.html) | light | Brand | Warm greys, serif headings, document-like calm. |
| [Pinterest image-first](themes/pinterest.html) | light | Brand | Red pin accent, masonry-ready cards, rounded imagery. |
| [Webflow polished marketing](themes/webflow.html) | light | Brand | Clean marketing polish, confident blue CTA. |
| [Coinbase institutional blue](themes/coinbase.html) | light | Brand | Trust-first blue, heavy numbers, calm surfaces. |
| [Kraken purple data](themes/kraken.html) | dark | Brand | Deep navy with violet data accents. |
| [Revolut fintech dark](themes/revolut.html) | dark | Brand | Glossy dark cards, gradient light, premium fintech. |
| [Wise bright green](themes/wise.html) | light | Brand | Lime accent, dark forest ink, cheerful clarity. |
| [Airbnb coral warmth](themes/airbnb.html) | light | Brand | Photography-first, rounded cards, coral CTA. |
| [Apple premium white space](themes/apple.html) | light | Brand | Huge headline, airy spacing, cinematic restraint. |
| [BMW engineering dark](themes/bmw.html) | dark | Brand | Precise dark surfaces, blue engineering accent. |
| [IBM Carbon blue](themes/ibm.html) | light | Brand | Carbon grid discipline, zero radius, Plex throughout. |
| [NVIDIA green-black](themes/nvidia.html) | dark | Brand | Black with aggressive green, technical power. |
| [SpaceX stark full-bleed](themes/spacex.html) | dark | Brand | All-caps display type, black ground, nothing decorative. |
| [Spotify bold green](themes/spotify.html) | dark | Brand | Bold condensed feel, vibrant green on near-black. |
| [Uber tight black white](themes/uber.html) | light | Brand | Heavy type, tight tracking, urban directness. |
| [Arc browser soft gradient](themes/arc.html) | light | Brand | Pastel gradient wash, soft rounded surfaces. |
| [Nothing dot-matrix tech](themes/nothing.html) | dark | Brand | Monospace labels, dot grid, stark product honesty. |
| [Glassmorphism frosted glass](themes/glassmorphism.html) | dark | Archetype | Translucent panels, blurred depth, luminous edges. |
| [Neubrutalism hard shadow](themes/neubrutalism.html) | light | Archetype | Thick black borders, offset shadows, loud accent blocks. |
| [Neumorphism soft clay](themes/neumorphism.html) | light | Archetype | Extruded soft surfaces, low contrast, no hard borders. |
| [Editorial serif magazine](themes/editorial.html) | light | Archetype | Serif display, drop-cap rhythm, print-magazine columns. |
| [Swiss international style](themes/swiss.html) | light | Archetype | Grid, Helvetica logic, one red accent, zero rounding. |
| [Terminal phosphor](themes/terminal.html) | dark | Archetype | Phosphor green, scanline grid, keyboard-first. |
| [Retro 8-bit arcade](themes/retro8bit.html) | dark | Archetype | Pixel type, chunky borders, arcade cabinet colour. |
| [Vaporwave sunset](themes/vaporwave.html) | dark | Archetype | Purple sunset gradient, pink/cyan neon, retro-future. |
| [Cyberpunk neon grid](themes/cyberpunk.html) | dark | Archetype | Cyan/magenta neon, technical overlays, hard edges. |
| [Pastel soft UI](themes/pastel.html) | light | Archetype | Low-contrast pastels, very round, gentle and soft. |
| [Claymorphism chunky soft](themes/claymorphism.html) | light | Archetype | Puffy rounded shapes, thick soft shadows, toy-like depth. |
| [Bento box grid](themes/bento.html) | dark | Archetype | Asymmetric tile grid, mixed card sizes, orange highlight. |
| [Gradient mesh + grain](themes/meshgrain.html) | dark | Archetype | Blurred colour mesh, film grain, aurora feel. |
| [Paper sketch / hand drawn](themes/sketch.html) | light | Archetype | Notebook ground, wobbly borders, highlighter marks. |
| [Luxury dark serif gold](themes/luxury.html) | dark | Archetype | Black and gold, hairline rules, couture spacing. |
| [Blueprint engineering](themes/blueprint.html) | dark | Archetype | Blue drafting paper, measurement ticks, mono labels. |
| [Y2K chrome gloss](themes/y2k.html) | light | Archetype | Chrome bevels, iridescent gradients, early-2000s optimism. |
| [Memphis playful shapes](themes/memphis.html) | light | Archetype | Confetti shapes, thick outlines, upbeat primary mix. |
| [Organic nature calm](themes/nature.html) | light | Archetype | Earthy neutrals, serif warmth, sustainable-brand calm. |
| [Brutalist type block](themes/brutalist.html) | dark | Archetype | Massive type blocks, exposed structure, raw edges. |
| [Monochrome editorial](themes/monochrome.html) | light | Archetype | Grayscale only, serif/sans pairing, gallery restraint. |
| [Academic journal](themes/academic.html) | light | Archetype | Full serif, rule lines, footnoted credibility. |
| [Modern startup SaaS](themes/startup.html) | light | Archetype | The polished default: clean cards, soft shadow, indigo CTA. |
| [AI product dark violet](themes/ai.html) | dark | Archetype | Violet glow, gradient type, neural ambience. |
| [Fintech trustworthy](themes/fintech.html) | light | Archetype | Calm teal, tabular figures, institutional confidence. |
| [Sportswear high energy](themes/sportswear.html) | dark | Archetype | Volt accent, huge condensed type, motion lines. |
| [Wellness spa calm](themes/wellness.html) | light | Archetype | Sage and sand, airy spacing, slow and restorative. |
| [Gaming neon HUD](themes/gaming.html) | dark | Archetype | HUD frames, magenta/cyan glow, angular panels. |
| [Kids bright rounded](themes/kids.html) | light | Archetype | Big rounded type, primary colours, playful and safe. |
| [Corporate trustworthy](themes/corporate.html) | light | Archetype | Restrained navy, structured sections, annual-report calm. |
| [Photography portfolio](themes/photography.html) | dark | Archetype | Full-bleed imagery framing, thin serif captions. |
| [Art deco gold geometry](themes/artdeco.html) | dark | Archetype | Gold rules, symmetrical framing, 1920s geometry. |
| [Ultra-minimal mono](themes/minimalmono.html) | light | Archetype | Almost nothing: hairlines, whitespace, one weight. |

## Notes

Layouts and copy are original; palettes approximate each product's public visual
language for reference purposes. Fonts are Google Fonts substitutes for proprietary
faces. Sample content ("Aperture") is placeholder.
