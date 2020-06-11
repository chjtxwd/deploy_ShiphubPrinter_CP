import paramiko
import requests

def addgk888t(store):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(store, username='xx', password='xx')
    url = 'http://' + store + ':631'
    rsp = requests.get(url, stream=True)
    ip = rsp.raw._connection.sock.getpeername()[0]
    part = ip.split('.',3)
    shiphub = part[0] + '.' + part[1] + '.' + part[2] + '.178'
    print(shiphub)
    command = '/usr/sbin/lpadmin -p GK888t  -v socket://'+ shiphub + ':9100  -m  drv:///sample.drv/zebra.ppd -o printer-is-shared=false'
    #command = 'lpadmin'
    print(command)
    stdin, stdout, stderr = client.exec_command(command)

    print('stdout - {0}'.format(stdout.read().decode()))
    print('stderr - {0}'.format(stderr.read().decode()))

    client.close()
    return


addgk888t("s388cp01")
SBLIST = ['S1018CP01', 'S1019CP01', 'S1020CP01', 'S1021CP01', 'S1022CP01', 'S1023CP01', 'S1026CP01', 'S1027CP01',
          'S1028CP01', 'S1029CP01', 'S1030CP01', 'S1031CP01', 'S1032CP01', 'S1202CP01', 'S1203CP01', 'S1204CP01',
          'S1205CP01', 'S1206CP01', 'S1207CP01', 'S1209CP01', 'S1210CP01', 'S1211CP01', 'S1212CP01', 'S1213CP01',
          'S1216CP01', 'S1219CP01', 'S1220CP01', 'S1221CP01', 'S1224CP01', 'S1225CP01', 'S1226CP01', 'S1227CP01',
          'S1228CP01', 'S1230CP01', 'S1231CP01', 'S1232CP01', 'S1233CP01', 'S1234CP01', 'S1236CP01', 'S1238CP01',
          'S1239CP01', 'S1240CP01', 'S1245CP01', 'S1249CP01', 'S1250CP01', 'S1252CP01', 'S1253CP01', 'S1254CP01',
          'S1255CP01', 'S1256CP01', 'S1258CP01', 'S1259CP01', 'S1260CP01', 'S1261CP01', 'S1262CP01', 'S1263CP01',
          'S1265CP01', 'S1266CP01', 'S1267CP01', 'S1268CP01', 'S1269CP01', 'S1270CP01', 'S1271CP01', 'S1272CP01',
          'S1273CP01', 'S1275CP01', 'S1276CP01', 'S1277CP01', 'S1278CP01', 'S1280CP01', 'S1281CP01', 'S1282CP01',
          'S1283CP01', 'S1284CP01', 'S1285CP01', 'S1286CP01', 'S1287CP01', 'S1288CP01', 'S1289CP01', 'S1290CP01',
          'S1291CP01', 'S1293CP01', 'S1294CP01', 'S1295CP01', 'S1296CP01', 'S1297CP01', 'S1298CP01', 'S1299CP01',
          'S1300CP01', 'S1621CP01', 'S1622CP01', 'S1623CP01', 'S1625CP01', 'S1626CP01', 'S1627CP01', 'S1628CP01',
          'S1629CP01', 'S1630CP01', 'S1631CP01', 'S1632CP01', 'S1635CP01', 'S1636CP01', 'S1637CP01', 'S1638CP01',
          'S1650CP01', 'S1651CP01', 'S1652CP01', 'S1653CP01', 'S1655CP01', 'S1656CP01', 'S1657CP01', 'S1659CP01',
          'S1660CP01', 'S1661CP01', 'S1662CP01', 'S1663CP01', 'S1664CP01', 'S1665CP01', 'S1666CP01', 'S1667CP01',
          'S1669CP01', 'S1670CP01', 'S1671CP01', 'S1672CP01', 'S1673CP01', 'S1675CP01', 'S1676CP01', 'S1677CP01',
          'S1678CP01', 'S1679CP01', 'S1680CP01', 'S1682CP01', 'S1683CP01', 'S1685CP01', 'S1686CP01', 'S1687CP01',
          'S1688CP01', 'S1702CP01', 'S1703CP01', 'S1705CP01', 'S1706CP01', 'S1707CP01', 'S1709CP01', 'S1710CP01',
          'S1711CP01', 'S1713CP01', 'S1715CP01', 'S1717CP01', 'S1718CP01', 'S1719CP01', 'S1720CP01', 'S1722CP01',
          'S1723CP01', 'S1725CP01', 'S1726CP01', 'S1727CP01', 'S1728CP01', 'S1729CP01', 'S1751CP01', 'S1752CP01',
          'S1753CP01', 'S1757CP01', 'S1758CP01', 'S1759CP01', 'S1760CP01', 'S1761CP01', 'S1763CP01', 'S1765CP01',
          'S1767CP01', 'S1768CP01', 'S1770CP01', 'S1777CP01', 'S388CP01', 'S389CP01', 'S390CP01', 'S391CP01',
          'S392CP01', 'S416CP01', 'S418CP01', 'S419CP01', 'S420CP01', 'S421CP01', 'S422CP01', 'S423CP01', 'S430CP01',
          'S488CP01', 'S489CP01', 'S490CP01', 'S491CP01', 'S508CP01', 'S558CP01', 'S559CP01', 'S561CP01', 'S562CP01',
          'S589CP01', 'S592CP01', 'S593CP01', 'S665CP01', 'S669CP01', 'S680CP01', 'S681CP01', 'S682CP01', 'S685CP01',
          'S686CP01', 'S687CP01', 'S688CP01', 'S689CP01', 'S708CP01', 'S780CP01', 'S781CP01', 'S782CP01', 'S783CP01',
          'S784CP01', 'S786CP01', 'S788CP01', 'S789CP01', 'S792CP01', 'S800CP01', 'S803CP01', 'S804CP01', 'S805CP01',
          'S807CP01', 'S822CP01', 'S842CP01', 'S850CP01', 'S855CP01', 'S856CP01', 'S857CP01', 'S858CP01', 'S859CP01',
          'S860CP01', 'S861CP01', 'S873CP01', 'S888CP01', 'S901CP01', 'S902CP01', 'S903CP01', 'S904CP01', 'S905CP01',
          'S906CP01', 'S907CP01', 'S908CP01', 'S909CP01', 'S910CP01', 'S912CP01', 'S913CP01', 'S914CP01', 'S916CP01',
          'S917CP01', 'S918CP01', 'S919CP01', 'S920CP01', 'S921CP01', 'S922CP01', 'S923CP01', 'S924CP01', 'S925CP01',
          'S927CP01', 'S929CP01', 'S930CP01', 'S931CP01', 'S934CP01', 'S942CP01', 'S947CP01', 'S949CP01', 'S950CP01',
          'S951CP01', 'S953CP01', 'S955CP01', 'S956CP01', 'S958CP01', 'S959CP01', 'S960CP01', 'S961CP01', 'S962CP01',
          'S963CP01', 'S966CP01', 'S967CP01', 'S968CP01', 'S970CP01', 'S971CP01', 'S972CP01', 'S973CP01', 'S985CP01',
          'S986CP01', 'S987CP01', 'S989CP01', 'S990CP01', 'S991CP01', 'S992CP01', 'S994CP01', 'S995CP01', 'S999CP01']


