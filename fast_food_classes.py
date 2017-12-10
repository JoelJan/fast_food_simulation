class customer:
#    int id_customer
#    int start_time
#    int patience
#    bool take_away
#    int time_to_eat
    def _init_(self,id_customer,start_time,patience,take_away,time_to_eat):
        self.id_customer=id_customer
        self.start_time=start_time
        self.patience=patience
        self.take_away=take_away
        self.time_to_eat=time_to_eat

class service:
#    int id_service
#    int time_to_order
#    int time_to_prepare
    def _init_(self,id_service,time_to_order,time_to_prepare):
        self.id_service=id_service
        self.time_to_order=time_to_order
        self.time_to_prepare=time_to_prepare
        self.queue=[]
    def enqueue(self,customer):
        self.queue.append(customer)
    def dequeue(self):
        self.queue.pop(0)
    def length_queue(self):
        return(len(self.queue))

class cook:
#    int id_cook
#    int time_to_cook
    def _init_(self,id_cook,time_to_cook):
        self.id_cook=id_cook
        self.time_to_cook=time_to_cook
        queue=[]
        preparation_time=0
    def enqueue(self,service):
        if queue==[]:
            preparation_time=0
        self.queue.append(sevice)
    def is_cooked():
        if self.queue<>[] and self.preparation_time % self.time_to_cook==0:
            self.queue.pop(0)
            preparation_time=0
    def length_queue(self):
        return(len(self.queue)*time_to_cook-self.preparation_time)

class fast_food_model:
#   float unit
#   hh:mm:ss open and close time
#   int places
#   list of cooks
#   list of service
#   list of customers (ordered by start_time)
    def _init_(self,unit,open_time,close_time,places):
        self.unit=unit
        self.open_time=open_time
        self.close_time=close_time
        self.places=places
        lst_cook=[]
        lst_service=[]
        pass
    def read_empolyes():
        pass
    def new_customer():
        pass
    def serve_food():
        pass
    def find_best_cook():
        pass
    def find_shortest_queue(lst_of_employee):
        #works for cooks and for service
        min_queue=min([empl.length_queue() for empl in lst_of_employee])
        for emloyee in lst_of_employee:
            if employee.length_queue()==min_queue:
                return(employee)

