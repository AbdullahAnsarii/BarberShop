from threading import Thread, Lock, Event
import time, random


mutex = Lock()

#Interval in seconds
MinIntervalOfCustomer = 2 #It is the minimum duration of customer
MaxIntervalOfCustomer = 7  #It is the maximum duration of customer
MinimumDurationOfHairCut = 3  #It is the minimum duration of customer
MaximumDurationOfHairCut = 9   #It is the maximum duration of customer

class ShopOfBarber:
        CustomerIsWaiting = [] #initializing list of waiting customers
        CustomersAreFinish = [] #initializing list of ; when there is no customer in shop

        def __init__(self, barber, chairs_available):
                self.barber = barber
                self.chairs_available = chairs_available #chairs available in barber shop
                print('Welcome to Our Barber Shop | Hope you will enjoy the services') #print the welcome note
                print('There are {0} seats in the waiting area of Barber Shop'.format(chairs_available)) #print the no of available seats
                print('Customer min duration {0} seconds'.format(MinIntervalOfCustomer)) #print the durations
                print('Customer max duration {0} seconds'.format(MaxIntervalOfCustomer))#print the durations
                print('Haircut min duration {0} seconds'.format(MinimumDurationOfHairCut)) #print the durations
                print('Haircut max duration {0} seconds'.format(MaximumDurationOfHairCut)) #print the durations
                print('*********************************')

        def ShopIsOpen(self): #when shop is open 
                print('BarberShop is open now')
                workingThread = Thread(target = self.barberIsWorking)
                workingThread.start()

        def barberIsWorking(self): #when barber is working 
                while True:
                        mutex.acquire()

                        if len(self.CustomerIsWaiting) > 0: #when there is a customer, call cuthair function
                                c = self.CustomerIsWaiting[0]
                                del self.CustomerIsWaiting[0]
                                mutex.release()
                                self.barber.cutHair(c)
                        elif len(self.CustomerIsWaiting) <= 0: #if there is no customer then barber going to sleep
                                mutex.release()
                                print('Oh there is no customer .. :( , Barber is going to sleep')
                                barber.sleep()
                                print('Barber is waking up')
                        
                
        def Balk(self, customer): #when customer enter the barber shop and looking for a chair in waiting area
                mutex.acquire()
                print('>> {0} entered the shop and looking for a seat'.format(customer.name))

                if len(self.CustomerIsWaiting) == self.chairs_available: #if waiting area is full then customer leave the shop
                        print('Waiting room is full, {0} is leaving.'.format(customer.name))
                        mutex.release()
                else: # if chair is available then customer wait for his turn
                        print('{0} sat down in the waiting room'.format(customer.name))	
                        self.CustomerIsWaiting.append(c)	
                        mutex.release()
                        barber.wakeUp()

class Customer:
        def __init__(self, name):
                self.name = name
        def getHairCut(self, customer): #gethaircut function in the customer thread
                getHairCut=Barber.cutHair()
                return getHairCut

class Barber:
        barberWorkingEvent = Event()

        def sleep(self):
                self.barberWorkingEvent.wait()

        def wakeUp(self):
                self.barberWorkingEvent.set()

        def cutHair(self, customer): #barber is busy in hair cutting
        
                self.barberWorkingEvent.clear()

                print('{0} is having a haircut'.format(customer.name)) #print the customer name which is currently having a hair cut

                randomHairCuttingTime = random.randrange(MinimumDurationOfHairCut, MaximumDurationOfHairCut+1)
                time.sleep(randomHairCuttingTime)
                print('{0} is done'.format(customer.name))


if __name__ == '__main__':
        customers = [] #list of all the customers
        customers.append(Customer('Zain'))
        customers.append(Customer('Ali'))
        customers.append(Customer('Usman'))
        customers.append(Customer('Anas'))
        customers.append(Customer('Taha'))
        customers.append(Customer('ishaq'))
        customers.append(Customer('Ilyas'))
        customers.append(Customer('Burak'))
        customers.append(Customer('Engin'))
        customers.append(Customer('Saeed'))
        customers.append(Customer('Kamran'))
        customers.append(Customer('Hasan'))
        customers.append(Customer('Bilal'))
        customers.append(Customer('Athar'))
        customers.append(Customer('Feroz'))
        customers.append(Customer('Habib'))
        customers.append(Customer('Zakaria'))
        customers.append(Customer('Hamza'))
        customers.append(Customer('Imran'))
        customers.append(Customer('Umer'))
        customers.append(Customer('Faizan'))
        customers.append(Customer('Irtiza'))
        customers.append(Customer('Rehmat'))
        customers.append(Customer('Akbar'))
        customers.append(Customer('Ahmed'))
        customers.append(Customer('Saleem'))
        customers.append(Customer('Adil'))
        customers.append(Customer('Sufyan'))
        customers.append(Customer('Noman'))


        barber = Barber()

        barberShop = ShopOfBarber(barber, chairs_available=6)#total chairs of customers are 6 in the barbershop
        barberShop.ShopIsOpen()

        while len(customers) > 0:
                c = customers.pop()	
                #New customer enters the barbershop
                barberShop.Balk(c) #when customer enter in the barbershop
                customerInterval = random.randrange(MinIntervalOfCustomer,MaxIntervalOfCustomer+1)
                time.sleep(customerInterval) 
                
                        
