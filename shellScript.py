import subprocess
# ba = dir(subprocess)
# print ba

threeDall = subprocess.Popen(['dnwho', '-v', 'boswell3d'],stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].splitlines()
twoDall = subprocess.Popen(['dnwho', '-v', 'boswell2d'],stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].splitlines()

workstations = ['7910:','7610:','7600:','HP-Z:']

threeDfarm = [line for line in threeDall for ws in workstations if ws in line]
twoDfarm = [line for line in twoDall for ws in workstations if ws in line]

print '\n'+str.upper('3D Crew with Workstations that can be used on Farm')+'\n'
print '\n'.join(threeDfarm)+'\n\n'
print str.upper('2D Crew with Workstations that can be used on Farm')+'\n'
print '\n'.join(twoDfarm)+'\n'
