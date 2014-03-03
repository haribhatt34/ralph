# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


MACS_RESPONSE = '''<?xml version="1.0"?><s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:wxf="http://schemas.xmlsoap.org/ws/2004/09/transfer"><s:Header><wsa:To>http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous</wsa:To><wsa:Action>http://www.ibm.com/iBMC/sp/Monitors/GetHostMacAddressesResponse</wsa:Action><wsa:RelatesTo>dt:1348742659504</wsa:RelatesTo><wsa:From><wsa:Address>http://10.10.10.10/wsman</wsa:Address></wsa:From><wsa:MessageID>uuid:111efb9a-f7d8-4977-8472-bcad40212a71</wsa:MessageID></s:Header><s:Body><GetHostMacAddressesResponse><HostMACaddress><HostMaddr><Description>Host Ethernet MAC Address 1</Description><Address>6E:F3:DD:E5:96:40</Address></HostMaddr><HostMaddr><Description>Host Ethernet MAC Address 2</Description><Address>6E:F3:DD:E5:96:42</Address></HostMaddr></HostMACaddress></GetHostMacAddressesResponse></s:Body></s:Envelope>
'''

MEMORY_RESPONSE = '''<?xml version="1.0"?><s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:wxf="http://schemas.xmlsoap.org/ws/2004/09/transfer"><s:Header><wsa:To>http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous</wsa:To><wsa:Action>http://www.ibm.com/iBMC/sp/Monitors/GetMemoryInfoResponse</wsa:Action><wsa:RelatesTo>dt:1348742659500</wsa:RelatesTo><wsa:From><wsa:Address>http://10.10.10.10/wsman</wsa:Address></wsa:From><wsa:MessageID>uuid:dc560696-2ba4-4917-b7e7-1aac1983b727</wsa:MessageID></s:Header><s:Body><GetMemoryInfoResponse><Memory><MemoryInfo><Description>DIMM 2</Description><PartNumber>HMT351R7BF111-H9</PartNumber><SerialNumber>33b8a111</SerialNumber><ManufactureDate>4511</ManufactureDate><Type>DDR3</Type><Size>4</Size></MemoryInfo><MemoryInfo><Description>DIMM 3</Description><PartNumber>M393B1K70CH0-YH9</PartNumber><SerialNumber>b38aa222</SerialNumber><ManufactureDate>2211</ManufactureDate><Type>DDR3</Type><Size>8</Size></MemoryInfo><MemoryInfo><Description>DIMM 6</Description><PartNumber>M393B1K70CH0-YH9</PartNumber><SerialNumber>a78aa333</SerialNumber><ManufactureDate>2211</ManufactureDate><Type>DDR3</Type><Size>8</Size></MemoryInfo><MemoryInfo><Description>DIMM 9</Description><PartNumber>EBJ40RF4ECFA-DJ-F</PartNumber><SerialNumber>b5240987</SerialNumber><ManufactureDate>4711</ManufactureDate><Type>DDR3</Type><Size>4</Size></MemoryInfo><MemoryInfo><Description>DIMM 11</Description><PartNumber>EBJ40RF4ECFA-DJ-F</PartNumber><SerialNumber>sn11042b</SerialNumber><ManufactureDate>4711</ManufactureDate><Type>DDR3</Type><Size>4</Size></MemoryInfo><MemoryInfo><Description>DIMM 12</Description><PartNumber>M393B1K70CH0-YH9</PartNumber><SerialNumber>11222385</SerialNumber><ManufactureDate>2211</ManufactureDate><Type>DDR3</Type><Size>8</Size></MemoryInfo><MemoryInfo><Description>DIMM 15</Description><PartNumber>M393B1K70CH0-YH9</PartNumber><SerialNumber>123da482</SerialNumber><ManufactureDate>2211</ManufactureDate><Type>DDR3</Type><Size>8</Size></MemoryInfo><MemoryInfo><Description>DIMM 18</Description><PartNumber>EBJ40RF4ECFA-DJ-F</PartNumber><SerialNumber>d9240aab</SerialNumber><ManufactureDate>4711</ManufactureDate><Type>DDR3</Type><Size>4</Size></MemoryInfo></Memory></GetMemoryInfoResponse></s:Body></s:Envelope>
'''

