class DeembedderNumericParser(DeembedderParser):
    def __init__(self, f=None, args=None):
        DeembedderParser.__init__(self, f, args)
    def Deembed(self,systemSParameters=None):
        self._ProcessLines()
        self.m_sd.CheckConnections()
        NumUnknowns=len(self.m_sd.UnknownNames())
        result=[[] for i in range(NumUnknowns)]
        for n in range(len(self.m_f)):
            system=None
            for d in range(len(self.m_spc)):
                if self.m_spc[d][0] == 'system':
                    system=self.m_spc[d][1][n]
                else:
                    self.m_sd.AssignSParameters(self.m_spc[d][0],
                        self.m_spc[d][1][n])
            if not systemSParameters is None:
                system=systemSParameters[n]
            unl=DeembedderNumeric(self.m_sd).CalculateUnknown(system)
            if NumUnknowns == 1: unl=[unl]
            for u in range(NumUnknowns):
                result[u].append(unl[u])
        sf=[SParameters(self.m_f,r) for r in result]
        if len(sf)==1:
            return sf[0]
        return sf
