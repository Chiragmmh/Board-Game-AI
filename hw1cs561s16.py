import sys
import copy
import numbers
import decimal
def end_state(placement):
    i=0
    while i<5 :
       j=0
       while j<5:
            if placement[i][j]=='*' :
                return False

            j+=1
       i+=1
    return True

def evaluate(values,placement) :
   current_X=0
   current_O=0
   i=0
   while i<5 :
       j=0
       while j<5:
            if placement[i][j]=='X' :
                current_X += int(values[i][j])
            if placement[i][j]=='O' :
                current_O += int(values[i][j])

            j+=1
       i+=1
   if Mainplayer=='X':
    return current_X-current_O
   else :
    return current_O-current_X
   current_X=0
   current_O=0
def raid(x,y,player,placement,temp_placement):
    if player=='X':
        opponent='O'
    else :
        opponent='X'
        player='O'
    if x-1>=0 and placement[x-1][y]==opponent :
                        temp_placement[x][y]=player
                        temp_placement[x-1][y]=player
    if y-1>=0 and placement[x][y-1]==opponent :
                        temp_placement[x][y]=player
                        temp_placement[x][y-1]=player
    if x+1<=4 and placement[x+1][y]==opponent :
                        temp_placement[x][y]=player
                        temp_placement[x+1][y]=player
    if y+1<=4 and placement[x][y+1]==opponent :
                        temp_placement[x][y]=player
                        temp_placement[x][y+1]=player

    return temp_placement
def insert_player(x,y,placement,player):
    if player=='X':
        opponent='O'
    else :
        opponent='X'
        player='O'
    if x-1>=0 and placement[x-1][y]==player :
                        placement=raid(x,y,player,placement,placement)
    if y-1>=0 and placement[x][y-1]==player :
                         placement=raid(x,y,player,placement,placement)
    if x+1<=4 and placement[x+1][y]==player :
                         placement=raid(x,y,player,placement,placement)
    if y+1<=4 and placement[x][y+1]==player :
                         placement=raid(x,y,player,placement,placement)
    placement[x][y]=player
    return placement
check=[]
def greedy_bfs(values,placement,player):
   temp_placement=[]

   if player=='X':
        opponent='O'
   else :
        opponent='X'
        player='O'
   i=0
   global check
   while i<5 :
       j=0
       while j<5:


                if placement[i][j]=='X'or placement[i][j]=='O':
                    check.append(str('A'))
                if placement[i][j]=='*' :
                    temp_placement=copy.deepcopy(placement)
                    if i-1>=0 and placement[i-1][j]==Mainplayer :
                            temp_placement=raid(i,j,player,placement,temp_placement)
                    if j-1>=0 and placement[i][j-1]==Mainplayer :
                            temp_placement=raid(i,j,player,placement,temp_placement)
                    if i+1<=4 and placement[i+1][j]==Mainplayer :
                            temp_placement=raid(i,j,player,placement,temp_placement)
                    if j+1<=4 and placement[i][j+1]==Mainplayer :
                            temp_placement=raid(i,j,player,placement,temp_placement)
                    temp_placement[i][j]=player
                    check.append(int(evaluate(values,temp_placement)))

                j+=1
       i+=1
   print check
   d=sorted(check, key=lambda x: (isinstance(x, numbers.Number), x))
   c=d[-1]
   index=check.index(c)
   indexg_i=index/5
   indexg_j=index%5
   print index
   print indexg_i
   print indexg_j
   if end_state(placement)==False:
        print insert_player(indexg_i,indexg_j,placement,player)
   while len(check) > 0 :
       check.pop()
   return placement
index_i=int
index_j=int
Values=[]
player=str
Mainplayer=str
def node_aplhabet(i):
    if i==0:
        return 'A'
    elif i==1:
        return 'B'
    elif i==2:
        return 'C'
    elif i==3:
        return 'D'
    elif i==4:
        return 'E'

