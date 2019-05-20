sections = ('CPU-Z TXT Report',
            'Binaries',
            'Processors',
            'APICs',
            'Timers',
            'Processors Information',
            'Thread dumps',
            'BIOS',
            'Chipset',
            'Memory SPD',
            'Monitoring',
            'LPCIO',
            'Hardware Monitors',
            'PCI Devices',
            'DMI',
            'Storage',
            'USB Devices',
            'Graphics',
            'Graphic APIs',
            'Display Adapters',
            'Software',
            'Register Spaces')

file = open('test_cpuz.txt', 'r')

i        = 0
old_line = ''
section  = ''

for line in file:    
    if line[0] == '-':
        section = str(old_line).strip()
        i+=1
        print('{:2} {}'.format(i, str(old_line).strip()))
    old_line = line
    
    if section == sections[2]:
        if len(line.strip()) == 0:
            continue

        key   = str(line).split('\t')[0]
        value = str(line).split('\t')[-1:][0]        
        value = str(value).replace('\n', '')
        
        if key == 'Number of sockets':
            print(key, value)
            
        if key == 'Number of threads':
            print(key, value)
        
