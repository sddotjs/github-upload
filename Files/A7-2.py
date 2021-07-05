fname = input("Enter file name: ")
fhandle = open(fname,"r")
count = 0
total_confidence_val = 0.0
for line in fhandle:
    if line.startswith("X-DSPAM-Confidence:") :
        count = count + 1
        confidence_val_str = line[line.find(":") + 1:]
        confidence_val_str = confidence_val_str.strip()
        try:
            confidence_val_float = float(confidence_val_str)
        except:
            print("Non-number found for Confidence Value at line", count)
        total_confidence_val = total_confidence_val + confidence_val_float

print("Average spam confidence:",total_confidence_val/count)
