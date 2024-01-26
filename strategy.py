from finance_structures import Candle, Order, Glass


#универсальный класс стратегии
class Strategy(object):
    #список всех свечек, зафиженый в стратегию
    feed = []
    #наименование стратегии
    strategy_name = "undefined"
    period = -1
    number_of_stocks = 0
    money = 0
    local_glass = Glass()
    my_orders = []
    def __init__(self, nm, local_glass):
        self.feed = []
        self.strategy_name = nm
        self.local_glass = local_glass

    def __init__(self):
        self.feed = []
        self.strategy_name = "undefined"

    def Feed(self, cand):
        if (self.strategy_name == "undefined"):
            raise("Undefined Behaviour: the strategy is either unnamed either undefined")
        if (type(cand) != Candle):
            raise("Type Error: attempt to feed non-candle to a Strategy template")
        if (cand.is_undefined()):
            raise("Undefined Behaviour: attempt to feed an undefined candle")
        self.feed.append(cand)
        self.OnCandleAdded(cand)

    # должно вернуть список пар (int, Order), где первый int тип операции, 0 - создание, 1 - отмена. если отмена - пустой заказ с айдишником отменяемого заказа
    def Process(self, glass):
        if (self.strategy_name == "undefined"):
            raise("Undefined Behaviour: the strategy is either undefined")
        pass

    def OnCandleAdded(self, candle):
        pass

    def AddMoney(self, x):
        self.money += x

    def OnBuyOrderSatisfied(self, order, quantity):
        self.number_of_stocks += quantity
        #self.money -= order.price * quantity
        pass

    def OnSellOrderSatisfied(self, order, quantity):
        #self.number_of_stocks -= quantity
        self.money += order.price * quantity
        pass

