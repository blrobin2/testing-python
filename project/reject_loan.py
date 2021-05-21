from project.loan import Loan

def reject_loan(loan: Loan) -> Loan:
  if loan.amount > 250_000:
    loan.reject()

  return loan
