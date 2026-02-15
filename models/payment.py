# -*- coding: utf-8 -*-
"""
نموذج بيانات الدفعات
"""

from datetime import datetime
from database.db_manager import DatabaseManager

class Payment:
    def __init__(self, data=None):
        if data:
            self.id = data.get('id')
            self.receipt_number = data.get('receipt_number')
            self.customer_id = data.get('customer_id')
            self.amount_paid = data.get('amount_paid', 0)
            self.payment_method = data.get('payment_method', 'cash')
            self.payment_date = data.get('payment_date')
            self.payment_type = data.get('payment_type', 'subscription')
            self.notes = data.get('notes', '')
            self.created_at = data.get('created_at')
        else:
            self.id = None
            self.receipt_number = None
            self.customer_id = None
            self.amount_paid = 0
            self.payment_method = 'cash'
            self.payment_date = None
            self.payment_type = 'subscription'
            self.notes = ''
            self.created_at = None
    
    @staticmethod
    def get_all():
        """الحصول على جميع المدفوعات"""
        db = DatabaseManager()
        conn = db.connect()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM payments ORDER BY payment_date DESC')
        rows = cursor.fetchall()
        conn.close()
        
        payments = []
        for row in rows:
            payment_data = {
                'id': row[0],
                'receipt_number': row[1],
                'customer_id': row[2],
                'amount_paid': row[4],
                'payment_method': row[6],
                'payment_date': row[8],
                'payment_type': row[9],
                'created_at': row[11]
            }
            payments.append(Payment(payment_data))
        
        return payments
