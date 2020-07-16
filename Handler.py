# from Lab import Lab
# from ServiceTime import ServiceTime
from filler import generateSampleOrder
from filler import generateSampleUserWithPrescs

class Handler:
    def __init__(self):
        self.__order = None

    def enterPrescriptionID(self, pid):
        user = generateSampleUserWithPrescs() # TODO: JUST A SAMPLE USER ~~~~~~~~~~ DELETE IT IN FUTURE ~~~~~~~~~~~~~~~~~~~~``
        user_prescs = user.getPrescriptions()
        
        presc = None
        for each_presc in user_prescs:
            if each_presc.getPrescriptionDetail().getPrescID() == pid:
                presc = each_presc
                break
        
        order = user.createOrder(presc.getPrescriptionDetail())
        self.setOrder(order)

    def createTests(self):
        pass

    def getTests(self):
        return self.__order.getPrescDetail().getTests()

    def chooseTests(self, tests):
        self.__order.chooseTests(tests) 

    def getTimes(self):
        self.__order = generateSampleOrder() # TODO: JUST A SAMPLE ORDER ~~~~~~~~~~ DELETE IT IN FUTURE ~~~~~~~~~~~~~~~~~~~~``
        lab = self.__order.getLab()
        totaltimes = lab.getAvailableTimes()
        filtered_times = []
        for i in totaltimes:
            find = False
            for j in filtered_times:
                if i.getDate() == j.getDate():
                    find = True
                    break
            if not find:
                filtered_times.append(i)
        filtered_times.sort(key=lambda x: x.getDate())
        return filtered_times

    def chooseTime(self, service_time):
        # service_time.setAccessibility(False)
        self.__order.setServiceTime(service_time)
        print(f"the chosen time is: {str(self.__order.getServiceTime())}")
    
    def getPrice(self):
        self.__order = generateSampleOrder() # TODO: JUST A SAMPLE ORDER ~~~~~~~~~~ DELETE IT IN FUTURE ~~~~~~~~~~~~~~~~~~~~``
        price = self.__order.doPricing()
        return price

    def getLabs(self):
        return self.__order.getFinalLabs()
    
    def chooseLab(self, lab):
        self.__order.setLab(lab)

    def enterAddress(self, address):
        self.__order.setAddress(address)

    def enterFaultCode(self, fault_code):
        pass

    def startNewOrder(self):
        pass

    def payOnline(self):
        self.__order = generateSampleOrder() # TODO: JUST A SAMPLE ORDER ~~~~~~~~~~ DELETE IT IN FUTURE ~~~~~~~~~~~~~~~~~~~~``
        status = self.__order.doPayment()
        return status

    def getOrder(self):
        return self.__order

    def setOrder(self, order):
        self.__order = order