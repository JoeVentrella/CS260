def moveTheTower(poleHeight,fromPole, toPole, withPole):
    """ Takes the towerHeight and 3 pole names"""

    if poleHeight >= 1:

        moveTheTower(poleHeight-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTheTower(poleHeight-1,withPole,toPole,fromPole)


def moveDisk(fromp,top):
    """Prints out a statement each time a disc moves"""

    print("moving disk from",fromp,"to",top)


moveTheTower(10,"A","B","C")