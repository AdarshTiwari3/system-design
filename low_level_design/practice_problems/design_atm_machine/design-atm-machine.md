# Design an ATM Machine

### Requirements

1. The ATM system should allow users to perform essential banking operations such as **checking account balance**, **withdrawing cash**, and **depositing money**.

2. Users must be authenticated securely using an **ATM card** and a **PIN (Personal Identification Number)** before accessing any services.

3. The ATM should communicate with the **bank’s backend system** to verify user credentials, fetch account details, and execute transactions.

4. The system must include a **cash dispensing mechanism** to release the requested amount during withdrawal operations.

5. The ATM should support **multiple users concurrently** while maintaining **data consistency and transaction safety**.

6. The system should provide an **intuitive and user-friendly interface** to ensure smooth interaction for users of all experience levels.

### Core Objects

### 1. Account

Represents a bank account and stores:

- Account number
- Customer details
- Balance

Supports deposit and withdrawal operations.

---

### 2. Card

Represents an ATM card with:

- Card number
- Expiry date

Used for user identification.

---

### 3. ATM

Acts as the central controller of the system.

Responsibilities:

- Manages ATM states
- Coordinates authentication, banking, and cash dispensing
- Maintains per-session transaction data

---

## Design Approach

### State Pattern

ATM behavior changes based on its state:

- Idle
- Card Inserted
- Authenticated
- Processing

Each state defines allowed actions and transitions.

---

## Services

### AuthService

- Validates PIN securely

### BankService

- Manages accounts
- Executes balance, withdraw, and deposit operations

### CashDispenser

- Dispenses cash during withdrawal

---

### CashDispenser

- Dispenses physical cash during withdrawal
- Can be extended using CoR for denomination handling

---

## Exceptions

The system uses **domain-specific exceptions** for clarity:

- Authentication exceptions (e.g., invalid PIN)
- Domain exceptions (e.g., insufficient balance, invalid amount, account not found)

Exceptions are raised at the service layer and handled at the state layer.

---

## Concurrency

- Each ATM session is independent
- Shared resources are protected using locks at the service layer

---

## Transaction Flow

1. Insert card
2. Enter PIN
3. Select operation
4. Process transaction
5. ATM returns to idle state

---
