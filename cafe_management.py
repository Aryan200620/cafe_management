import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from datetime import datetime


# ============================================================
# DATABASE CONNECTION
# ============================================================

DB_HOST = "localhost"
DB_USER = "root"

# CHANGE THIS TO YOUR MYSQL PASSWORD
DB_PASSWORD = "123456"

DB_NAME = "cafe_management"


def get_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )


# ============================================================
# COLORS
# ============================================================

DARK = "#2D1B12"
BROWN = "#6F4E37"
LIGHT_BROWN = "#EFE0CF"
CREAM = "#FAF7F2"
WHITE = "#FFFFFF"
GREEN = "#277D57"
RED = "#BE3C3C"
BLUE = "#3C64B4"
GRAY = "#666666"


# ============================================================
# MAIN APPLICATION
# ============================================================

class CafeApp:

    def __init__(self, root):

        self.root = root

        self.root.title("Cafe Management System")

        self.root.geometry("1200x750")

        self.root.minsize(1000, 650)

        self.root.configure(bg=CREAM)

        self.current_user = ""

        self.cart = []

        self.show_login()


    # ========================================================
    # CLEAR SCREEN
    # ========================================================

    def clear_screen(self):

        for widget in self.root.winfo_children():
            widget.destroy()


    # ========================================================
    # BUTTON
    # ========================================================

    def create_button(
        self,
        parent,
        text,
        command,
        color=BROWN,
        width=15
    ):

        button = tk.Button(
            parent,
            text=text,
            command=command,
            bg=color,
            fg="white",
            activebackground=color,
            activeforeground="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            cursor="hand2",
            width=width,
            padx=8,
            pady=8
        )

        return button


    # ========================================================
    # LOGIN
    # ========================================================

    def show_login(self):

        self.clear_screen()

        self.root.geometry("500x450")

        main = tk.Frame(
            self.root,
            bg=CREAM
        )

        main.pack(
            fill="both",
            expand=True
        )

        # ----------------------------------------------------
        # HEADER
        # ----------------------------------------------------

        header = tk.Frame(
            main,
            bg=DARK,
            height=110
        )

        header.pack(
            fill="x"
        )

        tk.Label(
            header,
            text="☕ CAFE",
            bg=DARK,
            fg="white",
            font=("Segoe UI", 30, "bold")
        ).pack(pady=(20, 0))

        tk.Label(
            header,
            text="Management System",
            bg=DARK,
            fg="#E8D8C8",
            font=("Segoe UI", 12)
        ).pack()

        # ----------------------------------------------------
        # FORM
        # ----------------------------------------------------

        form = tk.Frame(
            main,
            bg=CREAM
        )

        form.pack(
            pady=35
        )

        tk.Label(
            form,
            text="Username",
            bg=CREAM,
            font=("Segoe UI", 12, "bold")
        ).grid(
            row=0,
            column=0,
            sticky="w",
            pady=8
        )

        self.username_entry = tk.Entry(
            form,
            font=("Segoe UI", 12),
            width=25
        )

        self.username_entry.grid(
            row=1,
            column=0,
            pady=(0, 10)
        )

        tk.Label(
            form,
            text="Password",
            bg=CREAM,
            font=("Segoe UI", 12, "bold")
        ).grid(
            row=2,
            column=0,
            sticky="w",
            pady=8
        )

        self.password_entry = tk.Entry(
            form,
            show="*",
            font=("Segoe UI", 12),
            width=25
        )

        self.password_entry.grid(
            row=3,
            column=0,
            pady=(0, 15)
        )

        login_button = self.create_button(
            form,
            "LOGIN",
            self.login,
            BROWN,
            20
        )

        login_button.grid(
            row=4,
            column=0,
            pady=10
        )

        tk.Label(
            form,
            text="Default login: admin / admin123",
            bg=CREAM,
            fg=GRAY,
            font=("Segoe UI", 9)
        ).grid(
            row=5,
            column=0,
            pady=5
        )

        self.username_entry.focus()

        self.password_entry.bind(
            "<Return>",
            lambda event: self.login()
        )


    # ========================================================
    # LOGIN CHECK
    # ========================================================

    def login(self):

        username = self.username_entry.get().strip()

        password = self.password_entry.get()

        if not username or not password:

            messagebox.showwarning(
                "Login",
                "Please enter username and password."
            )

            return

        try:

            connection = get_connection()

            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT id
                FROM users
                WHERE username = %s
                AND password = %s
                """,
                (username, password)
            )

            result = cursor.fetchone()

            cursor.close()

            connection.close()

            if result:

                self.current_user = username

                self.show_dashboard()

            else:

                messagebox.showerror(
                    "Login Failed",
                    "Invalid username or password."
                )

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )


    # ========================================================
    # DASHBOARD
    # ========================================================

    def show_dashboard(self):

        self.clear_screen()

        self.root.geometry("1200x750")

        # ====================================================
        # SIDEBAR
        # ====================================================

        sidebar = tk.Frame(
            self.root,
            bg=DARK,
            width=220
        )

        sidebar.pack(
            side="left",
            fill="y"
        )

        sidebar.pack_propagate(False)

        tk.Label(
            sidebar,
            text="☕ CAFE",
            bg=DARK,
            fg="white",
            font=("Segoe UI", 26, "bold")
        ).pack(
            pady=(25, 5)
        )

        tk.Label(
            sidebar,
            text="Management",
            bg=DARK,
            fg="#E8D8C8",
            font=("Segoe UI", 11)
        ).pack(
            pady=(0, 25)
        )

        self.sidebar_button(
            sidebar,
            "🏠  Dashboard",
            self.show_dashboard
        )

        self.sidebar_button(
            sidebar,
            "🍔  Menu",
            self.show_menu
        )

        self.sidebar_button(
            sidebar,
            "🛒  Orders",
            self.show_orders
        )

        self.sidebar_button(
            sidebar,
            "👥  Customers",
            self.show_customers
        )

        self.sidebar_button(
            sidebar,
            "👨‍💼  Employees",
            self.show_employees
        )

        self.sidebar_button(
            sidebar,
            "📊  Sales",
            self.show_sales
        )

        spacer = tk.Frame(
            sidebar,
            bg=DARK
        )

        spacer.pack(
            expand=True,
            fill="both"
        )

        self.sidebar_button(
            sidebar,
            "🚪  Logout",
            self.logout
        )

        # ====================================================
        # MAIN AREA
        # ====================================================

        content = tk.Frame(
            self.root,
            bg=CREAM
        )

        content.pack(
            side="left",
            fill="both",
            expand=True
        )

        # ----------------------------------------------------
        # HEADER
        # ----------------------------------------------------

        header = tk.Frame(
            content,
            bg=WHITE,
            height=75
        )

        header.pack(
            fill="x"
        )

        tk.Label(
            header,
            text="Dashboard",
            bg=WHITE,
            fg=DARK,
            font=("Segoe UI", 25, "bold")
        ).pack(
            side="left",
            padx=25,
            pady=20
        )

        tk.Label(
            header,
            text=f"Welcome, {self.current_user}",
            bg=WHITE,
            fg=GRAY,
            font=("Segoe UI", 11)
        ).pack(
            side="right",
            padx=25
        )

        # ----------------------------------------------------
        # DASHBOARD CONTENT
        # ----------------------------------------------------

        body = tk.Frame(
            content,
            bg=CREAM
        )

        body.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=25
        )

        # ----------------------------------------------------
        # CARDS
        # ----------------------------------------------------

        cards = tk.Frame(
            body,
            bg=CREAM
        )

        cards.pack(
            fill="x"
        )

        cards.columnconfigure(
            (0, 1, 2, 3),
            weight=1
        )

        order_count = self.get_count(
            "orders"
        )

        customer_count = self.get_count(
            "customers"
        )

        employee_count = self.get_count(
            "employees"
        )

        sales = self.get_total_sales()

        self.dashboard_card(
            cards,
            0,
            "🛒",
            "Total Orders",
            str(order_count),
            BLUE
        )

        self.dashboard_card(
            cards,
            1,
            "👥",
            "Customers",
            str(customer_count),
            GREEN
        )

        self.dashboard_card(
            cards,
            2,
            "💰",
            "Total Sales",
            f"₹{sales:.2f}",
            BROWN
        )

        self.dashboard_card(
            cards,
            3,
            "👨‍💼",
            "Employees",
            str(employee_count),
            RED
        )

        # ----------------------------------------------------
        # WELCOME PANEL
        # ----------------------------------------------------

        welcome = tk.Frame(
            body,
            bg=WHITE,
            highlightbackground="#E0D8D0",
            highlightthickness=1
        )

        welcome.pack(
            fill="both",
            expand=True,
            pady=(30, 0)
        )

        tk.Label(
            welcome,
            text="☕ Welcome to your Cafe!",
            bg=WHITE,
            fg=DARK,
            font=("Segoe UI", 22, "bold")
        ).pack(
            pady=(50, 10)
        )

        tk.Label(
            welcome,
            text=(
                "Manage your cafe from one place.\n\n"
                "🍔 Manage menu items\n"
                "🛒 Create customer orders\n"
                "👥 Manage customers\n"
                "👨‍💼 Manage employees\n"
                "📊 Track sales and revenue"
            ),
            bg=WHITE,
            fg=GRAY,
            font=("Segoe UI", 13),
            justify="center"
        ).pack()


    # ========================================================
    # SIDEBAR BUTTON
    # ========================================================

    def sidebar_button(
        self,
        parent,
        text,
        command
    ):

        button = tk.Button(
            parent,
            text=text,
            command=command,
            bg=DARK,
            fg="white",
            activebackground=BROWN,
            activeforeground="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            anchor="w",
            padx=25,
            cursor="hand2"
        )

        button.pack(
            fill="x",
            pady=2
        )

        return button


    # ========================================================
    # DASHBOARD CARD
    # ========================================================

    def dashboard_card(
        self,
        parent,
        column,
        icon,
        title,
        value,
        color
    ):

        card = tk.Frame(
            parent,
            bg=WHITE,
            height=130,
            highlightbackground="#E0D8D0",
            highlightthickness=1
        )

        card.grid(
            row=0,
            column=column,
            sticky="nsew",
            padx=7
        )

        tk.Label(
            card,
            text=icon,
            bg=WHITE,
            fg=color,
            font=("Segoe UI", 24)
        ).pack(
            anchor="w",
            padx=18,
            pady=(15, 0)
        )

        tk.Label(
            card,
            text=title,
            bg=WHITE,
            fg=GRAY,
            font=("Segoe UI", 11, "bold")
        ).pack(
            anchor="w",
            padx=18
        )

        tk.Label(
            card,
            text=value,
            bg=WHITE,
            fg=color,
            font=("Segoe UI", 23, "bold")
        ).pack(
            anchor="w",
            padx=18
        )


    # ========================================================
    # DATABASE HELPERS
    # ========================================================

    def get_count(self, table):

        try:

            connection = get_connection()

            cursor = connection.cursor()

            cursor.execute(
                f"SELECT COUNT(*) FROM {table}"
            )

            result = cursor.fetchone()[0]

            cursor.close()

            connection.close()

            return result

        except:

            return 0


    def get_total_sales(self):

        try:

            connection = get_connection()

            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT COALESCE(SUM(total), 0)
                FROM orders
                """
            )

            result = cursor.fetchone()[0]

            cursor.close()

            connection.close()

            return float(result)

        except:

            return 0


    # ========================================================
    # MENU
    # ========================================================

    def show_menu(self):

        self.clear_screen()

        self.create_layout(
            "Menu Management"
        )

        # ====================================================
        # FORM
        # ====================================================

        form = tk.Frame(
            self.main_content,
            bg=WHITE
        )

        form.pack(
            fill="x",
            padx=20,
            pady=20
        )

        tk.Label(
            form,
            text="Item Name",
            bg=WHITE
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        self.menu_name = tk.Entry(
            form,
            width=15
        )

        self.menu_name.grid(
            row=1,
            column=0,
            padx=5
        )

        tk.Label(
            form,
            text="Category",
            bg=WHITE
        ).grid(
            row=0,
            column=1,
            padx=5
        )

        self.menu_category = tk.Entry(
            form,
            width=15
        )

        self.menu_category.grid(
            row=1,
            column=1,
            padx=5
        )

        tk.Label(
            form,
            text="Price",
            bg=WHITE
        ).grid(
            row=0,
            column=2,
            padx=5
        )

        self.menu_price = tk.Entry(
            form,
            width=12
        )

        self.menu_price.grid(
            row=1,
            column=2,
            padx=5
        )

        tk.Label(
            form,
            text="Stock",
            bg=WHITE
        ).grid(
            row=0,
            column=3,
            padx=5
        )

        self.menu_stock = tk.Entry(
            form,
            width=10
        )

        self.menu_stock.grid(
            row=1,
            column=3,
            padx=5
        )

        self.create_button(
            form,
            "Add Item",
            self.add_menu,
            GREEN
        ).grid(
            row=1,
            column=4,
            padx=5
        )

        self.create_button(
            form,
            "Update",
            self.update_menu,
            BLUE
        ).grid(
            row=1,
            column=5,
            padx=5
        )

        self.create_button(
            form,
            "Delete",
            self.delete_menu,
            RED
        ).grid(
            row=1,
            column=6,
            padx=5
        )

        # ====================================================
        # TABLE
        # ====================================================

        table_frame = tk.Frame(
            self.main_content,
            bg=CREAM
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        columns = (
            "ID",
            "Item Name",
            "Category",
            "Price",
            "Stock"
        )

        self.menu_table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        for column in columns:

            self.menu_table.heading(
                column,
                text=column
            )

            self.menu_table.column(
                column,
                width=130
            )

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.menu_table.yview
        )

        self.menu_table.configure(
            yscrollcommand=scrollbar.set
        )

        self.menu_table.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.menu_table.bind(
            "<<TreeviewSelect>>",
            self.menu_selected
        )

        self.load_menu()


    # ========================================================
    # LOAD MENU
    # ========================================================

    def load_menu(self):

        for row in self.menu_table.get_children():

            self.menu_table.delete(row)

        try:

            connection = get_connection()

            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT id, item_name, category,
                       price, quantity
                FROM menu
                ORDER BY id DESC
                """
            )

            rows = cursor.fetchall()

            for row in rows:

                self.menu_table.insert(
                    "",
                    "end",
                    values=row
                )

            cursor.close()

            connection.close()

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )


    # ========================================================
    # MENU SELECT
    # ========================================================

    def menu_selected(self, event):

        selected = self.menu_table.selection()

        if not selected:
            return

        values = self.menu_table.item(
            selected[0]
        )["values"]

        self.menu_name.delete(0, tk.END)
        self.menu_name.insert(0, values[1])

        self.menu_category.delete(0, tk.END)
        self.menu_category.insert(0, values[2])

        self.menu_price.delete(0, tk.END)
        self.menu_price.insert(0, values[3])

        self.menu_stock.delete(0, tk.END)
        self.menu_stock.insert(0, values[4])


    # ========================================================
    # ADD MENU
    # ========================================================

    def add_menu(self):

        try:

            name = self.menu_name.get().strip()

            category = self.menu_category.get().strip()

            price = float(
                self.menu_price.get()
            )

            stock = int(
                self.menu_stock.get()
            )

            if not name or not category:

                raise ValueError(
                    "Please enter item name and category."
                )

            connection = get_connection()

            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO menu
                (item_name, category, price, quantity)
                VALUES (%s, %s, %s, %s)
                """,
                (
                    name,
                    category,
                    price,
                    stock
                )
            )

            connection.commit()

            cursor.close()

            connection.close()

            messagebox.showinfo(
                "Success",
                "Menu item added successfully!"
            )

            self.clear_menu_fields()

            self.load_menu()

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )


    # ========================================================
    # UPDATE MENU
    # ========================================================

    def update_menu(self):

        selected = self.menu_table.selection()

        if not selected:

            messagebox.showwarning(
                "Update",
                "Select an item from the table first."
            )

            return

        values = self.menu_table.item(
            selected[0]
        )["values"]

        item_id = values[0]

        try:

            name = self.menu_name.get()

            category = self.menu_category.get()

            price = float(
                self.menu_price.get()
            )

            stock = int(
                self.menu_stock.get()
            )

            connection = get_connection()

            cursor = connection.cursor()

            cursor.execute(
                """
                UPDATE menu
                SET item_name=%s,
                    category=%s,
                    price=%s,
                    quantity=%s
                WHERE id=%s
                """,
                (
                    name,
                    category,
                    price,
                    stock,
                    item_id
                )
            )

            connection.commit()

            cursor.close()

            connection.close()

            messagebox.showinfo(
                "Success",
                "Menu item updated!"
            )

            self.load_menu()

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )


    # ========================================================
    # DELETE MENU
    # ========================================================

    def delete_menu(self):

        selected = self.menu_table.selection()

        if not selected:

            messagebox.showwarning(
                "Delete",
                "Select an item from the table first."
            )

            return

        values = self.menu_table.item(
            selected[0]
        )["values"]

        item_id = values[0]

        answer = messagebox.askyesno(
            "Confirm Delete",
            f"Delete '{values[1]}'?"
        )

        if not answer:
            return

        try:

            connection = get_connection()

            cursor = connection.cursor()

            cursor.execute(
                "DELETE FROM menu WHERE id=%s",
                (item_id,)
            )

            connection.commit()

            cursor.close()

            connection.close()

            messagebox.showinfo(
                "Deleted",
                "Menu item deleted."
            )

            self.clear_menu_fields()

            self.load_menu()

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )


    def clear_menu_fields(self):

        self.menu_name.delete(0, tk.END)

        self.menu_category.delete(0, tk.END)

        self.menu_price.delete(0, tk.END)

        self.menu_stock.delete(0, tk.END)


    # ========================================================
    # CUSTOMERS
    # ========================================================

    def show_customers(self):

        self.clear_screen()

        self.create_layout(
            "Customer Management"
        )

        form = tk.Frame(
            self.main_content,
            bg=WHITE
        )

        form.pack(
            fill="x",
            padx=20,
            pady=20
        )

        tk.Label(
            form,
            text="Customer Name",
            bg=WHITE
        ).grid(
            row=0,
            column=0
        )

        self.customer_name = tk.Entry(
            form,
            width=20
        )

        self.customer_name.grid(
            row=1,
            column=0,
            padx=10
        )

        tk.Label(
            form,
            text="Phone",
            bg=WHITE
        ).grid(
            row=0,
            column=1
        )

        self.customer_phone = tk.Entry(
            form,
            width=15
        )

        self.customer_phone.grid(
            row=1,
            column=1,
            padx=10
        )

        self.create_button(
            form,
            "Add",
            self.add_customer,
            GREEN
        ).grid(
            row=1,
            column=2,
            padx=5
        )

        self.create_button(
            form,
            "Update",
            self.update_customer,
            BLUE
        ).grid(
            row=1,
            column=3,
            padx=5
        )

        self.create_button(
            form,
            "Delete",
            self.delete_customer,
            RED
        ).grid(
            row=1,
            column=4,
            padx=5
        )

        # TABLE

        frame = tk.Frame(
            self.main_content,
            bg=CREAM
        )

        frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        columns = (
            "ID",
            "Name",
            "Phone"
        )

        self.customer_table = ttk.Treeview(
            frame,
            columns=columns,
            show="headings"
        )

        for column in columns:

            self.customer_table.heading(
                column,
                text=column
            )

            self.customer_table.column(
                column,
                width=200
            )

        self.customer_table.pack(
            fill="both",
            expand=True
        )

        self.customer_table.bind(
            "<<TreeviewSelect>>",
            self.customer_selected
        )

        self.load_customers()


    def load_customers(self):

        for row in self.customer_table.get_children():

            self.customer_table.delete(row)

        try:

            connection = get_connection()

            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT id, name, phone
                FROM customers
                ORDER BY id DESC
                """
            )

            for row in cursor.fetchall():

                self.customer_table.insert(
                    "",
                    "end",
                    values=row
                )

            cursor.close()

            connection.close()

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )


    def customer_selected(self, event):

        selected = self.customer_table.selection()

        if not selected:
            return

        values = self.customer_table.item(
            selected[0]
        )["values"]

        self.customer_name.delete(
            0,
            tk.END
        )

        self.customer_name.insert(
            0,
            values[1]
        )

        self.customer_phone.delete(
            0,
            tk.END
        )

        self.customer_phone.insert(
            0,
            values[2]
        )


    def add_customer(self):

        name = self.customer_name.get().strip()

        phone = self.customer_phone.get().strip()

        if not name:

            messagebox.showwarning(
                "Customer",
                "Enter customer name."
            )

            return

        try:

            connection = get_connection()

            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO customers
                (name, phone)
                VALUES (%s, %s)
                """,
                (name, phone)
            )

            connection.commit()

            cursor.close()

            connection.close()

            messagebox.showinfo(
                "Success",
                "Customer added!"
            )

            self.customer_name.delete(
                0,
                tk.END
            )

            self.customer_phone.delete(
                0,
                tk.END
            )

            self.load_customers()

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )


    def update_customer(self):

        selected = self.customer_table.selection()

        if not selected:

            messagebox.showwarning(
                "Update",
                "Select a customer first."
            )

            return

        values = self.customer_table.item(
            selected[0]
        )["values"]

        customer_id = values[0]

        try:

            connection = get_connection()

            cursor = connection.cursor()

            cursor.execute(
                """
                UPDATE customers
                SET name=%s,
                    phone=%s
                WHERE id=%s
                """,
                (
                    self.customer_name.get(),
                    self.customer_phone.get(),
                    customer_id
                )
            )

            connection.commit()

            cursor.close()

            connection.close()

            messagebox.showinfo(
                "Success",
                "Customer updated!"
            )

            self.load_customers()

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )


    def delete_customer(self):

        selected = self.customer_table.selection()

        if not selected:

            messagebox.showwarning(
                "Delete",
                "Select a customer first."
            )

            return

        values = self.customer_table.item(
            selected[0]
        )["values"]

        customer_id = values[0]

        if not messagebox.askyesno(
            "Confirm",
            f"Delete '{values[1]}'?"
        ):

            return

        try:

            connection = get_connection()

            cursor = connection.cursor()

            cursor.execute(
                "DELETE FROM customers WHERE id=%s",
                (customer_id,)
            )

            connection.commit()

            cursor.close()

            connection.close()

            messagebox.showinfo(
                "Deleted",
                "Customer deleted."
            )

            self.load_customers()

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )


    # ========================================================
    # EMPLOYEES
    # ========================================================

    def show_employees(self):

        self.clear_screen()

        self.create_layout(
            "Employee Management"
        )

        form = tk.Frame(
            self.main_content,
            bg=WHITE
        )

        form.pack(
            fill="x",
            padx=20,
            pady=20
        )

        labels = [
            "Name",
            "Phone",
            "Role",
            "Salary"
        ]

        for i, label in enumerate(labels):

            tk.Label(
                form,
                text=label,
                bg=WHITE
            ).grid(
                row=0,
                column=i,
                padx=5
            )

        self.employee_name = tk.Entry(
            form,
            width=15
        )

        self.employee_name.grid(
            row=1,
            column=0,
            padx=5
        )

        self.employee_phone = tk.Entry(
            form,
            width=13
        )

        self.employee_phone.grid(
            row=1,
            column=1,
            padx=5
        )

        self.employee_role = tk.Entry(
            form,
            width=13
        )

        self.employee_role.grid(
            row=1,
            column=2,
            padx=5
        )

        self.employee_salary = tk.Entry(
            form,
            width=12
        )

        self.employee_salary.grid(
            row=1,
            column=3,
            padx=5
        )

        self.create_button(
            form,
            "Add",
            self.add_employee,
            GREEN
        ).grid(
            row=1,
            column=4,
            padx=5
        )

        self.create_button(
            form,
            "Update",
            self.update_employee,
            BLUE
        ).grid(
            row=1,
            column=5,
            padx=5
        )

        self.create_button(
            form,
            "Delete",
            self.delete_employee,
            RED
        ).grid(
            row=1,
            column=6,
            padx=5
        )

        # TABLE

        frame = tk.Frame(
            self.main_content,
            bg=CREAM
        )

        frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        columns = (
            "ID",
            "Name",
            "Phone",
            "Role",
            "Salary"
        )

        self.employee_table = ttk.Treeview(
            frame,
            columns=columns,
            show="headings"
        )

        for column in columns:

            self.employee_table.heading(
                column,
                text=column
            )

            self.employee_table.column(
                column,
                width=150
            )

        self.employee_table.pack(
            fill="both",
            expand=True
        )

        self.employee_table.bind(
            "<<TreeviewSelect>>",
            self.employee_selected
        )

        self.load_employees()


    def load_employees(self):

        for row in self.employee_table.get_children():

            self.employee_table.delete(row)

        try:

            connection = get_connection()

            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT id, name, phone,
                       role, salary
                FROM employees
                ORDER BY id DESC
                """
            )

            for row in cursor.fetchall():

                self.employee_table.insert(
                    "",
                    "end",
                    values=row
                )

            cursor.close()

            connection.close()

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )


    def employee_selected(self, event):

        selected = self.employee_table.selection()

        if not selected:
            return

        values = self.employee_table.item(
            selected[0]
        )["values"]

        entries = [
            self.employee_name,
            self.employee_phone,
            self.employee_role,
            self.employee_salary
        ]

        for entry, value in zip(
            entries,
            values[1:]
        ):

            entry.delete(
                0,
                tk.END
            )

            entry.insert(
                0,
                value
            )


    def add_employee(self):

        try:

            name = self.employee_name.get()

            phone = self.employee_phone.get()

            role = self.employee_role.get()

            salary = float(
                self.employee_salary.get()
            )

            connection = get_connection()

            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO employees
                (name, phone, role, salary)
                VALUES (%s, %s, %s, %s)
                """,
                (
                    name,
                    phone,
                    role,
                    salary
                )
            )

            connection.commit()

            cursor.close()

            connection.close()

            messagebox.showinfo(
                "Success",
                "Employee added!"
            )

            self.load_employees()

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )


    def update_employee(self):

        selected = self.employee_table.selection()

        if not selected:

            messagebox.showwarning(
                "Update",
                "Select an employee first."
            )

            return

        values = self.employee_table.item(
            selected[0]
        )["values"]

        employee_id = values[0]

        try:

            connection = get_connection()

            cursor = connection.cursor()

            cursor.execute(
                """
                UPDATE employees
                SET name=%s,
                    phone=%s,
                    role=%s,
                    salary=%s
                WHERE id=%s
                """,
                (
                    self.employee_name.get(),
                    self.employee_phone.get(),
                    self.employee_role.get(),
                    float(
                        self.employee_salary.get()
                    ),
                    employee_id
                )
            )

            connection.commit()

            cursor.close()

            connection.close()

            messagebox.showinfo(
                "Success",
                "Employee updated!"
            )

            self.load_employees()

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )


    def delete_employee(self):

        selected = self.employee_table.selection()

        if not selected:

            messagebox.showwarning(
                "Delete",
                "Select an employee first."
            )

            return

        values = self.employee_table.item(
            selected[0]
        )["values"]

        employee_id = values[0]

        if not messagebox.askyesno(
            "Confirm Delete",
            f"Delete '{values[1]}'?"
        ):

            return

        try:

            connection = get_connection()

            cursor = connection.cursor()

            cursor.execute(
                "DELETE FROM employees WHERE id=%s",
                (employee_id,)
            )

            connection.commit()

            cursor.close()

            connection.close()

            messagebox.showinfo(
                "Deleted",
                "Employee deleted."
            )

            self.load_employees()

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )


    # ========================================================
    # ORDERS
    # ========================================================

    def show_orders(self):

        self.clear_screen()

        self.create_layout(
            "Create Order"
        )

        self.cart = []

        # ====================================================
        # ORDER TOP
        # ====================================================

        top = tk.Frame(
            self.main_content,
            bg=WHITE
        )

        top.pack(
            fill="x",
            padx=20,
            pady=20
        )

        tk.Label(
            top,
            text="Customer",
            bg=WHITE,
            font=("Segoe UI", 11, "bold")
        ).grid(
            row=0,
            column=0,
            padx=10
        )

        self.customer_combo = ttk.Combobox(
            top,
            width=25,
            state="readonly"
        )

        self.customer_combo.grid(
            row=1,
            column=0,
            padx=10
        )

        self.load_customer_combo()

        tk.Label(
            top,
            text="Menu Item",
            bg=WHITE,
            font=("Segoe UI", 11, "bold")
        ).grid(
            row=0,
            column=1,
            padx=10
        )

        self.item_combo = ttk.Combobox(
            top,
            width=35,
            state="readonly"
        )

        self.item_combo.grid(
            row=1,
            column=1,
            padx=10
        )

        self.load_item_combo()

        tk.Label(
            top,
            text="Quantity",
            bg=WHITE,
            font=("Segoe UI", 11, "bold")
        ).grid(
            row=0,
            column=2,
            padx=10
        )

        self.order_quantity = tk.Entry(
            top,
            width=8
        )

        self.order_quantity.grid(
            row=1,
            column=2,
            padx=10
        )

        self.create_button(
            top,
            "Add To Cart",
            self.add_to_cart,
            GREEN
        ).grid(
            row=1,
            column=3,
            padx=10
        )

        # ====================================================
        # CART TABLE
        # ====================================================

        frame = tk.Frame(
            self.main_content,
            bg=CREAM
        )

        frame.pack(
            fill="both",
            expand=True,
            padx=20
        )

        columns = (
            "Item",
            "Quantity",
            "Price",
            "Total"
        )

        self.cart_table = ttk.Treeview(
            frame,
            columns=columns,
            show="headings"
        )

        for column in columns:

            self.cart_table.heading(
                column,
                text=column
            )

            self.cart_table.column(
                column,
                width=180
            )

        self.cart_table.pack(
            fill="both",
            expand=True
        )

        # ====================================================
        # BOTTOM
        # ====================================================

        bottom = tk.Frame(
            self.main_content,
            bg=WHITE
        )

        bottom.pack(
            fill="x",
            padx=20,
            pady=20
        )

        self.total_label = tk.Label(
            bottom,
            text="Total: ₹0.00",
            bg=WHITE,
            fg=BROWN,
            font=("Segoe UI", 22, "bold")
        )

        self.total_label.pack(
            side="left",
            padx=20
        )

        self.create_button(
            bottom,
            "Remove Item",
            self.remove_from_cart,
            RED
        ).pack(
            side="right",
            padx=5
        )

        self.create_button(
            bottom,
            "Place Order",
            self.place_order,
            BROWN
        ).pack(
            side="right",
            padx=5
        )


    # ========================================================
    # CUSTOMER COMBO
    # ========================================================

    def load_customer_combo(self):

        try:

            connection = get_connection()

            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT id, name
                FROM customers
                ORDER BY name
                """
            )

            rows = cursor.fetchall()

            self.customer_combo["values"] = [
                f"{row[0]} | {row[1]}"
                for row in rows
            ]

            cursor.close()

            connection.close()

            if rows:

                self.customer_combo.current(0)

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )


    # ========================================================
    # MENU COMBO
    # ========================================================

    def load_item_combo(self):

        try:

            connection = get_connection()

            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT id, item_name,
                       price, quantity
                FROM menu
                WHERE quantity > 0
                ORDER BY item_name
                """
            )

            rows = cursor.fetchall()

            self.item_combo["values"] = [
                f"{row[0]} | {row[1]} | ₹{row[2]} | Stock: {row[3]}"
                for row in rows
            ]

            cursor.close()

            connection.close()

            if rows:

                self.item_combo.current(0)

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )


    # ========================================================
    # ADD TO CART
    # ========================================================

    def add_to_cart(self):

        selected = self.item_combo.get()

        if not selected:

            messagebox.showwarning(
                "Order",
                "Select a menu item."
            )

            return

        try:

            quantity = int(
                self.order_quantity.get()
            )

            if quantity <= 0:

                raise ValueError

        except:

            messagebox.showwarning(
                "Quantity",
                "Enter a valid quantity."
            )

            return

        parts = selected.split(" | ")

        menu_id = int(parts[0])

        item_name = parts[1]

        price = float(
            parts[2].replace("₹", "")
        )

        stock = int(
            parts[3].replace(
                "Stock: ",
                ""
            )
        )

        if quantity > stock:

            messagebox.showwarning(
                "Stock",
                f"Only {stock} items available."
            )

            return

        found = False

        for item in self.cart:

            if item["menu_id"] == menu_id:

                if item["quantity"] + quantity > stock:

                    messagebox.showwarning(
                        "Stock",
                        "Not enough stock."
                    )

                    return

                item["quantity"] += quantity

                found = True

                break

        if not found:

            self.cart.append(
                {
                    "menu_id": menu_id,
                    "name": item_name,
                    "quantity": quantity,
                    "price": price
                }
            )

        self.refresh_cart()

        self.order_quantity.delete(
            0,
            tk.END
        )


    # ========================================================
    # REFRESH CART
    # ========================================================

    def refresh_cart(self):

        for row in self.cart_table.get_children():

            self.cart_table.delete(row)

        total = 0

        for item in self.cart:

            item_total = (
                item["quantity"]
                * item["price"]
            )

            total += item_total

            self.cart_table.insert(
                "",
                "end",
                values=(
                    item["name"],
                    item["quantity"],
                    f"₹{item['price']:.2f}",
                    f"₹{item_total:.2f}"
                )
            )

        self.total_label.config(
            text=f"Total: ₹{total:.2f}"
        )


    # ========================================================
    # REMOVE FROM CART
    # ========================================================

    def remove_from_cart(self):

        selected = self.cart_table.selection()

        if not selected:

            messagebox.showwarning(
                "Cart",
                "Select an item first."
            )

            return

        index = self.cart_table.index(
            selected[0]
        )

        self.cart.pop(index)

        self.refresh_cart()


    # ========================================================
    # PLACE ORDER
    # ========================================================

    def place_order(self):

        if not self.cart:

            messagebox.showwarning(
                "Order",
                "Cart is empty."
            )

            return

        customer = self.customer_combo.get()

        if not customer:

            messagebox.showwarning(
                "Customer",
                "Select a customer."
            )

            return

        customer_id = int(
            customer.split(" | ")[0]
        )

        total = sum(
            item["quantity"]
            * item["price"]
            for item in self.cart
        )

        connection = None

        try:

            connection = get_connection()

            cursor = connection.cursor()

            # ------------------------------------------------
            # INSERT ORDER
            # ------------------------------------------------

            cursor.execute(
                """
                INSERT INTO orders
                (customer_id, total)
                VALUES (%s, %s)
                """,
                (
                    customer_id,
                    total
                )
            )

            order_id = cursor.lastrowid

            # ------------------------------------------------
            # INSERT ITEMS + UPDATE STOCK
            # ------------------------------------------------

            for item in self.cart:

                cursor.execute(
                    """
                    INSERT INTO order_items
                    (order_id, menu_id,
                     quantity, price)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (
                        order_id,
                        item["menu_id"],
                        item["quantity"],
                        item["price"]
                    )
                )

                cursor.execute(
                    """
                    UPDATE menu
                    SET quantity =
                        quantity - %s
                    WHERE id = %s
                    """,
                    (
                        item["quantity"],
                        item["menu_id"]
                    )
                )

            connection.commit()

            cursor.close()

            connection.close()

            # ------------------------------------------------
            # SHOW BILL
            # ------------------------------------------------

            self.show_bill(
                order_id,
                customer,
                total
            )

            self.cart = []

            self.refresh_cart()

            self.item_combo["values"] = []

            self.load_item_combo()

        except Exception as error:

            if connection:

                connection.rollback()

                connection.close()

            messagebox.showerror(
                "Order Error",
                str(error)
            )


    # ========================================================
    # BILL
    # ========================================================

    def show_bill(
        self,
        order_id,
        customer,
        total
    ):

        bill_window = tk.Toplevel(
            self.root
        )

        bill_window.title(
            "Cafe Bill"
        )

        bill_window.geometry(
            "500x600"
        )

        bill_window.configure(
            bg=WHITE
        )

        text = tk.Text(
            bill_window,
            font=("Courier New", 12),
            bg=WHITE,
            fg=DARK,
            padx=20,
            pady=20
        )

        text.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        bill = ""

        bill += "================================\n"

        bill += "           ☕ MY CAFE\n"

        bill += "================================\n"

        bill += f"Order ID : {order_id}\n"

        bill += f"Customer : {customer}\n"

        bill += (
            "Date     : "
            + datetime.now().strftime(
                "%d-%m-%Y %H:%M"
            )
            + "\n"
        )

        bill += "--------------------------------\n"

        for item in self.cart:

            bill += (
                f"{item['name']:<18}"
                f"{item['quantity']:>3} x "
                f"₹{item['price']:>7.2f}\n"
            )

        bill += "--------------------------------\n"

        bill += (
            f"TOTAL: ₹{total:.2f}\n"
        )

        bill += "================================\n"

        bill += "          Thank You!\n"

        bill += "================================\n"

        text.insert(
            tk.END,
            bill
        )

        text.config(
            state="disabled"
        )

        self.create_button(
            bill_window,
            "Close",
            bill_window.destroy,
            BROWN
        ).pack(
            pady=(0, 20)
        )


    # ========================================================
    # SALES
    # ========================================================

    def show_sales(self):

        self.clear_screen()

        self.create_layout(
            "Sales & Orders"
        )

        frame = tk.Frame(
            self.main_content,
            bg=CREAM
        )

        frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        columns = (
            "Order ID",
            "Customer",
            "Date",
            "Total"
        )

        table = ttk.Treeview(
            frame,
            columns=columns,
            show="headings"
        )

        for column in columns:

            table.heading(
                column,
                text=column
            )

            table.column(
                column,
                width=200
            )

        table.pack(
            fill="both",
            expand=True
        )

        try:

            connection = get_connection()

            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT
                    o.id,
                    COALESCE(
                        c.name,
                        'Walk-in Customer'
                    ),
                    o.order_date,
                    o.total
                FROM orders o
                LEFT JOIN customers c
                ON o.customer_id = c.id
                ORDER BY o.id DESC
                """
            )

            for row in cursor.fetchall():

                table.insert(
                    "",
                    "end",
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        f"₹{row[3]:.2f}"
                    )
                )

            cursor.close()

            connection.close()

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )


    # ========================================================
    # COMMON LAYOUT
    # ========================================================

    def create_layout(self, title):

        # ====================================================
        # SIDEBAR
        # ====================================================

        sidebar = tk.Frame(
            self.root,
            bg=DARK,
            width=220
        )

        sidebar.pack(
            side="left",
            fill="y"
        )

        sidebar.pack_propagate(False)

        tk.Label(
            sidebar,
            text="☕ CAFE",
            bg=DARK,
            fg="white",
            font=("Segoe UI", 26, "bold")
        ).pack(
            pady=(25, 5)
        )

        tk.Label(
            sidebar,
            text="Management",
            bg=DARK,
            fg="#E8D8C8",
            font=("Segoe UI", 11)
        ).pack(
            pady=(0, 25)
        )

        self.sidebar_button(
            sidebar,
            "🏠  Dashboard",
            self.show_dashboard
        )

        self.sidebar_button(
            sidebar,
            "🍔  Menu",
            self.show_menu
        )

        self.sidebar_button(
            sidebar,
            "🛒  Orders",
            self.show_orders
        )

        self.sidebar_button(
            sidebar,
            "👥  Customers",
            self.show_customers
        )

        self.sidebar_button(
            sidebar,
            "👨‍💼  Employees",
            self.show_employees
        )

        self.sidebar_button(
            sidebar,
            "📊  Sales",
            self.show_sales
        )

        spacer = tk.Frame(
            sidebar,
            bg=DARK
        )

        spacer.pack(
            expand=True,
            fill="both"
        )

        self.sidebar_button(
            sidebar,
            "🚪  Logout",
            self.logout
        )

        # ====================================================
        # CONTENT
        # ====================================================

        container = tk.Frame(
            self.root,
            bg=CREAM
        )

        container.pack(
            side="left",
            fill="both",
            expand=True
        )

        header = tk.Frame(
            container,
            bg=WHITE,
            height=75
        )

        header.pack(
            fill="x"
        )

        tk.Label(
            header,
            text=title,
            bg=WHITE,
            fg=DARK,
            font=("Segoe UI", 25, "bold")
        ).pack(
            side="left",
            padx=25,
            pady=20
        )

        tk.Label(
            header,
            text=f"👤 {self.current_user}",
            bg=WHITE,
            fg=GRAY,
            font=("Segoe UI", 11)
        ).pack(
            side="right",
            padx=25
        )

        self.main_content = tk.Frame(
            container,
            bg=CREAM
        )

        self.main_content.pack(
            fill="both",
            expand=True
        )


    # ========================================================
    # LOGOUT
    # ========================================================

    def logout(self):

        answer = messagebox.askyesno(
            "Logout",
            "Are you sure you want to logout?"
        )

        if answer:

            self.current_user = ""

            self.cart = []

            self.show_login()


# ============================================================
# START APPLICATION
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = CafeApp(root)

    root.mainloop()