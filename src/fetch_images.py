#!/usr/bin/env python3
"""Descarga las imágenes generadas con Higgsfield y las optimiza a JPG en img/gen/."""
import io, urllib.request
from pathlib import Path
from PIL import Image
B = "https://d8j0ntlcm91z4.cloudfront.net/user_3EVFQGGB0uS6Dss87xRgYs1Fdup/"
IMGS = {
 "hero": ("hf_20261103_103555_ac071175-8ce7-4dfd-a1fd-455ccf4ac4bf.png", 2400),
 "hills": ("hf_20261103_103620_9db7ae6a-1527-4351-9f52-eed1af037d23.png", 2200),
 "forest": ("hf_20261103_103620_039cc4b6-698d-4edb-99c4-f949032603cf.png", 2200),
 "meadow": ("hf_20261103_103553_3d720645-3c10-4c72-a4a9-adafc682206d.png", 2200),
 "r-corredera": ("hf_20261103_103851_3a438df4-cfcb-4e37-98e2-957f4b90d130.png", 900),
 "r-oscilo": ("hf_20261103_103553_11621e1f-5da1-43ef-ae99-75ddffa207ca.png", 900),
 "r-puerta": ("hf_20261103_103851_f96a363d-aea3-41fb-b0c2-4cb248231960.png", 900),
 "r-mallorquina": ("hf_20261103_103922_d8eef4d0-0f31-4cc0-b013-0b888c70ffc2.png", 900),
 "r-mampara": ("hf_20261103_103921_fc507a7e-12d5-46f0-84dc-9d5ebd31f3d0.png", 900),
 "r-pergola": ("hf_20261103_103554_3c1e4604-3753-4a78-9978-940aa1b1ff76.png", 900),
}
IMGS.update({
 "vista": ("hf_20261103_121524_77162703-47b0-4b0b-b8c0-84fc6985fbba.png", 2000),
 "fachada": ("hf_20261103_121408_2cc4656c-1e90-41c2-96d3-00934950ef6d.png", 2200),
 "taller": ("hf_20261103_121409_dd332d4c-0fca-4b0f-965a-5e5c49e580a2.png", 2200),
 "terraza": ("hf_20261103_121407_cb5dd4db-9f4b-453b-b7b4-8e95501d1e7d.png", 2200),
 "interior": ("hf_20261103_121407_6e40b7ae-5334-4fdf-8781-1cd370b86566.png", 2400),
 "mosquitera": ("hf_20261103_122642_eaf82400-c699-4b29-af49-542fca5cef3f.png", 900),
})
for k in ["hero", "hills", "forest", "meadow"]:
    IMGS.pop(k)
out = Path(__file__).resolve().parent.parent / "img" / "gen"
out.mkdir(parents=True, exist_ok=True)
for name, (f, w) in IMGS.items():
    im = Image.open(io.BytesIO(urllib.request.urlopen(B + f, timeout=60).read())).convert("RGB")
    im.thumbnail((w, w))
    im.save(out / f"{name}.jpg", quality=82, optimize=True, progressive=True)
    print(name, im.size)