c=0
def minimax(values,placement,depth,player,parent):
    global c
    global Mainplayer
    global index_i
    global index_j
    value=0
    depth_counter=int(depth)
    if end_state(placement)==True:
        return evaluate(values,placement)
    if player=='X':
        next_player='O'
    else :
        next_player='X'
        player='O'
    check1=[]
    if depth_counter==0 :
        print 0
        print  evaluate(values,placement)
        return evaluate(values,placement)
    xlist=[]
    olist=[]
    i=0

    while i<5 :
        j=0
        while j<5:

            if placement[i][j]=='X'or placement[i][j]=='O':
                    if player== Mainplayer:
                        xlist.append(str('A'))
                    else :
                        olist.append(str('B'))
            if placement[i][j]=='*' :
                temp_placement=copy.deepcopy(placement)
                if i-1>=0 and placement[i-1][j]==player :
                        temp_placement=raid(i,j,player,placement,temp_placement)
                if j-1>=0 and placement[i][j-1]==player :
                        temp_placement=raid(i,j,player,placement,temp_placement)
                if i+1<=4 and placement[i+1][j]==player :
                        temp_placement=raid(i,j,player,placement,temp_placement)
                if j+1<=4 and placement[i][j+1]==player :
                        temp_placement=raid(i,j,player,placement,temp_placement)
                temp_placement[i][j]=player
                check1.append(int(evaluate(values,temp_placement)))
                print temp_placement
                print check1
                if player== Mainplayer:
                    var='-Infinity'
                    depth_print=int(depth_actual)-int(depth)+1
                    if depth_counter>1:
                        traverse_log.write(node_aplhabet(j)+str(i+1)+','+str(depth_print)+','+str('Infinity')+'\n')
                    else:
                        traverse_log.write(node_aplhabet(j)+str(i+1)+','+str(depth_print)+','+str(evaluate(values,temp_placement))+'\n')
                    c=max(evaluate(values,temp_placement),c)
                    a=minimax(values,temp_placement,depth_counter-1,next_player,node_aplhabet(j)+str(i+1))
                    xlist.append(a)
                    d=sorted(xlist, key=lambda x: (isinstance(x, numbers.Number), x))
                    c=d[-1]
                    var=c
                    if depth_print-1 == 0:
                        traverse_log.write("root"+','+str(depth_print-1)+','+str(var)+'\n')
                    else:
                        traverse_log.write(parent+','+str(depth_print-1)+','+str(c)+'\n')
                    index=xlist.index(c)
                    index_i=index/5
                    index_j=index%5
                    print index_i
                    print index_j
                else :
                    depth_print=int(depth_actual)-int(depth)+1
                    if depth_counter>1:
                        traverse_log.write(node_aplhabet(j)+str(i+1)+','+str(depth_print)+','+str('-Infinity')+'\n')
                    else:
                        traverse_log.write(node_aplhabet(j)+str(i+1)+','+str(depth_print)+','+str(evaluate(values,temp_placement))+'\n')
                    c=min(evaluate(values,temp_placement),c)
                    b=minimax(values,temp_placement,depth_counter-1,next_player,node_aplhabet(j)+str(i+1))
                    olist.append(b)
                    c=min(olist)
                    traverse_log.write(parent+','+str(depth_print-1)+','+str(c)+'\n')




            j+=1
        i+=1

    return c
