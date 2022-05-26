import pygame
import time


class Root:

    def __init__(self, res: tuple[int] = (800,600) , title: str = "Title"):
        self.window = pygame.display.set_mode(res)
        pygame.display.set_caption(title)
        self.running = True
        self.frame_rate = 60

    def run(self, event_handler: callable = None):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event_handler is not None:
                event_handler(event)

        if self.running:
            return True
        else:
            pygame.quit()
            return False

    def end_frame(self):
        pygame.display.update()
        self.window.fill((0,0,0))
        time.sleep(1/self.frame_rate)
        

    
