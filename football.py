import wrap

def sozdat_schet():
    return str(schet_leviy) + " | " + str(schet_praviy)

def stolknovenie_x(panel):
    global skorost_x
    if wrap.sprite.is_collide_sprite(ball, panel):
        if skorost_x > 0:
            wrap.sprite.move_right_to(ball, wrap.sprite.get_left(panel))
        else:
            wrap.sprite.move_left_to(ball, wrap.sprite.get_right(panel))
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





@wrap.on_key_always(wrap.K_LEFT,wrap.K_DOWN,wrap.K_UP,wrap.K_RIGHT,wrap.K_d,wrap.K_a,wrap.K_s,wrap.K_w)
def dvizenie_pravogo (keys):
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
skorost_x=-20
skorost_y=-20

@wrap.always()
def polet_sharika():
    global skorost_x,skorost_y,schet_praviy,schet_leviy

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
    if wrap.sprite.get_left(ball) <= 0:
        wrap.sprite.move_left_to(ball, 0)
        schet_leviy = schet_leviy + 1
        wrap.sprite_text.set_text(tablo, sozdat_schet())
        skorost_x = abs(skorost_x)







