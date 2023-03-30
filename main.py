nfinp=int(input("Give me the number of inputs (1-8):"))
eq=0

if nfinp == 4:
    eq=int(input("You want 1) Karnaugh Map or 2) Quine McCluskey?"))



if  (0 < nfinp < 4) or eq == 1:
        #K_Map for 2 inputs.
    def inp2_k_map(mt,nip):
        for i in range(50):print("-",end='')
        print()
        prnt=input("Enter Variables with single space(A B) : ").split(" ")
        for i in range(len(mt)):
            mt[i]='0b'+bin(mt[i])[2:].lstrip('0')
        op=''
        ans=[[0,0],[0,0]]
        ansmx=[[0,0],[0,0]]
        flag=0
        temp=[]
        for i in range(2):
            for j in range(2):
                p='0b'+(bin(i)[2:]+bin(j)[2:]).lstrip('0')
                if p in mt:
                    ans[i][j]=1
        for i in range(50):print("-",end='')
        print()
        print("The kmap plotted : ")
        if nip==1:
            for each in ans:print(*each)
        elif nip==2:
            for i in range(2):
                for j in range(2):
                    if ans[i][j]==1:
                        ansmx[i][j]=0
                    else:
                        ansmx[i][j]=1
            for each in ansmx:print(*each)
        if ans==[[1,1],[1,1]]:
            flag=1
            op='1'

        if flag==0:
            for i in range(2):
                if ans[i]==[1,1]:
                    if nip==1:
                        op='A ' if i==1 else "A' "
                    elif nip==2:
                        op="(A') " if i==1 else "(A) "
                    temp.extend([(i,0),(i,1)])
        
        if flag==0:
            if ans[0][0]==1 and ans[1][0]==1:
                if nip==1:
                    op=op+"B' "
                elif nip==2:
                    op=op+"(B) "
                temp.extend([(0,0),(1,0)])
            elif ans[0][1]==1 and ans[1][1]==1:
                if nip==1:
                    op=op+"B "
                elif nip==2:
                    op=op+"(B') "
                temp.extend([(0,1),(1,1)])
        if nip==1:
            vr=["A'B' ","A'B ","AB' ","AB "]
        elif nip==2:
            vr=["(A+B) ","(A+B') ","(A'+B) ","(A'+B') "]

        if flag==0:
            for i in range(2):
                for j in range(2):
                    if ans[i][j]==1 and (i,j) not in temp:
                        op=op+vr[int('0b'+bin(i)[2:]+bin(j)[2:],2)]
        op=op.rstrip(" ")
        if nip==1:
            op=op.replace(" ","+")
        op=op.replace("A",prnt[0])
        op=op.replace("B",prnt[1])
        for i in range(50):print("*",end='')
        print()
        print("The simplified equation is :",op)
        for i in range(50):print("*",end='')
        print()

    #K_Map for 4 inputs.
    def inp4_k_map(mt,nip):
        import copy
        for _ in range(50):print("-",end='')
        print()
        pr_v=input("Enter variables single space(A B C D) : ").split(" ")
        an=[]
        anmx=[]
        (tmp,flag)=(0,0)
        op=''
        for i in range(4):
            an.append([0]*4)
            anmx.append([0]*4)

        for i in range(4):
            for j in range(4):
                if i<2:
                    bi='0'+bin(i)[2:]
                else:
                    bi=bin(i)[2:]
                if j<2:
                    bj='0'+bin(j)[2:]
                else:
                    bj=bin(j)[2:]
                p=int('0b'+bi+bj,2)
                if p in mt:
                    an[i][j]=1
        for i in range(4):
            (an[i][2],an[i][3])=(an[i][3],an[i][2])
        for i in range(4):
            (an[2][i],an[3][i])=(an[3][i],an[2][i])

        for _ in range(50):print("-",end='') 
        print()
        print("The Karnaugh Map plotted is : ")
        if nip==1:
            for each in an:
                print(*each)
        elif nip==2:
            for i in range(4):
                for j in range(4):
                    if an[i][j]==1:
                        anmx[i][j]=0
                    else:
                        anmx[i][j]=1
            for each in anmx:print(*each)

        octa=[]
        qrd=[]
        qrd_ref=[]
        qrd_rep=[]
        dul=[]
        sngl=[]
        if nip==1:
            octa_val=[["C' ","D ","C ","D' "],["A' ","B ","A ","B' "]]  # 0 for vert and 1 for horz
            qrd_val=[["C'D' ","C'D ","CD ","CD' "],["A'B' ","A'B ","AB ","AB' "]]  # 0 for vert and 1 for horz
            qrd_val_4=[["A'C' ","A'D ","A'C ","A'D' "],["BC' ","BD ","BC ","BD' "],["AC' ","AD ","AC ","AD' "],["B'C' ","B'D ","B'C ","B'D' "]]
            dul_vert=[["A'C'D' ","A'C'D ","A'CD ","A'CD' "],["BC'D' ","BC'D ","BCD ","BCD' "],["AC'D' ","AC'D ","ACD ","ACD' "],["B'C'D' ","B'C'D ","B'CD ","B'CD' "]]
            dul_horz=[["A'B'C' ","A'B'D ","A'B'C ","A'B'D' "],["A'BC' ","A'BD ","A'BC ","A'BD' "],["ABC' ","ABD ","ABC ","ABD' "],["AB'C' ","AB'D ","AB'C ","AB'D' "]]
            sngl_val=[["A'B'C'D' ","A'B'C'D ","A'B'CD ","A'B'CD' "],["A'BC'D' ","A'BC'D ","A'BCD ","A'BCD' "],["ABC'D' ","ABC'D ","ABCD ","ABCD' "],["AB'C'D' ","AB'C'D ","AB'CD ","AB'CD' "]]
        elif nip==2:
            octa_val=[["(C) ","(D') ","(C') ","(D) "],["(A) ","(B') ","(A') ","(B) "]]  # 0 for vert and 1 for horz
            qrd_val=[["(C+D) ","(C+D') ","(C'+D') ","(C'+D) "],["(A+B) ","(A+B') ","(A'+B') ","(A'+B) "]]  # 0 for vert and 1 for horz
            qrd_val_4=[["(A+C) ","(A+D') ","(A+C') ","(A+D) "],["(B'+C) ","(B'+D') ","(B'+C') ","(B'+D) "],["(A'+C) ","(A'+D') ","(A'+C') ","(A'+D) "],["(B+C) ","(B+D') ","(B+C') ","(B+D) "]]
            dul_vert=[["(A+C+D) ","(A+C+D') ","(A+C'+D') ","(A+C'+D) "],["(B'+C+D) ","(B'+C+D') ","(B'+C'+D') ","(B'+C'+D) "],["(A'+C+D) ","(A'+C+D') ","(A'+C'+D') ","(A'+C'+D) "],["(B+C+D) ","(B+C+D') ","(B+C'+D') ","(B+C'+D) "]]
            dul_horz=[["(A+B+C) ","(A+B+D') ","(A+B+C') ","(A+B+D) "],["(A+B'+C) ","(A+B'+D') ","(A+B'+C') ","(A+B'+D) "],["(A'+B'+C) ","(A'+B'+D') ","(A'+B'+C') ","(A'+B'+D) "],["(A'+B+C) ","(A'+B+D') ","(A'+B+C') ","(A'+B+D) "]]
            sngl_val=[["(A+B+C+D) ","(A+B+C+D') ","(A+B+C'+D') ","(A+B+C'+D) "],["(A+B'+C+D) ","(A+B'+C+D') ","(A+B'+C'+D') ","(A+B'+C'+D) "],["(A'+B'+C+D) ","(A'+B'+C+D') ","(A'+B'+C'+D') ","(A'+B'+C'+D) "],["(A'+B+C+D) ","(A'+B+C+D') ","(A'+B+C'+D') ","(A'+B+C'+D) "]]

        if an==[[1]*4,[1]*4,[1]*4,[1]*4]:
            op='1'
        else:
            for i in range(-1,3):
                if an[i][0]==1 and an[i][1]==1 and an[i][2]==1 and an[i][-1]==1 and an[i+1][0]==1 and an[i+1][1]==1 and an[i+1][2]==1 and an[i+1][-1]==1:
                    op=op+octa_val[1][i]
                    octa.append([(i,0),(i,1),(i,2),(i,-1)])
                    if i<2:
                        octa.append([(i+1,0),(i+1,1),(i+1,2),(i+1,-1)])
                    else:
                        octa.append([(-1,0),(-1,1),(-1,2),(-1,-1)])
                    if i<2:
                        octa.append([(i,0),(i+1,0),(i,1),(i+1,1)])
                        octa.append([(i,1),(i+1,1),(i,2),(i+1,2)])
                        octa.append([(i,2),(i+1,2),(i,-1),(i+1,-1)])
                        octa.append([(i,-1),(i+1,-1),(i,0),(i+1,0)])
                    else:
                        octa.append([(i,0),(-1,0),(i,1),(-1,1)])
                        octa.append([(i,1),(-1,1),(i,2),(-1,2)])
                        octa.append([(i,2),(-1,2),(i,-1),(-1,-1)])
                        octa.append([(i,-1),(-1,-1),(i,0),(-1,0)])

            for i in range(-1,3):
                if an[0][i]==1 and an[1][i]==1 and an[2][i]==1 and an[-1][i]==1 and an[0][i+1]==1 and an[1][i+1]==1 and an[2][i+1]==1 and an[-1][i+1]==1:
                    op=op+octa_val[0][i]    
                    octa.append([(0,i),(1,i),(2,i),(-1,i)])
                    if i<2:
                        octa.append([(0,i+1),(1,i+1),(2,i+1),(-1,i+1)])
                    else:
                        octa.append([(0,-1),(1,-1),(2,-1),(-1,-1)])
                    if i<2:
                        octa.append([(0,i),(1,i),(0,i+1),(1,i+1)])
                        octa.append([(1,i),(2,i),(1,i+1),(2,i+1)])
                        octa.append([(2,i),(-1,i),(2,i+1),(-1,i+1)])
                        octa.append([(-1,i),(0,i),(-1,i+1),(0,i+1)])
                    else:
                        octa.append([(0,i),(1,i),(0,-1),(1,-1)])
                        octa.append([(1,i),(2,i),(1,-1),(2,-1)])
                        octa.append([(2,i),(-1,i),(2,-1),(-1,-1)])
                        octa.append([(-1,i),(0,i),(-1,-1),(0,-1)])

            for i in range(-1,3):
                if an[i][0]==1 and an[i][1]==1 and an[i][2]==1 and an[i][-1]==1:
                    qrd_ref.append([(i,0),(i,1),(i,2),(i,-1)])
                if an[0][i]==1 and an[1][i]==1 and an[2][i]==1 and an[-1][i]==1:
                    qrd_ref.append([(0,i),(1,i),(2,i),(-1,i)])

            for i in range(-1,3):
                for j in range(-1,3):
                    if an[i][j]==1 and an[i][j+1]==1 and an[i+1][j]==1 and an[i+1][j+1]==1:
                        if i==2 and j==2:
                            temp=[(i,j),(-1,j),(i,-1),(-1,-1)]
                        elif i==2 and j<2:
                            temp=[(i,j),(-1,j),(i,j+1),(-1,j+1)]
                        elif j==2 and i<2:
                            temp=[(i,j),(i+1,j),(i,-1),(i+1,-1)]
                        else:
                            temp=[(i,j),(i+1,j),(i,j+1),(i+1,j+1)]
                        qrd_ref.append(temp)
            
                
            for i in range(-1,3):
                if an[i][0]==1 and an[i][1]==1 and an[i][2]==1 and an[i][-1]==1:
                    if [(i,0),(i,1),(i,2),(i,-1)] not in octa:
                        op=op+qrd_val[1][i]
                        qrd.append([(i,0),(i,1)])
                        qrd.append([(i,1),(i,2)])
                        qrd.append([(i,2),(i,-1)])
                        qrd.append([(i,-1),(i,0)])

            for i in range(-1,3):
                if an[0][i]==1 and an[1][i]==1 and an[2][i]==1 and an[-1][i]==1:
                    if [(0,i),(1,i),(2,i),(-1,i)] not in octa:
                        op=op+qrd_val[0][i]
                        qrd.append([(0,i),(1,i)])
                        qrd.append([(1,i),(2,i)])
                        qrd.append([(2,i),(-1,i)])
                        qrd.append([(-1,i),(0,i)])

            for i in range(-1,3):
                for j in range(-1,3):
                    if an[i][j]==1 and an[i][j+1]==1 and an[i+1][j]==1 and an[i+1][j+1]==1:
                        if i==2 and j==2:
                            temp=[(i,j),(-1,j),(i,-1),(-1,-1)]
                        elif i==2 and j<2:
                            temp=[(i,j),(-1,j),(i,j+1),(-1,j+1)]
                        elif j==2 and i<2:
                            temp=[(i,j),(i+1,j),(i,-1),(i+1,-1)]
                        else:
                            temp=[(i,j),(i+1,j),(i,j+1),(i+1,j+1)]
                        if temp not in octa:
                            op=op+qrd_val_4[i][j]
                            if i<2 and j<2:
                                qrd.append([(i,j),(i,j+1)])
                                qrd.append([(i+1,j),(i+1,j+1)])
                                qrd.append([(i,j),(i+1,j)])
                                qrd.append([(i,j+1),(i+1,j+1)])
                            if j==2 and i<2:
                                qrd.append([(i,j),(i,-1)])
                                qrd.append([(i+1,j),(i+1,-1)])
                                qrd.append([(i,j),(i+1,j)])
                                qrd.append([(i,-1),(i+1,-1)])
                            if j<2 and i==2:
                                qrd.append([(i,j),(i,j+1)])
                                qrd.append([(-1,j),(-1,j+1)])
                                qrd.append([(i,j),(-1,j)])
                                qrd.append([(i,j+1),(-1,j+1)])
                            if i==2 and j==2:
                                qrd.append([(i,j),(i,-1)])
                                qrd.append([(-1,j),(-1,-1)])
                                qrd.append([(i,j),(-1,j)])
                                qrd.append([(i,-1),(-1,-1)])
                        
            for i in range(-1,3):
                for j in range(-1,3):
                    if an[i][j]==1 and an[i][j+1]==1:
                        if j==2:
                            temp=[(i,j),(i,-1)]
                        else:
                            temp=[(i,j),(i,j+1)]
                        if temp not in qrd:
                            op=op+dul_horz[i][j]
                            if j==2:
                                dul.append([(i,j),(i,-1)])
                            else:
                                dul.append([(i,j),(i,j+1)])
                    if an[i][j]==1 and an[i+1][j]==1:
                        if i==2:
                            temp=[(i,j),(-1,j)]
                        else:
                            temp=[(i,j),(i+1,j)]
                        if temp not in qrd:
                            op=op+dul_vert[i][j]
                            if i==2:
                                dul.append([(i,j),(-1,j)])
                            else:
                                dul.append([(i,j),(i+1,j)])

            for each in octa:
                sngl.extend(each)
            for each in qrd:
                sngl.extend(each)
            for each in dul:
                sngl.extend(each)
            for i in range(-1,3):
                for j in range(-1,3):
                    if an[i][j]==1:
                        if (i,j) not in sngl:
                            op=op+sngl_val[i][j]

            op=op.strip()
            opl=op.split(" ")
            for i in range(len(opl)):
                opl[i]=opl[i]+" "
        
            dulref=copy.deepcopy(dul)

            for each in dul:
                (d1,d2)=(each[0],each[1])
                (cntd1,cntd2)=(0,0)
                for each in dulref:
                    if d1 in each:
                        cntd1+=1
                    if d2 in each:
                        cntd2+=1
                for each in qrd_ref:
                    if d1 in each:
                        cntd1+=1
                    if d2 in each:
                        cntd2+=1   
                if cntd1>1 and cntd2>1:
                    try:
                        if d1[0]==d2[0]:
                            opl.remove(dul_horz[d1[0]][d1[1]])
                        if d1[1]==d2[1]:
                            opl.remove(dul_vert[d1[0]][d1[1]])
                        dulref.remove([(d1[0],d1[1]),(d2[0],d2[1])])
                    except ValueError:
                        continue
        
            for each in qrd_ref:
                (d1,d2,d3,d4)=(each[0],each[1],each[2],each[3])
                (d1cnt,d2cnt,d3cnt,d4cnt)=(0,0,0,0)
                for each1 in dul:
                    if d1 in each1:
                        d1cnt+=1
                    if d2 in each1:
                        d2cnt+=1
                    if d3 in each1:
                        d3cnt+=1
                    if d4 in each1:
                        d4cnt+=1
                for each2 in qrd_ref:
                    if each!=each2:
                        if d1 in each2:
                            d1cnt+=1
                        if d2 in each2:
                            d2cnt+=1
                        if d3 in each2:
                            d3cnt+=1
                        if d4 in each2:
                            d4cnt+=1
                if d1cnt>0 and d2cnt>0 and d3cnt>0 and d4cnt>0:
                    try:
                        if d1[0]!=d2[0] and d1[1]!=d3[1]:
                            opl.remove(qrd_val_4[d1[0]][d1[1]])
                    except ValueError:
                        continue

            for each in qrd_ref:
                (d1,d2,d3,d4)=(each[0],each[1],each[2],each[3])
                (d1cnt,d2cnt,d3cnt,d4cnt)=(0,0,0,0)
                for each1 in qrd_ref:
                    if each1!=each:
                        if d1 in each1:
                            d1cnt+=1
                        if d2 in each1:
                            d2cnt+=1
                        if d3 in each1:
                            d3cnt+=1
                        if d4 in each1:
                            d4cnt+=1
                    if d1cnt>0 and d2cnt>0 and d3cnt>0 and d4cnt>0:
                        try:
                            if d1[0]==d2[0]==d3[0]==d4[0]:
                                opl.remove(qrd_val[1][d1[0]])
                            elif d1[1]==d2[1]==d3[1]==d4[1]:
                                opl.remove(qrd_val[0][d1[1]])
                        except ValueError:
                            continue
                        
            op=''.join(opl)
        for _ in range(50):print("*",end='')
        print()
        op=op.strip(" ")
        if nip==1:
            op=op.replace(" "," + ")
        op=op.replace("A",pr_v[0])
        op=op.replace("B",pr_v[1])
        op=op.replace("C",pr_v[2])
        op=op.replace("D",pr_v[3])
        print("Simplified equation is :",op)

        for _ in range(50):print("*",end='')
        print()


    #K_Map for 3 inputs.
    def inp3_k_map(mt,nip):
        for i in range(50):print("-",end='')
        print()
        var_re=input("Enter variables with single space(A B C) : ").split(" ")
        ansg=[[0,0,0,0],[0,0,0,0]]
        ansgmx=[[0,0,0,0],[0,0,0,0]]
        op=''
        flag=0
        qrd=[]
        dul=[]
        sngl=[]
        if nip==1:
            qrd_var_2_2=["B' ","C ","B ","C' "]
            qrd_var_1_4=["A' ","A "]
            dul_vert=["B'C' ","B'C ","BC ","BC' "]
            dul_horz=[["A'B' ","A'C ","A'B ","A'C' "],["AB' ","AC ","AB ","AC'"]]
            sngl_val=[["A'B'C' ","A'B'C ","A'BC ","A'BC' "],["AB'C' ","AB'C ","ABC ","ABC' "]]
        elif nip==2:
            qrd_var_2_2=["(B) ","(C') ","(B') ","(C) "]
            qrd_var_1_4=["(A) ","(A') "]
            dul_vert=["(B+C) ","(B+C') ","(B'+C') ","(B'+C) "]
            dul_horz=[["(A+B) ","(A+C') ","(A+B') ","(A+C) "],["(A'+B) ","(A'+C') ","(A'+B') ","(A'+C) "]]
            sngl_val=[["(A+B+C) ","(A+B+C') ","(A+B'+C') ","(A+B'+C) "],["(A'+B+C) ","(A'+B+C') ","(A'+B'+C') ","(A'+B'+C) "]]
        for i in range(2):
            for j in range(4):
                p=int('0b'+bin(i)[2:]+bin(j)[2:],2)
                if (i==1) and (j==0 or j==1):
                    p=int('0b'+bin(i)[2:]+'0'+bin(j)[2:],2)
                if p in mt:
                    ansg[i][j]=1


        for i in range(2):
            (ansg[i][2],ansg[i][3])=(ansg[i][3],ansg[i][2])
        for i in range(50):print("-",end='')
        print()
        print("K-Map plotted : ")
        if nip==1:
            for each in ansg:print(*each)
        elif nip==2:
            for i in range(2):
                for j in range(4):
                    if ansg[i][j]==1:
                        ansgmx[i][j]=0
                    else:
                        ansgmx[i][j]=1
            for each in ansgmx:print(*each)

        if ansg==[[1]*4,[1]*4]:
            op=op+'1'
            flag=1
        if flag==0:
            for j in range(-1,3):
                if ansg[0][j]==1 and ansg[-1][j]==1 and ansg[0][j+1]==1 and ansg[-1][j+1]==1:
                    qrd.append([(0,j),(-1,j)])
                    if j<2:
                        qrd.append([(0,j+1),(-1,j+1)])
                        qrd.append([(0,j),(0,j+1)])
                        qrd.append([(-1,j),(-1,j+1)])
                    else:
                        qrd.append([(0,-1),(-1,-1)])
                        qrd.append([(0,j),(0,-1)])
                        qrd.append([(-1,j),(-1,-1)])
                    op=op+qrd_var_2_2[j]
        if flag==0:
            for i in range(-1,1):
                if ansg[i]==[1,1,1,1]:
                    qrd.append([(i,-1),(i,0)])
                    qrd.append([(i,0),(i,1)])
                    qrd.append([(i,1),(i,2)])
                    qrd.append([(i,2),(i,-1)])
                    op=op+qrd_var_1_4[i]
        if flag==0:
            for j in range(-1,3):
                if ansg[0][j]==1 and ansg[1][j]==1:
                    temp=0
                    if [(0,j),(-1,j)] in qrd:
                        temp=1
                    elif [(-1,j),(0,j)] in qrd:
                        temp=1
                    if temp==0:
                        dul.append([(0,j),(-1,j)])
                        op=op+dul_vert[j]
                    
        if flag==0:
            for i in range(-1,1):
                for j in range(-1,3):
                    if ansg[i][j]==1 and ansg[i][j+1]==1:
                        temp=0
                        if j==2:
                            if [(i,j),(i,-1)] in qrd:
                                temp=1
                            elif [(i,-1),(i,j)] in qrd:
                                temp=1
                        else:
                            if [(i,j),(i,j+1)] in qrd:
                                temp=1
                            elif [(i,j+1),(i,j)] in qrd:
                                temp=1
                        if temp==0:
                            if j==2:
                                dul.append([(i,2),(i,-1)])
                            else:
                                dul.append([(i,j),(i,j+1)])
                            op=op+dul_horz[i][j]

        op=op.rstrip(" ")
        opl=op.split(" ")
        for i in range(len(opl)):
            opl[i]=opl[i]+" "
        
        for each in dul:
            d1cnt=0
            d2cnt=0
            (d1,d2)=(each[0],each[1])
            for each1 in dul:
                if d1 in each1:
                    d1cnt+=1
                if d2 in each1:
                    d2cnt+=1
            if d1cnt>1 and d2cnt>1:
                (d1i,d1j)=d1
                (d2i,d2j)=d2
                if d1i==d2i:
                    p=dul_horz[d1i][d1j]
                    opl.remove(p)
                else:
                    p=dul_vert[d1j]
                    opl.remove(p)
                dul.remove([d1,d2])
        op="".join(opl)

        for _ in qrd:
            for each in _:
                sngl.append(each)
        for _ in dul:
            for each in _:
                sngl.append(each)

        if flag==0:
            for i in range(-1,1):
                for j in range(-1,3):
                    if ansg[i][j]==1:
                        if (i,j) not in sngl:
                            op=op+sngl_val[i][j]

        op=op.rstrip(" ")
        if nip==1:
            op=op.replace(' ',' + ')

        op=op.replace("A",var_re[0])
        op=op.replace("B",var_re[1])
        op=op.replace("C",var_re[2])
        for i in range(50):print("*",end='')
        print()
        print("The simplified equation is :",op)
        for i in range(50):print("*",end='')
        print()

    #main
    ask='y'
    while ask=='y':
        for _ in range(50):print("-",end='')
        print()
        mimastr=input("Enter 'SOP' for SOP(Minterms) or 'POS' for POS(Maxterms) : ").lower()
        if mimastr=='pos':
            mima=2
        elif mimastr=='sop':
            mima=1
        if mima==1:
            mt=list(map(int,input("Enter Minterms : ").split()))
        else:
            mt=list(map(int,input("Enter Maxterms : ").split()))
        if nfinp==2:
            inp2_k_map(mt,mima)
        elif nfinp==3:
            inp3_k_map(mt,mima)
        elif nfinp==4:
            inp4_k_map(mt,mima)
        else:
            print("You committed some mistake, please check the inputs next time.")
        ask=input("Enter 'y' for another K-Map or 'n' to exit : ").lower()
        for i in range(25):print("--",end='')
        print()
