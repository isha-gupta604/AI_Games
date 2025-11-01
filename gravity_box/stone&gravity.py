def gravity(mat):
    m,n=len(mat),len(mat[0])
    for i in range(n):
        col=0
        for j in range(m):
            if mat[j][i]=='*':
                col+=1
        row=m-1
        for k in range(col):
            mat[row][i]='*'
            row-=1
        while row>=0:
            mat[row][i]='.'
            row-=1
    return mat

def rotate(mat,dir):
    m,n=len(mat)-1,len(mat[0])-1
    ans=[]
    if dir.lower()=='right':
        for i in range(n+1):
            lis=[]
            for j in range(m,-1,-1):
                lis.append(mat[j][i])
            ans.append(lis)
    elif dir.lower()=='left':
        for i in range(n,-1,-1):
            lis=[]
            for j in range(m+1):
                lis.append(mat[j][i])
            ans.append(lis)
    return (ans)

m,n=map(int, input('enter rows & column number: ').split())
mat=list()
print("Provide description of the box\n'*' represents stone and '.' represents space")
for i in range(m):
    lis=input(f"row {i+1}: ").split()
    mat.append(lis)
k=int(input(" No. of rotations: "))
print("Enter directions for rotation")
steps=[]
for i in range(k):
    steps.append(input(f'direction {i+1}: '))
ans=gravity(mat)
print("\nGiven box after application of gravity:")
for i in ans:
    print(i)
for i in steps:
    ans=rotate(ans,i)
    ans=gravity(ans)
    print(f"\n After {i} Rotation:")
    for i in ans:
        print(i)
