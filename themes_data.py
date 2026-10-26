"""Theme definitions for the frontend theme gallery.

Each theme is a token set + a few structural knobs. `build.py` turns these into
one full sample page per theme and the browsable index. Edit values here and
re-run `python build.py` -- never hand-edit the generated HTML.
"""

# ---------------------------------------------------------------- helpers

FALLBACK = {
    "sans": 'system-ui, -apple-system, "Segoe UI", Roboto, sans-serif',
    "serif": 'Georgia, "Times New Roman", serif',
    "mono": '"SF Mono", ui-monospace, Consolas, monospace',
}

# Google Fonts families that only ship 400 (no weight range in the URL)
STATIC_ONLY = {"Press Start 2P", "VT323", "Bebas Neue"}

THEMES = []


def T(slug, name, cat, mode, pal, fh, fb, radius, treat,
      hero="split", flags=(), note=""):
    """Register one theme.

    pal    = (bg, surface, line, text, muted, accent, accent2)
    fh/fb  = "Family Name|sans"  heading / body font
    treat  = flat | soft | hard | glow   (surface treatment)
    hero   = split | center | stack
    flags  = caps mono grad grain grid blur glow wide tight pill
    """
    bg, surface, line, text, muted, accent, accent2 = pal
    THEMES.append(dict(
        slug=slug, name=name, cat=cat, mode=mode, bg=bg, surface=surface,
        line=line, text=text, muted=muted, accent=accent, accent2=accent2,
        fh=fh, fb=fb, radius=radius, treat=treat, hero=hero,
        flags=list(flags), note=note,
    ))


DARK, LIGHT = "dark", "light"

# ---------------------------------------------------------------- brands
# Palettes approximate each product's public visual language. Layouts are
# original; only colour/type posture is borrowed.

T("claude", "Claude / Anthropic warm editorial", "Brand", LIGHT,
  ("#F5F4EE", "#FBFAF6", "#DEDBD2", "#1F1E1B", "#6B6A63", "#C15F3C", "#8C7A6B"),
  "Instrument Serif|serif", "Inter|sans", 14, "flat", "split",
  ("wide",), "Warm paper, terracotta accent, large editorial serif.")

T("cohere", "Cohere data-vivid", "Brand", LIGHT,
  ("#FFFFFF", "#F6F7F5", "#E2E5E0", "#0E1912", "#5C6B62", "#39594D", "#FF7759"),
  "Inter|sans", "Inter|sans", 12, "soft", "split",
  ("grad",), "Restrained green with a coral counter-accent.")

T("elevenlabs", "ElevenLabs cinematic dark", "Brand", DARK,
  ("#08080A", "#111114", "#26262B", "#F2F2F4", "#8D8D96", "#E8E8EA", "#6E56CF"),
  "Inter|sans", "Inter|sans", 10, "glow", "center",
  ("glow", "grad"), "Near-black stage, waveform-style detail, single violet spark.")

T("minimax", "Minimax neon bold", "Brand", DARK,
  ("#0A0A0F", "#13131B", "#262633", "#F6F6FA", "#8F8FA6", "#FF4D6D", "#7B61FF"),
  "Sora|sans", "Sora|sans", 16, "glow", "split",
  ("glow", "tight"), "Big type, saturated dual-neon accent, dark product surfaces.")

T("mistral", "Mistral orange minimal", "Brand", LIGHT,
  ("#FFFAF0", "#FFFFFF", "#EFE4D2", "#1A1712", "#6E6354", "#FF7000", "#1A1712"),
  "Inter|sans", "Inter|sans", 8, "flat", "split",
  ("caps",), "Cream ground, single hot-orange accent, tight uppercase labels.")

T("ollama", "Ollama terminal mono", "Brand", LIGHT,
  ("#FFFFFF", "#F5F5F5", "#DFDFDF", "#0A0A0A", "#5F5F5F", "#0A0A0A", "#5F5F5F"),
  "JetBrains Mono|mono", "JetBrains Mono|mono", 2, "flat", "stack",
  ("mono",), "Pure monochrome, zero radius, everything monospaced.")

T("opencode", "OpenCode dev mono", "Brand", DARK,
  ("#0D0D0D", "#161616", "#2A2A2A", "#EDEDED", "#8A8A8A", "#E5A00D", "#EDEDED"),
  "JetBrains Mono|mono", "JetBrains Mono|mono", 3, "flat", "stack",
  ("mono",), "Dark IDE feel, amber caret accent, compact rows.")

