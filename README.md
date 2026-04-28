# Minecraft Cabal Resource Pack

This repository hosts the public resource pack zip used by the Cabal Minecraft server.

- Pack zip for server delivery: `cabal-land-ticket-pack.zip`
- Editable source files: `source/`
- Includes custom icons for server items:
  - Land Ticket Slot
  - Land Claim Transfer Ticket
  - Evoker Eye

Server tickets use the **same technique as cabal-claim**: stacks stay as vanilla `minecraft:map` / `writable_book` / `paper` with `custom_model_data` (910001–910003). This pack only swaps **models/textures** — no new item IDs.

**Glow / “light”:** Resource packs can stack extra **`item/generated` layers** (see `cabal_ticket_glow_overlay`) for a luminous look. Vanilla Java **does not** let held items cast real block light or dynamic world illumination from a pack alone; the server already enables **enchantment glint** on those stacks for extra sparkle.

Current `sha1` of `cabal-land-ticket-pack.zip`:

`2d51d838b213b71e78c3a4539bbff300a409983a`

Pinned Git revision for `raw.githubusercontent.com` URLs (server `server.properties`): `b6924fad7212049a7e44526d3e3c08cfd6612aca`
