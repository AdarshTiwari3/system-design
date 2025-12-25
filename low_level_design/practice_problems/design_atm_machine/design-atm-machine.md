# Design an ATM Machine

### Requirements

1. The ATM system should allow users to perform essential banking operations such as **checking account balance**, **withdrawing cash**, and **depositing money**.

2. Users must be authenticated securely using an **ATM card** and a **PIN (Personal Identification Number)** before accessing any services.

3. The ATM should communicate with the **bank’s backend system** to verify user credentials, fetch account details, and execute transactions.

4. The system must include a **cash dispensing mechanism** to release the requested amount during withdrawal operations.

5. The ATM should support **multiple users concurrently** while maintaining **data consistency and transaction safety**.

6. The system should provide an **intuitive and user-friendly interface** to ensure smooth interaction for users of all experience levels.

### Core Objects

1. **Account**- represents account number and account details.
