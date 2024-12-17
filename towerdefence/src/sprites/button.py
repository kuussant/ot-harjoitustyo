import pygame
import sound


class Button(pygame.sprite.Sprite):
    def __init__(self, sounds, bg_img, fg_img, pos):
        super().__init__()
        self.bg_img = bg_img
        self.fg_img = fg_img

        self.click_sound = sounds["button_sound1"]
        self.highlight_sound = sounds["button_sound2"]

        self.width = self.bg_img.get_width()
        self.height = self.bg_img.get_height()
        self.pos = pos

        self.bg_rect = self.bg_img.get_rect(center=self.pos)
        self.fg_rect = self.fg_img.get_rect(center=self.pos)

        self.bg_mask = pygame.mask.from_surface(self.bg_img)
        self.bg_shadow_img = self.bg_mask.to_surface(setcolor=(0, 0, 0, 100))

        self.pressed = False
        self.disabled = False
        self.highlight = False

    def update(self):
        return self._handle_mouse_interaction()

    def draw(self, display):
        offset = 4 if self.highlight else 0
        display.blit(self.bg_shadow_img, (self.bg_rect.x, self.bg_rect.y))
        display.blit(self.bg_img, (self.bg_rect.x-offset, self.bg_rect.y-offset))
        display.blit(self.fg_img, (self.fg_rect.x-offset, self.fg_rect.y-offset))

        if self.disabled:
            display.blit(self.bg_shadow_img, (self.bg_rect.x, self.bg_rect.y))

    def set_disabled(self, value: bool):
        self.disabled = value

    def _handle_mouse_interaction(self):
        if not self.disabled:
            if self.bg_rect.collidepoint(pygame.mouse.get_pos()):
                if not self.highlight:
                    sound.play(self.highlight_sound, 0.2)
                
                self.highlight = True

                if pygame.mouse.get_pressed()[0] == 1 and self.pressed == False:
                    sound.play(self.click_sound, 0.3)
                    self.pressed = True
            else:
                self.highlight = False

            if pygame.mouse.get_pressed()[0] == 0:
                self.pressed = False

            return self.pressed
        
    def refresh(self):
        self.pressed = False
        self.disabled = False
        self.highlight = False