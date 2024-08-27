from django.test import TestCase
from .models import User, Account, Category, Transaction

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(userName="testuser", email="testuser@example.com", password="testpassword")

    def test_user_creation(self):
        self.assertEqual(self.user.userName, "testuser")
        self.assertEqual(self.user.email, "testuser@example.com")

class AccountModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(userName="testuser", email="testuser@example.com", password="testpassword")
        self.account = Account.objects.create(accountName="Test Account", accountType="Savings", balance=1000.00, userName=self.user)

    def test_account_creation(self):
        self.assertEqual(self.account.accountName, "Test Account")
        self.assertEqual(self.account.accountType, "Savings")
        self.assertEqual(self.account.balance, 1000.00)

class CategoryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(userName="testuser", email="testuser@example.com", password="testpassword")
        self.category = Category.objects.create(categoryName="Test Category", categoryType="Expense", userName=self.user)

    def test_category_creation(self):
        self.assertEqual(self.category.categoryName, "Test Category")
        self.assertEqual(self.category.categoryType, "Expense")

class TransactionModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(userName="testuser", email="testuser@example.com", password="testpassword")
        self.accountName = Account.objects.create(accountName="Test Account", accountType="Savings", balance=1000.00, userName=self.user)
        self.categoryName = Category.objects.create(categoryName="Test Category", categoryType="Expense", userName=self.user)
        self.transaction = Transaction.objects.create(
            transactionTitle="Test Transaction",
            transactionType="expense",
            amount=100.00,
            accountName=self.accountName,
            categoryName=self.categoryName
        )

    def test_transaction_creation(self):
        self.assertEqual(self.transaction.transactionTitle, "Test Transaction")
        self.assertEqual(self.transaction.transactionType, "expense")
        self.assertEqual(self.transaction.amount, 100.00)