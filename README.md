## India TCS 206C(1H) for ERPNext

Implementing TCS - 206C(1H) Introduced by Finance Act, 2020 in India for ERPNext.


### What Works
- add a TCS row(if customer turnover is greater than given threshold) to the bottom of Sales Taxes and Charges table in Sales Invoice and apply the given rate, TCS account head and description.(via validate hook)


### TODO/Unhandled cases
- appling a different rate of TCS for unregistered users
- TCS needs to be paid to the government only when collection of the invoice amount happens, for credit sales based customers a module to calculate TCS payable based on collection is needed.


#### License

GPL-3.0