class coveraged_file():
    def __init__(self):
        pass
    def mult(self,a:int,b:int,c:int=1)->int:
        if(c>1):
            return 0
        if(a>b>c):
            return a*b*c
        if(b>a):
            raise RuntimeError("a > b")

