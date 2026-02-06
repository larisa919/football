import wrap
wrap.add_sprite_dir("sprites")
wrap.world.create_world(800,600)
wrap.world.set_back_color(100,100,100)
ball=wrap.sprite.add("ball",400,300,"blue")
tablo=wrap.sprite.add_text("0:0",400,50, text_color=(255,255,255),font_size=70)
left=wrap.sprite.add("mario-items",100,300,"block_bricks")
right=wrap.sprite.add("mario-items",700,300,"moving_platform1")
polosa=wrap.sprite.add("mario-items",400,300,"cloud_platform")
wrap.sprite.set_size(left,30,200)
wrap.sprite.set_angle(right,180)
wrap.sprite.set_size(right,200,30)
wrap.sprite.set_size_percent(ball,150,150)
wrap.sprite.set_angle(polosa,180)
wrap.sprite.set_size_percent(polosa,1000,20)
skorost_x=-10
skorost_y=-10


@wrap.always()
def polet_sharika():
    global skorost_x,skorost_y

    wrap.sprite.move(ball,skorost_x,skorost_y)

    if wrap.sprite.get_bottom(ball)>=600:
        wrap.sprite.move_bottom_to(ball,600)
        skorost_y=-abs(skorost_y)
    if wrap.sprite.get_top(ball)<=0:
        wrap.sprite.move_top_to(ball,0)
        skorost_y=abs(skorost_y)

    if wrap.sprite.is_collide_sprite(ball,left):
        skorost_x=-skorost_x

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






