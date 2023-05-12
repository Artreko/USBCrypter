import wmi
import os
from check_key import read_file
from datetime import datetime, timedelta

c = wmi.WMI()

disks = [(drive.Caption, drive.VolumeSerialNumber) for drive in c.Win32_LogicalDisk()]


def get_path_secret_file(disks, filename):
    for disk in disks:
        try:
            if filename not in os.listdir(disk[0]):
                continue
        except PermissionError:
            continue
        return disk


disk = get_path_secret_file(disks, 'secret.key')
if not disk:
    print('У вас нет доступа')
    exit()


key = read_file(f'{disk[0]}\\secret.key', disk[1])

end_date = datetime.strptime(key['date_creation'], '%Y-%m-%d %H:%M:%S.%f') + timedelta(minutes=key['lifetime'])


if end_date < datetime.now():
    print('Ключ действия истек')
    exit()


hello = {
    1: 'Здарова',
    2: 'Привет',
    3: 'Здравствуй',
}[key['level']]

print(f'{hello}, {key["owner"]}')
