# -*- coding: utf-8 -*-
"""
نموذج بيانات التعاقد
"""

from datetime import datetime
from database.db_manager import DatabaseManager

class Contract:
    def __init__(self, data=None):
        if data:
            self.id = data.get('id')
            self.contract_number = data.get('contract_number')
            self.customer_id = data.get('customer_id')
            self.contract_type = data.get('contract_type', 'new')
            self.subscription_type = data.get('subscription_type', 'monthly')
            self.start_date = data.get('start_date')
            self.end_date = data.get('end_date')
            self.total_amount = data.get('total_amount', 0)
            self.final_amount = data.get('final_amount', 0)
            self.status = data.get('status', 'active')
            self.created_at = data.get('created_at')
        else:
            self.id = None
            self.contract_number = None
            self.customer_id = None
            self.contract_type = 'new'
            self.subscription_type = 'monthly'
            self.start_date = None
            self.end_date = None
            self.total_amount = 0
            self.final_amount = 0
            self.status = 'active'
            self.created_at = None
    
    @staticmethod
    def get_all():
        """الحصول على جميع التعاقدات"""
        db = DatabaseManager()
        conn = db.connect()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM contracts ORDER BY created_at DESC')
        rows = cursor.fetchall()
        conn.close()
        
        contracts = []
        for row in rows:
            contract_data = {
                'id': row[0],
                'contract_number': row[1],
                'customer_id': row[2],
                'contract_type': row[3],
                'subscription_type': row[4],
                'start_date': row[5],
                'end_date': row[6],
                'total_amount': row[7],
                'final_amount': row[9],
                'status': row[11],
                'created_at': row[14]
            }
            contracts.append(Contract(contract_data))
        
        return contracts
