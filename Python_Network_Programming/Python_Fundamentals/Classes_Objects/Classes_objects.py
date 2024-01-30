class MyRouter(object):
    "class that describes the characteristics of a router"
    def __init__(self, routername, model, sno, ios):
        self.routername = routername
        self.model = model
        self.sno = sno
        self.ios = ios
    def print_router(self, manu_date):
        print("Router name is : ", self.routername)
        print("Router model is : ", self.model)
        print("Router sno is : ", self.sno)
        print("Router ios is : ", self.ios)
        print("Router model & manufacturing date is : ", self.model + manu_date)