import io
import os

fdir="wordlists/"

fnames=os.listdir(fdir)

for fname in fnames:
	print(fname)
	words=io.open("{}/{}".format(fdir,fname),"r",encoding="utf8").read().splitlines()
	out = io.open("wordlists_processed/{}".format(fname.replace("Name","")),"w+",encoding="utf8")
	out.write("\n".join(sorted(list(set(words)))).lower())