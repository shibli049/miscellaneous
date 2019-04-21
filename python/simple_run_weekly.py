#! /usr/local/bin/python3.7

from datetime import date
import json
from subprocess import  run
import logging
logging.basicConfig(level=logging.INFO,
                    format=' %(asctime)s - %(levelname)s - %(message)s')

ALERT_DAY='Thursday'
filename = 'run_flag.json'
CMD = "~/script.sh"


# default
data = {'sent': False}
try:
    current_day = date.today().strftime("%A")
    logging.info("current day: {}, alert day: {}".format(current_day, ALERT_DAY))
    if current_day == ALERT_DAY:
        with open(filename, 'r') as f:    
            try: 
                data = json.loads("\n".join(f.readlines()))
            except (BaseException, Exception) as e:
                pass
        logging.info("data: {}".format(data))
        if  not data['sent']:
            run(CMD)
            data['sent'] = True
        
    t = json.dumps(data, indent=2)
    with open(filename, 'w') as f:
        f.writelines(t)
    
except (BaseException, Exception) as e:
    pass
