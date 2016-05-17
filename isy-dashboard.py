from flask import Flask, abort, request, render_template, redirect
from xml.etree import ElementTree
import requests, time, definitions

app = Flask(__name__)

isy_rest_address = definitions.ISYADDRESS
isy_admin = definitions.ISYADMIN
isy_pwd = definitions.ISYPASSWORD
sleep = .25

@app.before_request
def limit_remote_addr():
	if '10.0.0.' not in request.remote_addr:
                if '10.10.0.' not in request.remote_addr:
                        abort(404)

@app.route('/')
@app.route('/index/')
def index():
	return 'Home page'

@app.route('/isy/')
def root():
	return render_template('isy_root.html')

@app.route('/isy/<group>/')
def specific_group(group):
        nodes = get_nodes(group)
	if not nodes:
		abort(404)

        nodeStatus = {}
	for switch in nodes:
                nodeStatus[switch.name] = get_status(switch)
        
	return render_template('isy_' + group + '.html',status=nodeStatus)

@app.route('/isy/<group>/all_off/')
def all_off(group):
        nodes = get_nodes(group)
        if not nodes:
                # Would like to display an error message to the user here
                return redirect('/isy/' + group + '/', code = 302)

        for switch in nodes:
                light_off(switch)

        time.sleep(sleep)
        return redirect('/isy/' + group + '/', code = 302)

@app.route('/isy/<group>/all_on/')
def all_on(group):
        nodes = get_nodes(group)
        if not nodes:
                # Would like to display an error message to the user here
                return redirect('/isy/' + group + '/', code = 302)

        for switch in nodes:
                light_on(switch)

        time.sleep(sleep)
        return redirect('/isy/' + group + '/', code = 302)

@app.route('/isy/<group>/<name>/toggle/')
def toggle(group, name):
        nodes = get_nodes(group)
        if not nodes:
                # Would like to display an error message to the user here
                return redirect('/isy/' + group + '/', code = 302)

        for switch in nodes:
                if switch.name == name:
                        if get_status(switch) == 'On':
                                light_off(switch)
                        else:
                                light_on(switch)

        time.sleep(sleep)
        return redirect('/isy/' + group + '/', code = 302)

# The if/elif statements will need to be updated to use the group names called by your html toggle function
def get_nodes(group):
        """Return a list of switchObj objects

        Argument:
        group -- the name as listed in definitions.py of the group of switches"""
        
        # UPDATE ME
        # Update the text between single quotes to the group names used in your .html
        # Update the name following "definitions." to the name of the group in your definitions.py file
        if group == 'first':
                return definitions.FIRST_FLOOR
        elif group == 'outside':
                return definitions.OUTSIDE
        else:
                return None

def light_off(switch):
        """Sends the off command to the address of the passed in switchObj"""
        requests.get(isy_rest_address+'/nodes/'+switch.address+'/cmd/DOF/',auth=(isy_admin,isy_pwd))
        if switch.slave:
                light_off(switch.slave)
                
def light_on(switch):
        """Sends the on command to the address of the passed in switchObj"""
        requests.get(isy_rest_address+'/nodes/'+switch.address+'/cmd/DON/',auth=(isy_admin,isy_pwd))
        if switch.slave:
                light_on(switch.slave)

def get_status(switch):
        """Returns the formatted status from ISY of the switchObj passed in"""
	nodeXml = requests.get(isy_rest_address+'nodes/'+switch.address,auth=(isy_admin,isy_pwd))	
	nodeData = ElementTree.fromstring(nodeXml.content)
	for prop in nodeData.findall('properties'):
		return prop[2].attrib['formatted']
        

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')
