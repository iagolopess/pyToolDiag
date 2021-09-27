import wmi

ver = wmi.WMI().Win32_Process.methods.keys()

# print(ver)

ver2 = wmi.WMI().Win32_Process.properties.keys()

# print(ver2)

ver3 = wmi.WMI().Win32_LogicalDisk()

print(ver3)