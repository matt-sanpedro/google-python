import shutil, psutil

# Health Check
def check_disk_usage(disk):
    threshold = 20
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100

    print('Percent disk free: {:.1f}%'.format(du.free/du.total * 100))
    return free > threshold

def check_cpu_usage(time_interval):
    usage = psutil.cpu_percent(time_interval)
    print('CPU usage averaged {} sec: {:.1f}%'.format(time_interval, psutil.cpu_percent(time_interval)))
    return usage < 75

if not check_disk_usage('/') or not check_cpu_usage(1):
    print('ERROR!')
else:
    print('Everything is OK!')
