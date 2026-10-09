@namespace
class SpriteKind:
    Decorativo = SpriteKind.create()
    Map = SpriteKind.create()
    Boss = SpriteKind.create()
    Indicator = SpriteKind.create()
    Key = SpriteKind.create()
    Heart = SpriteKind.create()
    Antorcha = SpriteKind.create()
    SpecialKey = SpriteKind.create()
    Door = SpriteKind.create()
    SpecialDoor = SpriteKind.create()

def on_on_overlap(sprite42, otherSprite42):
    if ataque_prota < ataque_prota2:
        sprites.destroy(otherSprite42, effects.ashes, 200)
        music.play(music.create_song(assets.song("""
                ashes
                """)),
            music.PlaybackMode.UNTIL_DONE)
    else:
        sprite42.start_effect(effects.ashes, 1000)
        scene.camera_shake(5, 500)
        info.change_life_by(-1)
        music.play(music.create_song(assets.song("""
                muerte_prota
                """)),
            music.PlaybackMode.IN_BACKGROUND)
        sprites.destroy(otherSprite42)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

def GenerarPuerta():
    global puerta
    for valor in tiles.get_tiles_by_type(assets.tile("""
        puerta_4_nivel_1
        """)):
        if nivel <= 10:
            puerta = sprites.create(assets.image("""
                myImage8
                """), SpriteKind.Door)
        elif nivel > 10 and nivel <= 20:
            puerta = sprites.create(assets.image("""
                myImage7
                """), SpriteKind.Door)
        elif nivel > 20 and nivel <= 30:
            puerta = sprites.create(assets.image("""
                myImage9
                """), SpriteKind.Door)
        tiles.place_on_random_tile(puerta, assets.tile("""
            puerta_4_nivel_1
            """))
        puerta.y += -7

