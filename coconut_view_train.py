from ultralytics import YOLO

model = YOLO("yolov8n-cls.pt")



model.train(
    data=r"C:\Users\venka\Downloads\coconut (4)\coconut\coconut\view",
    epochs=50,
    imgsz=224
)
