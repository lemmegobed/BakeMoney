from django.shortcuts import render,redirect
from .models import Transaction
from django.db.models import Sum  
from .models import *  

def home(request):
    # ดึงข้อมูลทั้งหมด
    transactions = Transaction.objects.all().order_by('-date')[:5]  # รายการล่าสุด 5 รายการ
    total_income = Transaction.objects.filter(category='income').aggregate(total=models.Sum('amount'))['total'] or 0
    total_expense = Transaction.objects.filter(category='expense').aggregate(total=models.Sum('amount'))['total'] or 0
    balance = total_income - total_expense

    context = {
        'transactions': transactions,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
    }
    return render(request, 'member/home.html', context)

def add_transaction(request):
    # ตรวจสอบว่าเป็นการร้องขอแบบ POST หรือไม่
    if request.method == 'POST':
        amount = request.POST['amount']  # จำนวนเงิน
        category = request.POST['category']  # หมวดหมู่ (รายรับ หรือ รายจ่าย)
        description = request.POST['description']  # คำอธิบาย
        
        # สร้างรายการการเงินใหม่
        transaction = Transaction(amount=amount, category=category, description=description)
        transaction.save()  # บันทึกลงในฐานข้อมูล
        
        return redirect('home')  # เปลี่ยนไปหน้าแรกหลังบันทึกข้อมูล

    return render(request, 'member/add.html')  # แสดงฟอร์มสำหรับเพิ่มข้อมูล