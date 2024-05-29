import pygame
import settings
class Settings:

     def __init__(self):
         pass

     def enable(self):

            self.screen.fill(settings.BACKGROUND_C)
            self.settings_text = self.font2.render("settings", False, 'White')

            self.user_amount_text = self.font2.render(f"starting usage amount: {settings.usage}", False, 'White')

            self.text_user_amount = self.user_amount_text.get_rect(
                topleft=(50, 60))
            self.text_settings = self.settings_text.get_rect(
                topleft=(50, 20))

            pygame.draw.rect(self.screen, 'Black',
                             self.text_user_amount.inflate(10, 10), 0, 4)

            pygame.draw.rect(self.screen, 'Black',
                             self.text_settings.inflate(10, 10), 0, 4)

            self.screen.blit(self.user_amount_text, self.text_user_amount)
            self.screen.blit(self.settings_text, self.text_settings)

            print('settings')
            if self.quit:

                self.screen.fill(settings.BACKGROUND_C)
                self.select = False
                self.quit = False

            print(settings.usage)