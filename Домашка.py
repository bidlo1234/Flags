from time import sleep
import pygame as pg

window = pg.display.set_mode((800, 800))
pg.display.set_caption("flag")
window.fill((0, 255, 0))

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()

    pg.draw.rect(window, (255, 255, 255), (0, 0, 360, 210))
    pg.draw.rect(window, (0, 0, 255), (0, 70, 360, 70))
    pg.draw.rect(window, (255, 0, 0), (0, 140, 360, 70))
    pg.draw.rect(window, (255, 255, 255), (450, 0, 234, 210))
    pg.draw.rect(window, (0,49,83), (450, 0, 117, 210)) #синий франц
    pg.draw.rect(window, (227,38,54), (680, 0, 107, 210)) #красный франц
    pg.draw.rect(window, (0, 0, 0), (0, 300, 360, 70)) #черный герм
    pg.draw.rect(window, (227,38,54), (0, 370, 360, 70)) #красный герм
    pg.draw.rect(window, (255,215,0), (0, 440, 360, 70)) #желтый герм
    pg.draw.rect(window, (255, 255, 255), (450, 300, 350, 210)) #белый япон
    pg.draw.circle(window, (227,38,54), (625, 406), 70, 0)
    pg.display.update()
