from gurobipy import *
m=Model('OR')

def main():
    StartCons=(0,0,12,35,15)
    EndCons=(24,30,30,39,45)
    miniCons=(15,20,1,3,25)
    S={}
    E={}
    for i in range(5):
        S[i]=m.addVar(vtype=GRB.INTEGER,name='S%d'%i)
        E[i]=m.addVar(vtype=GRB.INTEGER,name='E%d'%i)
    for i in  range(5):
        m.addConstr(E[i]-S[i]==miniCons[i],"cmini")
        m.addConstr(E[i]<=EndCons[i],"endcons")
        m.addConstr(S[i]>=StartCons[i],"startcons")
    m.addConstr( S[1]>=S[0]+7   ,"cons2")
    m.addConstr( S[2]>=E[0]+5   ,"cons3")
    m.addConstr( S[3]>=E[2]     ,"cons4")
    m.addConstr( S[4]>=E[0]     ,"cons5")
    
    m.setObjective(E[4],GRB.MINIMIZE)
    m.optimize()
    V = m.getVars()
    for i in [0,2,4,6,8]:
        print("第 %d 項作業: 第%d天 -> 第%d天"%(i/2+1,V[i].x,V[i+1].x))
    print ("最佳化目標值: %d 天"%m.objVal)






if __name__ == '__main__':
    main()