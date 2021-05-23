h, w = map(int, input().split())

if h == 1 and w == 1:
    print("Draw")
    exit()

a = []

for i in range(h):
    a.append([c for c in input()])

game = {
    'x': 0,
    'y': 0,
    'n': 0,
    'takahashi': 0,
    'aoki': 0
}

def check(game, opt):
    if opt == 'right':
        game['x'] += 1
    else:
        game['y'] += 1
    
    if game['x'] >= w:
        return False

    if game['y'] >= h:
        return False

    return True


def next(game, opt):
    player = 'takahashi' if game['n'] % 2 == 0 else 'aoki'
    
    if a[game['y']][game['x']] == '+':
        game[player] += 1
    else:
        game[player] -= 1

    game['n'] += 1

    return game

draw_flag = False

def exec(game):
    # print(game)
    global draw_flag
    
    for opt in ['right', 'down']:
        result = game.copy()
        if not check(result, opt):
            continue

        result = next(result, opt)
        
        # ゲーム終了
        if result['x'] == (w - 1) and result['y'] == (h - 1):
            print(game)
            if game['takahashi'] > game['aoki']:
                print('Takahashi')
                exit()
            
            if game['takahashi'] == game['aoki']:
                draw_flag = True
        
        exec(result)

exec(game)

if draw_flag:
    print("Draw")
else:
    print("Aoki")
