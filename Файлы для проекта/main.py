import sqlite3
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget,
                             QApplication,
                             QMessageBox,
                             QListWidgetItem,
                             QDialog,
                             QInputDialog)

from tasks import Ui_Form as tasksForm
from categories import Ui_Form as categoriesForm

DATABASE_NAME = 'tasks_db.db'


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


def createTables(con):
    try:
        with con:
            con.execute("""
                CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL UNIQUE
                );
            """)
            con.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL UNIQUE,
                description TEXT NULL,
                done INTEGER NOT NULL DEFAULT 0,
                category_id INTEGER NOT NULL,
                FOREIGN KEY (category_id) REFERENCES categories (id) 
                ON DELETE CASCADE
                );
            """)
    except sqlite3.DatabaseError as e:
        print(f'{e.__class__.__name__}: {e}')
        sys.exit(-1)


class Categories(QDialog, categoriesForm):
    def __init__(self, con):
        super().__init__()
        self.setupUi(self)
        self.con = con
        # вывод данных и подключение сигналов виджетов
        # ...

    def loadCategories(self):
        """Загрузка и вывод категорий в categoriesList."""
        # ...

    def addCategory(self):
        """Добавление категории с помощью ввода
        имени категории в QInputDialog.
        """
        # ...

    def deleteCategory(self):
        """Удаление категории с подтверждением через QMessageBox."""
        # ...


class Tasks(QWidget, tasksForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect(DATABASE_NAME)
        createTables(self.con)
        self.con.execute("PRAGMA foreign_keys = 1")
        # вывод данных и подключение сигналов виджетов
        # ...
        self.categoriesButton.clicked.connect(self.showCategories)

    def loadTasks(self):
        """Загрузка и вывод задач в tasksList.
        Выполненные задачи выводятся со статусом CheckState.Checked.
        Если в filterCategory установлено значение категории, то выводятся
        только задачи выбранной категории.
        """
        # ...

    def loadCategories(self):
        """Загрузка и вывод задач в виджеты
        selectCategory и filterCategory.
        """
        # ...

    def taskDetail(self, item):
        """Вывод подробностей задачи в
        taskTitle, taskDescription, selectCategory
        при выделении задачи в tasksList и
        изменение поля done задачи в базе данных.
        """
        # ...

    def addTask(self):
        """Добавление задачи в базу данных со значениями полей
        taskTitle, taskDescription, selectCategory.
        """
        # ...

    def deleteTask(self):
        """Удаление задачи с подтверждением через QMessageBox."""
        # ...

    def showCategories(self):
        """Открытие модального окна Categories."""
        self.categoriesWindow = Categories(self.con)
        self.categoriesWindow.exec()
        self.loadTasks()
        self.loadCategories()


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    window = Tasks()
    window.show()
    sys.exit(app.exec())
