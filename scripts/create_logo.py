"""
Generate an attractive professional logo for Device Risk Analysis
"""
import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs("assets", exist_ok=True)
width, height = 400, 400
img = Image.new("RGBA", (width, height), (255, 255, 255, 0))
draw = ImageDraw.Draw(img)

# Outer circle
center_x, center_y = 200, 200
draw.ellipse([20, 20, 380, 380], fill="#0f172a", outline="#3b82f6", width=8)

# Shield geometry in center
shield_pts = [
    (200, 80),
    (310, 120),
    (290, 240),
    (200, 320),
    (110, 240),
    (90, 120)
]
draw.polygon(shield_pts, fill="#1e293b", outline="#60a5fa", width=5)

# Inner accent lines
inner_shield = [
    (200, 105),
    (285, 140),
    (270, 230),
    (200, 295),
    (130, 230),
    (115, 140)
]
draw.polygon(inner_shield, fill="#0f172a", outline="#38bdf8", width=3)

# Center icon: Server / Device with pulse check
draw.rounded_rectangle([150, 150, 250, 185], radius=6, fill="#334155", outline="#94a3b8", width=2)
draw.ellipse([165, 163, 175, 173], fill="#22c55e")
draw.ellipse([185, 163, 195, 173], fill="#38bdf8")

draw.rounded_rectangle([150, 195, 250, 230], radius=6, fill="#334155", outline="#94a3b8", width=2)
draw.ellipse([165, 208, 175, 218], fill="#22c55e")
draw.ellipse([185, 208, 195, 218], fill="#eab308")

# Checkmark in shield base
check_pts = [(175, 255), (195, 275), (235, 235)]
draw.line(check_pts, fill="#22c55e", width=7, joint="curve")

img.save("assets/logo.png", "PNG")
print("Saved assets/logo.png successfully")
