#!/usr/bin/env python3
"""Draw the entry picture for make.fun's 24 November 2026 news-image bounty.

The picture is a broadsheet front page, 1024x1024, drawn with PIL from
the world news reported on Tuesday 24 November 2026:

  lead    NATO alarm over reports Russia may launch a nuclear-armed
          satellite; alliance chief Rutte vows a defence of space
  panel   Israeli airstrike kills Hamas's internal security chief in
          Gaza City, and at least six others
  panel   Russian attack on a Zaporizhzhia apartment block kills 2
          and wounds 40, including four children
  panel   Two men arrested after a break-in at Prince William's
          Norfolk home, Anmer Hall
  panel   GTA VI hacker sentenced to seven years in London and
          released on licence; landmine deaths hit a five-year high;
          Honda recalls 810,000 cars over airbag risks

Run:  python3 generate.py   (writes entry.png beside this file)
"""
from PIL import Image, ImageDraw, ImageFont

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

PAPER = (247, 242, 231)
INK = (18, 18, 18)
RED = (178, 34, 34)
BLUE = (30, 70, 140)
GREY = (90, 90, 90)


def F(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= maxw:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def textbox(draw, xy, text, font, fill, maxw, leading=1.12):
    x, y = xy
    for line in wrap(draw, text, font, maxw):
        draw.text((x, y), line, font=font, fill=fill)
        y += int(font.size * leading)
    return y


def story_box(draw, box, kicker, head, body, accent):
    x0, y0, x1, y1 = box
    draw.rectangle(box, outline=INK, width=2)
    draw.rectangle([x0, y0, x1, y0 + 30], fill=accent)
    draw.text((x0 + 10, y0 + 6), kicker, font=F(SANS_B, 17), fill=(255, 255, 255))
    y = textbox(draw, (x0 + 10, y0 + 42), head, F(SANS_B, 27), INK, x1 - x0 - 20)
    textbox(draw, (x0 + 10, y + 4), body, F(SANS, 19), GREY, x1 - x0 - 20)


def page(date_line, lead_kicker, lead_head, lead_body, stories, out):
    img = Image.new("RGB", (1024, 1024), PAPER)
    d = ImageDraw.Draw(img)
    # Masthead: paper name in a black band, the date picked out in gold.
    d.rectangle([0, 0, 1024, 118], fill=INK)
    t = "THE DAILY WORLD"
    f = F(SERIF_B, 62)
    d.text(((1024 - d.textlength(t, font=f)) / 2, 12), t, font=f, fill=(255, 255, 255))
    f2 = F(SANS_B, 25)
    d.text(((1024 - d.textlength(date_line, font=f2)) / 2, 84),
           date_line, font=f2, fill=(255, 205, 90))
    # Lead story under a red rule.
    d.rectangle([28, 140, 996, 148], fill=RED)
    d.text((28, 160), lead_kicker, font=F(SANS_B, 22), fill=RED)
    y = textbox(d, (28, 192), lead_head, F(SERIF_B, 47), INK, 968)
    y = textbox(d, (28, y + 8), lead_body, F(SANS, 23), GREY, 968)
    d.rectangle([28, y + 10, 996, y + 14], fill=INK)
    # Four panels in a 2x2 grid fill the rest of the page.
    top = y + 34
    cell_h = (1000 - top) // 2
    boxes = [
        (28, top, 500, top + cell_h - 12),
        (524, top, 996, top + cell_h - 12),
        (28, top + cell_h, 500, 1000),
        (524, top + cell_h, 996, 1000),
    ]
    for box, (kick, head, body, acc) in zip(boxes, stories):
        story_box(d, box, kick, head, body, acc)
    img.save(out, optimize=True)
    print(out, img.size)


if __name__ == "__main__":
    page(
        "TUESDAY · 24 NOVEMBER 2026 · THE DAY IN ONE PICTURE",
        "SPACE & SECURITY — TOP STORY",
        "NATO alarm over Russia's nuclear satellite plans",
        "Reports that Moscow may launch a nuclear-armed satellite within "
        "weeks drew a vow from NATO chief Mark Rutte: the alliance will "
        "defend itself against any threat in space.",
        [
            ("GAZA", "Israeli strike kills Hamas security chief",
             "An airstrike on Gaza City killed the head of Hamas's internal "
             "security apparatus and at least six others, medics and police "
             "said.", RED),
            ("UKRAINE", "Zaporizhzhia apartment hit: 2 dead, 40 hurt",
             "An overnight Russian attack struck a residential building in "
             "Zaporizhzhia, wounding 40 people including four children.",
             BLUE),
            ("BRITAIN", "Break-in at Prince William's Norfolk home",
             "Police arrested two men after masked intruders entered Anmer "
             "Hall on the Sandringham estate; the Prince and Princess of "
             "Wales were away.", (120, 60, 160)),
            ("AROUND THE WORLD", "GTA VI hacker jailed — and walks free",
             "A London court sentenced the GTA VI leaker to seven years, "
             "then released him on licence. Also today: landmine deaths "
             "hit a five-year high of 7,000, and Honda recalled 810,000 "
             "cars over airbag risks.", (200, 120, 20)),
        ],
        "entry.png",
    )
