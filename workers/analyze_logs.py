#!/usr/bin/env python

expected_max = 99
log_file = '/var/log/celery/worker.log'
strip_text = 'Completed task test_sleep with int '

lines = []
with open(log_file, 'r') as f:
    for line in f:
        if strip_text in line:
            clean_line = line.replace(strip_text, '')
            clean_line = clean_line.replace('\n', '')
            try:
                lines.append(int(clean_line))
            except:
                pass

lines.sort()
# slow
for i in range(expected_max+1):
    if i not in lines:
        print "missing {} in log".format(i)

# fase
# for i in range(len(lines)):
#     if lines[i] != i:
#         print "missing {} in log".format(i)
#         break

print lines
