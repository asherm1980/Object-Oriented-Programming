class Timer:
    def __init__(self, val1=0, val2=0, val3=0):
        #
        # Write code here
        #
        self.th=str(val1)
        if len(self.th)==1:
            self.th='0'+self.th
        self.tm=str(val2)
        if len(self.tm)==1:
            self.tm='0'+self.tm
        
        self.ts=str(val3)
        if len(self.ts)==1:
            self.ts='0'+self.ts




    def __str__(self):
        #
        # Write code here
        #
        return self.th+':'+self.tm+':'+self.ts

    def next_second(self):
        #
        # Write code here
        #
        val1=self.ts
        
        self.ts=str(int(val1)+1)
        if len(self.ts)==1:
            self.ts='0'+self.ts
        elif self.ts=='60':
            self.ts='00'
            val2=self.tm
            self.tm=str(int(val2)+1)
            if len(self.tm)==1:
               self.tm='0'+self.tm            
            elif self.tm=='60':
                self.tm='00'    
                val3=self.th
                self.th=str(int(val3)+1)
                if len(self.th)==1:
                   self.th='0'+self.th                
                elif self.th=='24':
                   self.th='00'
        return self.__str__()
        

    def prev_second(self):
        val1=self.ts
        self.ts=str(int(val1)-1)
        if len(self.ts)==1:
            self.ts='0'+self.ts
        elif self.ts=='-1':
            self.ts='59'
            val2=self.tm
            self.tm=str(int(val2)-1)
            if len(self.tm)==1:
               self.tm='0'+self.tm
            elif self.tm=='-1':
                self.tm='59'    
                val3=self.th
                self.th=str(int(val3)-1)
                if len(self.th)==1:
                  self.th='0'+self.th
                elif self.th=='-1':
                   self.th='23'
        return self.__str__()

timer = Timer(23, 1, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
