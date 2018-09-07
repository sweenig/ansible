import ast, os, re
from pprint import pprint

bcolors = {
  "HEADER" : '\033[95m',
  "OKBLUE" : '\033[94m',
  "OKGREEN" : '\033[92m',
  "WARNING" : '\033[93m',
  "FAIL" : '\033[91m',
  "ENDC" : '\033[0m',
  "BOLD" : '\033[1m',
  "UNDERLINE" : '\033[4m'
}

def colorprint(msg1, c1="ENDC", msg2="", c2="ENDC", s=' '):
  if c1 not in bcolors.keys():
    print("Invalid color: %s does not exist" % c1)
  if c2 not in bcolors.keys():
    print("Invalid color: %s does not exist" % c2)
  if c1 in bcolors.keys() and c2 in bcolors.keys():
    print(bcolors[c1] + msg1 + bcolors["ENDC"] + s + bcolors[c2] + msg2 + bcolors["ENDC"])
  

file_list = os.listdir('outputfiles')
compare_list = []
for file in file_list:
  m=re.match('(.*)\.pre.*',file)
  if bool(m):
    compare_list.append(('outputfiles/' + m.group(1) + '.precrqdetails.py','outputfiles/' + m.group(1) + '.postcrqdetails.py'))
for pair in compare_list:
  with open(pair[0]) as f:
    flist=ast.literal_eval(f.read())
  with open(pair[1]) as d:
    dlist=ast.literal_eval(d.read())

    i = 0
    fn = []
    for i in range(len(flist[2])):
      if flist[2][i][:4]!='Devi' and len(flist[2][i])!=0 and flist[2][i][:4]!='Capa' and flist[2][i][:1]!=' ' and flist[2][i][:4]!='Tota':
        fn.append([flist[2][i]] + flist[2][i+1].split())
        i += 1
      i += 1

    i = 0
    dn = []
    for i in range(len(dlist[2])):
      if dlist[2][i][:4]!='Devi' and len(dlist[2][i])!=0 and dlist[2][i][:4]!='Capa' and dlist[2][i][:1]!=' ' and dlist[2][i][:4]!='Tota':
        dn.append([dlist[2][i]] + dlist[2][i+1].split())
        i += 1
      i += 1

    for f,d in zip(fn,dn):
      if f[0]==d[0] and f[1]==d[1] and f[2]==d[2] and f[-3]==d[-3] and f[-2]==d[-2] and f[-1]==d[-1]:
        neighbor_plain = pair + (f[0],f[1],f[2],f[-3],f[-2],f[-1])
        colorprint('OK:', 'OKGREEN', '%s neighbors match %s (%s %s%s to %s %s%s)' % neighbor_plain, 'OKBLUE')
      else:
        colorprint('BAD:', 'WARNING', '%s\'s neighbors do not match %s\'s' % pair, 'FAIL')
        pprint(fn)
        pprint(dn)

    if flist[3] == dlist[3]:
      colorprint('OK:', 'OKGREEN', '%s\'s interfaces match %s\'s' % pair, 'OKBLUE')
    else:
      colorprint('BAD:', 'WARNING', '%s\'s interfaces do not match %s\'s' % pair, 'FAIL')
      pprint(flist[3])
      pprint(dlist[3])

    if flist[5] == dlist[5]:
      colorprint('OK:', 'OKGREEN', '%s\'s keys match %s\'s' % pair, 'OKBLUE')
    else:
      colorprint('BAD:', 'WARNING', '%s\'s keys do not match %s\'s' % pair, 'FAIL')
      pprint(flist[5])
      pprint(dlist[5])

    print('\n' * 1)

