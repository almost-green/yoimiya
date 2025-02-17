import re
text = 'one, two...ten'
re1=re.split('[,. ]+', text)
print(re1)
#re1=re.split('[,. ]+', text, maxsplit=1)
#print(re1)