T("replicate", "Replicate code-forward", "Brand", LIGHT,
  ("#FFFFFF", "#FAFAFA", "#E6E6E6", "#111111", "#666666", "#EA2804", "#111111"),
  "Inter|sans", "JetBrains Mono|mono", 6, "flat", "split",
  ("mono",), "White canvas, mono body copy, one hot red accent.")

T("runwayml", "Runway cinematic black", "Brand", DARK,
  ("#000000", "#0D0D0D", "#242424", "#FFFFFF", "#9A9A9A", "#FFFFFF", "#00C2FF"),
  "Inter|sans", "Inter|sans", 4, "flat", "center",
  ("wide",), "Full black, huge white type, media-first composition.")

T("together", "Together AI blueprint", "Brand", DARK,
  ("#0B1120", "#111A2E", "#1F2C47", "#E7EEFB", "#8FA1C0", "#0EA5E9", "#6366F1"),
  "IBM Plex Sans|sans", "IBM Plex Sans|sans", 8, "flat", "split",
  ("grid",), "Blueprint grid, technical labels, cyan/indigo pair.")

T("voltagent", "VoltAgent void emerald", "Brand", DARK,
  ("#050505", "#0D0D0D", "#1F1F1F", "#F2F2F2", "#8A8A8A", "#10B981", "#34D399"),
  "JetBrains Mono|mono", "Inter|sans", 6, "flat", "stack",
  ("mono",), "Void black, terminal blocks, emerald signal.")

T("xai", "xAI stark mono", "Brand", DARK,
  ("#000000", "#0A0A0A", "#1E1E1E", "#FFFFFF", "#8C8C8C", "#FFFFFF", "#8C8C8C"),
  "JetBrains Mono|mono", "JetBrains Mono|mono", 0, "flat", "stack",
  ("mono", "caps"), "Absolute monochrome, hairline rules, all caps.")

T("cursor", "Cursor gradient dark", "Brand", DARK,
  ("#0C0C0D", "#141416", "#26262A", "#EFEFF1", "#8C8C94", "#8B5CF6", "#3B82F6"),
  "Inter|sans", "Inter|sans", 10, "glow", "split",
  ("glow", "grad"), "Charcoal panels with a violet-to-blue sweep.")

T("expo", "Expo tight code", "Brand", DARK,
  ("#0B0B0F", "#141419", "#242430", "#F1F1F5", "#8E8E9C", "#4630EB", "#00D2FF"),
  "Inter|sans", "JetBrains Mono|mono", 8, "flat", "split",
  ("tight",), "Compressed tracking, product-UI density, expo indigo.")

T("linear", "Linear precise dark", "Brand", DARK,
  ("#08090A", "#101113", "#1F2124", "#F7F8F8", "#8A8F98", "#5E6AD2", "#8B93E8"),
  "Inter|sans", "Inter|sans", 8, "soft", "split",
  ("tight",), "Near-black, hairline borders, one refined indigo accent.")

T("lovable", "Lovable playful gradient", "Brand", LIGHT,
  ("#FFF8F2", "#FFFFFF", "#F3E4D8", "#241B16", "#7A6A60", "#FF5C8A", "#FFB347"),
  "DM Sans|sans", "DM Sans|sans", 20, "soft", "center",
  ("grad",), "Peach wash, pink-to-amber gradient, friendly round shapes.")

T("mintlify", "Mintlify reading green", "Brand", LIGHT,
  ("#FFFFFF", "#F7F9F8", "#E3E9E6", "#0C1A14", "#5C6B65", "#0D9373", "#111111"),
  "Inter|sans", "Inter|sans", 8, "flat", "split",
  (), "Documentation calm: generous line height, green links.")

T("posthog", "PostHog playful data", "Brand", LIGHT,
  ("#FFF8F2", "#FFFFFF", "#EFE0D4", "#1C1410", "#6F6058", "#F54E00", "#1D4AFF"),
  "Rubik|sans", "Rubik|sans", 12, "soft", "split",
  (), "Warm off-white, orange primary, unexpectedly bright blue.")

T("raycast", "Raycast chrome glow", "Brand", DARK,
  ("#070708", "#111112", "#26262A", "#F4F4F6", "#8B8B93", "#FF6363", "#7C5CFF"),
  "Inter|sans", "Inter|sans", 12, "glow", "split",
  ("glow", "grad"), "Command-palette chrome, red-to-violet glow.")