elif (4 < nfinp < 9) or eq == 2:
    # Quine McCluskey algorithm for minimizing logical expressions
    # Author: Suman Adhikari

    def mul(x,y): # Multiply 2 minterms
        res = []
        for i in x:
            if i+"'" in y or (len(i)==2 and i[0] in y):
                return []
            else:
                res.append(i)
        for i in y:
            if i not in res:
                res.append(i)
        return res

    def multiply(x,y): # Multiply 2 expressions
        res = []
        for i in x:
            for j in y:
                tmp = mul(i,j)
                res.append(tmp) if len(tmp) != 0 else None
        return res

    def refine(my_list,dc_list): # Removes don't care terms from a given list and returns refined list
        res = []
        for i in my_list:
            if int(i) not in dc_list:
                res.append(i)
        return res

    def findEPI(x): # Function to find essential prime implicants from prime implicants chart
        res = []
        for i in x:
            if len(x[i]) == 1:
                res.append(x[i][0]) if x[i][0] not in res else None
        return res

    def findVariables(x): # Function to find variables in a meanterm. For example, the minterm --01 has C' and D as variables
        var_list = []
        for i in range(len(x)):
            if x[i] == '0':
                var_list.append(chr(i+65)+"'")
            elif x[i] == '1':
                var_list.append(chr(i+65))
        return var_list

    def flatten(x): # Flattens a list
        flattened_items = []
        for i in x:
            flattened_items.extend(x[i])
        return flattened_items

    def findminterms(a): #Function for finding out which minterms are merged. For example, 10-1 is obtained by merging 9(1001) and 11(1011)
        gaps = a.count('-')
        if gaps == 0:
            return [str(int(a,2))]
        x = [bin(i)[2:].zfill(gaps) for i in range(pow(2,gaps))]
        temp = []
        for i in range(pow(2,gaps)):
            temp2,ind = a[:],-1
            for j in x[0]:
                if ind != -1:
                    ind = ind+temp2[ind+1:].find('-')+1
                else:
                    ind = temp2[ind+1:].find('-')
                temp2 = temp2[:ind]+j+temp2[ind+1:]
            temp.append(str(int(temp2,2)))
            x.pop(0)
        return temp

    def compare(a,b): # Function for checking if 2 minterms differ by 1 bit only
        c = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                mismatch_index = i
                c += 1
                if c>1:
                    return (False,None)
        return (True,mismatch_index)

    def removeTerms(_chart,terms): # Removes minterms which are already covered from chart
        for i in terms:
            for j in findminterms(i):
                try:
                    del _chart[j]
                except KeyError:
                    pass

    mt = [int(i) for i in input("Enter the minterms: ").strip().split()]
    dc = [int(i) for i in input("Enter the don't cares(If any): ").strip().split()]
    mt.sort()
    minterms = mt+dc
    minterms.sort()
    size = len(bin(minterms[-1]))-2
    groups,all_pi = {},set()

    # Primary grouping starts
    for minterm in minterms:
        try:
            groups[bin(minterm).count('1')].append(bin(minterm)[2:].zfill(size))
        except KeyError:
            groups[bin(minterm).count('1')] = [bin(minterm)[2:].zfill(size)]
    # Primary grouping ends

    #Primary group printing starts
    print("\n\n\n\nGroup No.\tMinterms\tBinary of Minterms\n%s"%('='*50))
    for i in sorted(groups.keys()):
        print("%5d:"%i) # Prints group number
        for j in groups[i]:
            print("\t\t    %-20d%s"%(int(j,2),j)) # Prints minterm and its binary representation
        print('-'*50)
    #Primary group printing ends

    # Process for creating tables and finding prime implicants starts
    while True:
        tmp = groups.copy()
        groups,m,marked,should_stop = {},0,set(),True
        l = sorted(list(tmp.keys()))
        for i in range(len(l)-1):
            for j in tmp[l[i]]: # Loop which iterates through current group elements
                for k in tmp[l[i+1]]: # Loop which iterates through next group elements
                    res = compare(j,k) # Compare the minterms
                    if res[0]: # If the minterms differ by 1 bit only
                        try:
                            groups[m].append(j[:res[1]]+'-'+j[res[1]+1:]) if j[:res[1]]+'-'+j[res[1]+1:] not in groups[m] else None # Put a '-' in the changing bit and add it to corresponding group
                        except KeyError:
                            groups[m] = [j[:res[1]]+'-'+j[res[1]+1:]] # If the group doesn't exist, create the group at first and then put a '-' in the changing bit and add it to the newly created group
                        should_stop = False
                        marked.add(j) # Mark element j
                        marked.add(k) # Mark element k
            m += 1
        local_unmarked = set(flatten(tmp)).difference(marked) # Unmarked elements of each table
        all_pi = all_pi.union(local_unmarked) # Adding Prime Implicants to global list
        print("Unmarked elements(Prime Implicants) of this table:",None if len(local_unmarked)==0 else ', '.join(local_unmarked)) # Printing Prime Implicants of current table
        if should_stop: # If the minterms cannot be combined further
            print("\n\nAll Prime Implicants: ",None if len(all_pi)==0 else ', '.join(all_pi)) # Print all prime implicants
            break
        # Printing of all the next groups starts
        print("\n\n\n\nGroup No.\tMinterms\tBinary of Minterms\n%s"%('='*50))
        for i in sorted(groups.keys()):
            print("%5d:"%i) # Prints group number
            for j in groups[i]:
                print("\t\t%-24s%s"%(','.join(findminterms(j)),j)) # Prints minterms and its binary representation
            print('-'*50)
        # Printing of all the next groups ends
    # Process for creating tables and finding prime implicants ends


    # Printing and processing of Prime Implicant chart starts
    sz = len(str(mt[-1])) # The number of digits of the largest minterm
    chart = {}
    print('\n\n\nPrime Implicants chart:\n\n    Minterms    |%s\n%s'%(' '.join((' '*(sz-len(str(i))))+str(i) for i in mt),'='*(len(mt)*(sz+1)+16)))
    for i in all_pi:
        merged_minterms,y = findminterms(i),0
        print("%-16s|"%','.join(merged_minterms),end='')
        for j in refine(merged_minterms,dc):
            x = mt.index(int(j))*(sz+1) # The position where we should put 'X'
            print(' '*abs(x-y)+' '*(sz-1)+'X',end='')
            y = x+sz
            try:
                chart[j].append(i) if i not in chart[j] else None # Add minterm in chart
            except KeyError:
                chart[j] = [i]
        print('\n'+'-'*(len(mt)*(sz+1)+16))
    # Printing and processing of Prime Implicant chart ends

    EPI = findEPI(chart) # Finding essential prime implicants
    print("\nEssential Prime Implicants: "+', '.join(str(i) for i in EPI))
    removeTerms(chart,EPI) # Remove EPI related columns from chart

    if(len(chart) == 0): # If no minterms remain after removing EPI related columns
        final_result = [findVariables(i) for i in EPI] # Final result with only EPIs
    else: # Else follow Petrick's method for further simplification
        P = [[findVariables(j) for j in chart[i]] for i in chart]
        while len(P)>1: # Keep multiplying until we get the SOP form of P
            P[1] = multiply(P[0],P[1])
            P.pop(0)
        final_result = [min(P[0],key=len)] # Choosing the term with minimum variables from P
        final_result.extend(findVariables(i) for i in EPI) # Adding the EPIs to final solution
    print('\n\nSolution: F = '+' + '.join(''.join(i) for i in final_result))

    input("\nPress enter to exit...")
else:
    print("ERROR")
