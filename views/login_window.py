# -*- coding: utf-8 -*-
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtCore import Qt
import hashlib
from database.db_manager import DatabaseManager

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart-Point - تسجيل الدخول")
        self.setFixedSize(400, 300)
        self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        
        layout = QVBoxLayout()
        
        title = QLabel("مرحباً بك في Smart-Point")
        title.setStyleSheet("font-size: 18pt; font-weight: bold; color: #2196F3;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        layout.addWidget(QLabel("اسم المستخدم:"))
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("admin")
        layout.addWidget(self.username_input)
        
        layout.addWidget(QLabel("كلمة المرور:"))
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setPlaceholderText("admin123")
        layout.addWidget(self.password_input)
        
        login_btn = QPushButton("تسجيل الدخول")
        login_btn.clicked.connect(self.login)
        layout.addWidget(login_btn)
        
        self.setLayout(layout)
    
    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        
        if not username or not password:
            QMessageBox.warning(self, "خطأ", "الرجاء إدخال اسم المستخدم وكلمة المرور!")
            return
        
        db = DatabaseManager()
        conn = db.connect()
        cursor = conn.cursor()
        
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        cursor.execute('''
            SELECT * FROM users WHERE username = ? AND password_hash = ?
        ''', (username, password_hash))
        
        user = cursor.fetchone()
        conn.close()
        
        if user:
            from views.main_window import MainWindow
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()
        else:
            QMessageBox.warning(self, "خطأ", "اسم المستخدم أو كلمة المرور غير صحيحة!")
