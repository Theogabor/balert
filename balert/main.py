#! /usr/bin/python
from multiprocessing.dummy import Pool as ThreadPool
from sys import argv, exit
from Bsettings import bpath,SetLevel
from Voice import voice
from BatteryStatus import battery
import argparse,logging,subprocess

def setupCron():
    try:
        location_f = subprocess.Popen("whereis balert", shell=True, stdout=subprocess.PIPE).stdout.read().strip().split(':')[1].strip()
        cmd = subprocess.Popen("crontab -l", shell=True, stdout=subprocess.PIPE).stdout.read()
        if not ('balert' in cmd): # avoid multiple cronjob creation
            cmd += "*/10 * * * * " + location_f + "\n"
            tmp = open("/tmp/temp_cron.impossible", 'w')
            tmp.write(cmd)
            tmp.close()
            subprocess.Popen("crontab /tmp/temp_cron.impossible", shell=True)
            logging.info("Successfully set up the cron job.")
        else:
            pass
    except:
        logging.debug("Error writing the cron job.")
        

def main():

    parser = argparse.ArgumentParser(description=" \
             Listen the voice of your battery whenever she is low!",epilog="Author:\
             tushar.rishav@gmail.com")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-r", "--rate", help="Rate of speaking.(100-200)",
                       type=int)
    group.add_argument("-v", "--vol", help="Volume of speaking.(1.0)",
                       type=str)
    group.add_argument("-l", "--lang", help="Language speaking.(1.0)",
                       type=str)
    group.add_argument("-m", "--msg", help="Alert message of your own",
                       type=str)
    group.add_argument("-c", "--charge", help="Decide the critical charge level",
                       type=int, default=20)
    args = parser.parse_args()
    if len(argv) == 1:
        pass
    al = voice()
    if args.rate:
        al.set_rate(args.rate)
    elif args.vol:
        al.set_vol(args.vol)
    elif args.lang:
        al.set_lang(args.lang)
    elif args.msg:
        al.msg = args.msg
    elif args.charge:
        SetLevel.CHARGE = args.charge
    __ = battery()
    _ = __.get_low_battery_warning_level()
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug(_)
    if _[0] == 0 and _[1]:
        al.msg += "All cool! %d Percent remaining" %_[1]
    elif _[0] == 1:
        al.msg += "Low Battery! %d Percent remaining" %_[1]
        logging.info(al.msg)
        al.speak()
    else:
        al.msg += " Battrey is Charging!"
    setupCron()



if __name__ == "__main__":
    main()




    
