#!/usr/bin/env python3
# Usage ./edgeswitch_sfp_information.py IPADDRESS USUARIO SENHA PORTASSH

from __future__ import print_function
import traceback
import paramiko
from paramiko_expect import SSHClientInteraction
import re
import json
import sys

def main():
    # Set login credentials and the server prompt
    HOSTNAME = sys.argv[1]
    USERNAME = sys.argv[2]
    PASSWORD = sys.argv[3]
    PORTA = sys.argv[4]
    HOSTNAME_FILE = HOSTNAME.replace(".","_")
    PROMPT = '>'
    REGULAR_EXPRESSION = '(^0/.*)'
    SFP_DATA = ["SFP_INDEX", "TEMPERATURA", "VOLTAGEM", "CORRENTE", "TX-POWER", "RX-POWER", "TX-FAULT", "LOS"]

    # Use SSH client to login
    try:
        # Create a new SSH client object
        client = paramiko.SSHClient()

        # Set SSH key parameters to auto accept unknown hosts
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the host
        client.connect(hostname=HOSTNAME, username=USERNAME, password=PASSWORD, port=PORTA)

        # Create a client interaction class which will interact with the host
        with SSHClientInteraction(client, timeout=10, display=False, buffer_size=4096) as interact:
            interact.expect(PROMPT, default_match_prefix='.*')

            # Run the first command and capture the cleaned output, if you want
            # the output without cleaning, simply grab CORRENTE_output instead.
            interact.send('show fiber-ports optics 0/1')
            interact.expect(PROMPT, default_match_prefix='.*')
            sfp1 = interact.current_output_clean
            sfp1 = sfp1.replace("N/A", "0")
            sfp1 = sfp1.replace("No", "0")
            sfp1 = sfp1.replace("Yes", "1")

            interact.send('show fiber-ports optics 0/2')
            interact.expect(PROMPT, default_match_prefix='.*')
            sfp2 = interact.current_output_clean
            sfp2 = sfp2.replace("N/A", "0")
            sfp2 = sfp2.replace("No", "0")
            sfp2 = sfp2.replace("Yes", "1")

            interact.send('show fiber-ports optics 0/3')
            interact.expect(PROMPT, default_match_prefix='.*')
            sfp3 = interact.current_output_clean
            sfp3 = sfp3.replace("N/A", "0")
            sfp3 = sfp3.replace("No", "0")
            sfp3 = sfp3.replace("Yes", "1")

            interact.send('show fiber-ports optics 0/4')
            interact.expect(PROMPT, default_match_prefix='.*')
            sfp4 = interact.current_output_clean
            sfp4 = sfp4.replace("N/A", "0")
            sfp4 = sfp4.replace("No", "0")
            sfp4 = sfp4.replace("Yes", "1")

            interact.send('show fiber-ports optics 0/5')
            interact.expect(PROMPT, default_match_prefix='.*')
            sfp5 = interact.current_output_clean
            sfp5 = sfp5.replace("N/A", "0")
            sfp5 = sfp5.replace("No", "0")
            sfp5 = sfp5.replace("Yes", "1")

            interact.send('show fiber-ports optics 0/6')
            interact.expect(PROMPT, default_match_prefix='.*')
            sfp6 = interact.current_output_clean
            sfp6 = sfp6.replace("N/A", "0")
            sfp6 = sfp6.replace("No", "0")
            sfp6 = sfp6.replace("Yes", "1")

            interact.send('show fiber-ports optics 0/7')
            interact.expect(PROMPT, default_match_prefix='.*')
            sfp7 = interact.current_output_clean
            sfp7 = sfp7.replace("N/A", "0")
            sfp7 = sfp7.replace("No", "0")
            sfp7 = sfp7.replace("Yes", "1")

            interact.send('show fiber-ports optics 0/8')
            interact.expect(PROMPT, default_match_prefix='.*')
            sfp8 = interact.current_output_clean
            sfp8 = sfp8.replace("N/A", "0")
            sfp8 = sfp8.replace("No", "0")
            sfp8 = sfp8.replace("Yes", "1")

            interact.send('show fiber-ports optics 0/9')
            interact.expect(PROMPT, default_match_prefix='.*')
            sfp9 = interact.current_output_clean
            sfp9 = sfp9.replace("N/A", "0")
            sfp9 = sfp9.replace("No", "0")
            sfp9 = sfp9.replace("Yes", "1")

            interact.send('show fiber-ports optics 0/10')
            interact.expect(PROMPT, default_match_prefix='.*')
            sfp10 = interact.current_output_clean
            sfp10 = sfp10.replace("N/A", "0")
            sfp10 = sfp10.replace("No", "0")
            sfp10 = sfp10.replace("Yes", "1")

            interact.send('show fiber-ports optics 0/11')
            interact.expect(PROMPT, default_match_prefix='.*')
            sfp11 = interact.current_output_clean
            sfp11 = sfp11.replace("N/A", "0")
            sfp11 = sfp11.replace("No", "0")
            sfp11 = sfp11.replace("Yes", "1")

            interact.send('show fiber-ports optics 0/12')
            interact.expect(PROMPT, default_match_prefix='.*')
            sfp12 = interact.current_output_clean
            sfp12 = sfp12.replace("N/A", "0")
            sfp12 = sfp12.replace("No", "0")
            sfp12 = sfp12.replace("Yes", "1")


            # Send the exit command and expect EOF (a cLOSed session)
            interact.send('quit')
            interact.expect()

        output_sfp1 = re.findall(REGULAR_EXPRESSION, sfp1, re.MULTILINE)
        if not output_sfp1:
            output_sfp1 = {"SFP_INDEX": "0/1", "TEMPERATURA": "0", "VOLTAGEM": "0", "CORRENTE": "0", "TX-POWER": "0", "RX-POWER": "0", "TX-FAULT": "No", "LOS": "No"}
        else:
            output_sfp1 = output_sfp1[0].split()
            output_sfp1 = dict(zip(SFP_DATA, output_sfp1))

        output_sfp2 = re.findall(REGULAR_EXPRESSION, sfp2, re.MULTILINE)
        if not output_sfp2:
            output_sfp2 = {"SFP_INDEX": "0/2", "TEMPERATURA": "0", "VOLTAGEM": "0", "CORRENTE": "0", "TX-POWER": "0", "RX-POWER": "0", "TX-FAULT": "No", "LOS": "No"}
        else:
            output_sfp2 = output_sfp2[0].split()
            output_sfp2 = dict(zip(SFP_DATA, output_sfp2))

        output_sfp3 = re.findall(REGULAR_EXPRESSION, sfp3, re.MULTILINE)
        if not output_sfp3:
            output_sfp3 = {"SFP_INDEX": "0/3", "TEMPERATURA": "0", "VOLTAGEM": "0", "CORRENTE": "0", "TX-POWER": "0", "RX-POWER": "0", "TX-FAULT": "No", "LOS": "No"}
        else:
            output_sfp3 = output_sfp3[0].split()
            output_sfp3 = dict(zip(SFP_DATA, output_sfp3))

        output_sfp4 = re.findall(REGULAR_EXPRESSION, sfp4, re.MULTILINE)
        if not output_sfp4:
            output_sfp4 = {"SFP_INDEX": "0/4", "TEMPERATURA": "0", "VOLTAGEM": "0", "CORRENTE": "0", "TX-POWER": "0", "RX-POWER": "0", "TX-FAULT": "No", "LOS": "No"}
        else:
            output_sfp4 = output_sfp4[0].split()
            output_sfp4 = dict(zip(SFP_DATA, output_sfp4))

        output_sfp5 = re.findall(REGULAR_EXPRESSION, sfp5, re.MULTILINE)
        if not output_sfp5:
            output_sfp5 = {"SFP_INDEX": "0/5", "TEMPERATURA": "0", "VOLTAGEM": "0", "CORRENTE": "0", "TX-POWER": "0", "RX-POWER": "0", "TX-FAULT": "No", "LOS": "No"}
        else:
            output_sfp5 = output_sfp5[0].split()
            output_sfp5 = dict(zip(SFP_DATA, output_sfp5))

        output_sfp6 = re.findall(REGULAR_EXPRESSION, sfp6, re.MULTILINE)
        if not output_sfp6:
            output_sfp6 = {"SFP_INDEX": "0/6", "TEMPERATURA": "0", "VOLTAGEM": "0", "CORRENTE": "0", "TX-POWER": "0", "RX-POWER": "0", "TX-FAULT": "No", "LOS": "No"}
        else:
            output_sfp6 = output_sfp6[0].split()
            output_sfp6 = dict(zip(SFP_DATA, output_sfp6))

        output_sfp7 = re.findall(REGULAR_EXPRESSION, sfp7, re.MULTILINE)
        if not output_sfp7:
            output_sfp7 = {"SFP_INDEX": "0/7", "TEMPERATURA": "0", "VOLTAGEM": "0", "CORRENTE": "0", "TX-POWER": "0", "RX-POWER": "0", "TX-FAULT": "No", "LOS": "No"}
        else:
            output_sfp7 = output_sfp7[0].split()
            output_sfp7 = dict(zip(SFP_DATA, output_sfp7))

        output_sfp8 = re.findall(REGULAR_EXPRESSION, sfp8, re.MULTILINE)
        if not output_sfp8:
            output_sfp8 = {"SFP_INDEX": "0/8", "TEMPERATURA": "0", "VOLTAGEM": "0", "CORRENTE": "0", "TX-POWER": "0", "RX-POWER": "0", "TX-FAULT": "No", "LOS": "No"}
        else:
            output_sfp8 = output_sfp8[0].split()
            output_sfp8 = dict(zip(SFP_DATA, output_sfp8))

        output_sfp9 = re.findall(REGULAR_EXPRESSION, sfp9, re.MULTILINE)
        if not output_sfp9:
            output_sfp9 = {"SFP_INDEX": "0/9", "TEMPERATURA": "0", "VOLTAGEM": "0", "CORRENTE": "0", "TX-POWER": "0", "RX-POWER": "0", "TX-FAULT": "No", "LOS": "No"}
        else:
            output_sfp9 = output_sfp9[0].split()
            output_sfp9 = dict(zip(SFP_DATA, output_sfp9))

        output_sfp10 = re.findall(REGULAR_EXPRESSION, sfp10, re.MULTILINE)
        if not output_sfp10:
            output_sfp10 = {"SFP_INDEX": "0/10", "TEMPERATURA": "0", "VOLTAGEM": "0", "CORRENTE": "0", "TX-POWER": "0", "RX-POWER": "0", "TX-FAULT": "No", "LOS": "No"}
        else:
            output_sfp10 = output_sfp10[0].split()
            output_sfp10 = dict(zip(SFP_DATA, output_sfp10))

        output_sfp11 = re.findall(REGULAR_EXPRESSION, sfp11, re.MULTILINE)
        if not output_sfp11:
            output_sfp11 = {"SFP_INDEX": "0/11", "TEMPERATURA": "0", "VOLTAGEM": "0", "CORRENTE": "0", "TX-POWER": "0", "RX-POWER": "0", "TX-FAULT": "No", "LOS": "No"}
        else:
            output_sfp11 = output_sfp11[0].split()
            output_sfp11 = dict(zip(SFP_DATA, output_sfp11))

        output_sfp12 = re.findall(REGULAR_EXPRESSION, sfp12, re.MULTILINE)
        if not output_sfp12:
            output_sfp12 = {"SFP_INDEX": "0/12", "TEMPERATURA": "0", "VOLTAGEM": "0", "CORRENTE": "0", "TX-POWER": "0", "RX-POWER": "0", "TX-FAULT": "No", "LOS": "No"}
        else:
            output_sfp12 = output_sfp12[0].split()
            output_sfp12 = dict(zip(SFP_DATA, output_sfp12))

        lista = []
        lista.append(output_sfp1)
        lista.append(output_sfp2)
        lista.append(output_sfp3)
        lista.append(output_sfp4)
        lista.append(output_sfp5)
        lista.append(output_sfp6)
        lista.append(output_sfp7)
        lista.append(output_sfp8)
        lista.append(output_sfp9)
        lista.append(output_sfp10)
        lista.append(output_sfp11)
        lista.append(output_sfp12)

        #json_string = json.dumps(lista)
        #print(json_string)

        with open('/tmp/edgeswitch_'+HOSTNAME_FILE+'_data.json', 'w') as json_file:
            json.dump(lista, json_file)

    except Exception:
        traceback.print_exc()
    finally:
        try:
            client.close()
        except Exception:
            pass

if __name__ == '__main__':
    script_arguments = len(sys.argv)
    if script_arguments < 5:
        print('Falta argumentos')
        sys.exit()
    main()
