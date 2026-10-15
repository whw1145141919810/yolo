from ultralytics import YOLO

model = YOLO(r"weights\best.pt")
model.predict(
    source=(r"scripts\runs\detect\predict\d65fb6a2d145feb7f3deddaaf75a9efc.mp4"),
    save=True,
    show=False,
)