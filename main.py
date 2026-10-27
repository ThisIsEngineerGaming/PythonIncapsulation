"""Demonstration of the finance package."""

from finance import BankAccount


def main() -> None:
    # Create two accounts
    acc1 = BankAccount("Ivan Petrenko", "UA12345678", 1000, "4821")
    acc2 = BankAccount("Olena Koval", "UA87654321", 250.50, "7390")

    print("=== Initial state ===")
    acc1.print_info()
    print()
    acc2.print_info()

    # Normal operations
    print("\n=== Operations ===")
    acc1.deposit(500)
    acc1.withdraw(200, "4821")
    acc1.transfer_to(acc2, 300, "4821")
    acc1.change_pin("4821", "5604")
    print("Operations completed successfully.")

    acc1.print_info()
    print()
    acc2.print_info()

    # Error handling checks
    print("\n=== Error checks ===")
    tests = [
        ("Negative balance", lambda: setattr(acc1, "balance", -10)),
        ("Withdraw more than balance", lambda: acc1.withdraw(99999, "5604")),
        ("Wrong PIN", lambda: acc1.withdraw(10, "0000")),
        ("Negative deposit", lambda: acc1.deposit(-50)),
        ("Weak PIN", lambda: acc1.change_pin("5604", "1111")),
        ("Reading the PIN", lambda: acc1.pin),
        ("Invalid account number", lambda: BankAccount("Test", "123", 0, "5604")),
        ("Transfer to self", lambda: acc1.transfer_to(acc1, 10, "5604")),
    ]

    for name, action in tests:
        try:
            action()
        except (ValueError, AttributeError) as error:
            print(f"[{name}] -> {error}")


if __name__ == "__main__":
    main()
