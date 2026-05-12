#!/usr/bin/env python3
from __future__ import annotations

import colorsys
import math
from pathlib import Path

from PIL import Image, ImageDraw


SIZE = 16
FRAMES = 18


def hsv_to_rgb_tuple(h: float, s: float, v: float) -> tuple[int, int, int]:
    r, g, b = colorsys.hsv_to_rgb(h % 1.0, s, v)
    return int(r * 255), int(g * 255), int(b * 255)


def make_frame(kind: str, index: int) -> Image.Image:
    img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 255))
    draw = ImageDraw.Draw(img)
    phase = index / FRAMES
    for y in range(SIZE):
        for x in range(SIZE):
            u = x / max(1, SIZE - 1)
            v = y / max(1, SIZE - 1)
            wave = math.sin((u * 10.0) + (v * 13.0) + index * 0.8) * 0.08
            hue = phase + (u * 0.45) + (v * 0.2) + wave
            sat = 0.82 + 0.15 * math.sin((x + index * 3) * 0.45)
            val = 0.88 + 0.12 * math.cos((y + index * 4) * 0.37)
            r, g, b = hsv_to_rgb_tuple(hue, max(0.45, min(1.0, sat)), max(0.55, min(1.0, val)))
            draw.point((x, y), fill=(r, g, b, 255))

    # TNT-style dark seam lines keep readability.
    for line in [4, 11]:
        draw.line([(0, line), (SIZE - 1, line)], fill=(30, 30, 30, 170), width=1)
    for line in [5, 10]:
        draw.line([(line, 0), (line, SIZE - 1)], fill=(20, 20, 20, 140), width=1)

    if kind == "side":
        draw.rectangle([0, 6, SIZE - 1, 9], fill=(0, 0, 0, 190))
        draw.text((2, 5), "NUK", fill=(255, 80, 40, 255))
    elif kind == "top":
        draw.ellipse([2, 2, SIZE - 3, SIZE - 3], outline=(255, 255, 255, 170), width=1)
        draw.ellipse([5, 5, SIZE - 6, SIZE - 6], fill=(255, 255, 255, 90))
    else:  # bottom
        draw.rectangle([1, 1, SIZE - 2, SIZE - 2], outline=(60, 60, 60, 190), width=1)
        draw.line([(1, 1), (SIZE - 2, SIZE - 2)], fill=(255, 255, 255, 80), width=1)
        draw.line([(SIZE - 2, 1), (1, SIZE - 2)], fill=(255, 255, 255, 80), width=1)
    return img


def write_sheet(target: Path, kind: str) -> None:
    sheet = Image.new("RGBA", (SIZE, SIZE * FRAMES), (0, 0, 0, 255))
    for i in range(FRAMES):
        frame = make_frame(kind, i)
        sheet.paste(frame, (0, i * SIZE))
    target.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(target)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    tex = root / "source" / "assets" / "minecraft" / "textures" / "block"
    write_sheet(tex / "tnt_side.png", "side")
    write_sheet(tex / "tnt_top.png", "top")
    write_sheet(tex / "tnt_bottom.png", "bottom")
    print("Generated animated nuke TNT textures.")


if __name__ == "__main__":
    main()
