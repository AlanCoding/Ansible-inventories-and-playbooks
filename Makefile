netcat:
	nc -l 8099

sim:
	python simulate.py

timeout-sim:
	time ansible-playbook -i host/python -u arominger playbook/ping.yml --timeout 1
