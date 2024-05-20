import logging
import os
log_folder='logs'
log_file='logs/current.log'
os.makedirs(log_folder,exist_ok=True)
string='[%(asctime)s:line_number:%(lineno)d: %(name)s: %(levelname)s: %(message)s]'
logging.basicConfig(level=logging.DEBUG, format=string, handlers=[logging.FileHandler(log_file)])
logger=logging.getLogger('mylog')

class Atm():
    def __init__(self):
        while True:
            try:
                initial_balance=float(input('enter initial balance'))
                if initial_balance<=0:
                    raise ValueError ('balance can not be negetive')
                elif type(initial_balance)!=float:
                    raise TypeError("balance can't be string")
                else:
                    break
            except Exception as e:
                logger.error(e)
        self.balance=initial_balance
        while True:
            try:
                pin=int(input('set your pin'))
                if len(str(pin))<4:
                    raise ValueError ('set a pin more than 4 digits')
                elif type(pin)!=int:
                    raise TypeError("pin can't be a string")
                else:
                    print('successfully pin set')
                    break
            except Exception as e:
                logger.warning(e)
            
        self.pin=pin
        menus=input('select menu..'"""
        1- change pin
        2- balance inquery
        3- withdraw
        4- exit """)
        if menus=='1':
            self.change_pin()
        elif menus=='2':
            self.balance_inquery()
        elif menus =='3':
            self.withdraw()
        else:
            exit()
    def change_pin(self):
        count=0
        while count!=3:
            pin1=int(input('enter old pin'))
            if pin1!=self.pin:
                logger.warning('wrong pin')
                count+=1
            else: break
        while True:
            pin2=int(input('enter new pin'))
            if type(pin2)!=int:
                logger.warning("pin can't be string")
            else: break
        self.pin=pin2
        logger.info('successfully pin changed')
        print('pin changed')
    def balance_inquery(self):
        count=0
        while count!=3:
            pin=int(input('enter your pin'))
            if pin!=self.pin:
                print('wrong password')
                count+=1
            else:
                logger.debug('log in success')
                break
        else:
            logger.critical('account blocked for next 24 hours')
            print('account blocked for next 24 hours')
            exit()
        print(self.balance)
    def withdraw(self):
        while True:
            try:
                amount=int(input('enter the amount'))
                if amount>self.balance:
                    raise ValueError('low balance')
                elif amount<0:
                    raise ValueError("amount can't be -ve")
                elif type(amount)!=int:
                    raise TypeError("amount can't be string")
                else:
                    break
            except Exception as e:
                logger.warning(e)
        count=0
        while count!=3:
            pin=int(input('enter your pin'))
            if pin!=self.pin:
                print('wrong password')
                count+=1
            else:
                logger.debug('log in success')
                break
        else:
            logger.critical('account blocked for next 24 hours')
            print('account blocked for next 24 hours')
            exit()
        self.balance=self.balance-amount
        print(f'amount deducted, balance is{self.balance}')

       
atm=Atm()


        
