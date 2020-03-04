import cv2

#   カメラのキャプチャ開始
while True:
    #  画像を取得
    _, img = cam.read()
    #  画像を表示
    cv2.imshow('PUSH ENTER KEY', img)
    #  ENTER KEY が押されたら終了する
    if cv2.waitKey(1) == 13: break

#  リソースの解放
cam.release()
cv2.destroyAllWindow()
