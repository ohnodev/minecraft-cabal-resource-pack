#!/usr/bin/env python3
from __future__ import annotations

import colorsys
import math
from pathlib import Path

from PIL import Image, ImageDraw


FRAME_WIDTH = 64
FRAME_HEIGHT = 32
FRAME_COUNT = 12


def hsv_rgb(h: float, s: float, v: float) -> tuple[int, int, int]:
    r, g, b = colorsys.hsv_to_rgb(h % 1.0, max(0.0, min(1.0, s)), max(0.0, min(1.0, v)))
    return int(r * 255), int(g * 255), int(b * 255)


def build_frame(frame_idx: int) -> Image.Image:
    img = Image.new("RGBA", (FRAME_WIDTH, FRAME_HEIGHT), (0, 0, 0, 255))
    draw = ImageDraw.Draw(img)
    base_shift = frame_idx / FRAME_COUNT
    for y in range(FRAME_HEIGHT):
        for x in range(FRAME_WIDTH):
            u = x / FRAME_WIDTH
            v = y / FRAME_HEIGHT
            swirl = math.sin((u * 8.0) + (v * 11.0) + frame_idx * 0.7) * 0.08
            hue = base_shift + u * 0.7 + v * 0.2 + swirl
            sat = 0.85 + 0.15 * math.sin((x + frame_idx * 5) * 0.2)
            val = 0.9 + 0.1 * math.sin((y + frame_idx * 3) * 0.35)
            draw.point((x, y), fill=(*hsv_rgb(hue, sat, val), 255))

    for stripe in range(5):
        x0 = int((stripe * 13 + frame_idx * 4) % FRAME_WIDTH)
        draw.rectangle([x0, 0, min(FRAME_WIDTH - 1, x0 + 3), FRAME_HEIGHT - 1], fill=(255, 255, 255, 70))

    draw.rectangle([16, 0, 23, 4], fill=(255, 180, 40, 255))
    draw.rectangle([16, 5, 23, 7], fill=(230, 60, 40, 255))
    return img


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    output = root / "source" / "assets" / "minecraft" / "textures" / "entity" / "chicken" / "chicken.png"
    output.parent.mkdir(parents=True, exist_ok=True)

    sheet = Image.new("RGBA", (FRAME_WIDTH, FRAME_HEIGHT * FRAME_COUNT), (0, 0, 0, 255))
    for i in range(FRAME_COUNT):
        frame = build_frame(i)
        sheet.paste(frame, (0, i * FRAME_HEIGHT))
    sheet.save(output)
    print(f"wrote {output}")


if __name__ == "__main__":
    main()