T("resend", "Resend minimal mono", "Brand", DARK,
  ("#000000", "#0C0C0C", "#222222", "#F5F5F5", "#8F8F8F", "#FFFFFF", "#A3E635"),
  "Inter|sans", "JetBrains Mono|mono", 6, "flat", "center",
  ("mono",), "Black, white, monospace labels, no decoration.")

T("sentry", "Sentry data dense", "Brand", DARK,
  ("#181225", "#211A33", "#332B4D", "#F2EFF8", "#A99FC0", "#F06BA8", "#7553FF"),
  "Rubik|sans", "Rubik|sans", 8, "soft", "split",
  (), "Purple-dark dashboard, pink signal, dense stat rows.")

T("supabase", "Supabase emerald dark", "Brand", DARK,
  ("#121212", "#1A1A1A", "#2C2C2C", "#EDEDED", "#8C8C8C", "#3ECF8E", "#1F9E6B"),
  "Inter|sans", "Inter|sans", 8, "flat", "split",
  ("mono",), "Developer dark with a single emerald accent.")

T("superhuman", "Superhuman premium glow", "Brand", DARK,
  ("#141317", "#1B1A20", "#2C2A33", "#F5F3F8", "#9A96A6", "#8A6BFF", "#C9A4FF"),
  "Inter|sans", "Inter|sans", 14, "glow", "split",
  ("glow", "grad"), "Keyboard-first premium dark with violet halo.")

T("vercel", "Vercel black and white", "Brand", LIGHT,
  ("#FFFFFF", "#FAFAFA", "#EAEAEA", "#000000", "#666666", "#000000", "#0070F3"),
  "Geist|sans", "Geist|sans", 6, "flat", "center",
  ("tight",), "Geist system, hairline borders, geometric precision.")

T("warp", "Warp block terminal", "Brand", DARK,
  ("#0A0A0A", "#141414", "#282828", "#F0F0F0", "#8A8A8A", "#01A0FF", "#F0F0F0"),
  "Inter|sans", "JetBrains Mono|mono", 6, "flat", "stack",
  ("mono",), "Command blocks, blue focus ring, IDE density.")

T("zapier", "Zapier warm friendly", "Brand", LIGHT,
  ("#FFF3E8", "#FFFFFF", "#F2DFCE", "#2B1B10", "#77665A", "#FF4F00", "#2B1B10"),
  "DM Sans|sans", "DM Sans|sans", 16, "soft", "split",
  (), "Warm cream, illustration-friendly, generous rounding.")

T("clickhouse", "ClickHouse yellow technical", "Brand", LIGHT,
  ("#FFFFFF", "#FFFDF2", "#EDE7CF", "#141414", "#6B6754", "#FFCC01", "#141414"),
  "Inter|sans", "JetBrains Mono|mono", 4, "flat", "split",
  ("grid",), "Documentation-first, yellow highlight blocks, mono data.")

T("composio", "Composio integration dark", "Brand", DARK,
  ("#08080C", "#101016", "#232330", "#F2F2F7", "#8B8B99", "#6C5CE7", "#22D3EE"),
  "Inter|sans", "Inter|sans", 12, "soft", "split",
  (), "Dark canvas with colourful integration chips.")

T("hashicorp", "HashiCorp enterprise B/W", "Brand", LIGHT,
  ("#FFFFFF", "#F4F4F4", "#DCDCDC", "#0D0D0D", "#6A6A6A", "#0D0D0D", "#1060FF"),
  "Inter|sans", "Inter|sans", 4, "flat", "split",
  ("caps",), "Enterprise neutral, black rules, minimal flourish.")

T("mongodb", "MongoDB leaf green", "Brand", LIGHT,
  ("#FFFFFF", "#F9FBF9", "#E1EAE3", "#001E2B", "#4C6A5B", "#00ED64", "#001E2B"),
  "Inter|sans", "Inter|sans", 8, "flat", "split",
  ("mono",), "Developer docs posture, bright leaf green.")

T("sanity", "Sanity red content-first", "Brand", LIGHT,
  ("#F9F9F9", "#FFFFFF", "#E6E6E6", "#101112", "#63656A", "#F03E2F", "#101112"),
  "Inter|sans", "Inter|sans", 6, "flat", "stack",
  ("tight",), "Editorial content blocks, red accent, flat surfaces.")

