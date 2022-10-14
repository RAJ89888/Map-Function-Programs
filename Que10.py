StringVal={"Raj":"vohera","JAY":"shah"}
ans=map(lambda x:(x[0].lower(),x[1]+"@gmail.com"),StringVal.items())
print(dict(ans))