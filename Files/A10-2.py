#fname = input("Enter file name:")
#if fname < 1 : fname = "mbox-short.txt"
fname = "mbox-short.txt"
fhandle = open(fname, "r")

all_emails_byhour = dict()
for line in fhandle :
    if not line.startswith("From"): continue
    words = line.split()
    if words[0] == "From:" : continue
    time_sent = words[5]
    hour_part = time_sent[:time_sent.find(":")]
    all_emails_byhour[hour_part] = all_emails_byhour.get(hour_part,0) + 1

tmp = list()
tmp = sorted(all_emails_byhour.items())

for k,v in tmp:
    print(k,v)
