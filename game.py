import random
import time
def displayIntro():
    print("Долгий путь по стране драконов подошел к концу.")
    print("Перед собой вы видите две пещеры. Дракон в одной из них сейчас сторожит свои сокровища.А второй отправился на ближайшее пастбище пообедат")
    print("К сожалению, вы не видели из какой пещеры улетел дракон, и теперь вам придется полностью доверится удаче")
    print()
def chooseCave():
    cave = ""
    while cave != "1" and cave != "2":
        print("В какую пещеру ты хочешь войти (1 или 2)?")
        cave = input()
    return cave
def checkCave(chooseCave):
    print("Вы осторожно крадетесь по сырой и мрачной пещере…")
    time.sleep(2)
    print("Вокруг в беспорядке разбросаны кости тех, кому не повезло…")
    time.sleep(2)
    print("Внезапно…")
    print()
    time.sleep(2)
    friendlyCave = random.randint(1,2)
    if chooseCave == str(friendlyCave):
        print("… мгла расступается и вашему взору предстает настоящая гора сокровищ!")
        print("Быстро набив карманы драгоценностями, вы быстро покидаете пещеру, пока дракон не вернулся. Счастливая старость теперь обеспечена.")
    else:
        print("Огромный дракон преградил вам путь. Не тратя лишних слов на дискуссии, он сразу приступает к обеду.")
        time.sleep(2)
        print("Сегодня в пещере появится несколько новых костей… Ваших.")
playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print("Хотите попробовать еще разок? (yes или no)")
    playAgain = input()