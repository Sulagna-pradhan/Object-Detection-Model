from transformers import pipeline
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import cv2
import numpy as np

# Initialize the object detection pipeline
pipe = pipeline("object-detection", model="facebook/detr-resnet-50")

# Attempt to open the camera with various indices
camera_indices = [0, 1, 2, 3]
cap = None
for index in camera_indices:
    cap = cv2.VideoCapture(index)
    if cap.isOpened():
        print(f"Camera opened successfully with index {index}")
        break
    else:
        cap.release()
        cap = None

if cap is None or not cap.isOpened():
    print("Error: Could not open camera with any index.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Convert the frame to an image
    pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # Run the object detection
    results = pipe(pil_image)

    # Draw the bounding boxes on the frame
    for result in results:
        box = result['box']
        xmin = int(box['xmin'])
        ymin = int(box['ymin'])
        xmax = int(box['xmax'])
        ymax = int(box['ymax'])

        # Draw the bounding box
        cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
        # Put the label and score
        label = f"{result['label']} ({result['score']:.2f})"
        cv2.putText(frame, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Object Detection', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close any OpenCV windows
cap.release()
cv2.destroyAllWindows()
