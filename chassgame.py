grid=[(["."]*8)[:]for x in range(8)]
turn=1
def init_grid():
    global grid
    arr = ["r", "h", "b", "k", "q", "b", "h", "k"]
    for x in range(len(grid[0])):
        grid[0][x] = "b" + arr[x]
    for x in range(len(grid[-1])):
        grid[-1][x] = "w" + arr[x]
    for x in range(len(grid[1])):
        grid[1][x] = "b" + arr[x]
    for x in range(len(grid[-2])):
        grid[-2][x] = "w" + arr[x]
def print_grid():
    global grid
    for x in grid:
        print(x)
def movable(x,y,ex,ey):
    return True
def validate_move(x,y,ex,ey):
    global turn,grid
    coin=grid[x][y]
    end_coin=grid[ex][ey]
    if(turn==1 and (coin[0]=="b" or end_coin[0]=="w")) or (turn==0 and (coin[0]=="w" or end_coin[0]=="b")):
           return False
    else:
        res=movable(x,y,ex,ey)
        if res is True:
            grid[ex][ey]=coin
            grid[x][y]="."
        else:
            print("invalid move machan byr try again latter")
def move():
    global turn
    if(turn==1):
        print("white move")
        x,y=map(int,input("enter the start point:").split("."))
        ex,ey =map(int,input("enter the end point:").split("."))
        res=validate_move(x,y,ex,ey)
        turn=0
    else:
        print("black move")
        x,y=map(int,input("enter the start point:").split("."))
        ex,ey=map(int,input("enter the end point:").split("."))
        res=validate_move(x,y,ex,ey)
        turn=1
init_grid()
while True:
    move()
    print_grid()