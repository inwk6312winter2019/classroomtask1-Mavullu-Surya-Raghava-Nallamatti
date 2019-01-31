def nestedcapitalize(l):
    res=[]
    for i in l:
        if type(i) is list:
            i = nestedcapitalize(i)
        else:
            i = i.capitalize()  
        res.append(i)
    return(res)




print(nestedcapitalize([['baLli','kali'],'Bhsd',['thali']]))

