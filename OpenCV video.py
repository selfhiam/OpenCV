import cv2

cap1 = cv2.VideoCapture('./city.mp4')
cap2 = cv2.VideoCapture('./bird.mp4')

frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))

fps1 = cap1.get(cv2.CAP_PROP_FPS)
fps2 = cap2.get(cv2.CAP_PROP_FPS)

effect_frame = int(fps1 * 2)
delay = int(1000 / fps1)

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter.fourcc(*'avc1')
out = cv2.VideoWriter('mix.mp4', fourcc, fps1, (w, h))

for i in range(frame_cnt1 - effect_frame):
    ret, frame = cap1.read()
    cv2.imshow('frame', frame)
    out.write(frame)
    cv2.waitKey(delay)

for i in range(effect_frame):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    dx = int(w * i / effect_frame)

    alpha = 1.0 - i / effect_frame
    frame = cv2.addWeighted(frame1, alpha, frame2, 1 - alpha, 0)
    out.write(frame)
    cv2.imshow('frame', frame)
    cv2.waitKey(delay)

for i in range(effect_frame, frame_cnt2):
    ret, frame = cap2.read()
    cv2.imshow('frame', frame)
    out.write(frame)
    cv2.waitKey(delay)

cap1.release()
cap2.release()
out.release()