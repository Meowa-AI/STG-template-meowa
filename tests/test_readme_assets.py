#!/usr/bin/env python3
import struct
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
UNIT_IDS = [
    "prime",
    "artillery",
    "science",
    "hornet",
    "firefly",
    "scorpion",
    "scarab",
    "hornet_leader",
]
ANIMATION_NAMES = ["idle", "attack", "hit"]
README_GIF_SIZE = (128, 128)


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def gif_size(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    assert data[:6] in (b"GIF87a", b"GIF89a"), f"{path} is not a GIF"
    return struct.unpack("<HH", data[6:10])


def test_readme_lists_all_character_static_sprites_and_gifs() -> None:
    readme = read("README.md")
    for unit_id in UNIT_IDS:
        assert f"assets/sprites/{unit_id}.png" in readme
        for animation_name in ANIMATION_NAMES:
            gif_rel = f"assets/readme/characters/{unit_id}_{animation_name}.gif"
            gif_path = ROOT / gif_rel
            assert gif_rel in readme
            assert gif_path.exists(), f"{gif_rel} is missing"
            assert gif_size(gif_path) == README_GIF_SIZE


if __name__ == "__main__":
    test_readme_lists_all_character_static_sprites_and_gifs()
    print("ok test_readme_lists_all_character_static_sprites_and_gifs")