T("stripe", "Stripe gradient elegance", "Brand", LIGHT,
  ("#FFFFFF", "#F6F9FC", "#E3E8EE", "#0A2540", "#425466", "#635BFF", "#00D4FF"),
  "Inter|sans", "Inter|sans", 10, "soft", "split",
  ("grad",), "Weight-300 elegance, signature violet gradient.")

T("airtable", "Airtable structured colour", "Brand", LIGHT,
  ("#FFFFFF", "#F7F8FA", "#E4E7EC", "#1D1F25", "#61646C", "#FCB400", "#18BFFF"),
  "Inter|sans", "Inter|sans", 10, "soft", "split",
  (), "Structured data blocks, warm yellow + blue pairing.")

T("cal", "Cal.com neutral simple", "Brand", LIGHT,
  ("#FFFFFF", "#F9F9F9", "#E5E5E5", "#111111", "#666666", "#111111", "#3B82F6"),
  "Manrope|sans", "Inter|sans", 8, "soft", "split",
  (), "Quiet neutral UI, developer honesty, no ornament.")

T("clay", "Clay organic art direction", "Brand", LIGHT,
  ("#F7F6F3", "#FFFFFF", "#E4E1D8", "#1B1A17", "#6E6A62", "#5B5BD6", "#B4E1C1"),
  "Fraunces|serif", "Inter|sans", 24, "soft", "center",
  ("wide",), "Cream ground, soft organic shapes, muted violet.")

T("figma", "Figma multicolour playful", "Brand", LIGHT,
  ("#FFFFFF", "#F7F7F7", "#E4E4E4", "#1E1E1E", "#666666", "#F24E1E", "#A259FF"),
  "Inter|sans", "Inter|sans", 12, "soft", "center",
  ("grad",), "Multi-hue accents, playful yet professional.")

T("framer", "Framer motion bold", "Brand", DARK,
  ("#0A0A0A", "#131313", "#262626", "#FFFFFF", "#909090", "#0099FF", "#0055FF"),
  "Inter|sans", "Inter|sans", 10, "flat", "split",
  ("tight", "glow"), "Black + electric blue, motion-first framing.")

T("intercom", "Intercom conversational blue", "Brand", LIGHT,
  ("#FFFFFF", "#F5F9FF", "#DCE8F7", "#0B1B2B", "#5A6B7D", "#1F8DED", "#0B1B2B"),
  "Inter|sans", "Inter|sans", 14, "soft", "split",
  (), "Friendly blue, chat-shaped surfaces, generous padding.")

T("miro", "Miro canvas yellow", "Brand", LIGHT,
  ("#FFFFFF", "#FFFDF0", "#EDE6CC", "#1A1A1A", "#6B6B6B", "#FFD02F", "#1A1A1A"),
  "Inter|sans", "Inter|sans", 16, "soft", "center",
  (), "Sunny yellow accent on a bright white canvas.")

T("notion", "Notion warm minimal", "Brand", LIGHT,
  ("#FFFFFF", "#F7F6F3", "#E9E7E2", "#191919", "#73726E", "#191919", "#E9E7E2"),
  "Lora|serif", "Inter|sans", 4, "flat", "stack",
  (), "Warm greys, serif headings, document-like calm.")

T("pinterest", "Pinterest image-first", "Brand", LIGHT,
  ("#FFFFFF", "#F1F1F1", "#E0E0E0", "#111111", "#5F5F5F", "#E60023", "#111111"),
  "DM Sans|sans", "DM Sans|sans", 18, "soft", "split",
  (), "Red pin accent, masonry-ready cards, rounded imagery.")

T("webflow", "Webflow polished marketing", "Brand", LIGHT,
  ("#FFFFFF", "#F8F9FB", "#E1E5EA", "#080808", "#5C636E", "#146EF5", "#080808"),
  "Inter|sans", "Inter|sans", 8, "soft", "split",
  (), "Clean marketing polish, confident blue CTA.")

T("coinbase", "Coinbase institutional blue", "Brand", LIGHT,
  ("#FFFFFF", "#F5F8FF", "#DCE4F2", "#0A0B0D", "#5B6472", "#0052FF", "#0A0B0D"),
  "Inter|sans", "Inter|sans", 10, "soft", "split",
  ("tight",), "Trust-first blue, heavy numbers, calm surfaces.")

