# Extract features from bounding boxes
features = []
for bbox in bounding_boxes:
    x, y, w, h = bbox
    features.append([w, h, w/h])  # width, height, aspect ratio

# Predict class of each vehicle
predictions = model.predict(np.array(features))
labels = ['car', 'truck']
predicted_classes = [labels[int(pred)] for pred in predictions]

# Draw label on frame
for bbox, label in zip(bounding_boxes, predicted_classes):
    x, y, w, h = bbox
    cv2.putText(frame, label, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA)

# Show frame
cv2.imshow('frame', frame)
if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()



