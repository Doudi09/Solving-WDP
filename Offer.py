class Offer:

    def __init__(self, line):
        i = 0
        self.offers = []
        for w in line.split():
            if (i == 0):
                self.price = float(w)
            else:
                self.offers.append(int(w))
            i = i + 1
        self.offer_nmbr = i

    def show(self):
        print("the price : ",self.price)
        print("the objects  ",self.offers)



   
    def havecommonobjectwith(self,offer):
        for e in self.offers:
            if(e in offer.offers):
                return True
        return False


