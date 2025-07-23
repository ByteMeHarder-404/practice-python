import sys, time,datetime
import sevseg

now=datetime.datetime.now()
midnight=(now + datetime.timedelta(days=1)).replace(hour=0,minute=0,second=0)
remaining=midnight-now
secondsleft=int(remaining.total_seconds())

try:
    while True:
        hours=str(secondsleft//3600)
        minutes=str((secondsleft%3600)//60)
        seconds=str(secondsleft%60)

        hDigits=sevseg.getSevSegStr(hours,2)
        htop,hmid,hbot=hDigits.splitlines()

        mDigits=sevseg.getSevSegStr(minutes,2)
        mtop,mmid,mbot=mDigits.splitlines()

        sDigits=sevseg.getSevSegStr(seconds,2)
        stop,smid,sbot=sDigits.splitlines()

        print(htop+'     '+mtop+'     '+stop)
        print(hmid+'  *  '+mmid+'  *  '+smid)
        print(hbot+'  *  '+mbot+'  *  '+sbot)

        if secondsleft==0:
            print('***BOOM***')
            break

        print()
        print('Press Ctrl-C to exit.')

        time.sleep(1)
        secondsleft-=1
except KeyboardInterrupt:
    sys.exit()