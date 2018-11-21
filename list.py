l1=['a', 'b', 'c']
l2=['b','d']
common=[x for x in l1 if x in l2]
print("common elements between l1 and l2",common)
diff=[x for x in l1 if x not in l2]
print("elements present in l1 not in l2",diff)
