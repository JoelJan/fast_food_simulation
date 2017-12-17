class customer:
#    int id_customer
#    int start_time
#    int patience
#    bool take_away
#    int time_to_eat
    def __init__(self,id_customer,start_time,patience,take_away,time_to_eat):
        self.id_customer=id_customer
        self.start_time=start_time
        self.patience=patience
        self.take_away=take_away
        self.time_to_eat=time_to_eat
    def get_start_time(self):
        return(self.start_time)

class service:
#    int id_service
#    int time_to_order
#    int time_to_prepare
    def __init__(self,id_service,time_to_order,time_to_prepare):
        self.id_service=id_service
        self.time_to_order=time_to_order
        self.time_to_prepare=time_to_prepare
        self.queue=[]
        self.ordering_time=0
        self.serving_time=0
        self.cnt_to_serve=0
    def enqueue(self,customer):
        self.queue.append(customer)
    def dequeue(self):
        return(self.queue.pop(0))
    def length_queue(self):
        return(len(self.queue))
    def service_tick(self):
        if self.queue:
            ## if I am ordering
            if self.ordering_time>0:
                self.ordering_time=self.ordering_time+1
                if self.ordering_time % self.time_to_order==0:
                    return('to_cook')
            elif self.cnt_to_serve>0:
                self.serving_time=self.serving_time+1
                if self.serving_time % self.time_to_prepare:
                    self.cnt_to_serve=self.cnt_to_serve-1
                    return('to_table')
            else:
                self.ordering_time=self.ordering_time+1
                if self.ordering_time % self.time_to_order==0:
                    return('to_cook')





class cook:
#    int id_cook
#    int time_to_cook
    def __init__(self,id_cook,time_to_cook):
        self.id_cook=id_cook
        self.time_to_cook=time_to_cook
        self.queue=[]
        self.preparation_time=0
    def enqueue(self,service):
        if queue==[]:
           self.preparation_time=0
        self.queue.append(service)
    def is_cooked(self):
        self.preparation_time=self.preparation_time+1
        if self.queue and self.preparation_time % self.time_to_cook==0:
            self.preparation_time=0
            return(self.queue.pop(0))
    def length_queue(self):
        return(len(self.queue)*self.time_to_cook-self.preparation_time)

class fast_food_model:
#   float unit
#   hh:mm:ss open and close time
#   int places
#   list of cooks
#   list of service
#   list of customers (ordered by start_time)
    def __init__(self,unit,open_time,close_time,places,input_file):
        self.unit=unit
        self.open_time=open_time
        self.close_time=close_time
        self.places=places
        self.file=open(input_file,'r')
        self.lst_cooks=self.read_employes(self.file,'cook')
        self.lst_service=self.read_employes(self.file,'service')
        self.table_queue=[] #table queue is queue of time to eat (int)
        self.time=0
        self.unhappy=0
        self.happy=0
        self.last_customer=self.read_customer(self.file)
    def read_line(self,f):
        try:
            line=f.readline().rstrip('\n')
            line=tuple([int(x) for x in line.split(';')])
            return(line)
        except:
            print(' ')
    def read_employes(self,f,t,debug=True):
        lst_to_return=[]
        line=self.read_line(f)
        while line:
            if debug:
                print(line)
            if t=='cook':
                lst_to_return.append(cook(*line))
            elif t=='service':
                lst_to_return.append(service(*line))
            line=self.read_line(f)
        return(lst_to_return)
    def read_customer(self,f,debug=True):
        line=self.read_line(f)
        if debug==True:
            print(line)
        if line:
            return(customer(*line))
    def print_log(self):
        print('Cooks:')
        for cook in self.lst_cooks:
            print (cook.id_cook)
            print ([s.id_service for s in cook.queue])
        print('Service:')
        for service in self.lst_service:
            print (service.id_service)
            print ([customer.id_customer for customer in service.queue])
        print('table')
        print(self.table_queue)
    def time_tick(self,debug=True):
        #decrease waiting time by 1 for eating ones
        self.table_queue[:(min(len(self.table_queue),self.places))]=[x-1 for x in self.table_queue[:min(len(self.table_queue),self.places)]]
        #remove those with time 0
        while self.table_queue.count(0)>0:
            self.table_queue.remove(0)
            self.happy=self.happy+1
        # This will move customers whose food is cooked in table queue or away
        for service in [s.is_cooked() for s in self.lst_cooks]:
            if service:
                customer_with_food=service.dequeue()
                if (customer_with_food.food_away):
                    self.happy=self.happy+1
                else:
                    self.table_queue.append(customer_with_food.time_to_eat)
        # Make an order

        # This will move read customer while they time is actual time. Each of the chooses shortest service queue
        while self.last_customer and self.last_customer.get_start_time()==self.time:
            best_service=self.find_shortest_queue(self.lst_service)
            if debug:
                print('XXXXXXXXXXXXXX')
                print (best_service.id_service)
            if best_service.length_queue()<=self.last_customer.patience: # If customet is not patience enought, he will leave
                best_service.enqueue(self.last_customer)
            else:
                self.unhappy=self.unhappy+1
            self.last_customer=self.read_customer(self.file)

        self.time=self.time+1
        if debug:
            print('time')
            print(self.time)
            self.print_log()

    def find_shortest_queue(self,lst_of_employee):
        #works for cooks and for service
        min_queue=min([empl.length_queue() for empl in lst_of_employee])
        for employee in lst_of_employee:
            if employee.length_queue()==min_queue:
                return(employee)

#tests:
ffm=fast_food_model(1,'10:00','11:00',2,'test_employ.txt')
for i in range(1,10):
    ffm.time_tick()
