#IP header
#raw sockets
#parse IP header using struct module
#regular expressions

import socket
import sys
import struct
import re

def receiveData(s):
    data = ''
    try:
        data = s.recvfrom(65565)
    except timeout:
        data = ''
    except:
        print "An error happened."
        sys.exc_info()

    return data[0]

#get the time of the service - 8 bits

def getTOS(data):
    precedence = {  0 :'Routine',
                    1 :'Priority',
                    2 :'Immediate',
                    3 :'Flash',
                    4 :'Flash override',
                    5 :'CRITIC/ECP',
                    6 :'Internetwork control',
                    7 :'Network control'}
    delay = {0 :'normal delay', 1 :'low delay'}
    throughput = {0: 'normal throughput', 1 :'high throughput'}
    reliability = {0: 'normal reliability', 1 :'high reliability'}
    cost = {0: 'normal monetary cost', 1: 'minimize monetary cost'}

    #00000000
    #PreDTRC0
    D = data & 0x10
    D >>= 4
    T = data & 0x8
    T >>= 3
    R = data & 0x4
    R >>= 2
    M = data & 0x2
    M >>= 1
    tabs = '\n\t\t\t'
    TOS = precedence[data >> 5] + tabs + delay[D] + tabs + throughput[T] + tabs + reliability[R] + tabs + cost[M] 
    return TOS

def getFlags(data):
    flagR = {0: '0 - Reserved Bit'}
    flagDF = {0: '0 - Fragment if neccessary', 1: '1 - Do not fragment'}
    flagMF = {0: '0 - Last Fragment', 1: '1 - More Fragments'}

    R = data & 0x8000
    R >>= 15
    DF = data & 0x4000
    DF >>= 14
    MF = data & 0x2000
    MF >>= 13

    tabs = '\n\t\t\t'
    flags = flagR[R] + tabs + flagDF[DF] + tabs + flagMF[MF]
    return flags

def getProtocol(n):
    protocolFile = open('protocols.txt', 'r')
    protocolData = protocolFile.read()
    protocol = re.findall(r'\n' + str(n) + '(?:.)+\n', protocolData)
    if protocol:
        protocol = protocol[0]
        protocol = protocol.replace('\n', '')
        protocol = protocol.replace(str(n), '')
        protocol = protocol.lstrip()
        return protocol
    else:
        return 'No such protocol was found.'

# the public network interface
HOST = socket.gethostbyname(socket.gethostname())

# create a raw socket and bind it to the public interface
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind((HOST, 0))

# Include IP headers
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# receive all packages
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# receive a package
#print s.recvfrom(65565)
data = receiveData(s)
unpackedData = struct.unpack('!BBHHHBBH4s4s', data[:20])

version_IHL = unpackedData[0]
version = version_IHL >> 4
IHL = version_IHL & 0xF
TOS = unpackedData[1]
totalLength = unpackedData[2]
ID = unpackedData[3]
flags = unpackedData[4]
fragmentOffset = unpackedData[4] & 0x1FFF
TTL = unpackedData[5]
protocol = unpackedData[6]
checkSum = unpackedData[7]
sourceAddress = socket.inet_ntoa(unpackedData[8])
destinationAddress = socket.inet_ntoa(unpackedData[9])
try:
    destinationHostName = socket.gethostbyaddr(destinationAddress)
except:
    destinationHostName = "Host not found."
    
print 'An IP packed with the size %i was captured.\n' % (totalLength)
print "Raw data: " + data
print "\nParsed data:"
print "Version:\t\t" + str(version)
print "Header Length:\t\t" + str(IHL*4) + " bytes"
print "Type of Service:\t\t" + getTOS(TOS)
print "Length:\t\t" + str(totalLength)
print "ID:\t\t" + str(hex(ID)) + " (" + str(ID) + ")"
print "Flags:\t\t" + getFlags(flags)
print "Fragment Offest:\t\t" + str(fragmentOffset)
print "TTL:\t\t" + str(TTL)
print "Protocol:\t\t" + getProtocol(protocol)
print "CheckSum:\t\t" + str(checkSum)
print "Source:\t\t" + sourceAddress
print "Destination:\t\t" + destinationAddress
print "DestinationHN:\t\t" + destinationHostName[0]
print "Payload:\n" + data[20:]


# disabled promiscuous mode
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
