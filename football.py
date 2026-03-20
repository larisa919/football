import wrap,time

def sozdat_schet():
    return str(schet_leviy) + " | " + str(schet_praviy)

def stolknovenie_x(panel):
    global skorost_x

    if wrap.sprite.is_collide_sprite(ball, panel):
        if skorost_x > 0:
            wrap.sprite.move_right_to(ball, wrap.sprite.get_left(panel))
        else:
            wrap.sprite.move_left_to(ball, wrap.sprite.get_right(panel))
        if wrap.sprite.get_centery(ball)-wrap.sprite.get_top(panel)>=visota_kvadrata*4:
            print(5)
        elif wrap.sprite.get_centery(ball)-wrap.sprite.get_top(panel)>=visota_kvadrata*3:
            print(4)
        elif wrap.sprite.get_centery(ball)-wrap.sprite.get_top(panel)>=visota_kvadrata*2:
            print(3)
        elif wrap.sprite.get_centery(ball)-wrap.sprite.get_top(panel)>=visota_kvadrata*1:
            print(2)
        else:
            print(1)
        skorost_x = -skorost_x

def stolknovenie_y(panel):
    global skorost_y
    if wrap.sprite.is_collide_sprite(ball,panel):
        if skorost_y>0:
             wrap.sprite.move_bottom_to(ball,wrap.sprite.get_top(panel))
        else:
            wrap.sprite.move_top_to(ball,wrap.sprite.get_bottom(panel))
        skorost_y=-skorost_y



def dvizenie_igroka(keys,button_right, button_left, button_down, button_up,igrok,r_max,l_min):
    if button_right in keys and wrap.sprite.get_right(igrok)<r_max :
        wrap.sprite.move(igrok,6,0)
        if wrap.sprite.get_right(igrok) >r_max:
            wrap.sprite.move_right_to(igrok, r_max)
    if button_down in keys and wrap.sprite.get_bottom(igrok)<600:
        wrap.sprite.move(igrok,0,6)
        if wrap.sprite.get_bottom(igrok) > 600:
            wrap.sprite.move_bottom_to(igrok, 600)
    if button_up in keys and wrap.sprite.get_top(igrok)>0:
        wrap.sprite.move(igrok,0,-6)
        if wrap.sprite.get_top(igrok) <0:
            wrap.sprite.move_top_to(igrok, 0)
    if button_left in keys and wrap.sprite.get_left(igrok)>l_min:
        wrap.sprite.move(igrok,-6,0)
        if wrap.sprite.get_left(igrok) <l_min:
            wrap.sprite.move_left_to(igrok, l_min)

@wrap.on_key_down(wrap.K_SPACE)
def nachat_otschet():
    global sostoyanie,time_0,a
    if sostoyanie==OZIDANIE:
        sostoyanie=OTSCHET
        wrap.sprite.move_to(ball,400,300)
        wrap.sprite.hide(probel)
        wrap.sprite.hide(gol)
        a=3
        wrap.sprite_text.set_text(vremya,str(a))
        wrap.sprite.show(vremya)
        time_0=time.time()

def nachat_ozidanie(vkluchi_gol):
    global sostoyanie
    sostoyanie=OZIDANIE
    if vkluchi_gol==True:
        wrap.sprite.show(gol)
    wrap.sprite.show(probel)

@wrap.always(1000)
def process_ozidanie():
    if sostoyanie!=OZIDANIE:
        return
    if wrap.sprite.is_visible(probel):
        wrap.sprite.hide(probel)
    else:wrap.sprite.show(probel)


@wrap.on_key_always(wrap.K_LEFT,wrap.K_DOWN,wrap.K_UP,wrap.K_RIGHT,wrap.K_d,wrap.K_a,wrap.K_s,wrap.K_w)
def dvizenie_pravogo (keys):
    if sostoyanie!=IGRA:
        return
    dvizenie_igroka(keys,wrap.K_d,wrap.K_a,wrap.K_s,wrap.K_w,left,400,0)
    dvizenie_igroka(keys,wrap.K_RIGHT,wrap.K_LEFT,wrap.K_DOWN,wrap.K_UP,right,800,400)


wrap.world.create_world(800,600)
wrap.world.set_back_color(100,100,100)
wrap.add_sprite_dir("sprites")
ball=wrap.sprite.add("ball",700,200,"blue")

schet_leviy=0
schet_praviy=0

tablo=wrap.sprite.add_text(sozdat_schet(),400,50, text_color=(255,255,255),font_size=70)
left=wrap.sprite.add("mario-items",100,300,"block_bricks")
right=wrap.sprite.add("mario-items",700,300,"moving_platform1")
polosa=wrap.sprite.add("mario-items",400,300,"cloud_platform")
wrap.sprite.set_size(left,30,200)
wrap.sprite.set_angle(right,180)
wrap.sprite.set_size(right,200,30)
wrap.sprite.set_size_percent(ball,150,150)
wrap.sprite.set_angle(polosa,180)
wrap.sprite.set_size_percent(polosa,1000,20)
probel=wrap.sprite.add_text("НАЖМИТЕ НА ПРОБЕЛ ДЛЯ НАЧАЛА ИГРЫ",400,300,False)
otschet=wrap.sprite.add_text("ОТСЧЕТ",400,300,False)
gol=wrap.sprite.add_text("ГООООООЛ", 400, 150, font_size=100,visible=False)
skorost_x=-5
skorost_y=-5
OZIDANIE=1
OTSCHET=2
IGRA=3
GOL=4
sostoyanie=None
a=3
vremya=wrap.sprite.add_text(str(a),400,300,False,font_size=60)
time_0=0
nachat_ozidanie(False)
verh=wrap.sprite.get_top(right)
niz=wrap.sprite.get_bottom(right)
visota=niz-verh
visota_kvadrata=visota/5

@wrap.always()
def polet_sharika():
    global skorost_x,skorost_y,schet_praviy,schet_leviy,sostoyanie
    if sostoyanie!=IGRA:
        return

    wrap.sprite.move(ball,skorost_x,0)
    stolknovenie_x(left)
    stolknovenie_x(right)

    wrap.sprite.move(ball, 0, skorost_y)
    stolknovenie_y(left)
    stolknovenie_y(right)


    if wrap.sprite.get_bottom(ball)>=600:
        wrap.sprite.move_bottom_to(ball,600)
        skorost_y=-abs(skorost_y)
    if wrap.sprite.get_top(ball)<=0:
        wrap.sprite.move_top_to(ball,0)
        skorost_y=abs(skorost_y)
    if wrap.sprite.get_right(ball)>=800:
        wrap.sprite.move_right_to(ball,800)
        schet_praviy=schet_praviy+1
        wrap.sprite_text.set_text(tablo,sozdat_schet())
        skorost_x=-abs(skorost_x)

        nachat_ozidanie(True)
    if wrap.sprite.get_left(ball) <= 0:
        wrap.sprite.move_left_to(ball, 0)
        schet_leviy = schet_leviy + 1
        wrap.sprite_text.set_text(tablo, sozdat_schet())
        skorost_x = abs(skorost_x)

        nachat_ozidanie(True)

@wrap.always(100)
def smenit_otschet():
    global time_0,a,sostoyanie
    if sostoyanie!=OTSCHET:
        return

    time_1 = time.time()

    if time_1 - time_0 >= 1:
        a=a-1
        if a<1:
            sostoyanie=IGRA
            wrap.sprite.hide(vremya)
            return
        wrap.sprite_text.set_text(vremya, str(a))
        time_0=time.time()