T("kraken", "Kraken purple data", "Brand", DARK,
  ("#0B0E14", "#131824", "#232B3D", "#EAEEF7", "#8A93A6", "#7B3FE4", "#35D0BA"),
  "Inter|sans", "Inter|sans", 8, "soft", "split",
  (), "Deep navy with violet data accents.")

T("revolut", "Revolut fintech dark", "Brand", DARK,
  ("#07070A", "#111116", "#242430", "#F7F7FA", "#8E8E9E", "#FFFFFF", "#6C5CE7"),
  "Inter|sans", "Inter|sans", 16, "glow", "center",
  ("grad", "glow"), "Glossy dark cards, gradient light, premium fintech.")

T("wise", "Wise bright green", "Brand", LIGHT,
  ("#FFFFFF", "#F2FBEA", "#DBEBC8", "#163300", "#4A6B33", "#9FE870", "#163300"),
  "DM Sans|sans", "DM Sans|sans", 18, "soft", "split",
  (), "Lime accent, dark forest ink, cheerful clarity.")

T("airbnb", "Airbnb coral warmth", "Brand", LIGHT,
  ("#FFFFFF", "#F7F7F7", "#EBEBEB", "#222222", "#6A6A6A", "#FF385C", "#222222"),
  "DM Sans|sans", "DM Sans|sans", 18, "soft", "split",
  (), "Photography-first, rounded cards, coral CTA.")

T("apple", "Apple premium white space", "Brand", LIGHT,
  ("#FFFFFF", "#F5F5F7", "#E5E5E7", "#1D1D1F", "#6E6E73", "#0071E3", "#1D1D1F"),
  "-apple-system|sans", "-apple-system|sans", 18, "flat", "center",
  ("tight", "wide"), "Huge headline, airy spacing, cinematic restraint.")

T("bmw", "BMW engineering dark", "Brand", DARK,
  ("#0B0B0D", "#111114", "#26262B", "#F4F4F5", "#95959C", "#0066B1", "#FFFFFF"),
  "Inter|sans", "Inter|sans", 2, "flat", "split",
  ("caps",), "Precise dark surfaces, blue engineering accent.")

T("ibm", "IBM Carbon blue", "Brand", LIGHT,
  ("#FFFFFF", "#F4F4F4", "#E0E0E0", "#161616", "#525252", "#0F62FE", "#161616"),
  "IBM Plex Sans|sans", "IBM Plex Sans|sans", 0, "flat", "split",
  ("grid",), "Carbon grid discipline, zero radius, Plex throughout.")

T("nvidia", "NVIDIA green-black", "Brand", DARK,
  ("#000000", "#0D1208", "#233014", "#F2F5EC", "#93A583", "#76B900", "#B4FF3A"),
  "Inter|sans", "Inter|sans", 3, "flat", "split",
  ("tight",), "Black with aggressive green, technical power.")

T("spacex", "SpaceX stark full-bleed", "Brand", DARK,
  ("#000000", "#0A0A0A", "#222222", "#FFFFFF", "#9C9C9C", "#FFFFFF", "#9C9C9C"),
  "Bebas Neue|sans", "Inter|sans", 0, "flat", "center",
  ("caps", "wide"), "All-caps display type, black ground, nothing decorative.")

T("spotify", "Spotify bold green", "Brand", DARK,
  ("#121212", "#181818", "#2A2A2A", "#FFFFFF", "#B3B3B3", "#1ED760", "#FFFFFF"),
  "DM Sans|sans", "DM Sans|sans", 12, "soft", "split",
  ("tight",), "Bold condensed feel, vibrant green on near-black.")

T("uber", "Uber tight black white", "Brand", LIGHT,
  ("#FFFFFF", "#F6F6F6", "#E2E2E2", "#000000", "#6B6B6B", "#000000", "#276EF1"),
  "DM Sans|sans", "DM Sans|sans", 4, "flat", "split",
  ("tight",), "Heavy type, tight tracking, urban directness.")

T("arc", "Arc browser soft gradient", "Brand", LIGHT,
  ("#FDFCFB", "#FFFFFF", "#EDE9F5", "#191624", "#6A6478", "#7C4DFF", "#FF7AB6"),
  "Manrope|sans", "Manrope|sans", 20, "soft", "center",
  ("grad",), "Pastel gradient wash, soft rounded surfaces.")

