import pyautogui
import json

def main():
    width, height = pyautogui.size()
    x_fact = width/1920
    y_fact = height/1080
    towerx_fact = x_fact
    towery_fact = y_fact

    check = abs(y_fact/x_fact)
    if check > 1.3 or check < 0.74:
        towerx_fact = x_fact*1.1578125
        towery_fact = y_fact/1.10925925925

    pos = {

        "sniper_pos": ((towerx_fact * 1608),(towery_fact * 501)),
        "alchemist_pos": ((towerx_fact * 1551),(towery_fact * 544)),
        "village_pos": ((towerx_fact * 1581),(towery_fact * 622)),

        "top_ninja_pos": ((towerx_fact * 824),(towery_fact * 366)),
        "top_alchemist_pos": ((towerx_fact * 831),(towery_fact * 307)),
        "bottom_alchemist_pos": ((towerx_fact * 834),(towery_fact * 764)),
        "bottom_ninja_pos": ((towerx_fact * 835),(towery_fact * 696))
    }

    with open('towerpos.json', 'w') as f:
        json.dump(pos, f)

if __name__ == '__main__':
    main()


