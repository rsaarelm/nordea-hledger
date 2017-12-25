# Nordea-Hledger

Tool to import transaction logs from Nordea Bank into hledger

Usage:
    ./nordea-hledger < Tapahtumat_FI123123123123.txt > hledger.journal

## Itemizing credit card statements

(Note to self mostly, this is Vim-only and clumsy)

These just show up as monthly NORDEA RAHOITUS items in the Nordea export log,
but you can view separate credit card statements for each month in a pdf at
the Nordea web interface.

I copy-paste them as comments to the journal, and get something like this:

    ; 12.05. 30.06. 160512010305 CREDIT.SHOP 39.99
    2016/10/31 NORDEA RAHOITUS SUOMI OY
        expenses:credit-card        €39.99
        assets:bank:checking       €-39.99

The following Vim search-replace string (corrected for current year) reformats the comment lines into hledger entries:

    :s/.\s\+\(\d\d\).\(\d\d\). ......\s[^ ]\+\s\+\(.*\) \(\d\+.\d\d\)$/2017\/\2\/\1 \3\r    expenses:unknown            €\4\r    assets:bank:checking       €-\4\r/

Now at the start of the line for each credit statment line, run the macro with
`@a`. It'll extract the date from the ledger item below and convert the item
into an "unknown" expense. After converting each item, comment out the total
credit card statement so you don't get double accounting and manually fill in
the categories for the individual items.