indexab_i=0
indexab_j=0
h=0
def alphabeta(values,placement,depth,player,parent,alpha,beta):
    global h
    global Mainplayer
    global indexab_i
    global indexab_j
    depth_counter=int(depth)
    if end_state(placement)==True:
        return evaluate(values,placement)
    if player=='X':
        next_player='O'
    else :
        next_player='X'
        player='O'
    check1=[]
    if depth_counter==0 :
        return evaluate(values,placement)
    xlist=[]
    olist=[]
    i=0

    while i<5 :
        j=0
        while j<5:

            if placement[i][j]=='X'or placement[i][j]=='O':
                    if player== Mainplayer:
                        xlist.append(str('A'))
                    else :
                        olist.append(str('B'))
            if placement[i][j]=='*' :
                temp_placement=copy.deepcopy(placement)
                if i-1>=0 and placement[i-1][j]==player :
                        temp_placement=raid(i,j,player,placement,temp_placement)
                if j-1>=0 and placement[i][j-1]==player :
                        temp_placement=raid(i,j,player,placement,temp_placement)
                if i+1<=4 and placement[i+1][j]==player :
                        temp_placement=raid(i,j,player,placement,temp_placement)
                if j+1<=4 and placement[i][j+1]==player :
                        temp_placement=raid(i,j,player,placement,temp_placement)
                temp_placement[i][j]=player
                check1.append(int(evaluate(values,temp_placement)))
                print temp_placement
                print check1
                if player== Mainplayer:
                    var='-Infinity'
                    depth_print=int(depth_actual)-int(depth)+1
                    if depth_counter>1:
                        traverse_log.write(node_aplhabet(j)+str(i+1)+','+str(depth_print)+','+str('Infinity')+','+str(alpha)+','+str(beta)+'\n')
                    else:
                        traverse_log.write(node_aplhabet(j)+str(i+1)+','+str(depth_print)+','+str(evaluate(values,temp_placement))+','+str(alpha)+','+str(beta)+'\n')

                    a=alphabeta(values,temp_placement,depth_counter-1,next_player,node_aplhabet(j)+str(i+1),alpha,beta)
                    xlist.append(a)
                    d=sorted(xlist, key=lambda x: (isinstance(x, numbers.Number), x))
                    h=d[-1]
                    print h
                    if h>=beta:
                        indexab_i=i
                        indexab_j=j
                        print indexab_i
                        print indexab_j
                        if depth_print-1 == 0:
                            traverse_log.write("root"+','+str(depth_print-1)+','+str(var)+','+str(alpha)+','+str(beta)+'\n')
                        else:
                            traverse_log.write(parent+','+str(depth_print-1)+','+str(h)+','+str(alpha)+','+str(beta)+'\n')
                        return h
                    alpha=max(alpha,h)
                    print alpha
                    var=h
                    if depth_print-1 == 0:
                        traverse_log.write("root"+','+str(depth_print-1)+','+str(var)+','+str(alpha)+','+str(beta)+'\n')
                    else:
                        traverse_log.write(parent+','+str(depth_print-1)+','+str(h)+','+str(alpha)+','+str(beta)+'\n')
                    index=xlist.index(h)
                    indexab_i=index/5
                    indexab_j=index%5
                    print indexab_i
                    print indexab_j
                else :
                    depth_print=int(depth_actual)-int(depth)+1
                    if depth_counter>1:
                        traverse_log.write(node_aplhabet(j)+str(i+1)+','+str(depth_print)+','+str('-Infinity')+','+str(alpha)+','+str(beta)+'\n')
                    else:
                       traverse_log.write(node_aplhabet(j)+str(i+1)+','+str(depth_print)+','+str(evaluate(values,temp_placement))+','+str(alpha)+','+str(beta)+'\n')
                    b=alphabeta(values,temp_placement,depth_counter-1,next_player,node_aplhabet(j)+str(i+1),alpha,beta)
                    olist.append(b)
                    h=min(olist)
                    if h<=alpha:
                        traverse_log.write(parent+','+str(depth_print-1)+','+str(h)+','+str(alpha)+','+str(beta)+'\n')
                        return h
                    beta=min(beta,h)
                    traverse_log.write(parent+','+str(depth_print-1)+','+str(h)+','+str(alpha)+','+str(beta)+'\n')



            j+=1
        i+=1

    return h
