# -*- coding: utf-8 -*-
"""
النافذة الرئيسية للتطبيق
"""

from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                            QPushButton, QLabel, QFrame, QMessageBox)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart-Point - نظام إدارة الاشتراكات")
        self.setMinimumSize(1200, 700)
        self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        
        # الواجهة الرئيسية
        self.setup_ui()
        
        # عرض الشاشة الرئيسية
        self.show_dashboard()
    
    def setup_ui(self):
        """إعداد الواجهة"""
        # الويدجت الرئيسية
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # التخطيط الرئيسي
        main_layout = QHBoxLayout(central_widget)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # القائمة الجانبية
        sidebar = self.create_sidebar()
        main_layout.addWidget(sidebar)
        
        # منطقة المحتوى
        self.content_area = QWidget()
        self.content_area.setStyleSheet("background-color: #f5f5f5;")
        self.content_layout = QVBoxLayout(self.content_area)
        main_layout.addWidget(self.content_area, 1)
    
    def create_sidebar(self):
        """إنشاء القائمة الجانبية"""
        sidebar = QFrame()
        sidebar.setFixedWidth(250)
        sidebar.setStyleSheet("""
            QFrame {
                background-color: #2c3e50;
                border-right: 1px solid #34495e;
            }
            QPushButton {
                background-color: transparent;
                color: white;
                border: none;
                padding: 15px;
                text-align: right;
                font-size: 12pt;
            }
            QPushButton:hover {
                background-color: #34495e;
            }
            QPushButton:pressed {
                background-color: #1abc9c;
            }
        """)
        
        layout = QVBoxLayout(sidebar)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # الشعار
        logo = QLabel("Smart-Point")
        logo.setStyleSheet("""
            color: #1abc9c;
            font-size: 20pt;
            font-weight: bold;
            padding: 20px;
            background-color: #1a252f;
        """)
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(logo)
        
        # القائمة
        menu_items = [
            ("🏠 الرئيسية", self.show_dashboard),
            ("👥 العملاء", self.show_customers),
            ("📋 التعاقدات", self.show_contracts),
            ("💰 التحصيل", self.show_payments),
            ("💻 الأجهزة", self.show_devices),
            ("📱 الرسائل", self.show_messages),
            ("📊 التقارير", self.show_reports),
            ("⚙️ الإعدادات", self.show_settings),
        ]
        
        for text, handler in menu_items:
            btn = QPushButton(text)
            btn.clicked.connect(handler)
            layout.addWidget(btn)
        
        layout.addStretch()
        
        # زر الخروج
        exit_btn = QPushButton("🚪 خروج")
        exit_btn.clicked.connect(self.logout)
        exit_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                padding: 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        layout.addWidget(exit_btn)
        
        return sidebar
    
    def clear_content(self):
        """مسح المحتوى الحالي"""
        while self.content_layout.count():
            item = self.content_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
    
    def show_dashboard(self):
        """عرض الشاشة الرئيسية"""
        self.clear_content()
        
        # العنوان
        title = QLabel("📊 لوحة المعلومات")
        title.setStyleSheet("""
            font-size: 24pt;
            font-weight: bold;
            color: #2c3e50;
            padding: 20px;
        """)
        self.content_layout.addWidget(title)
        
        # البطاقات الإحصائية
        cards_layout = QHBoxLayout()
        
        cards_data = [
            ("👥 إجمالي العملاء", "100", "#3498db"),
            ("✅ عملاء نشطين", "85", "#2ecc71"),
            ("💰 المحصل هذا الشهر", "45,000 ج.م", "#1abc9c"),
            ("⏰ تنتهي قريباً", "12", "#e67e22"),
        ]
        
        for title_text, value, color in cards_data:
            card = self.create_stat_card(title_text, value, color)
            cards_layout.addWidget(card)
        
        self.content_layout.addLayout(cards_layout)
        self.content_layout.addStretch()
    
    def create_stat_card(self, title, value, color):
        """إنشاء بطاقة إحصائية"""
        card = QFrame()
        card.setStyleSheet(f"""
            QFrame {{
                background-color: white;
                border-left: 5px solid {color};
                border-radius: 8px;
                padding: 15px;
            }}
        """)
        
        layout = QVBoxLayout(card)
        
        title_label = QLabel(title)
        title_label.setStyleSheet("font-size: 11pt; color: #7f8c8d;")
        
        value_label = QLabel(value)
        value_label.setStyleSheet(f"font-size: 22pt; font-weight: bold; color: {color};")
        
        layout.addWidget(title_label)
        layout.addWidget(value_label)
        
        return card
    
    def show_customers(self):
        """عرض شاشة العملاء"""
        self.clear_content()
        label = QLabel("👥 إدارة العملاء")
        label.setStyleSheet("font-size: 24pt; padding: 20px;")
        self.content_layout.addWidget(label)
        
        info = QLabel("هذه الشاشة قيد التطوير...")
        info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.content_layout.addWidget(info)
        self.content_layout.addStretch()
    
    def show_contracts(self):
        """عرض شاشة التعاقدات"""
        self.clear_content()
        label = QLabel("📋 إدارة التعاقدات")
        label.setStyleSheet("font-size: 24pt; padding: 20px;")
        self.content_layout.addWidget(label)
        self.content_layout.addStretch()
    
    def show_payments(self):
        """عرض شاشة التحصيل"""
        self.clear_content()
        label = QLabel("💰 التحصيل والمدفوعات")
        label.setStyleSheet("font-size: 24pt; padding: 20px;")
        self.content_layout.addWidget(label)
        self.content_layout.addStretch()
    
    def show_devices(self):
        """عرض شاشة الأجهزة"""
        self.clear_content()
        label = QLabel("💻 إدارة الأجهزة")
        label.setStyleSheet("font-size: 24pt; padding: 20px;")
        self.content_layout.addWidget(label)
        self.content_layout.addStretch()
    
    def show_messages(self):
        """عرض شاشة الرسائل"""
        self.clear_content()
        label = QLabel("📱 الرسائل والتذكيرات")
        label.setStyleSheet("font-size: 24pt; padding: 20px;")
        self.content_layout.addWidget(label)
        self.content_layout.addStretch()
    
    def show_reports(self):
        """عرض شاشة التقارير"""
        self.clear_content()
        label = QLabel("📊 التقارير")
        label.setStyleSheet("font-size: 24pt; padding: 20px;")
        self.content_layout.addWidget(label)
        self.content_layout.addStretch()
    
    def show_settings(self):
        """عرض شاشة الإعدادات"""
        self.clear_content()
        label = QLabel("⚙️ الإعدادات")
        label.setStyleSheet("font-size: 24pt; padding: 20px;")
        self.content_layout.addWidget(label)
        self.content_layout.addStretch()
    
    def logout(self):
        """تسجيل الخروج"""
        reply = QMessageBox.question(
            self, "تأكيد الخروج",
            "هل تريد تسجيل الخروج؟",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessage
