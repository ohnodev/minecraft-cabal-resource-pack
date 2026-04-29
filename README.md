# Minecraft Cabal Resource Pack

This repository hosts the public resource pack zip used by the Cabal Minecraft server.

- Pack zip for server delivery: `cabal-land-ticket-pack.zip`
- Editable source files: `source/`
- Includes custom icons for server items:
  - Land Ticket Slot
  - Land Claim Transfer Ticket
  - Evoker Eye
- **Cabal bedrock** — replaces `assets/minecraft/textures/block/bedrock.png` with a darker teal-speckled animated texture used by the maze warden arena (`minecraft:bedrock` columns). Players without this pack still see vanilla gray bedrock.

Server tickets use the **same technique as cabal-claim**: stacks stay as vanilla `minecraft:map` / `writable_book` / `paper` with `custom_model_data` (910001–910003). This pack only swaps **models/textures** — no new item IDs.

Placed **blocks** cannot use `custom_model_data` (that is an **item** predicate). The Cabal look for indestructible maze shell blocks is done by **overriding the bedrock block texture** for everyone using this pack.

**Glow / “light”:** Resource packs can stack extra **`item/generated` layers** (see `cabal_ticket_glow_overlay`) for a luminous look. Vanilla Java **does not** let held items cast real block light or dynamic world illumination from a pack alone; the server already enables **enchantment glint** on those stacks for extra sparkle. Block “glow” here is **art only** (multi-frame `bedrock.png` + `bedrock.png.mcmeta`).

## Build the zip (from `source/`)

```bash
cd source && zip -r ../cabal-land-ticket-pack.zip pack.mcmeta assets
shasum -a 1 ../cabal-land-ticket-pack.zip
```

Point `server.properties` at `cabal-land-ticket-pack.zip` on `raw.githubusercontent.com` and set `resource-pack-sha1` to the `shasum` output.

Current `sha1` of `cabal-land-ticket-pack.zip`:

`bd0f8d0ce57c8c969020ddbf058099972877d224`

Pinned commit for `raw.githubusercontent.com/.../cabal-land-ticket-pack.zip` (update `server.properties` when the zip changes): `a79b08ab8043654ba40bb759005a33b014203586`