T("nothing", "Nothing dot-matrix tech", "Brand", DARK,
  ("#0A0A0A", "#131313", "#2B2B2B", "#F2F2F2", "#8A8A8A", "#FFFFFF", "#FF3B30"),
  "Space Grotesk|sans", "JetBrains Mono|mono", 2, "flat", "stack",
  ("mono", "caps", "grid"), "Monospace labels, dot grid, stark product honesty.")

# ---------------------------------------------------------------- archetypes
# Non-brand aesthetic movements: the ones people actually ask for by name.

T("glassmorphism", "Glassmorphism frosted glass", "Archetype", DARK,
  ("#0B1220", "#16233A", "#33465F", "#EAF2FF", "#A2B4CC", "#7DD3FC", "#C4B5FD"),
  "Inter|sans", "Inter|sans", 20, "glow", "split",
  ("blur", "glow", "grad"), "Translucent panels, blurred depth, luminous edges.")

T("neubrutalism", "Neubrutalism hard shadow", "Archetype", LIGHT,
  ("#FFFDF5", "#FFFFFF", "#000000", "#000000", "#3D3D3D", "#FF5CA8", "#FFD93D"),
  "Space Grotesk|sans", "Space Grotesk|sans", 2, "hard", "split",
  ("hard",), "Thick black borders, offset shadows, loud accent blocks.")

T("neumorphism", "Neumorphism soft clay", "Archetype", LIGHT,
  ("#E6E9EF", "#E6E9EF", "#D3D8E2", "#2A3040", "#6B7280", "#4F6BED", "#2A3040"),
  "Manrope|sans", "Manrope|sans", 22, "soft", "center",
  (), "Extruded soft surfaces, low contrast, no hard borders.")

T("editorial", "Editorial serif magazine", "Archetype", LIGHT,
  ("#FAF7F0", "#FFFFFF", "#DED7C8", "#191713", "#6A6358", "#1F2937", "#B45309"),
  "Fraunces|serif", "Inter|sans", 4, "flat", "stack",
  ("wide",), "Serif display, drop-cap rhythm, print-magazine columns.")

T("swiss", "Swiss international style", "Archetype", LIGHT,
  ("#FFFFFF", "#FFFFFF", "#111111", "#111111", "#5A5A5A", "#E30613", "#111111"),
  "Inter|sans", "Inter|sans", 0, "flat", "stack",
  ("tight", "grid"), "Grid, Helvetica logic, one red accent, zero rounding.")

T("terminal", "Terminal phosphor", "Archetype", DARK,
  ("#050A06", "#08120B", "#12321C", "#B9FFC9", "#4FBF6E", "#33FF66", "#33FF66"),
  "JetBrains Mono|mono", "JetBrains Mono|mono", 0, "flat", "stack",
  ("mono", "grid"), "Phosphor green, scanline grid, keyboard-first.")

T("retro8bit", "Retro 8-bit arcade", "Archetype", DARK,
  ("#1A1329", "#241A3A", "#3D2C63", "#FFE9A8", "#B7A6D9", "#FFD700", "#FF5F6D"),
  "Press Start 2P|mono", "VT323|mono", 0, "hard", "center",
  ("hard", "caps"), "Pixel type, chunky borders, arcade cabinet colour.")

T("vaporwave", "Vaporwave sunset", "Archetype", DARK,
  ("#2B1055", "#3A1A6E", "#6C3FB5", "#FFE9FB", "#C9A6E8", "#FF71CE", "#01CDFE"),
  "Syne|sans", "Inter|sans", 14, "glow", "center",
  ("grad", "glow"), "Purple sunset gradient, pink/cyan neon, retro-future.")

T("cyberpunk", "Cyberpunk neon grid", "Archetype", DARK,
  ("#05060A", "#0B0E17", "#1B2436", "#E8F6FF", "#7C8FA8", "#00F0FF", "#FF2D95"),
  "Orbitron|sans", "JetBrains Mono|mono", 2, "glow", "split",
  ("mono", "glow", "grid"), "Cyan/magenta neon, technical overlays, hard edges.")

T("pastel", "Pastel soft UI", "Archetype", LIGHT,
  ("#FFF6F9", "#FFFFFF", "#F4DFE8", "#33202A", "#7C6470", "#FF9EC4", "#A5B4FC"),
  "Quicksand|sans", "Nunito|sans", 26, "soft", "center",
  (), "Low-contrast pastels, very round, gentle and soft.")

