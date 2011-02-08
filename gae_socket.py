# -*- coding: utf-8 -*-

"""
  This modules provides socket related functions.
  
  Functions:
  
  gae_ntohs(), gae_ntohl() -- convert 16, 32 bit int from network to host byte order
  gae_htons(), gae_htonl() -- convert 16, 32 bit int from host to network byte order
  gae_inet_aton() -- convert IP addr string (123.45.67.89) to 32-bit packed format
  gae_inet_ntoa() -- convert 32-bit packed format IP to string (123.45.67.89)

  :author: Faruk Akgul  
  :license: GPL3, see LICENSE for details.
  
"""

def gae_inet_ntoa(addr):
  """
  convert 32-bit packed format IP to string (123.45.67.89)

  >>> gae_inet_ntoa(2130706433)
  '127.0.0.1'
  >>> gae_inet_ntoa(1113983848)
  '66.102.11.104'
  """
  i0 = (addr & 0xff000000) >> 24
  i1 = (addr & 0x00ff0000) >> 16
  i2 = (addr & 0x0000ff00) >> 8
  i3 = (addr & 0x000000ff)
  return str(i0) + '.' + str(i1) + '.' + str(i2) + '.' + str(i3)

def gae_inet_aton(addr):
  """
  convert IP addr string (123.45.67.89) to 32-bit format
  
    >>> gae_inet_aton('127.0.0.1')
    2130706433
    >>> gae_inet_aton('66.102.11.104')
    1113983848
  """
  addr = addr.split('.')
  num = int(addr[0]) << 24 | int(addr[1]) << 16 | int(addr[2]) << 8 | int(addr[3])
  return num

def gae_ntohs(addr):
  """
  convert 16 bit int from network to host byte order
  
    >>> gae_ntohs(2130706433)
    256
    >>> gae_ntohs(1113983848)
    26635
  """
  return ((addr >> 8) & 0xff) | ((addr & 0xff) << 8)
  
def gae_ntohl(addr):
  """
  convert 32 bit int from network to host byte order
  
    >>> gae_ntohl(2130706433)
    16777343L
    >>> gae_ntohl(1113983848)
    1745577538L
  """
  return ((addr >> 24) & 0xff) | ((addr >> 8) & 0xff00) | ((addr << 8) & 0xff0000) | ((addr << 24) & 0xff000000)
  
def gae_htons(addr):
  """
  convert 16 bit int from host to network byte order
  
    >>> gae_htons(9825)
    24870
    >>> gae_ntohs(1113983745)
    267
  """
  return ((addr >> 8) & 0xff) | ((addr & 0xff) << 8)

def gae_htonl(addr):
  """
  convert 32 bit int from host to network byte order
  
    >>> gae_htonl(9825)
    1629880320L
    >>> gae_ntohl(1113983745)
    17524290L
  """
  return ((addr >> 24) & 0xff) | ((addr >> 8) & 0xff00) | ((addr << 8) & 0xff0000) | ((addr << 24) & 0xff000000)
