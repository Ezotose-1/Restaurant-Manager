# Restaurant Manager


This scripti is restaurant management program. Thank's to this you can manage your stock, the prices of your items, take commandes from your customers and chek your restaurant statistics.

### Installation
* Download the file thank's to the github page. Or clone the project with the git link :
```shell
git clone https://github.com/Ezotose-1/Restaurant.git
```

* Run the script by using the python command :
```shell
python main.py
```

## Utilisation
This script is a console program using the Python language. You can use it by following the instructions of the menus.  
These type of menuing is used : 
```console
1. Option(1)      3. Option(3)
2. Option(2)      4. Option(4)
What do you wan't to do : (1-4)
> 
```
Just enter the number of the option you wan't to use.

You can also manually modify the menu and the stock by editing the files *menu.txt* and *stocks.txt*.  
**BUT** you need to follow the format :  
For menu.txt
```
dish - dish type - price
```

For stocks.txt
```
dish - count
```

### File architecture
```
Restaurant
└─ main.py
└─ stocks.txt
└─ menu.txt
└─ orders
   └─ DUBELLAY.txt
   └─ EPICURE.txt
   └─ MAUPASSANT.txt
   └─ ... (your orders files)
```

### Libraries
For the use of this content, there is no library needed. All the lib used are the original from Python : 
```python
import os
from os import system, name
import datetime
import sys
```


### Compatibility
To use this content, you must use Python **2.X or higher** *(3.X included)*.
The program have been made with Python *V3.6.9*, it have been tested with lower version.
All the script is Windows and Linux compatible.

   
### License
----
Developped by Pierre B.  
Languages : Python  
Free to use  
MIT  


**Free Software**
