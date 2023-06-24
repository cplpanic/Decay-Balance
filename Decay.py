"""

This script is a quick example for adding decay rates to money in an account & just a formality

The thought is that with a decay rate applyed to money we can avoid stagnate or money that stops circulation.

The block chain is to help keep a ledger, identify fraud, set decay rates, identify bottlenecks, deflate inflation.

Once a limit has been reatched funds will decay unless they are used \ transferd.

You can either pass consumed decay into deletion or charity \ public.  

"""

import time
coin = 1

def Start():

  global coin
  coin += 1

  print ("Funds = ",coin)


  time.sleep(2)

  if coin >= 5:
    Check()
  else:
    Start()
     

def Check():

  print("Funds have have stagnated or exceeded limit")
  print("Data has been enterd into the block chain")
  print("Decay rate has started")
  print("Funds must be used or transferd to stop decay rate")
  time.sleep(10)
  

Start()
