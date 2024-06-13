# Software Requirements Specification: ITER3

Requirements:
1. API endpoints:
    (1) /api/register-user
        - Request Fields:
            1. uuid
            2. name
            3. email_id
            4. annual_income
        - Response Fields:
            1. Error string in case of an error,
            2. uuid
    (2) /api/apply-loan
        - Request Fields:
            1. uuid
            2. loan_type
            3. loan_amount
            4. interest_rate
            5. term_period
            6. disbursement_date
        - Response Fields:
            1. Error String in case of an error,
            2. Loan_id
            3. Due_dates
    (3) /api/make-payment
        - Request Fields:
            1. Loan_id
            2. amount
        - Response Fields:
            1. Error string in case of an error.
    (4) /api/get-statement
        - Request Fields:
            1. Loan_id
        - Response Fields:
            1. Error string in case of an error,
            2. Past_transactions
                - Date
                - Principal
                - Interest
                - Amount_paid
            3. Upcoming_transactions
                - Date
                - Amount_due

2. Iteration 3 delieverables:
    - 
