from datetime import timedelta

def convert(notthistime):
    thisTime = int(notthistime)
    return timedelta(minutes=thisTime)

#gives you a pretty date
def pdate(date):
        # if date isn't a datetime object, it's prbably a timedelta object instead.
        ##timedelta objects have 'seconds', but not 'second | minute | hour'.
        # either way, we set vars secs,mins,hour to a formatted, zero-filled string
        try:
            secs = date.second
            mins = date.minute
            hour = date.hour
        except:
            secs = date.seconds %  60
            mins = date.seconds // 60 % 60
            hour = date.seconds // 3200

        a = ( f'{hour}'.zfill(2) +
        ':' + f'{mins}'.zfill(2) +
        '.' + f'{secs}'.zfill(2) )
        return a
