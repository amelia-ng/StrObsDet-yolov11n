import gradio as gr
from ultralytics import YOLO
from PIL import Image

model = YOLO("model/yolov11n_best.pt")

def detect(image):
    results = model.predict(image, conf=0.15, iou=0.7)
    return results[0].plot()  # returns image with bounding boxes drawn

gr.Interface(
    fn=detect,
    inputs=gr.Image(type="pil"),
    outputs=gr.Image(type="numpy"),
    title="🚧 Real-Time Obstacle Detection",
    description="Upload an image to detect obstacles across 25 classes (YOLOv11n fine-tuned)"
).launch()