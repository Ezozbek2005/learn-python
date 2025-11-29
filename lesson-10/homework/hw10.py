#1-misol
from datetime import datetime

# ===== Task klassi =====
class Task:
    def __init__(self, title, description, due_date):
        self.title = title                  # Vazifa nomi
        self.description = description      # Vazifa tavsifi
        self.due_date = due_date            # Yakunlash muddati (string)
        self.completed = False              # Vazifa bajarilganmi?

    def mark_complete(self):
        self.completed = True               # Vazifani bajarilgan deb belgilash

    def __str__(self):
        status = "✅ Bajarilgan" if self.completed else "❌ Bajarilmagan"
        return f"{self.title} - {self.description} | Muddati: {self.due_date} | Status: {status}"

# ===== ToDoList klassi =====
class ToDoList:
    def __init__(self):
        self.tasks = []  # Vazifalar ro‘yxati

    def add_task(self, task):
        """Yangi vazifa qo'shish"""
        self.tasks.append(task)
        print(f"✅ '{task.title}' vazifasi qo'shildi!")

    def list_all_tasks(self):
        """Barcha vazifalarni ko'rsatish"""
        if not self.tasks:
            print("📭 Vazifalar ro'yxati bo'sh.")
            return
        print("\n📋 Barcha vazifalar:")
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}")

    def list_incomplete_tasks(self):
        """Faqat bajarilmagan vazifalarni ko'rsatish"""
        incomplete_tasks = [task for task in self.tasks if not task.completed]
        if not incomplete_tasks:
            print("🎉 Barcha vazifalar bajarilgan!")
            return
        print("\n❌ Bajarilmagan vazifalar:")
        for idx, task in enumerate(incomplete_tasks, start=1):
            print(f"{idx}. {task}")

    def mark_task_complete(self, task_index):
        """Vazifani bajarilgan deb belgilash"""
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_complete()
            print(f"✅ '{self.tasks[task_index].title}' vazifasi bajarilgan deb belgilandi!")
        else:
            print("⚠️ Noto'g'ri indeks kiritildi.")

# ===== CLI (konsol menyu) =====
def main():
    todo_list = ToDoList()  # ToDoList obyektini yaratamiz

    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Yangi vazifa qo'shish")
        print("2. Vazifani bajarilgan deb belgilash")
        print("3. Barcha vazifalarni ko'rsatish")
        print("4. Faqat bajarilmagan vazifalarni ko'rsatish")
        print("5. Chiqish")
        
        choice = input("Tanlovingizni kiriting (1-5): ")

        if choice == "1":
            title = input("Vazifa nomi: ")
            description = input("Vazifa tavsifi: ")
            due_date = input("Yakunlash muddati (YYYY-MM-DD): ")
            task = Task(title, description, due_date)
            todo_list.add_task(task)

        elif choice == "2":
            todo_list.list_all_tasks()
            try:
                task_index = int(input("Bajarilgan vazifa raqamini kiriting: ")) - 1
                todo_list.mark_task_complete(task_index)
            except ValueError:
                print("⚠️ Iltimos, raqam kiriting.")

        elif choice == "3":
            todo_list.list_all_tasks()

        elif choice == "4":
            todo_list.list_incomplete_tasks()

        elif choice == "5":
            print("👋 Dasturni tugatdingiz.")
            break

        else:
            print("⚠️ Noto'g'ri tanlov, iltimos 1-5 oralig'ida raqam kiriting.")

# ===== Dastur ishga tushadi =====
if __name__ == "__main__":
    # Misol vazifalar bilan dastur sinovi
    main()



#2- misol

#===== Post klassi =====
class Post:
    def __init__(self, title, content, author):
        self.title = title       # Post sarlavhasi
        self.content = content   # Post matni
        self.author = author     # Muallif
        self.created_at = None   # Yaralgan vaqti (hozircha qo‘shimcha uchun)
        self.updated_at = None   # Oxirgi tahrir vaqti

    def edit_post(self, new_title, new_content):
        """Postni tahrirlash"""
        self.title = new_title
        self.content = new_content
        self.updated_at = "Hozirgi vaqt"  # Agar xohlasa datetime bilan aniqlash mumkin

    def __str__(self):
        """Postni string ko'rinishda chiqarish"""
        return f"📌 {self.title} by {self.author}\n{self.content}\n"

