cv2.imshow("Emotion Detector", frame)

# Exit when pressing 'q'
if cv2.waitKey(1) & 0xFF == ord('q'):
    xbreak

cap.release()
cv2.destroyAllWindows()
