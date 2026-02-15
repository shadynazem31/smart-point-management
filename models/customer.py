# -*- coding: utf-8 -*-
"""
نموذج بيانات العميل
"""

from datetime import datetime
from database.db_manager import DatabaseManager

class Customer:
    def __init__(self, data=None):
        if data:
            self.id = data.get('id')
            self.code = data.get('code')
            self.pharmacy_name = data.get('pharmacy_name')
            self.owner_name = data.get('owner_name')
            self.classification = data.get('classification', 'individual')
            self.mobile_primary = data.get('mobile_primary')
            self.mobile_secondary = data.get('mobile_secondary')
            self.whatsapp = data.get('whatsapp')
            self.phone_landline = data.get('phone_landline')
            self.email = data.get('email')
            self.address = data.get('address')
            self.status = data.get('status', 'active')
            self.subscription_type = data.get('subscription_type', 'monthly')
            self.subscription_price = data.get('subscription_price', 150)
            self.notes = data.get('notes', '')
            self.created_at = data.get('created_at')
        else:
            self.id = None
            self.code = None
            self.pharmacy_name = ''
            self.owner_name = ''
            self.classification = 'individual'
            self.mobile_primary = ''
            self.mobile_secondary = ''
            self.whatsapp = ''
            self.phone_landline = ''
            self.email = ''
            self.address = ''
            self.status = 'active'
            self.subscription_type = 'monthly'
            self.subscription_price = 150
            self.notes = ''
            self.created_at = None
    
    @staticmethod
    def get_all():
        """الحصول على جميع العملاء"""
        db = DatabaseManager()
        conn = db.connect()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM customers ORDER BY created_at DESC')
        rows = cursor.fetchall()
        conn.close()
        
        customers = []
        for row in rows:
            customer_data = {
                'id': row[0],
                'code': row[1],
                'pharmacy_name': row[2],
                'owner_name': row[3],
                'classification': row[4],
                'mobile_primary': row[5],
                'status': row[10],
                'subscription_type': row[12],
                'subscription_price': row[13]
            }
            customers.append(Customer(customer_data))
        
        return customers
    
    @staticmethod
    def get_by_id(customer_id):
        """الحصول على عميل بواسطة ID"""
        db = DatabaseManager()
        conn = db.connect()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM customers WHERE id = ?', (customer_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return Customer({
                'id': row[0],
                'code': row[1],
                'pharmacy_name': row[2],
                'owner_name': row[3],
                'classification': row[4],
                'mobile_primary': row[5],
                'mobile_secondary': row[6],
                'whatsapp': row[7],
                'phone_landline': row[8],
                'email': row[9],
                'address': row[10],
                'status': row[11],
                'subscription_type': row[12],
                'subscription_price': row[13],
                'notes': row[14],
                'created_at': row[15]
            })
        return None
    
    def save(self):
        """حفظ بيانات العميل"""
        db = DatabaseManager()
        conn = db.connect()
        cursor = conn.cursor()
        
        if self.id:
            # تحديث
            cursor.execute('''
                UPDATE customers 
                SET pharmacy_name=?, owner_name=?, classification=?,
                    mobile_primary=?, mobile_secondary=?, whatsapp=?,
                    phone_landline=?, email=?, address=?, status=?,
                    subscription_type=?, subscription_price=?, notes=?,
                    updated_at=?
                WHERE id=?
            ''', (self.pharmacy_name, self.owner_name, self.classification,
                  self.mobile_primary, self.mobile_secondary, self.whatsapp,
                  self.phone_landline, self.email, self.address, self.status,
                  self.subscription_type, self.subscription_price, self.notes,
                  datetime.now(), self.id))
        else:
            # إضافة جديد
            cursor.execute('''
                INSERT INTO customers (
                    code, pharmacy_name, owner_name, classification,
                    mobile_primary, mobile_secondary, whatsapp,
                    phone_landline, email, address, status,
                    subscription_type, subscription_price, notes
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (self.code, self.pharmacy_name, self.owner_name, self.classification,
                  self.mobile_primary, self.mobile_secondary, self.whatsapp,
                  self.phone_landline, self.email, self.address, self.status,
                  self.subscription_type, self.subscription_price, self.notes))
            
            self.id = cursor.lastrowid
        
        conn.commit()
        conn.close()
        return True