# ===== Blog klassi =====
class Blog:
    def __init__(self):
        self.posts = []  # Postlar ro‘yxati

    def add_post(self, post):
        """Yangi post qo'shish"""
        self.posts.append(post)
        print(f"✅ '{post.title}' post qo'shildi!")

    def list_all_posts(self):
        """Barcha postlarni ko'rsatish"""
        if not self.posts:
            print("📭 Hozircha postlar yo'q.")
            return
        print("\n📋 Barcha postlar:")
        for idx, post in enumerate(self.posts, start=1):
            print(f"{idx}. {post}")

    def list_posts_by_author(self, author):
        """Muallif bo'yicha postlarni ko'rsatish"""
        author_posts = [post for post in self.posts if post.author.lower() == author.lower()]
        if not author_posts:
            print(f"📭 '{author}' muallifga tegishli post yo'q.")
            return
        print(f"\n📌 '{author}' muallifga tegishli postlar:")
        for idx, post in enumerate(author_posts, start=1):
            print(f"{idx}. {post}")

    def delete_post(self, index):
        """Postni o'chirish"""
        if 0 <= index < len(self.posts):
            removed = self.posts.pop(index)
            print(f"❌ '{removed.title}' post o'chirildi!")
        else:
            print("⚠️ Noto'g'ri indeks.")

    def edit_post(self, index, new_title, new_content):
        """Postni tahrirlash"""
        if 0 <= index < len(self.posts):
            self.posts[index].edit_post(new_title, new_content)
            print(f"✏️ '{self.posts[index].title}' post tahrirlandi!")
        else:
            print("⚠️ Noto'g'ri indeks.")

# ===== CLI (konsol menyu) =====
def main():
    blog = Blog()

    # Misol postlar bilan dastur ishga tushish uchun
    blog.add_post(Post("Salom Dunyo", "Bu birinchi postimiz!", "Ezozbek"))
    blog.add_post(Post("Python darslari", "Python haqida qiziqarli faktlar.", "Ali"))
    blog.add_post(Post("OOP tushunchasi", "Object Oriented Programming asoslari.", "Ezozbek"))

    while True:
        print("\n===== BLOG MENU =====")
        print("1. Yangi post qo'shish")
        print("2. Barcha postlarni ko'rsatish")
        print("3. Muallif bo'yicha postlarni ko'rsatish")
        print("4. Postni o'chirish")
        print("5. Postni tahrirlash")
        print("6. Chiqish")

        choice = input("Tanlovingizni kiriting (1-6): ")

        if choice == "1":
            title = input("Post sarlavhasi: ")
            content = input("Post matni: ")
            author = input("Muallif: ")
            post = Post(title, content, author)
            blog.add_post(post)

        elif choice == "2":
            blog.list_all_posts()

        elif choice == "3":
            author = input("Muallif nomini kiriting: ")
            blog.list_posts_by_author(author)

        elif choice == "4":
            blog.list_all_posts()
            try:
                index = int(input("O'chiriladigan post raqamini kiriting: ")) - 1
                blog.delete_post(index)
            except ValueError:
                print("⚠️ Iltimos, raqam kiriting.")

        elif choice == "5":
            blog.list_all_posts()
            try:
                index = int(input("Tahrir qilinadigan post raqamini kiriting: ")) - 1
                new_title = input("Yangi sarlavha: ")
                new_content = input("Yangi matn: ")
                blog.edit_post(index, new_title, new_content)
            except ValueError:
                print("⚠️ Iltimos, raqam kiriting.")

        elif choice == "6":
            print("👋 Dasturni tugatdingiz.")
            break

        else:
            print("⚠️ Noto'g'ri tanlov, iltimos 1-6 oralig'ida raqam kiriting.")

# ===== Dastur ishga tushadi =====
if __name__ == "__main__":
    main()


# 3-misol

# ===== Account klassi =====
class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number   # Hisob raqami
        self.holder_name = holder_name         # Hisob egasi
        self.balance = balance                 # Hisob balansi

    def deposit(self, amount):
        """Hisobga pul qo'yish"""
        if amount > 0:
            self.balance += amount
            print(f"✅ {amount} so'm qo'shildi. Yangi balans: {self.balance}")
        else:
            print("⚠️ Iltimos, 0 dan katta summa kiriting.")

    def withdraw(self, amount):
        """Hisobdan pul yechish"""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"✅ {amount} so'm yechildi. Yangi balans: {self.balance}")
            else:
                print("⚠️ Balans yetarli emas!")
        else:
            print("⚠️ Iltimos, 0 dan katta summa kiriting.")

    def __str__(self):
        return f"🏦 Hisob raqami: {self.account_number} | Egasi: {self.holder_name} | Balans: {self.balance}"

