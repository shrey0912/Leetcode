class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        d={'L':0,'U':0,'D':0,'S':0}
        if len(password)<8:
            return False
        for i in range(len(password)):
            if i==0:
                if(password[i].isupper()):
                    d['U']+=1
                if(password[i].islower()):
                    d['L']+=1
                if(password[i].isdigit()):
                    d['D']+=1
                if password[i] in '!@#$%^&*()-+':
                    d['S']+=1
            else:
                if password[i]==password[i-1]:
                    return False
                else:
                    if(password[i].isupper()):
                        d['U']+=1
                    if(password[i].islower()):
                        d['L']+=1
                    if(password[i].isdigit()):
                        d['D']+=1
                    if password[i] in '!@#$%^&*()-+':
                        d['S']+=1
        for k,v in d.items():
            if d[k]==0:
                return False
        return True
