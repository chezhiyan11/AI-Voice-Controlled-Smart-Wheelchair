import cv2
import numpy as np

def start_ai_navigation():
    print("AI Navigation Mode Started")
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        
        if cv2.countNonZero(edges) > 8000:  # Obstacle detected
            print("⚠️ Obstacle in camera view!")
            # You can call send_command("STOP") here
            break
            
        cv2.imshow('Smart Wheelchair AI View', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()