# ===== Bank klassi =====
class Bank:
    def __init__(self):
        self.accounts = []  # Hisoblar ro‘yxati

    def add_account(self, account):
        self.accounts.append(account)
        print(f"✅ Hisob '{account.holder_name}' qo'shildi!")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def transfer_money(self, from_acc_num, to_acc_num, amount):
        from_acc = self.find_account(from_acc_num)
        to_acc = self.find_account(to_acc_num)
        if not from_acc or not to_acc:
            print("⚠️ Hisoblardan biri topilmadi!")
            return
        if amount > 0 and from_acc.balance >= amount:
            from_acc.withdraw(amount)
            to_acc.deposit(amount)
            print(f"✅ {amount} so'm {from_acc.holder_name} hisobidan {to_acc.holder_name} hisobiga o‘tkazildi.")
        else:
            print("⚠️ Pulni o'tkazib bo'lmadi.")

    def list_accounts(self):
        if not self.accounts:
            print("📭 Hozircha hisoblar yo'q.")
            return
        print("\n📋 Barcha hisoblar:")
        for idx, account in enumerate(self.accounts, start=1):
            print(f"{idx}. {account}")

# ===== CLI menyu =====
def main():
    bank = Bank()

    # Misol hisoblar bilan dastur ishga tushadi
    bank.add_account(Account("1001", "Ezozbek", 5000))
    bank.add_account(Account("1002", "Ali", 10000))
    bank.add_account(Account("1003", "Sara", 7500))

    while True:
        print("\n===== BANK MENU =====")
        print("1. Yangi hisob qo‘shish")
        print("2. Hisoblar ro‘yxatini ko‘rsatish")
        print("3. Balansni tekshirish")
        print("4. Pul qo‘yish (deposit)")
        print("5. Pul yechish (withdraw)")
        print("6. Pul o‘tkazish (transfer)")
        print("7. Chiqish")

        choice = input("Tanlovingizni kiriting (1-7): ")

        if choice == "1":
            acc_num = input("Hisob raqami: ")
            holder = input("Egasi: ")
            try:
                balance = float(input("Boshlang‘ich balans: "))
            except ValueError:
                print("⚠️ Iltimos, raqam kiriting.")
                continue
            bank.add_account(Account(acc_num, holder, balance))

        elif choice == "2":
            bank.list_accounts()

        elif choice == "3":
            acc_num = input("Hisob raqamini kiriting: ")
            account = bank.find_account(acc_num)
            if account:
                print(account)
            else:
                print("⚠️ Hisob topilmadi.")

        elif choice == "4":
            acc_num = input("Hisob raqamini kiriting: ")
            account = bank.find_account(acc_num)
            if account:
                try:
                    amount = float(input("Qo'yiladigan summa: "))
                    account.deposit(amount)
                except ValueError:
                    print("⚠️ Iltimos, raqam kiriting.")
            else:
                print("⚠️ Hisob topilmadi.")

        elif choice == "5":
            acc_num = input("Hisob raqamini kiriting: ")
            account = bank.find_account(acc_num)
            if account:
                try:
                    amount = float(input("Yechiladigan summa: "))
                    account.withdraw(amount)
                except ValueError:
                    print("⚠️ Iltimos, raqam kiriting.")
            else:
                print("⚠️ Hisob topilmadi.")

        elif choice == "6":
            from_acc = input("Pul jo‘natiladigan hisob raqami: ")
            to_acc = input("Pul qabul qiladigan hisob raqami: ")
            try:
                amount = float(input("O‘tkaziladigan summa: "))
                bank.transfer_money(from_acc, to_acc, amount)
            except ValueError:
                print("⚠️ Iltimos, raqam kiriting.")

        elif choice == "7":
            print("👋 Dasturni tugatdingiz.")
            break

        else:
            print("⚠️ Noto‘g‘ri tanlov, iltimos 1-7 oralig‘ida raqam kiriting.")

# ===== Dastur ishga tushadi =====
if __name__ == "__main__":
    main()
