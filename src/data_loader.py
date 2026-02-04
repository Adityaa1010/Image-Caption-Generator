def build_caption_dict(captions):
    cap_dict = {}
    for c in captions:
        img, txt = c.split('\t')
        txt = txt.replace("start ", "").replace(" end", "")
        cap_dict.setdefault(img, []).append(txt)
    return cap_dict
