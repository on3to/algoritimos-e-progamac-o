def cal_preço(p1 ,p2, p3):
    
    if p1 < p2 and p1 < p3:
        return ("o primeiro produto e mais barato")
    elif p2 < p1 and p2 < p3:
        return ("o segundo produto e mais barato")
    else:
        return("o terciro produto e mais barato") 