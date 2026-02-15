# -*- coding: utf-8 -*-
"""
Smart-Point Management System
نظام إدارة الاشتراكات والتحصيل
"""

import sys
import os
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database.db_manager import DatabaseManager
from views.login_window import LoginWindow

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Smart-Point Management")
    
    # إعداد الخط العربي
    try:
        font = QFont("Cairo", 10)
        app.setFont(font)
    except:
        font = QFont("Arial", 10)
        app.setFont(font)
    
    # تفعيل RTL للعربية
    app.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
    
    # إنشاء قاعدة البيانات
    db = DatabaseManager()
    if not os.path.exists('smart_point.db'):
        print("🔧 إنشاء قاعدة البيانات...")
        try:
            db.create_tables()
            db.init_default_data()
            print("✅ تم إنشاء قاعدة البيانات بنجاح!")
            print("=" * 50)
            print("📌 حساب الدخول الافتراضي:")
            print("   اسم المستخدم: admin")
            print("   كلمة المرور: admin123")
            print("=" * 50)
            
            QMessageBox.information(
                None,
                "مرحباً بك في Smart-Point",
                "تم إنشاء قاعدة البيانات بنجاح!\n\n"
                "📌 حساب الدخول الافتراضي:\n"
                "اسم المستخدم: admin\n"
                "كلمة المرور: admin123"
            )
        except Exception as e:
            print(f"❌ خطأ: {e}")
            QMessageBox.critical(None, "خطأ", f"فشل إنشاء قاعدة البيانات!\n\n{str(e)}")
            return
    
    # عرض شاشة تسجيل الدخول
    try:
        login = LoginWindow()
        login.show()
    except Exception as e:
        print(f"❌ خطأ: {e}")
        QMessageBox.critical(None, "خطأ", f"فشل تشغيل التطبيق!\n\n{str(e)}")
        return
    
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
