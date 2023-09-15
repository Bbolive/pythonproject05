#รับข้อมูลจำนวนเต็ม 5 จำนวนจากผู้ใช้ และคำนวณหาผลรวม และค่าเฉลี่ยของข้อมูลที่รับเข้ามาเป็นเท่าใด แล้วแสดงผลทางหน้าจอ

#ข้อ 4 ฟังก์ชัน ดังนั้นหาให้ได้ 4 ฟังก์ชัน

# ===================================================
# Program Averang 5 Number
# ===================================================
# Enter number 1 : <input>
# Enter number 2 : <input>
# Enter number 3 : <input>
# Enter number 4 : <input>
# Enter number 5 : <input>
# ===================================================
# Sum of 5 number is ; <output>
# Averang of 5 number is : <output> 

def inputNumber( ) :
    no1 = int(input('ป้อนจำนวนเต็มจำนวนที่ 1 '))
    no2 = int(input('ป้อนจำนวนเต็มจำนวนที่ 2 '))
    no3 = int(input('ป้อนจำนวนเต็มจำนวนที่ 3 '))
    no4 = int(input('ป้อนจำนวนเต็มจำนวนที่ 4 '))
    no5 = int(input('ป้อนจำนวนเต็มจำนวนที่ 5 '))
    return no1, no2, no3, no4, no5

def calSumNumber( no1, no2, no3, no4, no5 ) :
    sum_number = no1 + no2 + no3 + no4 + no5
    return sum_number
    
def calAverangeNumber( sum_number ) :
    averange_number =  sum_number/5
    return averange_number

def showProgramAverage( no1, no2, no3, no4, no5, sum_number, averange_number ) :
    print(f'จำนวนที่1 {no1}')
    print(f'จำนวนที่2 {no2}')
    print(f'จำนวนที่3 {no3}')
    print(f'จำนวนที่4 {no4}')
    print(f'จำนวนที่5 {no5}')
    print(f'ผลรวม {sum_number}')
    print(f'ค่าเฉลี่ย {averange_number}')

no1, no2, no3, no4, no5 = inputNumber()
sum_number = calSumNumber(no1, no2, no3, no4, no5)
averange_number = calAverangeNumber(sum_number)
print('--------------------------------------')
showProgramAverage( no1, no2, no3, no4, no5, sum_number, averange_number)
print('--------------------------------------')