T("claymorphism", "Claymorphism chunky soft", "Archetype", LIGHT,
  ("#EEF1FF", "#F7F9FF", "#DCE2F7", "#1E2340", "#666E8C", "#6C7BFF", "#FFB4C8"),
  "Nunito|sans", "Nunito|sans", 28, "soft", "split",
  (), "Puffy rounded shapes, thick soft shadows, toy-like depth.")

T("bento", "Bento box grid", "Archetype", DARK,
  ("#0B0B0F", "#131318", "#26262E", "#F2F2F5", "#8C8C99", "#F97316", "#38BDF8"),
  "Space Grotesk|sans", "Inter|sans", 18, "soft", "split",
  ("tight",), "Asymmetric tile grid, mixed card sizes, orange highlight.")

T("meshgrain", "Gradient mesh + grain", "Archetype", DARK,
  ("#0A0118", "#150726", "#2C1247", "#F5EEFF", "#A99BC4", "#A78BFA", "#22D3EE"),
  "Sora|sans", "Inter|sans", 24, "glow", "center",
  ("grad", "glow", "grain"), "Blurred colour mesh, film grain, aurora feel.")

T("sketch", "Paper sketch / hand drawn", "Archetype", LIGHT,
  ("#FBF7EC", "#FFFDF6", "#C9BFA8", "#2B2A26", "#6D6656", "#2F4B7C", "#C1440E"),
  "Caveat|sans", "Lora|serif", 6, "hard", "stack",
  ("hard",), "Notebook ground, wobbly borders, highlighter marks.")

T("luxury", "Luxury dark serif gold", "Archetype", DARK,
  ("#0E0E0C", "#151513", "#2E2C25", "#F1EDE4", "#A39C8A", "#C8A96A", "#E9D9B5"),
  "Cormorant Garamond|serif", "Inter|sans", 2, "flat", "center",
  ("caps", "wide"), "Black and gold, hairline rules, couture spacing.")

T("blueprint", "Blueprint engineering", "Archetype", DARK,
  ("#06203A", "#0A2A48", "#1D4A72", "#E6F4FF", "#9FC2DC", "#7DD3FC", "#FFFFFF"),
  "IBM Plex Mono|mono", "IBM Plex Sans|sans", 2, "flat", "split",
  ("grid", "mono", "caps"), "Blue drafting paper, measurement ticks, mono labels.")

T("y2k", "Y2K chrome gloss", "Archetype", LIGHT,
  ("#DFE6F3", "#F2F6FF", "#B9C4DC", "#141B33", "#5B6785", "#FF00A8", "#00D0FF"),
  "Chivo|sans", "Chivo|sans", 12, "glow", "center",
  ("grad", "glow"), "Chrome bevels, iridescent gradients, early-2000s optimism.")

T("memphis", "Memphis playful shapes", "Archetype", LIGHT,
  ("#FFFDF2", "#FFFFFF", "#1A1A1A", "#111111", "#5F5F5F", "#FF6B6B", "#4ECDC4"),
  "Baloo 2|sans", "Baloo 2|sans", 20, "hard", "split",
  ("hard",), "Confetti shapes, thick outlines, upbeat primary mix.")

T("nature", "Organic nature calm", "Archetype", LIGHT,
  ("#F7F5EF", "#FFFFFF", "#DED8C9", "#1F2A22", "#6A7267", "#3F6B4F", "#C9A227"),
  "Lora|serif", "Inter|sans", 20, "soft", "split",
  ("wide",), "Earthy neutrals, serif warmth, sustainable-brand calm.")

T("brutalist", "Brutalist type block", "Archetype", DARK,
  ("#111111", "#181818", "#3A3A3A", "#FFFFFF", "#9A9A9A", "#FFFFFF", "#FF4D00"),
  "Archivo|sans", "Inter|sans", 0, "hard", "stack",
  ("hard", "tight", "caps"), "Massive type blocks, exposed structure, raw edges.")

T("monochrome", "Monochrome editorial", "Archetype", LIGHT,
  ("#FFFFFF", "#F4F4F4", "#D9D9D9", "#0A0A0A", "#6E6E6E", "#0A0A0A", "#0A0A0A"),
  "Playfair Display|serif", "Inter|sans", 0, "flat", "stack",
  ("tight",), "Grayscale only, serif/sans pairing, gallery restraint.")