depth_actual=int
traverse_log=open('traverse_log.txt','w')
def main():
    global index_i
    global index_j
    global Mainplayer
    global depth_actual
    global traverse_log
    #input_file = open(sys.argv[2], 'r')
    input_file=open('input.txt','r')
    task_n = input_file.readline()
    task = task_n.rstrip('\r\n')
    if task=='4':
        f=open('trace_state.txt','w').close()
        Firstplayer_n = input_file.readline()
        Firstplayer = Firstplayer_n.rstrip('\r\n')
        print Firstplayer
        Firstplayeralgorithm_n=input_file.readline()
        Firstplayeralgorithm=Firstplayeralgorithm_n.rstrip('\r\n')
        print Firstplayeralgorithm
        Firstplayerdepth_n=input_file.readline()
        Firstplayerdepth=Firstplayerdepth_n.rstrip('\r\n')
        print Firstplayerdepth
        Secondplayer_n = input_file.readline()
        Secondplayer = Secondplayer_n.rstrip('\r\n')
        print Secondplayer
        Secondplayeralgorithm_n=input_file.readline()
        Secondplayeralgorithm=Secondplayeralgorithm_n.rstrip('\r\n')
        print Secondplayeralgorithm
        Secondplayerdepth_n=input_file.readline()
        Secondplayerdepth=Secondplayerdepth_n.rstrip('\r\n')
        print Secondplayerdepth
        Values = []
        Piece_placement=[]
        i=1
        for line in input_file:
            if i<6 :
                int = line.split()
                Values.append(int)
                i+=1
            else :
                line_stripped = line.rstrip('\r\n')
                word=list(line_stripped)
                Piece_placement.append(word)
        print Values
        print Piece_placement
        Simulation_placement=copy.deepcopy(Piece_placement)
        PlayerFlag=True
        while end_state(Simulation_placement)==False:
            if PlayerFlag==True:
                Mainplayer=copy.deepcopy(Firstplayer)
                algorithm=copy.deepcopy(Firstplayeralgorithm)
                depth_actual=copy.deepcopy(Firstplayerdepth)
                PlayerFlag=False
            else:
                Mainplayer=copy.deepcopy(Secondplayer)
                algorithm=copy.deepcopy(Secondplayeralgorithm)
                depth_actual=copy.deepcopy(Secondplayerdepth)
                PlayerFlag=True
            if algorithm=='1':
                print Simulation_placement
                a= greedy_bfs(Values,Simulation_placement,Mainplayer)
                Simulation_placement==copy.deepcopy(a)
                print Simulation_placement
                with open('trace_state.txt', 'a') as f:
                    i=0
                    while i<5:

                        for s in Simulation_placement[i]:
                            f.write(s)
                        f.write('\n')
                        i+=1
                f.close()
                print a
            if algorithm=='2':
                a= minimax(Values,Simulation_placement,depth_actual,Mainplayer,'root')
                print index_i
                print index_j
                d=insert_player(index_i,index_j,Simulation_placement,Mainplayer)
                Simulation_placement=copy.deepcopy(d)
                with open('trace_state.txt','a') as f :
                    i=0
                    while i<5:

                        for s in Simulation_placement[i]:
                            f.write(s)

                        f.write('\n')
                        i+=1
                f.close()
            if algorithm=='3':
                Mainalpha=decimal.Decimal('-Infinity')
                Mainbeta=decimal.Decimal('+Infinity')
                a=alphabeta(Values,Simulation_placement,depth_actual,Mainplayer,'root',Mainalpha,Mainbeta)
                print a
                Simulation_placement=insert_player(indexab_i,indexab_j,Simulation_placement,Mainplayer)
                with open('trace_state.txt','a') as f :
                    i=0
                    while i<5:

                        for s in Simulation_placement[i]:
                            f.write(s)

                        f.write('\n')
                        i+=1
                f.close()


    else:
        player_n = input_file.readline()
        Mainplayer = player_n.rstrip('\r\n')
        print Mainplayer
        depth_n = input_file.readline()
        depth_actual = depth_n.rstrip('\r\n')
        print depth_actual
        global Values
        Values = []
        Piece_placement=[]
        i=1
        for line in input_file:
            if i<6 :
                int = line.split()
                Values.append(int)
                i+=1
            else :
                line_stripped = line.rstrip('\r\n')
                word=list(line_stripped)
                Piece_placement.append(word)
        print Values
        print Piece_placement
        print evaluate(Values,Piece_placement)


    if task== '1':
        a= greedy_bfs(Values,Piece_placement,Mainplayer)

        with open('next_state.txt', 'w') as f:
            i=0
            while i<5:

                for s in a[i]:
                    f.write(s)

                f.write('\n')
                i+=1

        print a
        f.close()


    if task== '2':
        traverse_log.write('Node,Depth,Value\n')
        traverse_log.write('root,0,-Infinity\n')
        a= minimax(Values,Piece_placement,depth_actual,Mainplayer,'root')
        print a
        traverse_log.close()
        if end_state(Piece_placement)==False:
            print insert_player(index_i,index_j,Piece_placement,Mainplayer)
        print Piece_placement
        with open('next_state.txt','w') as f :
            i=0
            while i<5:

                for s in Piece_placement[i]:
                    f.write(s)

                f.write('\n')
                i+=1
        f.close()
    if task=='3':
        traverse_log.write('Node,Depth,Value,Alpha,Beta\n')
        traverse_log.write('root,0,-Infinity,-Infinity,Infinity\n')
        Mainalpha=decimal.Decimal('-Infinity')
        Mainbeta=decimal.Decimal('+Infinity')
        a=alphabeta(Values,Piece_placement,depth_actual,Mainplayer,'root',Mainalpha,Mainbeta)
        print a
        traverse_log.close()
        if end_state(Piece_placement)==False:
            print insert_player(indexab_i,indexab_j,Piece_placement,Mainplayer)
        print Piece_placement
        with open('next_state.txt','w') as f :
            i=0
            while i<5:

                for s in Piece_placement[i]:
                    f.write(s)

                f.write('\n')
                i+=1
        f.close()


if __name__ == '__main__':
    main()
