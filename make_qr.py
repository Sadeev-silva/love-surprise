"""
Generate a pink, heart-centred QR code that opens your deployed surprise.

Usage:
    python make_qr.py https://your-app-url.streamlit.app

Output:
    love_qr.png  — send it on WhatsApp with a caption like "Open when alone"

The QR uses high error correction (H), so the heart placed in the centre
does not stop it scanning.
"""

import sys

import qrcode
from qrcode.constants import ERROR_CORRECT_H
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from PIL import Image, ImageDraw


def make_heart(size: int = 220) -> Image.Image:
    """Draw a simple filled heart on a white rounded tile (in-memory)."""
    tile = Image.new("RGBA", (size, size), (255, 255, 255, 255))
    d = ImageDraw.Draw(tile)
    m = size // 10
    w = size - 2 * m
    # Two circles + a triangle make a heart.
    r = w // 4
    cy = m + r
    d.ellipse([m, m, m + 2 * r, m + 2 * r], fill=(216, 27, 79))
    d.ellipse([m + w - 2 * r, m, m + w, m + 2 * r], fill=(216, 27, 79))
    d.polygon(
        [
            (m + 2, cy),
            (m + w - 2, cy),
            (size // 2, size - m),
        ],
        fill=(216, 27, 79),
    )
    return tile


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python make_qr.py <your-deployed-url>")
        sys.exit(1)
    url = sys.argv[1]

    qr = qrcode.QRCode(error_correction=ERROR_CORRECT_H, box_size=14, border=3)
    qr.add_data(url)
    qr.make(fit=True)

    heart = make_heart()
    heart_path = "._heart_tmp.png"
    heart.save(heart_path)

    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        color_mask=RadialGradiantColorMask(
            back_color=(255, 255, 255),
            center_color=(233, 30, 99),   # bright pink centre
            edge_color=(163, 20, 60),     # deep crimson edge
        ),
        embeded_image_path=heart_path,
    )
    img.save("love_qr.png")
    print("Saved love_qr.png →", url)


if __name__ == "__main__":
    main()
