import os

port = input("AX.25 port name: ")
callsign = input("Callsign: ")
grid = input("Grid square: ")


dest_call = "QST"
digipeaters = ""


cmd = ""

while cmd != 'q':
	cmd = input("(c)q, send (m)essage, set (d)estination call, send (l)ocation, set digi(p)eater chain, (r)st, (7)3, (q)uit \n")[0]
	if cmd == 'c':
		os.system('beacon -s -d "' + dest_call + ' ' + digipeaters + '" ' + port + ' "CQ de ' + callsign + '"')
	if cmd == 'm':
		os.system('beacon -s -d "' + dest_call + ' ' + digipeaters + '" ' + port + ' "' + input() + '"')
	if cmd == 'd':
		dest_call = input()
	if cmd == 'l':
		os.system('beacon -s -d "' + dest_call + ' ' + digipeaters + '" ' + port + ' "my QTH is ' + grid + '"')
	if cmd == 'p':
		digipeaters = input()
	if cmd == 'r':
		os.system('beacon -s -d "' + dest_call + ' ' + digipeaters + '" ' + port + ' "ur ' + input() + " into " + grid + '"')
	if cmd == '7':
		os.system('beacon -s -d "' + dest_call + ' ' + digipeaters + '" ' + port + ' "73, Tnx for QSO"')
