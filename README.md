# Minecraft Cabal Resource Pack

This repository hosts the public resource pack zip used by the Cabal Minecraft server.

- Pack zip for server delivery: `cabal-land-ticket-pack.zip`
- Editable source files: `source/`
- Includes custom icons for server items:
  - Land Ticket Slot
  - Land Claim Transfer Ticket
  - Evoker Eye
- **Maze walls / warden shell** — this pack overrides **`minecraft:bedrock`** with the Cabal **green animated** block texture (subtle shimmer via `bedrock.png.mcmeta`). That applies **everywhere** bedrock appears in the world, not only the maze; the Cabal overworld maze is almost the only bedrock players see day-to-day.
- **Maze start (Cabal pattern)** — the maze RCON builder marks the **start** cell with **`minecraft:light_blue_concrete`**. This pack replaces `textures/block/light_blue_concrete.png` with the Cabal maze start look. **`minecraft:coal_block`** stays **vanilla** (the older approach retextured coal and looked like custom bedrock on any coal ore/build).

Server tickets use the **same technique as cabal-claim**: stacks stay as vanilla `minecraft:map` / `writable_book` / `paper` with `custom_model_data` (910001–910003). This pack only swaps **models/textures** — no new item IDs.

Placed **blocks** cannot use `custom_model_data` (that is an **item** predicate). The Cabal look for the maze **start** marker uses **`light_blue_concrete.png`**; maze power pads use vanilla colored concrete (see `cabal-maze`).

Ticket models are intentionally flat now (no extra glow overlay layers), so Land Ticket / Land Deed / Expansion Slot icons render without the ring aura.

## Build the zip (from `source/`)

```bash
cd source && zip -r ../cabal-land-ticket-pack.zip pack.mcmeta assets
shasum -a 1 ../cabal-land-ticket-pack.zip
```

Point `server.properties` at `cabal-land-ticket-pack.zip` on `raw.githubusercontent.com` and set `resource-pack-sha1` to the `shasum` output.

Current `sha1` of `cabal-land-ticket-pack.zip`:

`39682fea6e3e5f992837d07e89a508ee9043fefe`

To pin a **raw.githubusercontent.com** URL, use the git commit on `main` that contains the rebuilt `cabal-land-ticket-pack.zip` with this hash (this repo’s `main` after you push the change that updated the zip).
