import io
from random import choice

def open_wl(fpath):
	return io.open(fpath,mode="r",encoding="utf8").read().splitlines()

def cap_first(s):
	return s[0].upper() + s[1:]

def generate_composed_word(N,subwords,sep=""):
	subword_vec=[]
	for subword in subwords:
		subword_vec.append(subword)
	for _ in range(N):
		print(cap_first(sep.join([choice(sw) for sw in subword_vec])))

def get_fpath(fdir,fname):
	return "{}/{}".format(fdir,fname)



N=10
fdir = "wordlists/AL"

boss1 =open_wl(get_fpath(fdir,"Boss_SW1.txt"))
boss2 =open_wl(get_fpath(fdir,"Boss_SW2.txt"))
boss3 =open_wl(get_fpath(fdir,"Boss_SW3.txt"))

generate_composed_word(N,(boss1,boss2,boss3))

btown1 =open_wl(get_fpath(fdir,"BritishTown_SW1.txt"))
btown2 =open_wl(get_fpath(fdir,"BritishTown_SW2.txt"))

generate_composed_word(N,(btown1,btown2))

atown1 =open_wl(get_fpath(fdir,"AmericanTown_SW1.txt"))
atown2 =open_wl(get_fpath(fdir,"AmericanTown_SW2.txt"))

generate_composed_word(N,(atown1,atown2))

tech1 =open_wl(get_fpath(fdir,"TechPrefixes.txt"))
tech2 =open_wl(get_fpath(fdir,"TechSuffixes.txt"))

generate_composed_word(N,(tech1,tech2))

fdir = "wordlists/EN"

perso = open_wl(get_fpath(fdir,"PersonalityAdjective.txt"))
concepts = open_wl(get_fpath(fdir,"PhilosophicalConcepts.txt"))
ideo = open_wl(get_fpath(fdir,"IdeologiesAdjectives.txt"))
music = open_wl(get_fpath(fdir,"MusicTypes.txt"))

generate_composed_word(N,(["the"],perso,concepts,["of"],ideo,music),sep=" ")