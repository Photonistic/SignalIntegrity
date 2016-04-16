class SystemDescription(object):
    def __init__(self,sd=None):
        if not sd is None:
            self.Data = sd.Data
            self.m_UniqueDevice=sd.m_UniqueDevice
            self.m_UniqueNode=sd.m_UniqueNode
        else:
            self.Data = []
            self.m_UniqueDevice=UniqueNameFactory('#')
            self.m_UniqueNode=UniqueNameFactory('n')
    def __getitem__(self,item):
        return self.Data[item]
    def __len__(self):
        return len(self.Data)
...
    def AssignM(self,DeviceN,DeviceP,MName):
        di = self.IndexOfDevice(DeviceN)
        self[di][DeviceP-1].M = MName
    def DeviceNames(self):
        return [self[d].Name for d in range(len(self))]
    def IndexOfDevice(self,DeviceName):
        return self.DeviceNames().index(DeviceName)
    def _InsertNodeName(self,DeviceName,Port,AName,BName):
        di = self.IndexOfDevice(DeviceName)
        self[di][Port-1].A = AName
        self[di][Port-1].B = BName
    def CheckConnections(self):
        if not all([self[d][p].IsConnected()
            for d in range(len(self)) for p in range(len(self[d]))]):
            raise PySIExceptionSystemDescription('unconnected device ports')
...
    def AssignSParameters(self,DeviceName,SParameters):
        self[self.IndexOfDevice(DeviceName)].AssignSParameters(SParameters)
    def Print(self):
        print '\n','Device','Name','Port','Node','Name'
        for d in range(len(self)):
            print repr(d+1).rjust(6),
            self[d].Print(1)