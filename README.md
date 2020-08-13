# Zabbix-Template-Ubiquiti-Edgeswitch-16-XG-SFP-Monitoring

Template de monitoramento das portas SFP do Ubiquiti-Edgeswitch-16-XG
O template disponibiliza as seguintes informações sobre as portas (Corrente [mA] / LOS / RX-Power [dBm] / Temperatura / TX-Fault / TX-Power [dBm] / Voltagem)

Passos para utilização:

1) Os scripts são executados em Python3, é necessário instalar os pacotes paramiko e paramiko-expect: pip3 install paramiko paramiko-expect

2) Copiar os arquivos edgeswitch_sfp_information.py e o arquivo edgeswitch_read_json.py para o diretorio de scripts do Zabbix (por padrao /usr/lib/zabbix/externalscripts/)

3) Dar as permissões necessárias para os scripts:

  chown zabbix.zabbix edgeswitch_sfp_information.py

  chown zabbix.zabbix edgeswitch_read_json.py

  chmod 755 edgeswitch_sfp_information.py

  chmod 755 edgeswitch_read_json.py

  chmod +x edgeswitch_sfp_information.py

  chmod +x edgeswitch_read_json.py

4) Confirme se o usuario zabbix tem permissão de escrita/leitura na pasta /tmp (nessa pasta serão salvos os arquivos json com os dados dos disposiitivos)

5) Importar o arquivo de template no zabbix (Template Ubiquiti Edgeswitch 16 XG SFP Monitoring.xml)

6) Ao vincular o template a um host, altere as macros conforme necessário
  
  {$SSHPORT} - Porta de conexão SSH

  {$UBNTPASSWORD} - Senha de acesso ao dispositivo

  {$UBNTUSER} - Usuario de acesso ao dispositivo
