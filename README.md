# Minecraft Cabal Resource Pack

This repository hosts the public resource pack zip used by the Cabal Minecraft server.

- Pack zip for server delivery: `cabal-land-ticket-pack.zip`
- Editable source files: `source/`
- Includes custom icons for server items:
  - Land Ticket Slot
  - Land Claim Transfer Ticket
  - Evoker Eye
- **Cabal bedrock** — replaces `assets/minecraft/textures/block/bedrock.png` with a darker teal-speckled animated texture used by maze **walls** and the **warden** arena (`minecraft:bedrock` columns). Players without this pack still see vanilla gray bedrock.
- **Maze start (green “bedrock”)** — vanilla resource packs can only apply **one texture per block ID**. The maze **start** cell cannot use `minecraft:bedrock` if walls already use bedrock with a different tint. The server places **`minecraft:coal_block`** only for **start** markers; this pack replaces `textures/block/coal_block.png` with a **green-tinted bedrock-style** texture. Elsewhere in the world, normal coal blocks will look like that texture for players using the pack.

Server tickets use the **same technique as cabal-claim**: stacks stay as vanilla `minecraft:map` / `writable_book` / `paper` with `custom_model_data` (910001–910003). This pack only swaps **models/textures** — no new item IDs.

Placed **blocks** cannot use `custom_model_data` (that is an **item** predicate). The Cabal look for maze shell blocks is done by **overriding block textures** (`bedrock.png`, `coal_block.png`, …) for everyone using this pack.

**Glow / “light”:** Resource packs can stack extra **`item/generated` layers** (see `cabal_ticket_glow_overlay`) for a luminous look. Vanilla Java **does not** let held items cast real block light or dynamic world illumination from a pack alone; the server already enables **enchantment glint** on those stacks for extra sparkle. Block “glow” here is **art only** (multi-frame `bedrock.png` + `bedrock.png.mcmeta`).

## Build the zip (from `source/`)

```bash
cd source && zip -r ../cabal-land-ticket-pack.zip pack.mcmeta assets
shasum -a 1 ../cabal-land-ticket-pack.zip
```

Point `server.properties` at `cabal-land-ticket-pack.zip` on `raw.githubusercontent.com` and set `resource-pack-sha1` to the `shasum` output.

Current `sha1` of `cabal-land-ticket-pack.zip`:

`964d97370de5a143e32829ae850e34b5eb0606d5`

Pinned commit for `raw.githubusercontent.com/.../cabal-land-ticket-pack.zip` (update `server.properties` when the zip changes): `77e1be9b4b72db73c0f069a44095b8414a9b211a`
