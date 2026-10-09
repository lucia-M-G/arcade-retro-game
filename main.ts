namespace SpriteKind {
    export const Decorativo = SpriteKind.create()
    export const Map = SpriteKind.create()
    export const Boss = SpriteKind.create()
    export const Indicator = SpriteKind.create()
    export const Key = SpriteKind.create()
    export const Heart = SpriteKind.create()
    export const Antorcha = SpriteKind.create()
    export const SpecialKey = SpriteKind.create()
    export const Door = SpriteKind.create()
    export const SpecialDoor = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite42, otherSprite42) {
    if (ataque_prota < ataque_prota2) {
        sprites.destroy(otherSprite42, effects.ashes, 200)
        music.play(music.createSong(assets.song`ashes`), music.PlaybackMode.UntilDone)
    } else {
        sprite42.startEffect(effects.ashes, 1000)
        scene.cameraShake(5, 500)
        info.changeLifeBy(-1)
        music.play(music.createSong(assets.song`muerte_prota`), music.PlaybackMode.InBackground)
        sprites.destroy(otherSprite42)
    }
})
function GenerarPuerta () {
    for (let valor of tiles.getTilesByType(assets.tile`puerta_4_nivel_1`)) {
        if (nivel <= 10) {
            puerta = sprites.create(assets.image`myImage8`, SpriteKind.Door)
        } else if (nivel > 10 && nivel <= 20) {
            puerta = sprites.create(assets.image`myImage7`, SpriteKind.Door)
        } else if (nivel > 20 && nivel <= 30) {
            puerta = sprites.create(assets.image`myImage9`, SpriteKind.Door)
        }
        tiles.placeOnRandomTile(puerta, assets.tile`puerta_4_nivel_1`)
        puerta.y += -7
    }
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile1`, function (sprite, location) {
    prota.setPosition(spawn_x, spawn_y)
    music.play(music.createSong(assets.song`muerte_prota`), music.PlaybackMode.InBackground)
    info.changeLifeBy(-1)
})
function MostrarFlecha () {
    if (!(jugador_en_puerta)) {
        if (nivel <= 10) {
            flecha_puerta_nivel = sprites.create(assets.image`flecha_nivel1`, SpriteKind.Indicator)
            animation.runImageAnimation(
            flecha_puerta_nivel,
            assets.animation`animacion_flecha_nivel1`,
            150,
            true
            )
        } else if (nivel > 10 && nivel <= 20) {
            flecha_puerta_nivel = sprites.create(assets.image`flecha_nivel2`, SpriteKind.Indicator)
            animation.runImageAnimation(
            flecha_puerta_nivel,
            assets.animation`animacion_flecha_nivel2`,
            150,
            true
            )
        } else if (nivel > 20 && nivel <= 30) {
            flecha_puerta_nivel = sprites.create(assets.image`flecha_nivel3`, SpriteKind.Indicator)
            animation.runImageAnimation(
            flecha_puerta_nivel,
            assets.animation`animacion_flecha_nivel3`,
            150,
            true
            )
        }
        flecha_puerta_nivel.setPosition(puerta.x - 8, puerta.y - 40)
    }
}
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    if (partida) {
        if (characterAnimations.matchesRule(prota, characterAnimations.rule(Predicate.FacingRight))) {
            AtaqueDerecha()
        } else if (characterAnimations.matchesRule(prota, characterAnimations.rule(Predicate.FacingLeft))) {
            AtaqueIzquierda()
        }
        ataque_prota2 += 1
        pause(100)
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.SpecialKey, function (sprite3, otherSprite2) {
    sprites.destroyAllSpritesOfKind(SpriteKind.SpecialKey)
    llave_especial = true
    music.play(music.createSong(hex`
                    00f4010408020200001c00010a006400f401640000040000000000000000000000000005000004120000000400012704000800012a08000c00012a01001c000f05001202c102c20100040500280000006400280003140006020004120000000400012704000800012a08000c00012a
                    `), music.PlaybackMode.InBackground)
    game.splash("Conseguiste la llave", "del aula 408")
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.SpecialDoor, function (sprite2, otherSprite) {
    if (!(jugador_en_puerta_especial) && llave_especial) {
        flecha_puerta_nivel = sprites.create(assets.image`myImage5`, SpriteKind.Indicator)
        animation.runImageAnimation(
        flecha_puerta_nivel,
        assets.animation`animacion_flecha_nivel0`,
        150,
        true
        )
        flecha_puerta_nivel.setPosition(puerta_aula.x - 8, puerta_aula.y - 40)
        jugador_en_puerta_especial = true
    }
    if (controller.up.isPressed()) {
        if (llave_especial) {
            jugador_en_puerta_especial = false
            if (nivel == 9) {
                nivel = 408
            } else {
                nivel = 9
            }
            GenerarNivel()
        } else {
            game.splash("Necesitas la llave", "del aula 408")
        }
    }
})
function CreacionPersonaje () {
    prota = sprites.create(assets.image`player`, SpriteKind.Player)
    characterAnimations.setCharacterState(prota, characterAnimations.rule(Predicate.FacingRight))
    controller.moveSprite(prota, 100, 0)
    scene.cameraFollowSprite(prota)
    prota.ay = 200
    ataque_prota = 0
    ataque_prota2 = 0
    for (let valor2 of tiles.getTilesByType(assets.tile`myTile2`)) {
        tiles.placeOnTile(prota, valor2)
        spawn_x = prota.x
        spawn_y = prota.y
        PonerPared(valor2)
        if (nivel == 408) {
            mostrar_minimapa = false
            tiles.setTileAt(valor2, assets.tile`pared_aula`)
        }
    }
}
function EnemigoNivel2 () {
    for (let valor3 of tiles.getTilesByType(assets.tile`amarillo_enemigo`)) {
        enemigo = sprites.create(assets.image`muercielago_izquierda`, SpriteKind.Enemy)
        characterAnimations.loopFrames(
        enemigo,
        assets.animation`derecha_fantasma`,
        300,
        characterAnimations.rule(Predicate.MovingRight)
        )
        characterAnimations.runFrames(
        enemigo,
        assets.animation`murcielago_animacion_izquierda`,
        300,
        characterAnimations.rule(Predicate.NotMoving)
        )
        tiles.placeOnTile(enemigo, valor3)
        PonerPared(valor3)
        enemigo.ay = 200
        enemigo.follow(prota, 30)
    }
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Heart, function (sprite4, otherSprite3) {
    if (info.life() < max_corazones) {
        sprites.destroy(otherSprite3, effects.fire, 100)
        music.play(music.createSong(hex`
                            00f4010408020100001c00010a006400f4016400000400000000000000000000000000050000040c0000000400012704000800012a
                            `), music.PlaybackMode.InBackground)
        info.changeLifeBy(1)
    } else if (mensaje_corazon) {
        game.splash("No puedes superar", "los " + convertToText(max_corazones) + " corazones")
        mensaje_corazon = false
    }
})
function GenerarLlave () {
    for (let valor4 of tiles.getTilesByType(assets.tile`myTile`)) {
        llave = sprites.create(assets.image`myImage2`, SpriteKind.Key)
        animation.runImageAnimation(
        llave,
        assets.animation`myAnim`,
        200,
        true
        )
        tiles.placeOnTile(llave, valor4)
        PonerPared(valor4)
    }
    for (let valor5 of tiles.getTilesByType(assets.tile`myTile4`)) {
        llave = sprites.create(assets.image`myImage4`, SpriteKind.SpecialKey)
        animation.runImageAnimation(
        llave,
        assets.animation`myAnim2`,
        200,
        true
        )
        tiles.placeOnTile(llave, valor5)
        tiles.setTileAt(valor5, assets.tile`pared_nivel_3`)
    }
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (partida) {
        SistemaDeDobleSalto()
    }
})
function GenerarMinimapa () {
    sprites.destroy(mapStripe)
    myMinimap = minimap.minimap(MinimapScale.Sixteenth, 1, 15)
    mapStripe = sprites.create(minimap.getImage(myMinimap), SpriteKind.Map)
    minimap.includeSprite(myMinimap, prota, MinimapSpriteScale.Double)
    for (let valor6 of sprites.allOfKind(SpriteKind.Enemy)) {
        minimap.includeSprite(myMinimap, valor6, MinimapSpriteScale.Double)
    }
    if (boss_vivo) {
        minimap.includeSprite(myMinimap, boss_actual, MinimapSpriteScale.Double)
    }
    mapStripe.setPosition(scene.cameraProperty(CameraProperty.X) + 54, scene.cameraProperty(CameraProperty.Y) - 44)
}
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    if (partida && !(controller.right.isPressed())) {
        animation.runImageAnimation(
        prota,
        assets.animation`player_left_animated`,
        200,
        true
        )
        characterAnimations.setCharacterState(prota, characterAnimations.rule(Predicate.FacingLeft))
        ataque_prota2 = 0
    }
})
function EnemigoNivel3 () {
    for (let valor7 of tiles.getTilesByType(assets.tile`amarillo_enemigo`)) {
        enemigo = sprites.create(assets.image`caracol_izquierda`, SpriteKind.Enemy)
        characterAnimations.loopFrames(
        enemigo,
        assets.animation`pez_animacion_derecha`,
        300,
        characterAnimations.rule(Predicate.MovingRight)
        )
        characterAnimations.loopFrames(
        enemigo,
        assets.animation`pez_animacion_izquierda`,
        300,
        characterAnimations.rule(Predicate.MovingLeft)
        )
        tiles.placeOnTile(enemigo, valor7)
        PonerPared(valor7)
        enemigo.ay = 200
        enemigo.follow(prota, 30)
    }
}
function GenerarAntorchas () {
    if (nivel != 408) {
        for (let valor8 of tiles.getTilesByType(assets.tile`antorcha_nivel_1`)) {
            ColocarAnimacionAntorcha(valor8)
        }
        for (let valor9 of tiles.getTilesByType(assets.tile`antorcha_nivel_2`)) {
            ColocarAnimacionAntorcha(valor9)
        }
        for (let valor10 of tiles.getTilesByType(assets.tile`antorhca_nivel_3`)) {
            ColocarAnimacionAntorcha(valor10)
        }
    }
}
function ShowFinal () {
    tiles.setCurrentTilemap(tilemap`level3`)
    if (win) {
        scene.setBackgroundImage(assets.image`fondo_ganador`)
    } else {
        scene.setBackgroundImage(assets.image`fondo_perdedor`)
    }
    if (controller.A.isPressed()) {
        menu = true
        final = false
        music.play(music.createSong(assets.song`Cancion1`), music.PlaybackMode.LoopingInBackground)
        pause(1000)
    }
}
controller.right.onEvent(ControllerButtonEvent.Released, function () {
    if (partida && !(controller.left.isPressed())) {
        animation.runImageAnimation(
        prota,
        assets.animation`myAnim4`,
        200,
        false
        )
    }
})
controller.left.onEvent(ControllerButtonEvent.Released, function () {
    if (partida && !(controller.right.isPressed())) {
        animation.runImageAnimation(
        prota,
        assets.animation`myAnim3`,
        200,
        false
        )
    }
})
function GenerarMusica () {
    musica_randoom = randint(1, 3)
    if (musica_randoom == 1) {
        music.play(music.createSong(assets.song`Cancion2`), music.PlaybackMode.LoopingInBackground)
    } else if (musica_randoom == 2) {
        music.play(music.createSong(assets.song`Cancion3`), music.PlaybackMode.LoopingInBackground)
    } else if (musica_randoom == 3) {
        music.play(music.createSong(assets.song`Cancion4`), music.PlaybackMode.LoopingInBackground)
    }
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Boss, function (sprite5, otherSprite22) {
    if (sprite5.vy > 0 && sprite5.y < otherSprite22.y) {
        prota.setVelocity(0, -125)
        statusbar.value += -1
        music.play(music.createSoundEffect(WaveShape.Noise, 1259, 0, 255, 255, 100, SoundExpressionEffect.None, InterpolationCurve.Logarithmic), music.PlaybackMode.UntilDone)
    } else {
        info.changeLifeBy(-1)
        music.play(music.createSong(assets.song`muerte_prota`), music.PlaybackMode.InBackground)
    }
    pause(1000)
})
statusbars.onZero(StatusBarKind.EnemyHealth, function (status) {
    music.play(music.createSong(assets.song`ashes`), music.PlaybackMode.InBackground)
    sprites.destroy(boss_actual, effects.disintegrate, 500)
    sprites.destroy(statusbar)
    max_corazones += 10
    game.splash("+10 corazones maximos")
    mensaje_corazon = true
    nivel_superado = true
    boss_vivo = false
})
function GenerarNivel () {
    music.stopAllSounds()
    tipo_nivel = true
    jugador_en_puerta = false
    jugador_en_puerta_especial = false
    nivel_superado = false
    tipo_nivel = true
    DestruirSprites()
    scene.setBackgroundImage(assets.image`fondo_nivel_1`)
    if (nivel == 1) {
        tiles.setCurrentTilemap(tilemap`nivel58`)
    } else if (nivel == 2) {
        tiles.setCurrentTilemap(tilemap`nivel54`)
    } else if (nivel == 3) {
        tiles.setCurrentTilemap(tilemap`nivel56`)
    } else if (nivel == 4) {
        tiles.setCurrentTilemap(tilemap`nivel52`)
    } else if (nivel == 5) {
        tiles.setCurrentTilemap(tilemap`nivel50`)
    } else if (nivel == 6) {
        tiles.setCurrentTilemap(tilemap`nivel48`)
    } else if (nivel == 7) {
        tiles.setCurrentTilemap(tilemap`nivel46`)
    } else if (nivel == 8) {
        tiles.setCurrentTilemap(tilemap`nivel44`)
    } else if (nivel == 9) {
        tiles.setCurrentTilemap(tilemap`nivel42`)
    } else if (nivel == 10) {
        tipo_nivel = false
        tiles.setCurrentTilemap(tilemap`nivel10`)
    } else if (nivel == 11) {
        tiles.setCurrentTilemap(tilemap`nivel40`)
    } else if (nivel == 12) {
        tiles.setCurrentTilemap(tilemap`nivel38`)
    } else if (nivel == 13) {
        tiles.setCurrentTilemap(tilemap`nivel36`)
    } else if (nivel == 14) {
        tiles.setCurrentTilemap(tilemap`nivel34`)
    } else if (nivel == 15) {
        tiles.setCurrentTilemap(tilemap`nivel32`)
    } else if (nivel == 16) {
        tiles.setCurrentTilemap(tilemap`nivel16`)
    } else if (nivel == 17) {
        tiles.setCurrentTilemap(tilemap`nivel14`)
    } else if (nivel == 18) {
        tiles.setCurrentTilemap(tilemap`nivel18`)
    } else if (nivel == 19) {
        tiles.setCurrentTilemap(tilemap`nivel12`)
    } else if (nivel == 20) {
        tipo_nivel = false
        tiles.setCurrentTilemap(tilemap`nivel20`)
    } else if (nivel == 21) {
        tiles.setCurrentTilemap(tilemap`nivel21`)
    } else if (nivel == 22) {
        tiles.setCurrentTilemap(tilemap`nivel9`)
    } else if (nivel == 23) {
        tiles.setCurrentTilemap(tilemap`nivel23`)
    } else if (nivel == 24) {
        tiles.setCurrentTilemap(tilemap`nivel7`)
    } else if (nivel == 25) {
        tiles.setCurrentTilemap(tilemap`nivel25`)
    } else if (nivel == 26) {
        tiles.setCurrentTilemap(tilemap`nivel5`)
    } else if (nivel == 27) {
        tiles.setCurrentTilemap(tilemap`nivel27`)
    } else if (nivel == 28) {
        tiles.setCurrentTilemap(tilemap`nivel0`)
    } else if (nivel == 29) {
        tiles.setCurrentTilemap(tilemap`nivel29`)
    } else if (nivel == 30) {
        tipo_nivel = false
        tiles.setCurrentTilemap(tilemap`nivel30`)
    } else if (nivel == 408) {
        scene.setBackgroundImage(assets.image`cityscape`)
        tiles.setCurrentTilemap(tilemap`level`)
    }
    GenerarPuertaEspecial()
    GenerarPuerta()
    GenerarCorazones()
    GenerarAntorchas()
    CreacionPersonaje()
    CrearEnemigos()
    if (tipo_nivel) {
        GenerarLlave()
    } else {
        GenerarBoss()
    }
    MostrarNivel()
    GenerarMusica()
}
function Boss1 () {
    if (prota.x + 30 < boss_actual.x) {
        boss_actual.vx = -20
        if (nivel == 10) {
            boss_actual.setImage(assets.image`leviatan_izquierda`)
        } else if (nivel == 20) {
            boss_actual.setImage(assets.image`faraon_izquierda`)
        } else if (nivel == 30) {
            boss_actual.setImage(assets.image`myImage0`)
        }
    } else if (prota.x - 30 > boss_actual.x) {
        boss_actual.vx = 20
        if (nivel == 10) {
            boss_actual.setImage(assets.image`leviatan_derecha`)
        } else if (nivel == 20) {
            boss_actual.setImage(assets.image`faraon_derecha`)
        } else if (nivel == 30) {
            boss_actual.setImage(assets.image`myImage`)
        }
    } else {
        boss_actual.vx = 0
    }
}
function SistemaDeDobleSalto () {
    if (prota.isHittingTile(CollisionDirection.Bottom)) {
        prota.setVelocity(0, -125)
        salto = true
        music.play(music.createSong(hex`
                            0078000408010100001c00010a006400f4016400000400000000000000000000000000050000040c0000000100011b01000200011d
                            `), music.PlaybackMode.InBackground)
    } else if (salto == true) {
        prota.setVelocity(0, -125)
        salto = false
        music.play(music.createSong(hex`
                            0078000408010100001c00010a006400f4016400000400000000000000000000000000050000040c0000000100011b01000200011d
                            `), music.PlaybackMode.InBackground)
    }
}
function PonerPared (myLocation: tiles.Location) {
    if (nivel <= 10) {
        tiles.setTileAt(myLocation, assets.tile`pared_nivel_1`)
    } else if (nivel > 10 && nivel <= 20) {
        tiles.setTileAt(myLocation, assets.tile`pared_nivel_2`)
    } else if (nivel > 20 && nivel <= 30) {
        tiles.setTileAt(myLocation, assets.tile`pared_nivel_3`)
    }
}
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    if (partida && !(controller.left.isPressed())) {
        animation.runImageAnimation(
        prota,
        assets.animation`player_right_animated`,
        200,
        true
        )
        characterAnimations.setCharacterState(prota, characterAnimations.rule(Predicate.FacingRight))
        ataque_prota2 = 0
    }
})
function AtaqueIzquierda () {
    animation.runImageAnimation(
    prota,
    assets.animation`atacar_izquierda`,
    100,
    false
    )
    music.play(music.createSoundEffect(WaveShape.Noise, 1364, 1, 255, 255, 100, SoundExpressionEffect.Vibrato, InterpolationCurve.Logarithmic), music.PlaybackMode.InBackground)
    if (controller.left.isPressed()) {
        pause(100)
        animation.runImageAnimation(
        prota,
        assets.animation`player_left_animated`,
        200,
        true
        )
    }
}
function AtaqueDerecha () {
    animation.runImageAnimation(
    prota,
    assets.animation`atacar_derecha`,
    100,
    false
    )
    music.play(music.createSoundEffect(WaveShape.Noise, 1364, 1, 255, 255, 100, SoundExpressionEffect.Vibrato, InterpolationCurve.Logarithmic), music.PlaybackMode.InBackground)
    if (controller.right.isPressed()) {
        pause(100)
        animation.runImageAnimation(
        prota,
        assets.animation`player_right_animated`,
        200,
        true
        )
    }
}
function GenerarBoss () {
    statusbar = statusbars.create(40, 4, StatusBarKind.EnemyHealth)
    statusbar.max = 20
    statusbar.setColor(7, 2, 0)
    statusbar.setStatusBarFlag(StatusBarFlag.SmoothTransition, true)
    if (nivel == 10) {
        boss_actual = sprites.create(assets.image`leviatan_derecha`, SpriteKind.Boss)
        boss_actual.setScale(1.5, ScaleAnchor.Middle)
        for (let valor11 of tiles.getTilesByType(assets.tile`myTile3`)) {
            tiles.placeOnTile(boss_actual, valor11)
            PonerPared(valor11)
        }
    } else if (nivel == 20) {
        boss_actual = sprites.create(assets.image`faraon_derecha`, SpriteKind.Boss)
        boss_actual.setScale(1.5, ScaleAnchor.Middle)
        for (let valor12 of tiles.getTilesByType(assets.tile`myTile3`)) {
            tiles.placeOnTile(boss_actual, valor12)
            PonerPared(valor12)
        }
    } else if (nivel == 30) {
        boss_actual = sprites.create(assets.image`myImage0`, SpriteKind.Boss)
        for (let valor13 of tiles.getTilesByType(assets.tile`myTile3`)) {
            tiles.placeOnTile(boss_actual, valor13)
            PonerPared(valor13)
        }
        boss_actual.setScale(1.5, ScaleAnchor.Middle)
    }
    boss_actual.ay = 200
    statusbar.attachToSprite(boss_actual)
    boss_vivo = true
}
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    if (partida && nivel != 408) {
        if (mostrar_minimapa) {
            mostrar_minimapa = false
            sprites.destroy(mapStripe)
        } else {
            mostrar_minimapa = true
        }
    }
})
function EnemigoNivel1 () {
    for (let valor14 of tiles.getTilesByType(assets.tile`amarillo_enemigo`)) {
        enemigo = sprites.create(assets.image`fantasma_derecha`, SpriteKind.Enemy)
        characterAnimations.loopFrames(
        enemigo,
        assets.animation`derecha_fantasma0`,
        500,
        characterAnimations.rule(Predicate.MovingRight)
        )
        characterAnimations.loopFrames(
        enemigo,
        assets.animation`izquierda_fantasma`,
        500,
        characterAnimations.rule(Predicate.MovingLeft)
        )
        tiles.placeOnTile(enemigo, valor14)
        PonerPared(valor14)
        enemigo.ay = 200
        enemigo.follow(prota, 30)
    }
}
function MostrarLore () {
    game.setDialogTextColor(2)
    game.setDialogFrame(assets.image`fondo_1`)
    game.showLongText("Hace mucho tiempo existia un reino pacífico que, un triste dia, fue conquistado por un ejercito demoniaco.", DialogLayout.Full)
    game.showLongText("Tras mucho tiempo de batalla, este ejercito termino conquistando el reino y rebautizandolo como \"Reino Nochesfera\", controlado por 3 reyes.", DialogLayout.Full)
    game.showLongText("El 1r rey es Espectro, lider de los fantasmas, quien ha conquistado gran parte del territorio por sus estrategias militares.", DialogLayout.Full)
    game.showLongText("El 2o rey es Murcielagor, lider de los murcielagos, quien es responsable de grandes robos de suministros en las aldeas vecinas.", DialogLayout.Full)
    game.showLongText("El ultimo rey es Anguilo, lider de los tiburones, quien es quien crea el veneno que fluye en los rios de los territorios vecinos.", DialogLayout.Full)
    game.showLongText("Parecia que no habia esperanza, pero entonces apareció el caballero End, quien juro que derrotaria a los 3 reyes de la Nochesfera.", DialogLayout.Full)
    game.showLongText("Y asi, End se adentro al castillo de la Nochesfera para derrotar a los 3 reyes malignos.", DialogLayout.Full)
}
function ColocarAnimacionAntorcha (myLocation2: tiles.Location) {
    antorcha = sprites.create(assets.image`myImage3`, SpriteKind.Antorcha)
    animation.runImageAnimation(
    antorcha,
    assets.animation`myAnim1`,
    200,
    true
    )
    tiles.placeOnTile(antorcha, myLocation2)
    antorcha.y += -1
}
function CrearEnemigos () {
    if (nivel <= 10) {
        EnemigoNivel1()
    } else if (nivel > 10 && nivel <= 20) {
        EnemigoNivel2()
    } else if (nivel > 20 && nivel <= 30) {
        EnemigoNivel3()
    }
}
info.onLifeZero(function () {
    if (!(win) && !(end_game)) {
        llave_especial = false
        EndGame()
    }
})
function DestruirSprites () {
    sprites.destroyAllSpritesOfKind(SpriteKind.Boss)
    sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
    sprites.destroyAllSpritesOfKind(SpriteKind.Indicator)
    sprites.destroyAllSpritesOfKind(SpriteKind.Heart)
    sprites.destroyAllSpritesOfKind(SpriteKind.Antorcha)
    sprites.destroyAllSpritesOfKind(SpriteKind.Key)
    sprites.destroyAllSpritesOfKind(SpriteKind.Map)
    sprites.destroyAllSpritesOfKind(SpriteKind.Player)
    sprites.destroyAllSpritesOfKind(SpriteKind.SpecialKey)
    sprites.destroyAllSpritesOfKind(SpriteKind.Door)
    sprites.destroyAllSpritesOfKind(SpriteKind.SpecialDoor)
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Key, function (sprite62, otherSprite32) {
    sprites.destroy(otherSprite32, effects.ashes, 100)
    nivel_superado = true
    music.play(music.createSong(hex`
                    00f4010408020200001c00010a006400f401640000040000000000000000000000000005000004120000000400012704000800012a08000c00012a01001c000f05001202c102c20100040500280000006400280003140006020004120000000400012704000800012a08000c00012a
                    `), music.PlaybackMode.UntilDone)
})
function GenerarPuertaEspecial () {
    for (let valor15 of tiles.getTilesByType(assets.tile`myTile6`)) {
        puerta_aula = sprites.create(assets.image`myImage6`, SpriteKind.SpecialDoor)
        tiles.placeOnRandomTile(puerta_aula, assets.tile`myTile6`)
        puerta_aula.y += -7
    }
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Door, function (sprite6, otherSprite4) {
    if (nivel_superado) {
        MostrarFlecha()
        jugador_en_puerta = true
        pause(10)
        if (controller.up.isPressed()) {
            if (nivel == 30) {
                win = true
                EndGame()
            } else {
                music.play(music.createSoundEffect(WaveShape.Noise, 1, 452, 255, 255, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
                nivel += 1
                sprites.destroyAllSpritesOfKind(SpriteKind.Player)
                GenerarNivel()
            }
        }
    } else if (controller.up.isPressed()) {
        game.splash("Necesitas la llave")
    }
})
function MostrarInstrucciones () {
    game.setDialogTextColor(2)
    game.setDialogFrame(assets.image`fondo_1`)
    game.showLongText("A         : Saltar\\nA+A       : Doble salto\\nB         : Atacar\\nDER./IZQ. : Moverse\\nBAJO      : Minimapa\\nARRIBA    : Interactuar", DialogLayout.Full)
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function (sprite7, otherSprite5) {
    scene.cameraShake(5, 500)
    info.changeLifeBy(-1)
    sprites.destroy(otherSprite5)
    music.play(music.createSong(assets.song`muerte_prota`), music.PlaybackMode.InBackground)
})
function GenerarCorazones () {
    for (let valor16 of tiles.getTilesByType(assets.tile`myTile0`)) {
        corazon = sprites.create(assets.image`myImage1`, SpriteKind.Heart)
        animation.runImageAnimation(
        corazon,
        assets.animation`myAnim0`,
        200,
        true
        )
        tiles.placeOnTile(corazon, valor16)
        PonerPared(valor16)
    }
}
function MostrarNivel () {
    game.setDialogTextColor(2)
    game.setDialogFrame(assets.image`fondo_1`)
    game.showLongText("Nivel " + convertToText(nivel), DialogLayout.Full)
}
function EndGame () {
    music.stopAllSounds()
    end_game = true
    partida = false
    boss_vivo = false
    final = true
    mostrar_minimapa = false
    info.setLife(0)
    DestruirSprites()
    sprites.destroy(mapStripe)
    if (win) {
        music.play(music.melodyPlayable(music.magicWand), music.PlaybackMode.InBackground)
    } else {
        music.play(music.melodyPlayable(music.wawawawaa), music.PlaybackMode.InBackground)
    }
}
let projectile: Sprite = null
let corazon: Sprite = null
let end_game = false
let antorcha: Sprite = null
let salto = false
let tipo_nivel = false
let nivel_superado = false
let statusbar: StatusBarSprite = null
let musica_randoom = 0
let boss_actual: Sprite = null
let boss_vivo = false
let myMinimap: minimap.Minimap = null
let mapStripe: Sprite = null
let llave: Sprite = null
let enemigo: Sprite = null
let puerta_aula: Sprite = null
let jugador_en_puerta_especial = false
let flecha_puerta_nivel: Sprite = null
let jugador_en_puerta = false
let spawn_y = 0
let spawn_x = 0
let prota: Sprite = null
let puerta: Sprite = null
let nivel = 0
let ataque_prota2 = 0
let ataque_prota = 0
let llave_especial = false
let mensaje_corazon = false
let mostrar_minimapa = false
let win = false
let final = false
let partida = false
let menu = false
let max_corazones = 0
let atacar = false
pause(500)
scene.setBackgroundImage(assets.image`darkys_games_pantalla`)
pause(3000)
max_corazones = 10
menu = true
partida = false
final = false
win = false
mostrar_minimapa = true
mensaje_corazon = true
llave_especial = false
music.setVolume(70)
music.play(music.createSong(assets.song`Cancion1`), music.PlaybackMode.LoopingInBackground)
game.onUpdate(function () {
    if (menu) {
        scene.setBackgroundImage(assets.image`fondo_menu2`)
        if (controller.A.isPressed()) {
            menu = false
        } else if (controller.B.isPressed()) {
            MostrarLore()
            pause(1000)
        }
    } else if (!(partida) && !(final)) {
        MostrarInstrucciones()
        info.setLife(5)
        nivel = 1
        max_corazones = 10
        win = false
        end_game = false
        GenerarNivel()
        partida = true
    } else if (mostrar_minimapa) {
        GenerarMinimapa()
    }
    if (final) {
        ShowFinal()
    }
    if (boss_vivo) {
        Boss1()
    }
})
game.onUpdateInterval(2000, function () {
    if (boss_vivo) {
        if (prota.y < boss_actual.y) {
            if (prota.x < boss_actual.x - 10) {
                projectile = sprites.createProjectileFromSprite(assets.image`bola_de_plasma`, boss_actual, -100, -100)
            } else if (prota.x > boss_actual.x + 10) {
                projectile = sprites.createProjectileFromSprite(assets.image`bola_de_plasma`, boss_actual, 100, -100)
            } else {
                projectile = sprites.createProjectileFromSprite(assets.image`bola_de_plasma`, boss_actual, 0, -100)
            }
        } else if (prota.x < boss_actual.x - 10) {
            projectile = sprites.createProjectileFromSprite(assets.image`bola_de_plasma`, boss_actual, -100, 0)
        } else if (prota.x > boss_actual.x + 10) {
            projectile = sprites.createProjectileFromSprite(assets.image`bola_de_plasma`, boss_actual, 100, 0)
        }
        animation.runImageAnimation(
        projectile,
        assets.animation`bola_de_plasma_animado`,
        100,
        true
        )
    }
})
game.onUpdateInterval(100, function () {
    if (partida && prota.isHittingTile(CollisionDirection.Bottom)) {
        spawn_x = prota.x
        spawn_y = prota.y
    }
})
