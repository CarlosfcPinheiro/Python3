#Hours, minutes and second in a day

days = int(input('Insert a number of days: '))

hours = days*24
minutes = hours*60
seconds = minutes*60

print(f'\nThese {days} days, have: {hours} hours, {minutes} minutes and {seconds} seconds.')