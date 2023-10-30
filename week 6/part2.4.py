

txt = "This is a line"
txt = txt.lower()
lst={}
for ch in txt:
    c=txt.count(ch)
    lst.update({ch:c})
print (list(lst.items()))
