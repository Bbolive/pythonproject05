#คำนวณหาภาษีที่ต้องจ่าย และเงินเดือนสุทธิของพนักงาน แล้วแสดงผลทางหน้าจอ 
#โดยรับค่ารหัสพนักงาน ชื่อพนักงาน และเงินเดือนปกติของพนักงานทางแป้นพิมพ์ ทั้งนี้เงินเดือนสุทธิของพนักงานนั้นจะต้องหักค่าภาษีและเบี้ยประกันสังคมออกจากเงินเดือนปกติเสียก่อน
#โดยที่พนักงานต้องเสียภาษี 7% ของเงินเดือนปกติ และจ่ายค่าเบี้ยประกันสังคม 500 บาท

#ขอ 5 ฟังก์ชัน ดังนั้นต้องหาให้ได้ 5 ฟังก์ชัน

#===================================================================
# คำนวณเงินเดือนของพนักงาน
#===================================================================
#ป้อนรหัสพนักงาน : <input>
#ป้อนชื่อพนักงาน : <input>
#ป้อนเงินเดือนปกติ :<input> บาท
#===================================================================
#ภาษีเป็นเงิน : <output> บาท (ขอทศนิยม 2 ตำแหน่ง)
#เงินเดือนสุทธิเป็นเงิน :<output> บาท
#===================================================================

def inputData( ):
    password = int(input('ป้อนรหัสพนักงาน '))
    name = input('ป้อนชื่อพนักงาน ')
    money = int(input('ป้อนเงินเดือนปกติของพนักงาน '))
    return password, name, money

def calMoneyVat( money ) :
    money_vat = money * 0.07
    return money_vat

def calMoneySocialSecurity( money ) :
    money_social_security = money - 500
    return money_social_security

def Net( money_vate, money_social_security) :
    net = money_social_security - money_vate
    return net

def showNetSaraly( money_vat, net) :
    print(f'ภาษี : {money_vat:.2f} บาท\nเงินเดือน : {net} บาท')

password, name, money = inputData()
showNetSaraly( calMoneyVat( money ), Net( calMoneyVat( money ), calMoneySocialSecurity( money )))