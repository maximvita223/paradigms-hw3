class Observer:
    def reaction(self, message):
        pass

class ConcreteObserver(Observer):
    def reaction(self, message):
        print("Reaction to message - ", message)

class NotificationSystem :
    _observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.reaction(message)


subject = NotificationSystem()

observer1 = ConcreteObserver()
observer2 = ConcreteObserver()

subject.attach(observer1)
subject.attach(observer2)

subject.notify("Hello, World")  