T("academic", "Academic journal", "Archetype", LIGHT,
  ("#FCFBF7", "#FFFFFF", "#DDD8CA", "#1A1916", "#5F5B52", "#7B2D26", "#1A1916"),
  "Libre Baskerville|serif", "Lora|serif", 0, "flat", "stack",
  (), "Full serif, rule lines, footnoted credibility.")

T("startup", "Modern startup SaaS", "Archetype", LIGHT,
  ("#FFFFFF", "#F8FAFC", "#E2E8F0", "#0F172A", "#64748B", "#6366F1", "#22D3EE"),
  "Inter|sans", "Inter|sans", 12, "soft", "split",
  ("grad",), "The polished default: clean cards, soft shadow, indigo CTA.")

T("ai", "AI product dark violet", "Archetype", DARK,
  ("#0A0A14", "#12121F", "#262640", "#F0F0FA", "#8E8EAA", "#8B5CF6", "#22D3EE"),
  "Sora|sans", "Inter|sans", 16, "glow", "split",
  ("glow", "grad", "grain"), "Violet glow, gradient type, neural ambience.")

T("fintech", "Fintech trustworthy", "Archetype", LIGHT,
  ("#FFFFFF", "#F6F8FB", "#E1E7EF", "#0B1220", "#5B6779", "#0F766E", "#0B1220"),
  "Inter|sans", "Inter|sans", 10, "soft", "split",
  ("tight",), "Calm teal, tabular figures, institutional confidence.")

T("sportswear", "Sportswear high energy", "Archetype", DARK,
  ("#0A0A0A", "#141414", "#2E2E2E", "#FFFFFF", "#9C9C9C", "#D7FF00", "#FF3D00"),
  "Archivo|sans", "Inter|sans", 2, "hard", "split",
  ("tight", "caps", "hard"), "Volt accent, huge condensed type, motion lines.")

T("wellness", "Wellness spa calm", "Archetype", LIGHT,
  ("#F6F2EC", "#FFFFFF", "#E3DBD0", "#2A2622", "#6F6862", "#8A9A7B", "#C08B5C"),
  "Cormorant Garamond|serif", "Manrope|sans", 22, "soft", "center",
  ("wide",), "Sage and sand, airy spacing, slow and restorative.")

T("gaming", "Gaming neon HUD", "Archetype", DARK,
  ("#08030F", "#120A1F", "#2A1840", "#F5E9FF", "#9A86B8", "#C026D3", "#22D3EE"),
  "Orbitron|sans", "Inter|sans", 6, "glow", "split",
  ("glow", "grid", "caps"), "HUD frames, magenta/cyan glow, angular panels.")

T("kids", "Kids bright rounded", "Archetype", LIGHT,
  ("#FFFDF6", "#FFFFFF", "#EFE3C9", "#2B2118", "#6E6154", "#FF7A00", "#00B3A4"),
  "Baloo 2|sans", "Nunito|sans", 28, "soft", "center",
  (), "Big rounded type, primary colours, playful and safe.")

T("corporate", "Corporate trustworthy", "Archetype", LIGHT,
  ("#FFFFFF", "#F5F7FA", "#DDE3EA", "#0F1B2D", "#5A6675", "#1D4ED8", "#0F1B2D"),
  "Inter|sans", "Inter|sans", 4, "flat", "split",
  ("caps",), "Restrained navy, structured sections, annual-report calm.")

T("photography", "Photography portfolio", "Archetype", DARK,
  ("#0B0B0B", "#111111", "#2A2A2A", "#F5F5F5", "#909090", "#FFFFFF", "#909090"),
  "Cormorant Garamond|serif", "Inter|sans", 0, "flat", "center",
  ("wide", "caps"), "Full-bleed imagery framing, thin serif captions.")

T("artdeco", "Art deco gold geometry", "Archetype", DARK,
  ("#0C0B09", "#14120E", "#3B3325", "#F4EFE2", "#A79B85", "#D4AF37", "#F4EFE2"),
  "Playfair Display|serif", "Inter|sans", 0, "flat", "center",
  ("caps", "wide"), "Gold rules, symmetrical framing, 1920s geometry.")

T("minimalmono", "Ultra-minimal mono", "Archetype", LIGHT,
  ("#FCFCFC", "#FFFFFF", "#E8E8E8", "#111111", "#767676", "#111111", "#111111"),
  "Inter|sans", "Inter|sans", 0, "flat", "stack",
  ("tight",), "Almost nothing: hairlines, whitespace, one weight.")
