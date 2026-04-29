# Minecraft Cabal Resource Pack

This repository hosts the public resource pack zip used by the Cabal Minecraft server.

- Pack zip for server delivery: `cabal-land-ticket-pack.zip`
- Editable source files: `source/`
- Includes custom icons for server items:
  - Land Ticket Slot
  - Land Claim Transfer Ticket
  - Evoker Eye
- **Maze walls / warden shell** — uses vanilla **`minecraft:bedrock`** appearance (no pack override). The maze RCON builder fills walls and the warden blast shell with bedrock; players see default gray bedrock.
- **Maze start (green “bedrock”)** — vanilla resource packs only apply **one texture per block ID**, so the maze **start** cell uses **`minecraft:coal_block`** instead of a second bedrock style. This pack replaces `textures/block/coal_block.png` with a **green-tinted bedrock-style** texture. Elsewhere in the world, normal coal blocks will look like that texture for players using the pack.

Server tickets use the **same technique as cabal-claim**: stacks stay as vanilla `minecraft:map` / `writable_book` / `paper` with `custom_model_data` (910001–910003). This pack only swaps **models/textures** — no new item IDs.

Placed **blocks** cannot use `custom_model_data` (that is an **item** predicate). The Cabal look for the maze **start** marker uses **`coal_block.png`**; maze power pads use vanilla colored concrete (see `cabal-maze`).

**Glow / “light”:** Resource packs can stack extra **`item/generated` layers** (see `cabal_ticket_glow_overlay`) for a luminous look. Vanilla Java **does not** let held items cast real block light or dynamic world illumination from a pack alone; the server already enables **enchantment glint** on those stacks for extra sparkle.

## Build the zip (from `source/`)

```bash
cd source && zip -r ../cabal-land-ticket-pack.zip pack.mcmeta assets
shasum -a 1 ../cabal-land-ticket-pack.zip
```

Point `server.properties` at `cabal-land-ticket-pack.zip` on `raw.githubusercontent.com` and set `resource-pack-sha1` to the `shasum` output.

Current `sha1` of `cabal-land-ticket-pack.zip`:

`5ad35cc813dd3f32c43526b8b8ec9af2dc574db1`

To pin a **raw.githubusercontent.com** URL, use the git commit on `main` that contains the rebuilt `cabal-land-ticket-pack.zip` with this hash (this repo’s `main` after you push the change that updated the zip).
