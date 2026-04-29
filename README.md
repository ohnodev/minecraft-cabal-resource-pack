# Minecraft Cabal Resource Pack

This repository hosts the public resource pack zip used by the Cabal Minecraft server.

- Pack zip for server delivery: `cabal-land-ticket-pack.zip`
- Editable source files: `source/`
- Includes custom icons for server items:
  - Land Ticket Slot
  - Land Claim Transfer Ticket
  - Evoker Eye
- **Maze walls / warden shell** — **`minecraft:bedrock`** uses the **vanilla** texture (this pack does not override bedrock).
- **Maze start (Cabal pattern)** — the maze RCON builder marks the **start** cell with **`minecraft:light_blue_concrete`**. This pack replaces `textures/block/light_blue_concrete.png` with the Cabal maze style so **bedrock** and **`minecraft:coal_block`** stay **vanilla** everywhere (the old approach retextured coal blocks and looked like “custom bedrock” on any coal block).

Server tickets use the **same technique as cabal-claim**: stacks stay as vanilla `minecraft:map` / `writable_book` / `paper` with `custom_model_data` (910001–910003). This pack only swaps **models/textures** — no new item IDs.

Placed **blocks** cannot use `custom_model_data` (that is an **item** predicate). The Cabal look for the maze **start** marker uses **`light_blue_concrete.png`**; maze power pads use vanilla colored concrete (see `cabal-maze`).

**Glow / “light”:** Resource packs can stack extra **`item/generated` layers** (see `cabal_ticket_glow_overlay`) for a luminous look. Vanilla Java **does not** let held items cast real block light or dynamic world illumination from a pack alone; the server already enables **enchantment glint** on those stacks for extra sparkle.

## Build the zip (from `source/`)

```bash
cd source && zip -r ../cabal-land-ticket-pack.zip pack.mcmeta assets
shasum -a 1 ../cabal-land-ticket-pack.zip
```

Point `server.properties` at `cabal-land-ticket-pack.zip` on `raw.githubusercontent.com` and set `resource-pack-sha1` to the `shasum` output.

Current `sha1` of `cabal-land-ticket-pack.zip`:

`fc975cb75a151b4b81797a57b1ce34329d0a610e`

To pin a **raw.githubusercontent.com** URL, use the git commit on `main` that contains the rebuilt `cabal-land-ticket-pack.zip` with this hash (this repo’s `main` after you push the change that updated the zip).
