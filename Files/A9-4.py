#fname = input("Enter file name:")
#if fname < 1 : fname = "mbox-short.txt"
fname = "mbox-short.txt"
fhandle = open(fname,"r")

all_emails = dict()
for line in fhandle :
    if not line.startswith("From") : continue
    words = line.split()
    if words[0] == "From:" : continue
    sender = words[1]
    all_emails[sender] = all_emails.get(sender,0) + 1

most_sender = None
most_emails_sent_count = None
for sender, emails_sent_count in all_emails.items() :
    if most_sender is None :
        most_sender = sender
        most_emails_sent_count = emails_sent_count
    else :
        if emails_sent_count > most_emails_sent_count :
            most_sender = sender
            most_emails_sent_count = emails_sent_count

print(most_sender,most_emails_sent_count)
