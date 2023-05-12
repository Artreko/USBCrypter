import wmi
from key_generator.generator.generate_key_file import write_key

c = wmi.WMI()
disks = []

disks = [(drive.Name, drive.VolumeName, drive.VolumeSerialNumber, drive.Description, drive.DriveType) for drive in c.Win32_LogicalDisk()]
for i, drive in enumerate(disks):
    print(i, *drive)
    # print(f'{i}: {drive[0]}')
# a = {'Access': None, 'Availability': None, 'BlockSize': None, 'Caption': None, 'Compressed': None,
#      'ConfigManagerErrorCode': None, 'ConfigManagerUserConfig': None, 'CreationClassName': None, 'Description': None,
#      'DeviceID': None, 'DriveType': None, 'ErrorCleared': None, 'ErrorDescription': None, 'ErrorMethodology': None,
#      'FileSystem': None, 'FreeSpace': None, 'InstallDate': None, 'LastErrorCode': None, 'MaximumComponentLength': None,
#      'MediaType': None, 'Name': None, 'NumberOfBlocks': None, 'PNPDeviceID': None, 'PowerManagementCapabilities': None,
#      'PowerManagementSupported': None, 'ProviderName': None, 'Purpose': None, 'QuotasDisabled': None,
#      'QuotasIncomplete': None, 'QuotasRebuilding': None, 'Size': None, 'Status': None, 'StatusInfo': None,
#      'SupportsDiskQuotas': None, 'SupportsFileBasedCompression': None, 'SystemCreationClassName': None,
#      'SystemName': None, 'VolumeDirty': None, 'VolumeName': None, 'VolumeSerialNumber': None}

num = int(input('Выберите диск: '))
owner = input('Кому выдан ключ: ')
lifetime = int(input('Время жизни ключа в минутах: '))
level = int(input('Уровень доступа: '))
serial_number = disks[num][1]
disk = disks[num][0]

write_key(owner, lifetime, level, serial_number, disk)
