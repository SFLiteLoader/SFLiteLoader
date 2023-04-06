import pygame
import json

if __name__ == "__main__":
    pygame.init()
    # runtime values
    from lib import player
    from lib import runtime_values
    from lib import imgs
    from lib.plants import plants_list
    from lib import process
    from lib import drawObj

    runtime_values.players = [player.player(pygame.image.load(
        "assets/img/player.png"), pygame.math.Vector2(900, 100), runtime_values.screen, runtime_values.window_size)]
    
    with open("data/setting.json", 'r', encoding='utf8') as setting_file: # 셋팅파일 열기
        runtime_values.setting = json.load(setting_file)
    with open(f"data/lang/{runtime_values.setting['lang']}.json", 'r', encoding='utf8') as lang_file: # 언어파일 열기
        runtime_values.lang = json.load(lang_file)
        
    runtime_values.running = True
    runtime_values.my_dir = player.Direction.STOP #

    # 버전변수
    version = runtime_values.version
    version_text = f"{version[0]} {version[1]}.{version[2]}.{version[3]}"

    from lib import draw
    from lib import keyinput
    from lib import farm

    print(f'''
                         _    ___       ___
     _ __   _____      _| | _|_ _|_ __ |_ _|
    | '_ \\ / _ \\ \\ /\\ / / |/ /| || '_ \\ | |
    | | | |  __/\\ V  V /|   < | || | | || |
    |_| |_|\\___| \\_/\\_/ |_|\\_\\___|_| |_|___| Games
     ____         _____         ____
    / ___|       |  ___|       / ___|
    \\___ \\       | |_         | |  _
     ___) |      | _|         | |_| |
    |____/ imple |_|  arming   \\____|ame
    
    V. {version_text}
    ''', end="")
    runtime_values.logs.info("Start Loading")
    
    # 변수
    # colors
    SKYBLUE = pygame.Color(113, 199, 245)
    BLACK = pygame.Color(0, 0, 0)
    WHITE = pygame.Color(255, 255, 255)
    # 노래
    musics: dict[str,pygame.mixer.Sound]={
        "sfg" : pygame.mixer.Sound("assets/music/sfg.mp3")
    }

    # 세팅
    pygame.display.set_caption(f"sfg {version_text}! - by newkini")
    pygame.display.set_icon(pygame.image.load('assets/img/icon.png'))
    pygame.mouse.set_visible(False)
    if runtime_values.setting["musicStart"]:
        musics["sfg"].play(-1)

    # 게임와일
    runtime_values.logs.info("Finish Loading")
    while runtime_values.running:
        musPos: tuple = pygame.mouse.get_pos()
        df = runtime_values.clock.tick(runtime_values.fps) / 1000
        runtime_values.clock.tick(runtime_values.fps)

        # 그리기
        runtime_values.screen.blit(imgs.img("mus"),musPos) # 마우스 커서
        drawObj.drawObj(runtime_values, draw)

        # 처리
        process.process()
        keyinput.process()
        runtime_values.players[0].move(runtime_values.my_dir, df)
        farm.grow_plants()
        farm.rot_plants(runtime_values)
        pygame.display.update()  # 화면 업데이트

    runtime_values.logs.info("quit")
    runtime_values.logs.save()
    musics["sfg"].stop()
    pygame.quit()
