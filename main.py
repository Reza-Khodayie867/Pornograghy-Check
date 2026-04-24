from transformers import pipeline
from PIL import Image


def is_porn(image_path: str, threshold: float = 0.7) -> dict:
    img = Image.open(image_path).convert("RGB")
    clf = pipeline(
        "image-classification",
        model="AdamCodd/vit-base-nsfw-detector",
        device=-1,
        function_to_apply="softmax"
    )
    preds = clf(img, top_k=2)
    prob_nsfw = 0.0
    for p in preds:
        if p["label"].upper() == "NSFW":
            prob_nsfw = float(p["score"])
            break
    return {
        "is_porn": prob_nsfw >= threshold,
        "prob_nsfw": prob_nsfw,
        "label": "NSFW" if prob_nsfw >= threshold else "SFW"
    }

print(is_porn("img1.jpg", threshold=0.75))
