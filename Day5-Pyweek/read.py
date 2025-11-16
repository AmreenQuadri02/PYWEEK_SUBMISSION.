import cv2
import mediapipe as mp
import numpy as np
#Image Reading
# import cv2
# img=cv2.imread("Photos/cat.webp")
# cv2.imshow("Cat",img)
# cv2.waitKey(200)
# cv2.destroyAllWindows()

#GrayScale Image
# img=cv2.imread("Photos/cat.webp")
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("GrayScale Cat",gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



#Gaussian Blur
# img=cv2.imread("Photos/cat.webp")
# blur=cv2.GaussianBlur(img,(7,7),0)
# cv2.imshow("Blurred Cat",blur)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



#Video Reading
# cap=cv2.VideoCapture("Videos/cat.mp4")
# while True:
#     success, img=cap.read()
#     if not success:
#         break
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

#Webcam Reading
# cap=cv2.VideoCapture(0)

# while True:
#     success, img=cap.read()
#     cv2.flip(img, 1, img)  # Mirror the image
#     if not success:
#         break
#     cv2.imshow("Webcam", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

#Video Reszing
# cap=cv2.VideoCapture(0)
# while True:
#     success, img=cap.read()
#     cv2.flip(img, 1, img)  # Mirror the image
#     if not success:
#         break

#     img = cv2.resize(img, (640, 480))  # Resize to 640x480

#     cv2.imshow("Resized Webcam", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

#Video writing
# cap=cv2.VideoCapture(0)
# fourcc=cv2.VideoWriter_fourcc(*'XVID')
# out=cv2.VideoWriter("output.mp4",fourcc,20.0,(640,480))
# while True:
#     success, img=cap.read()
#     cv2.flip(img, 1, img)  # Mirror the image
#     if not success:
#         break
#     img = cv2.resize(img, (640, 480))  # Resize to 640x480
#     out.write(img)
#     cv2.imshow("Webcam Recording", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# out.release()
# cv2.destroyAllWindows()

#Drawing Shapes and Text on Webcam Feed
# cap=cv2.VideoCapture(0)
# while True:
#     success, img=cap.read()
#     cv2.flip(img, 1, img)  # Mirror the image
#     if not success:
#         break

#     # Drawing shapes and text on the webcam feed
#     cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 3)
#     cv2.circle(img, (300, 300), 50, (255, 0, 0), cv2.FILLED)
#     cv2.line(img, (0, 0), (400, 400), (255, 255, 0), 2)
#     cv2.putText(img, "Webcam Feed", (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

#     cv2.imshow("Webcam with Shapes", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()




#Webcam with Mediapipe
# cap=cv2.VideoCapture(0)
# mpHands=mp.solutions.hands
# hands=mpHands.Hands()
# mpDraw=mp.solutions.drawing_utils
# while True:
#     success, img=cap.read()
#     cv2.flip(img, 1, img)  # Mirror the image
#     if not success:
#         break

#     imgRGB=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     results=hands.process(imgRGB)

#     if results.multi_hand_landmarks:
#         for handLms in results.multi_hand_landmarks:
#             for id, lm in enumerate(handLms.landmark):
#                 h, w, c = img.shape
#                 cx, cy = int(lm.x * w), int(lm.y * h)
#                 print(id, cx, cy)
#                 if id == 4:  # Example: Draw a circle on the thumb tip
#                     cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
#             mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

#     cv2.imshow("Webcam", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

#Mediapipe using face recognition
# cap = cv2.VideoCapture(0)
# mpFaceMesh = mp.solutions.face_mesh
# faceMesh = mpFaceMesh.FaceMesh()
# mpDraw = mp.solutions.drawing_utils
# while True:
#     success, img = cap.read()
#     cv2.flip(img, 1, img)  # Mirror the image
#     if not success:
#         break

#     imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     results = faceMesh.process(imgRGB)

#     if results.multi_face_landmarks:
#         for faceLms in results.multi_face_landmarks:
#             mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_TESSELATION,
#                                   mpDraw.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
#                                   mpDraw.DrawingSpec(color=(0, 0, 255), thickness=1))

#     cv2.imshow("Webcam Face Mesh", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()
