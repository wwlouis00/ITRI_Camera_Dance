import pygame
import pygame.camera
from pygame.locals import *

def main():
    pygame.init()
    pygame.camera.init()

    # 取得所有可用的相機
    cameras = pygame.camera.list_cameras()

    if not cameras:
        print("找不到任何相機")
        return

    # 選擇第一個相機
    camera = pygame.camera.Camera(cameras[1], (640, 480))
    camera.start()

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Webcam")

    while True:
        # 從相機中獲取畫面
        image = camera.get_image()

        # 將畫面顯示在視窗上
        screen.blit(image, (0, 0))
        pygame.display.flip()

        # 檢查事件，如果是退出事件，則退出迴圈
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__ == "__main__":
    main()
