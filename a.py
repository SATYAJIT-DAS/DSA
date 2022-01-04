a = list(map(int, input().strip().split()))[:3]
s = input()
# ac, bc, cc = 0

while s > 0 and s<= 1000000:
    p1, p2 = input().split()
    swapCounter(p1,p2)
    

def swapCounter(p1, p2):
    if 1 <= p1 and p2 <= 3 and p1 != p2:
        
            
            