def on_overlap_tile(sprite, location):
    prota.set_position(spawn_x, spawn_y)
    music.play(music.create_song(assets.song("""
            muerte_prota
            """)),
        music.PlaybackMode.IN_BACKGROUND)
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile1
        """),
    on_overlap_tile)

def MostrarFlecha():
    global flecha_puerta_nivel
    if not (jugador_en_puerta):
        if nivel <= 10:
            flecha_puerta_nivel = sprites.create(assets.image("""
                    flecha_nivel1
                    """),
                SpriteKind.Indicator)
            animation.run_image_animation(flecha_puerta_nivel,
                assets.animation("""
                    animacion_flecha_nivel1
                    """),
                150,
                True)
        elif nivel > 10 and nivel <= 20:
            flecha_puerta_nivel = sprites.create(assets.image("""
                    flecha_nivel2
                    """),
                SpriteKind.Indicator)
            animation.run_image_animation(flecha_puerta_nivel,
                assets.animation("""
                    animacion_flecha_nivel2
                    """),
                150,
                True)
        elif nivel > 20 and nivel <= 30:
            flecha_puerta_nivel = sprites.create(assets.image("""
                    flecha_nivel3
                    """),
                SpriteKind.Indicator)
            animation.run_image_animation(flecha_puerta_nivel,
                assets.animation("""
                    animacion_flecha_nivel3
                    """),
                150,
                True)
        flecha_puerta_nivel.set_position(puerta.x - 8, puerta.y - 40)

def on_b_pressed():
    global ataque_prota2
    if partida:
        if characterAnimations.matches_rule(prota, characterAnimations.rule(Predicate.FACING_RIGHT)):
            AtaqueDerecha()
        elif characterAnimations.matches_rule(prota, characterAnimations.rule(Predicate.FACING_LEFT)):
            AtaqueIzquierda()
        ataque_prota2 += 1
        pause(100)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_on_overlap2(sprite3, otherSprite2):
    global llave_especial
    sprites.destroy_all_sprites_of_kind(SpriteKind.SpecialKey)
    llave_especial = True
    music.play(music.create_song(hex("""
            00f4010408020200001c00010a006400f401640000040000000000000000000000000005000004120000000400012704000800012a08000c00012a01001c000f05001202c102c20100040500280000006400280003140006020004120000000400012704000800012a08000c00012a
            """)),
        music.PlaybackMode.IN_BACKGROUND)
    game.splash("Conseguiste la llave", "del aula 408")
sprites.on_overlap(SpriteKind.player, SpriteKind.SpecialKey, on_on_overlap2)

def on_on_overlap3(sprite2, otherSprite):
    global flecha_puerta_nivel, jugador_en_puerta_especial, nivel
    if not (jugador_en_puerta_especial) and llave_especial:
        flecha_puerta_nivel = sprites.create(assets.image("""
            myImage5
            """), SpriteKind.Indicator)
        animation.run_image_animation(flecha_puerta_nivel,
            assets.animation("""
                animacion_flecha_nivel0
                """),
            150,
            True)
        flecha_puerta_nivel.set_position(puerta_aula.x - 8, puerta_aula.y - 40)
        jugador_en_puerta_especial = True
    if controller.up.is_pressed():
        if llave_especial:
            jugador_en_puerta_especial = False
            if nivel == 9:
                nivel = 408
            else:
                nivel = 9
            GenerarNivel()
        else:
            game.splash("Necesitas la llave", "del aula 408")
sprites.on_overlap(SpriteKind.player, SpriteKind.SpecialDoor, on_on_overlap3)

def CreacionPersonaje():
    global prota, ataque_prota, ataque_prota2, spawn_x, spawn_y, mostrar_minimapa
    prota = sprites.create(assets.image("""
        player
        """), SpriteKind.player)
    characterAnimations.set_character_state(prota, characterAnimations.rule(Predicate.FACING_RIGHT))
    controller.move_sprite(prota, 100, 0)
    scene.camera_follow_sprite(prota)
    prota.ay = 200
    ataque_prota = 0
    ataque_prota2 = 0
    for valor2 in tiles.get_tiles_by_type(assets.tile("""
        myTile2
        """)):
        tiles.place_on_tile(prota, valor2)
        spawn_x = prota.x
        spawn_y = prota.y
        PonerPared(valor2)
        if nivel == 408:
            mostrar_minimapa = False
            tiles.set_tile_at(valor2, assets.tile("""
                pared_aula
                """))
def EnemigoNivel2():
    global enemigo
    for valor3 in tiles.get_tiles_by_type(assets.tile("""
        amarillo_enemigo
        """)):
        enemigo = sprites.create(assets.image("""
                muercielago_izquierda
                """),
            SpriteKind.enemy)
        characterAnimations.loop_frames(enemigo,
            assets.animation("""
                derecha_fantasma
                """),
            300,
            characterAnimations.rule(Predicate.MOVING_RIGHT))
        characterAnimations.run_frames(enemigo,
            assets.animation("""
                murcielago_animacion_izquierda
                """),
            300,
            characterAnimations.rule(Predicate.NOT_MOVING))
        tiles.place_on_tile(enemigo, valor3)
        PonerPared(valor3)
        enemigo.ay = 200
        enemigo.follow(prota, 30)

def on_on_overlap4(sprite4, otherSprite3):
    global mensaje_corazon
    if info.life() < max_corazones:
        sprites.destroy(otherSprite3, effects.fire, 100)
        music.play(music.create_song(hex("""
                00f4010408020100001c00010a006400f4016400000400000000000000000000000000050000040c0000000400012704000800012a
                """)),
            music.PlaybackMode.IN_BACKGROUND)
        info.change_life_by(1)
    elif mensaje_corazon:
        game.splash("No puedes superar",
            "los " + convert_to_text(max_corazones) + " corazones")
        mensaje_corazon = False
sprites.on_overlap(SpriteKind.player, SpriteKind.Heart, on_on_overlap4)

def GenerarLlave():
    global llave
    for valor4 in tiles.get_tiles_by_type(assets.tile("""
        myTile
        """)):
        llave = sprites.create(assets.image("""
            myImage2
            """), SpriteKind.Key)
        animation.run_image_animation(llave, assets.animation("""
            myAnim
            """), 200, True)
        tiles.place_on_tile(llave, valor4)
        PonerPared(valor4)
    for valor5 in tiles.get_tiles_by_type(assets.tile("""
        myTile4
        """)):
        llave = sprites.create(assets.image("""
                myImage4
                """),
            SpriteKind.SpecialKey)
        animation.run_image_animation(llave, assets.animation("""
            myAnim2
            """), 200, True)
        tiles.place_on_tile(llave, valor5)
        tiles.set_tile_at(valor5, assets.tile("""
            pared_nivel_3
            """))

def on_a_pressed():
    if partida:
        SistemaDeDobleSalto()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def GenerarMinimapa():
    global myMinimap, mapStripe
    sprites.destroy(mapStripe)
    myMinimap = minimap.minimap(MinimapScale.SIXTEENTH, 1, 15)
    mapStripe = sprites.create(minimap.get_image(myMinimap), SpriteKind.Map)
    minimap.include_sprite(myMinimap, prota, MinimapSpriteScale.DOUBLE)
    for valor6 in sprites.all_of_kind(SpriteKind.enemy):
        minimap.include_sprite(myMinimap, valor6, MinimapSpriteScale.DOUBLE)
    if boss_vivo:
        minimap.include_sprite(myMinimap, boss_actual, MinimapSpriteScale.DOUBLE)
    mapStripe.set_position(scene.camera_property(CameraProperty.X) + 54,
        scene.camera_property(CameraProperty.Y) - 44)

def on_left_pressed():
    global ataque_prota2
    if partida and not (controller.right.is_pressed()):
        animation.run_image_animation(prota,
            assets.animation("""
                player_left_animated
                """),
            200,
            True)
        characterAnimations.set_character_state(prota, characterAnimations.rule(Predicate.FACING_LEFT))
        ataque_prota2 = 0
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def EnemigoNivel3():
    global enemigo
    for valor7 in tiles.get_tiles_by_type(assets.tile("""
        amarillo_enemigo
        """)):
        enemigo = sprites.create(assets.image("""
                caracol_izquierda
                """),
            SpriteKind.enemy)
        characterAnimations.loop_frames(enemigo,
            assets.animation("""
                pez_animacion_derecha
                """),
            300,
            characterAnimations.rule(Predicate.MOVING_RIGHT))
        characterAnimations.loop_frames(enemigo,
            assets.animation("""
                pez_animacion_izquierda
                """),
            300,
            characterAnimations.rule(Predicate.MOVING_LEFT))
        tiles.place_on_tile(enemigo, valor7)
        PonerPared(valor7)
        enemigo.ay = 200
        enemigo.follow(prota, 30)
def GenerarAntorchas():
    if nivel != 408:
        for valor8 in tiles.get_tiles_by_type(assets.tile("""
            antorcha_nivel_1
            """)):
            ColocarAnimacionAntorcha(valor8)
        for valor9 in tiles.get_tiles_by_type(assets.tile("""
            antorcha_nivel_2
            """)):
            ColocarAnimacionAntorcha(valor9)
        for valor10 in tiles.get_tiles_by_type(assets.tile("""
            antorhca_nivel_3
            """)):
            ColocarAnimacionAntorcha(valor10)
def ShowFinal():
    global menu, final
    tiles.set_current_tilemap(tilemap("""
        level3
        """))
    if win:
        scene.set_background_image(assets.image("""
            fondo_ganador
            """))
    else:
        scene.set_background_image(assets.image("""
            fondo_perdedor
            """))
    if controller.A.is_pressed():
        menu = True
        final = False
        music.play(music.create_song(assets.song("""
                Cancion1
                """)),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
        pause(1000)

def on_right_released():
    if partida and not (controller.left.is_pressed()):
        animation.run_image_animation(prota, assets.animation("""
            myAnim4
            """), 200, False)
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_left_released():
    if partida and not (controller.right.is_pressed()):
        animation.run_image_animation(prota, assets.animation("""
            myAnim3
            """), 200, False)
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def GenerarMusica():
    global musica_randoom
    musica_randoom = randint(1, 3)
    if musica_randoom == 1:
        music.play(music.create_song(assets.song("""
                Cancion2
                """)),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
    elif musica_randoom == 2:
        music.play(music.create_song(assets.song("""
                Cancion3
                """)),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
    elif musica_randoom == 3:
        music.play(music.create_song(assets.song("""
                Cancion4
                """)),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
    elif musica_randoom == 4:
        music.play(music.create_song(hex("""
                """)),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
    elif musica_randoom == 5:
        music.play(music.create_song(assets.song("""
                """)),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)

def on_on_overlap5(sprite5, otherSprite22):
    if sprite5.vy > 0 and sprite5.y < otherSprite22.y:
        prota.set_velocity(0, -125)
        statusbar.value += -1
        music.play(music.create_sound_effect(WaveShape.NOISE,
                1259,
                0,
                255,
                255,
                100,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LOGARITHMIC),
            music.PlaybackMode.UNTIL_DONE)
    else:
        info.change_life_by(-1)
        music.play(music.create_song(assets.song("""
                muerte_prota
                """)),
            music.PlaybackMode.IN_BACKGROUND)
    pause(1000)
sprites.on_overlap(SpriteKind.player, SpriteKind.Boss, on_on_overlap5)

def on_on_zero(status):
    global max_corazones, mensaje_corazon, nivel_superado, boss_vivo
    music.play(music.create_song(assets.song("""
            ashes
            """)),
        music.PlaybackMode.IN_BACKGROUND)
    sprites.destroy(boss_actual, effects.disintegrate, 500)
    sprites.destroy(statusbar)
    max_corazones += 10
    game.splash("+10 corazones maximos")
    mensaje_corazon = True
    nivel_superado = True
    boss_vivo = False
statusbars.on_zero(StatusBarKind.enemy_health, on_on_zero)

def GenerarNivel():
    global tipo_nivel, jugador_en_puerta, jugador_en_puerta_especial, nivel_superado
    music.stop_all_sounds()
    tipo_nivel = True
    jugador_en_puerta = False
    jugador_en_puerta_especial = False
    nivel_superado = False
    tipo_nivel = True
    DestruirSprites()
    scene.set_background_image(assets.image("""
        fondo_nivel_1
        """))
    if nivel == 1:
        tiles.set_current_tilemap(tilemap("""
            nivel58
            """))
    elif nivel == 2:
        tiles.set_current_tilemap(tilemap("""
            nivel54
            """))
    elif nivel == 3:
        tiles.set_current_tilemap(tilemap("""
            nivel56
            """))
    elif nivel == 4:
        tiles.set_current_tilemap(tilemap("""
            nivel52
            """))
    elif nivel == 5:
        tiles.set_current_tilemap(tilemap("""
            nivel50
            """))
    elif nivel == 6:
        tiles.set_current_tilemap(tilemap("""
            nivel48
            """))
    elif nivel == 7:
        tiles.set_current_tilemap(tilemap("""
            nivel46
            """))
    elif nivel == 8:
        tiles.set_current_tilemap(tilemap("""
            nivel44
            """))
    elif nivel == 9:
        tiles.set_current_tilemap(tilemap("""
            nivel42
            """))
    elif nivel == 10:
        tipo_nivel = False
        tiles.set_current_tilemap(tilemap("""
            nivel10
            """))
    elif nivel == 11:
        tiles.set_current_tilemap(tilemap("""
            nivel40
            """))
    elif nivel == 12:
        tiles.set_current_tilemap(tilemap("""
            nivel38
            """))
    elif nivel == 13:
        tiles.set_current_tilemap(tilemap("""
            nivel36
            """))
    elif nivel == 14:
        tiles.set_current_tilemap(tilemap("""
            nivel34
            """))
    elif nivel == 15:
        tiles.set_current_tilemap(tilemap("""
            nivel32
            """))
    elif nivel == 16:
        tiles.set_current_tilemap(tilemap("""
            nivel16
            """))
    elif nivel == 17:
        tiles.set_current_tilemap(tilemap("""
            nivel14
            """))
    elif nivel == 18:
        tiles.set_current_tilemap(tilemap("""
            nivel18
            """))
    elif nivel == 19:
        tiles.set_current_tilemap(tilemap("""
            nivel12
            """))
    elif nivel == 20:
        tipo_nivel = False
        tiles.set_current_tilemap(tilemap("""
            nivel20
            """))
    elif nivel == 21:
        tiles.set_current_tilemap(tilemap("""
            nivel21
            """))
    elif nivel == 22:
        tiles.set_current_tilemap(tilemap("""
            nivel9
            """))
    elif nivel == 23:
        tiles.set_current_tilemap(tilemap("""
            nivel23
            """))
    elif nivel == 24:
        tiles.set_current_tilemap(tilemap("""
            nivel7
            """))
    elif nivel == 25:
        tiles.set_current_tilemap(tilemap("""
            nivel25
            """))
    elif nivel == 26:
        tiles.set_current_tilemap(tilemap("""
            nivel5
            """))
    elif nivel == 27:
        tiles.set_current_tilemap(tilemap("""
            nivel27
            """))
    elif nivel == 28:
        tiles.set_current_tilemap(tilemap("""
            nivel0
            """))
    elif nivel == 29:
        tiles.set_current_tilemap(tilemap("""
            nivel29
            """))
    elif nivel == 30:
        tipo_nivel = False
        tiles.set_current_tilemap(tilemap("""
            nivel30
            """))
    elif nivel == 408:
        scene.set_background_image(assets.image("""
            cityscape
            """))
        tiles.set_current_tilemap(tilemap("""
            level
            """))
    GenerarPuertaEspecial()
    GenerarPuerta()
    GenerarCorazones()
    GenerarAntorchas()
    CreacionPersonaje()
    CrearEnemigos()
    if tipo_nivel:
        GenerarLlave()
    else:
        GenerarBoss()
    MostrarNivel()
    GenerarMusica()
def Boss1():
    if prota.x + 30 < boss_actual.x:
        boss_actual.vx = -20
        if nivel == 10:
            boss_actual.set_image(assets.image("""
                leviatan_izquierda
                """))
        elif nivel == 20:
            boss_actual.set_image(assets.image("""
                faraon_izquierda
                """))
        elif nivel == 30:
            boss_actual.set_image(assets.image("""
                myImage0
                """))
    elif prota.x - 30 > boss_actual.x:
        boss_actual.vx = 20
        if nivel == 10:
            boss_actual.set_image(assets.image("""
                leviatan_derecha
                """))
        elif nivel == 20:
            boss_actual.set_image(assets.image("""
                faraon_derecha
                """))
        elif nivel == 30:
            boss_actual.set_image(assets.image("""
                myImage
                """))
    else:
        boss_actual.vx = 0
def SistemaDeDobleSalto():
    global salto
    if prota.is_hitting_tile(CollisionDirection.BOTTOM):
        prota.set_velocity(0, -125)
        salto = True
        music.play(music.create_song(hex("""
                0078000408010100001c00010a006400f4016400000400000000000000000000000000050000040c0000000100011b01000200011d
                """)),
            music.PlaybackMode.IN_BACKGROUND)
    elif salto == True:
        prota.set_velocity(0, -125)
        salto = False
        music.play(music.create_song(hex("""
                0078000408010100001c00010a006400f4016400000400000000000000000000000000050000040c0000000100011b01000200011d
                """)),
            music.PlaybackMode.IN_BACKGROUND)
def PonerPared(myLocation: tiles.Location):
    if nivel <= 10:
        tiles.set_tile_at(myLocation, assets.tile("""
            pared_nivel_1
            """))
    elif nivel > 10 and nivel <= 20:
        tiles.set_tile_at(myLocation, assets.tile("""
            pared_nivel_2
            """))
    elif nivel > 20 and nivel <= 30:
        tiles.set_tile_at(myLocation, assets.tile("""
            pared_nivel_3
            """))

def on_right_pressed():
    global ataque_prota2
    if partida and not (controller.left.is_pressed()):
        animation.run_image_animation(prota,
            assets.animation("""
                player_right_animated
                """),
            200,
            True)
        characterAnimations.set_character_state(prota, characterAnimations.rule(Predicate.FACING_RIGHT))
        ataque_prota2 = 0
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def AtaqueIzquierda():
    animation.run_image_animation(prota,
        assets.animation("""
            atacar_izquierda
            """),
        100,
        False)
    music.play(music.create_sound_effect(WaveShape.NOISE,
            1364,
            1,
            255,
            255,
            100,
            SoundExpressionEffect.VIBRATO,
            InterpolationCurve.LOGARITHMIC),
        music.PlaybackMode.IN_BACKGROUND)
    if controller.left.is_pressed():
        pause(100)
        animation.run_image_animation(prota,
            assets.animation("""
                player_left_animated
                """),
            200,
            True)
def AtaqueDerecha():
    animation.run_image_animation(prota,
        assets.animation("""
            atacar_derecha
            """),
        100,
        False)
    music.play(music.create_sound_effect(WaveShape.NOISE,
            1364,
            1,
            255,
            255,
            100,
            SoundExpressionEffect.VIBRATO,
            InterpolationCurve.LOGARITHMIC),
        music.PlaybackMode.IN_BACKGROUND)
    if controller.right.is_pressed():
        pause(100)
        animation.run_image_animation(prota,
            assets.animation("""
                player_right_animated
                """),
            200,
            True)
def GenerarBoss():
    global statusbar, boss_actual, boss_vivo
    statusbar = statusbars.create(40, 4, StatusBarKind.enemy_health)
    statusbar.max = 20
    statusbar.set_color(7, 2, 0)
    statusbar.set_status_bar_flag(StatusBarFlag.SMOOTH_TRANSITION, True)
    if nivel == 10:
        boss_actual = sprites.create(assets.image("""
                leviatan_derecha
                """),
            SpriteKind.Boss)
        boss_actual.set_scale(1.5, ScaleAnchor.MIDDLE)
        for valor11 in tiles.get_tiles_by_type(assets.tile("""
            myTile3
            """)):
            tiles.place_on_tile(boss_actual, valor11)
            PonerPared(valor11)
    elif nivel == 20:
        boss_actual = sprites.create(assets.image("""
                faraon_derecha
                """),
            SpriteKind.Boss)
        boss_actual.set_scale(1.5, ScaleAnchor.MIDDLE)
        for valor12 in tiles.get_tiles_by_type(assets.tile("""
            myTile3
            """)):
            tiles.place_on_tile(boss_actual, valor12)
            PonerPared(valor12)
    elif nivel == 30:
        boss_actual = sprites.create(assets.image("""
            myImage0
            """), SpriteKind.Boss)
        for valor13 in tiles.get_tiles_by_type(assets.tile("""
            myTile3
            """)):
            tiles.place_on_tile(boss_actual, valor13)
            PonerPared(valor13)
        boss_actual.set_scale(1.5, ScaleAnchor.MIDDLE)
    boss_actual.ay = 200
    statusbar.attach_to_sprite(boss_actual)
    boss_vivo = True

def on_down_pressed():
    global mostrar_minimapa
    if partida and nivel != 408:
        if mostrar_minimapa:
            mostrar_minimapa = False
            sprites.destroy(mapStripe)
        else:
            mostrar_minimapa = True
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def EnemigoNivel1():
    global enemigo
    for valor14 in tiles.get_tiles_by_type(assets.tile("""
        amarillo_enemigo
        """)):
        enemigo = sprites.create(assets.image("""
                fantasma_derecha
                """),
            SpriteKind.enemy)
        characterAnimations.loop_frames(enemigo,
            assets.animation("""
                derecha_fantasma0
                """),
            500,
            characterAnimations.rule(Predicate.MOVING_RIGHT))
        characterAnimations.loop_frames(enemigo,
            assets.animation("""
                izquierda_fantasma
                """),
            500,
            characterAnimations.rule(Predicate.MOVING_LEFT))
        tiles.place_on_tile(enemigo, valor14)
        PonerPared(valor14)
        enemigo.ay = 200
        enemigo.follow(prota, 30)
def MostrarLore():
    game.set_dialog_text_color(2)
    game.set_dialog_frame(assets.image("""
        fondo_1
        """))
    game.show_long_text("Hace mucho tiempo existia un reino pacífico que, un triste dia, fue conquistado por un ejercito demoniaco.",
        DialogLayout.FULL)
    game.show_long_text("Tras mucho tiempo de batalla, este ejercito termino conquistando el reino y rebautizandolo como \"Reino Nochesfera\", controlado por 3 reyes.",
        DialogLayout.FULL)
    game.show_long_text("El 1r rey es Espectro, lider de los fantasmas, quien ha conquistado gran parte del territorio por sus estrategias militares.",
        DialogLayout.FULL)
    game.show_long_text("El 2o rey es Murcielagor, lider de los murcielagos, quien es responsable de grandes robos de suministros en las aldeas vecinas.",
        DialogLayout.FULL)
    game.show_long_text("El ultimo rey es Anguilo, lider de los tiburones, quien es quien crea el veneno que fluye en los rios de los territorios vecinos.",
        DialogLayout.FULL)
    game.show_long_text("Parecia que no habia esperanza, pero entonces apareció el caballero End, quien juro que derrotaria a los 3 reyes de la Nochesfera.",
        DialogLayout.FULL)
    game.show_long_text("Y asi, End se adentro al castillo de la Nochesfera para derrotar a los 3 reyes malignos.",
        DialogLayout.FULL)
def ColocarAnimacionAntorcha(myLocation2: tiles.Location):
    global antorcha
    antorcha = sprites.create(assets.image("""
        myImage3
        """), SpriteKind.Antorcha)
    animation.run_image_animation(antorcha,
        assets.animation("""
            myAnim1
            """),
        200,
        True)
    tiles.place_on_tile(antorcha, myLocation2)
    antorcha.y += -1
def CrearEnemigos():
    if nivel <= 10:
        EnemigoNivel1()
    elif nivel > 10 and nivel <= 20:
        EnemigoNivel2()
    elif nivel > 20 and nivel <= 30:
        EnemigoNivel3()

def on_life_zero():
    global llave_especial
    if not (win) and not (end_game):
        llave_especial = False
        EndGame()
info.on_life_zero(on_life_zero)

def DestruirSprites():
    sprites.destroy_all_sprites_of_kind(SpriteKind.Boss)
    sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Indicator)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Heart)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Antorcha)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Key)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Map)
    sprites.destroy_all_sprites_of_kind(SpriteKind.player)
    sprites.destroy_all_sprites_of_kind(SpriteKind.SpecialKey)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Door)
    sprites.destroy_all_sprites_of_kind(SpriteKind.SpecialDoor)

def on_on_overlap6(sprite62, otherSprite32):
    global nivel_superado
    sprites.destroy(otherSprite32, effects.ashes, 100)
    nivel_superado = True
    music.play(music.create_song(hex("""
            00f4010408020200001c00010a006400f401640000040000000000000000000000000005000004120000000400012704000800012a08000c00012a01001c000f05001202c102c20100040500280000006400280003140006020004120000000400012704000800012a08000c00012a
            """)),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.player, SpriteKind.Key, on_on_overlap6)

def GenerarPuertaEspecial():
    global puerta_aula
    for valor15 in tiles.get_tiles_by_type(assets.tile("""
        myTile6
        """)):
        puerta_aula = sprites.create(assets.image("""
                myImage6
                """),
            SpriteKind.SpecialDoor)
        tiles.place_on_random_tile(puerta_aula, assets.tile("""
            myTile6
            """))
        puerta_aula.y += -7

def on_on_overlap7(sprite6, otherSprite4):
    global jugador_en_puerta, win, nivel
    if nivel_superado:
        MostrarFlecha()
        jugador_en_puerta = True
        pause(10)
        if controller.up.is_pressed():
            if nivel == 30:
                win = True
                EndGame()
            else:
                music.play(music.create_sound_effect(WaveShape.NOISE,
                        1,
                        452,
                        255,
                        255,
                        500,
                        SoundExpressionEffect.NONE,
                        InterpolationCurve.LINEAR),
                    music.PlaybackMode.UNTIL_DONE)
                nivel += 1
                sprites.destroy_all_sprites_of_kind(SpriteKind.player)
                GenerarNivel()
    elif controller.up.is_pressed():
        game.splash("Necesitas la llave")
sprites.on_overlap(SpriteKind.player, SpriteKind.Door, on_on_overlap7)

def MostrarInstrucciones():
    game.set_dialog_text_color(2)
    game.set_dialog_frame(assets.image("""
        fondo_1
        """))
    game.show_long_text("A         : Saltar\\nA+A       : Doble salto\\nB         : Atacar\\nDER./IZQ. : Moverse\\nBAJO      : Minimapa\\nARRIBA    : Interactuar",
        DialogLayout.FULL)

def on_on_overlap8(sprite7, otherSprite5):
    scene.camera_shake(5, 500)
    info.change_life_by(-1)
    sprites.destroy(otherSprite5)
    music.play(music.create_song(assets.song("""
            muerte_prota
            """)),
        music.PlaybackMode.IN_BACKGROUND)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap8)

def GenerarCorazones():
    global corazon
    for valor16 in tiles.get_tiles_by_type(assets.tile("""
        myTile0
        """)):
        corazon = sprites.create(assets.image("""
            myImage1
            """), SpriteKind.Heart)
        animation.run_image_animation(corazon,
            assets.animation("""
                myAnim0
                """),
            200,
            True)
        tiles.place_on_tile(corazon, valor16)
        PonerPared(valor16)
def MostrarNivel():
    game.set_dialog_text_color(2)
    game.set_dialog_frame(assets.image("""
        fondo_1
        """))
    game.show_long_text("Nivel " + convert_to_text(nivel), DialogLayout.FULL)
def EndGame():
    global end_game, partida, boss_vivo, final, mostrar_minimapa
    music.stop_all_sounds()
    end_game = True
    partida = False
    boss_vivo = False
    final = True
    mostrar_minimapa = False
    info.set_life(0)
    DestruirSprites()
    sprites.destroy(mapStripe)
    if win:
        music.play(music.melody_playable(music.magic_wand),
            music.PlaybackMode.IN_BACKGROUND)
    else:
        music.play(music.melody_playable(music.wawawawaa),
            music.PlaybackMode.IN_BACKGROUND)
projectile: Sprite = None
corazon: Sprite = None
end_game = False
antorcha: Sprite = None
salto = False
tipo_nivel = False
nivel_superado = False
statusbar: StatusBarSprite = None
musica_randoom = 0
boss_actual: Sprite = None
boss_vivo = False
myMinimap: minimap.Minimap = None
mapStripe: Sprite = None
llave: Sprite = None
enemigo: Sprite = None
puerta_aula: Sprite = None
jugador_en_puerta_especial = False
flecha_puerta_nivel: Sprite = None
jugador_en_puerta = False
spawn_y = 0
spawn_x = 0
prota: Sprite = None
puerta: Sprite = None
nivel = 0
ataque_prota2 = 0
ataque_prota = 0
llave_especial = False
mensaje_corazon = False
mostrar_minimapa = False
win = False
final = False
partida = False
menu = False
max_corazones = 0
pause(500)
scene.set_background_image(assets.image("""
    darkys_games_pantalla
    """))
pause(3000)
max_corazones = 10
menu = True
partida = False
final = False
win = False
mostrar_minimapa = True
mensaje_corazon = True
llave_especial = False
atacar = False
music.set_volume(70)
music.play(music.create_song(assets.song("""
        Cancion1
        """)),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)

def on_on_update():
    global menu, nivel, max_corazones, win, end_game, partida
    if menu:
        scene.set_background_image(assets.image("""
            fondo_menu2
            """))
        if controller.A.is_pressed():
            menu = False
        elif controller.B.is_pressed():
            MostrarLore()
            pause(1000)
    elif not (partida) and not (final):
        MostrarInstrucciones()
        info.set_life(5)
        nivel = 1
        max_corazones = 10
        win = False
        end_game = False
        GenerarNivel()
        partida = True
    elif mostrar_minimapa:
        GenerarMinimapa()
    if final:
        ShowFinal()
    if boss_vivo:
        Boss1()
game.on_update(on_on_update)

def on_update_interval():
    global projectile
    if boss_vivo:
        if prota.y < boss_actual.y:
            if prota.x < boss_actual.x - 10:
                projectile = sprites.create_projectile_from_sprite(assets.image("""
                        bola_de_plasma
                        """),
                    boss_actual,
                    -100,
                    -100)
            elif prota.x > boss_actual.x + 10:
                projectile = sprites.create_projectile_from_sprite(assets.image("""
                        bola_de_plasma
                        """),
                    boss_actual,
                    100,
                    -100)
            else:
                projectile = sprites.create_projectile_from_sprite(assets.image("""
                        bola_de_plasma
                        """),
                    boss_actual,
                    0,
                    -100)
        elif prota.x < boss_actual.x - 10:
            projectile = sprites.create_projectile_from_sprite(assets.image("""
                    bola_de_plasma
                    """),
                boss_actual,
                -100,
                0)
        elif prota.x > boss_actual.x + 10:
            projectile = sprites.create_projectile_from_sprite(assets.image("""
                    bola_de_plasma
                    """),
                boss_actual,
                100,
                0)
        animation.run_image_animation(projectile,
            assets.animation("""
                bola_de_plasma_animado
                """),
            100,
            True)
game.on_update_interval(2000, on_update_interval)

def on_update_interval2():
    global spawn_x, spawn_y
    if partida and prota.is_hitting_tile(CollisionDirection.BOTTOM):
        spawn_x = prota.x
        spawn_y = prota.y
game.on_update_interval(100, on_update_interval2)
