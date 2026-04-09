# import layoutparser as lp
# import cv2

# # Load image
# image = cv2.imread("sample.png")

# # Load model (PubLayNet model)
# model = lp.Detectron2LayoutModel(
#     config_path="lp://PubLayNet/faster_rcnn_R_50_FPN_3x/config",
#     label_map={0: "Text", 1: "Title", 2: "List", 3: "Table", 4: "Figure"},
#     extra_config=["MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.5]
# )

# # Detect layout
# layout = model.detect(image)

# # Draw boxes on image
# output = lp.draw_box(image, layout, box_width=3)

# # Save result
# cv2.imwrite("output.jpg", output)

# print("Detection complete. Saved as output.jpg")


# import layoutparser as lp
# import cv2

# image = cv2.imread("sample.png")

# model = lp.Detectron2LayoutModel(
#     "lp://PubLayNet/faster_rcnn_R_50_FPN_3x/config",
#     extra_config=["MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.5],
#     label_map={0: "Text", 1: "Title", 2: "List", 3: "Table", 4: "Figure"}
# )

# layout = model.detect(image)
# print(layout)

# vis = lp.draw_box(image, layout, box_width=3)
# cv2.imwrite("output.jpg", vis)

# with open("layout_output.txt", "w", encoding="utf-8") as f:
#     f.write(str(layout))

# print("Done. Saved output.jpg and layout_output.txt")



import cv2
import numpy as np
import layoutparser as lp

IMAGE_PATH = "image.png"
CONFIG_PATH = "/workspace/config.yml"
MODEL_PATH = "/workspace/model_final.pth"
OUTPUT_IMAGE = "output_1.png"
OUTPUT_TEXT = "layout_output.txt"

image = cv2.imread(IMAGE_PATH)
if image is None:
    raise FileNotFoundError(f"Could not read image: {IMAGE_PATH}")

model = lp.Detectron2LayoutModel(
    config_path=CONFIG_PATH,
    model_path=MODEL_PATH,
    extra_config=["MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.5],
    label_map={0: "Text", 1: "Title", 2: "List", 3: "Table", 4: "Figure"}
)

layout = model.detect(image)

vis = lp.draw_box(image, layout, box_width=3)
cv2.imwrite(OUTPUT_IMAGE, np.array(vis))

with open(OUTPUT_TEXT, "w", encoding="utf-8") as f:
    for block in layout:
        f.write(str(block) + "\n")

print(f"Done. Saved {OUTPUT_IMAGE} and {OUTPUT_TEXT}")
print(layout)