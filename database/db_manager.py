# -*- coding: utf-8 -*-
import sqlite3
import hashlib
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_name='smart_point.db'):
        self.db_name = db_name
        self.conn = None
    
    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn
    
    def create_tables(self):
        conn = self.connect()
        cursor = conn.cursor()
        
        # جدول المستخدمين
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                full_name TEXT NOT NULL,
                role TEXT DEFAULT 'admin',
                is_active INTEGER DEFAULT 1,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_login DATETIME
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def init_default_data(self):
        conn = self.connect()
        cursor = conn.cursor()
        
        # إنشاء حساب admin افتراضي
        password = hashlib.sha256('admin123'.encode()).hexdigest()
        try:
            cursor.execute('''
                INSERT INTO users (username, password_hash, full_name, role)
                VALUES (?, ?, ?, ?)
            ''', ('admin', password, 'المدير', 'admin'))
            conn.commit()
        except:
            pass
        
        conn.close()
