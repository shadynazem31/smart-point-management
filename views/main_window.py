# -*- coding: utf-8 -*-
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                            QPushButton, QLabel, QFrame, QMessageBox)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart-Point - نظام إدارة الاشتراكات")
        self.setMinimumSize(1200, 700)
        self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.setup_ui()
        self.show_dashboard()
    
    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        sidebar = self.create_sidebar()
        main_layout.addWidget(sidebar)
        
        self.content_area = QWidget()
        self.content_area.setStyleSheet("background-color: #f5f5f5;")
        self.content_layout = QVBoxLayout(self.content_area)
        main_layout.addWidget(self.content_area, 1)
    
    def create_sidebar(self):
        sidebar = QFrame()
        sidebar.setFixedWidth(250)
        sidebar.setStyleSheet("""
            QFrame {
                background-color: #2c3e50;
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
        """)
        
        layout = QVBoxLayout(sidebar)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        
        logo = QLabel("Smart-Point")
        logo.setStyleSheet("color: #1abc9c; font-size: 20pt; font-weight: bold; padding: 20px; background-color: #1a252f;")
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(logo)
        
        menu_items = [
            ("🏠 الرئيسية", self.show_dashboard),
            ("👥 العملاء", self.show_customers),
            ("📋 التعاقدات", self.show_contracts),
            ("💰 التحصيل", self.show_payments),
        ]
        
        for text, handler in menu_items:
            btn = QPushButton(text)
            btn.clicked.connect(handler)
            layout.addWidget(btn)
        
        layout.addStretch()
        
        exit_btn = QPushButton("🚪 خروج")
        exit_btn.clicked.connect(self.logout)
        exit_btn.setStyleSheet("QPushButton { background-color: #e74c3c; padding: 15px; }")
        layout.addWidget(exit_btn)
        
        return sidebar
    
    def clear_content(self):
        while self.content_layout.count():
            item = self.content_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
    
    def show_dashboard(self):
        self.clear_content()
        title = QLabel("📊 لوحة المعلومات")
        title.setStyleSheet("font-size: 24pt; font-weight: bold; color: #2c3e50; padding: 20px;")
        self.content_layout.addWidget(title)
        
        cards_layout = QHBoxLayout()
        cards_data = [
            ("👥 إجمالي العملاء", "100", "#3498db"),
            ("✅ عملاء نشطين", "85", "#2ecc71"),
            ("💰 المحصل هذا الشهر", "45,000 ج.م", "#1abc9c"),
        ]
        
        for title_text, value, color in cards_data:
            card = self.create_stat_card(title_text, value, color)
            cards_layout.addWidget(card)
        
        self.content_layout.addLayout(cards_layout)
        self.content_layout.addStretch()
    
    def create_stat_card(self, title, value, color):
        card = QFrame()
        card.setStyleSheet(f"QFrame {{ background-color: white; border-left: 5px solid {color}; padding: 15px; }}")
        layout = QVBoxLayout(card)
        title_label = QLabel(title)
        title_label.setStyleSheet("font-size: 11pt; color: #7f8c8d;")
        value_label = QLabel(value)
        value_label.setStyleSheet(f"font-size: 22pt; font-weight: bold; color: {color};")
        layout.addWidget(title_label)
        layout.addWidget(value_label)
        return card
    
    def show_customers(self):
        self.clear_content()
        label = QLabel("👥 إدارة العملاء")
        label.setStyleSheet("font-size: 24pt; padding: 20px;")
        self.content_layout.addWidget(label)
        self.content_layout.addStretch()
    
    def show_contracts(self):
        self.clear_content()
        label = QLabel("📋 إدارة التعاقدات")
        label.setStyleSheet("font-size: 24pt; padding: 20px;")
        self.content_layout.addWidget(label)
        self.content_layout.addStretch()
    
    def show_payments(self):
        self.clear_content()
        label = QLabel("💰 التحصيل والمدفوعات")
        label.setStyleSheet("font-size: 24pt; padding: 20px;")
        self.content_layout.addWidget(label)
        self.content_layout.addStretch()
    
    def logout(self):
        reply = QMessageBox.question(self, "تأكيد الخروج", "هل تريد تسجيل الخروج؟",
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.close()