GENERIC_DATA_RESPONSE = '''<?xml version="1.0"?><s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:wxf="http://schemas.xmlsoap.org/ws/2004/09/transfer"><s:Header><wsa:To>http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous</wsa:To><wsa:Action>http://www.ibm.com/iBMC/sp/Monitors/GetVitalProductDataResponse</wsa:Action><wsa:RelatesTo>dt:1348742659499</wsa:RelatesTo><wsa:From><wsa:Address>http://10.10.10.10/wsman</wsa:Address></wsa:From><wsa:MessageID>uuid:e6829941-2510-4b3d-b9f3-61c7be372dfd</wsa:MessageID></s:Header><s:Body><GetVitalProductDataResponse><GetVitalProductDataResponse><MachineLevelVPD><ProductName>System x3550 M3</ProductName><MachineTypeAndModel>794452G</MachineTypeAndModel><SerialNumber>SN999888777</SerialNumber><UUID>99A4E4A303023961B8E1561E33328996</UUID></MachineLevelVPD><ComponentLevelVPD><FRUNumber>59Y3915</FRUNumber><FRUName>DASD Backplane 1</FRUName><SerialNumber>1122332211sn</SerialNumber><MfgID>USIS</MfgID></ComponentLevelVPD><ComponentLevelVPD><FRUNumber>39Y7229</FRUNumber><FRUName>Power Supply 1</FRUName><SerialNumber>sn776655</SerialNumber><MfgID>ACBE</MfgID></ComponentLevelVPD><ComponentLevelVPD><FRUNumber>39Y7229</FRUNumber><FRUName>Power Supply 2</FRUName><SerialNumber>K141115111</SerialNumber><MfgID>ACBE</MfgID></ComponentLevelVPD><ComponentActivityLog><FRUNumber>39Y7229</FRUNumber><FRUName>Power Supply 1</FRUName><SerialNumber>K1411183222</SerialNumber><MfgID>ACBE</MfgID><Action>Added</Action><TimeStamp>11/25/2011:13:53:13</TimeStamp></ComponentActivityLog><ComponentActivityLog><FRUNumber>59Y3915</FRUNumber><FRUName>DASD Backplane 1</FRUName><SerialNumber>Y010RW1AR111s</SerialNumber><MfgID>USIS</MfgID><Action>Added</Action><TimeStamp>11/25/2011:13:53:13</TimeStamp></ComponentActivityLog><ComponentActivityLog><FRUNumber>39Y7229</FRUNumber><FRUName>Power Supply 2</FRUName><SerialNumber>K14111511sn</SerialNumber><MfgID>ACBE</MfgID><Action>Added</Action><TimeStamp>01/27/2012:10:28:39</TimeStamp></ComponentActivityLog><VPD><FirmwareName>IMM</FirmwareName><VersionString>YUOOC7E</VersionString><ReleaseDate>09/30/2011</ReleaseDate></VPD><VPD><FirmwareName>UEFI</FirmwareName><VersionString>D6E154A</VersionString><ReleaseDate>09/23/2011</ReleaseDate></VPD><VPD><FirmwareName>DSA</FirmwareName><VersionString>DSYT89P </VersionString><ReleaseDate>10/28/2011</ReleaseDate></VPD></GetVitalProductDataResponse></GetVitalProductDataResponse></s:Body></s:Envelope>
'''

SN_RESPONSE = '''<?xml version="1.0"?><s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:wxf="http://schemas.xmlsoap.org/ws/2004/09/transfer"><s:Header><wsa:To>http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous</wsa:To><wsa:Action>http://www.ibm.com/iBMC/sp/iBMCControl/GetSPNameSettingsResponse</wsa:Action><wsa:RelatesTo>dt:1348742647137</wsa:RelatesTo><wsa:From><wsa:Address>http://10.10.10.10/wsman</wsa:Address></wsa:From><wsa:MessageID>uuid:d2ac4b59-9f60-456e-a182-6a077557e4c1</wsa:MessageID></s:Header><s:Body><GetSPNameSettingsResponse><SPName>SN# KD55ARA</SPName></GetSPNameSettingsResponse></s:Body></s:Envelope>
'''

PROCESSORS_RESPONSE = '''<?xml version="1.0"?><s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:wxf="http://schemas.xmlsoap.org/ws/2004/09/transfer"><s:Header><wsa:To>http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous</wsa:To><wsa:Action>http://www.ibm.com/iBMC/sp/Monitors/GetProcessorInfoResponse</wsa:Action><wsa:RelatesTo>dt:1348757382511</wsa:RelatesTo><wsa:From><wsa:Address>http://rack-605-12-mgmt.dc2/wsman</wsa:Address></wsa:From><wsa:MessageID>uuid:9e5ec08d-0fac-449a-80fa-37cc78290a21</wsa:MessageID></s:Header><s:Body><GetProcessorInfoResponse><Processor><ProcessorInfo><Description>Processor 1</Description><Speed>2666</Speed><Identifier>3030363735304141</Identifier><Type>Central</Type><Family>Intel Xeon</Family><Cores>8</Cores><Threads>1</Threads><Voltage>1.087000</Voltage><Datawidth>64</Datawidth></ProcessorInfo><ProcessorInfo><Description>Processor 2</Description><Speed>2666</Speed><Identifier>3030363735304141</Identifier><Type>Central</Type><Family>Intel Xeon</Family><Cores>8</Cores><Threads>1</Threads><Voltage>1.087000</Voltage><Datawidth>64</Datawidth></ProcessorInfo></Processor></GetProcessorInfoResponse></s:Body></s:Envelope>
'''
