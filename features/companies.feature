Feature:

  Scenario: create company and sell something
    Given I created company called 'Flomedia.pl' with income tax rate 19
    When I sell something for 12300 with vat at 23 rate
    Then my real income will be 8100.00

  Scenario: create company and sell/buy something
    Given I created company called 'Flomedia.pl' with income tax rate 19
    When I sell something for 12300 with vat at 23 rate
    When I buy Mobile for 1500 with vat at 23 rate
    Then my real income will be 8612.20

  Scenario: create company and sell: 1 item, buy: 2 items
    Given I created company called 'Flomedia.pl' with income tax rate 19
    When I sell something for 25000 with vat at 23 rate
    When I buy Computer for 11500 with vat at 23 rate
    When I buy Notebook for 2900 with vat at 23 rate
    Then my real income will be 21380.49

  Scenario: create company and sell or buy a lot of stuff
    Given I created company called 'Flomedia.pl' with income tax rate 19
    When I sell services for 25000 with vat at 23 rate
    When I buy Computer for 11500 with vat at 23 rate
    When I buy Notebook for 2900 with vat at 23 rate
    When I buy Book for 59.99 with vat at 5 rate
    When I sell services for 5000 with vat at 23 rate
    Then my real income will be 24686.89

  Scenario: create company and sell or buy a lot of stuff and compute taxes
    Given I created company called 'Flomedia.pl' with income tax rate 19
    When I sell services for 25000 with vat at 23 rate
    When I buy Computer for 11500 with vat at 23 rate
    When I buy Notebook for 2900 with vat at 23 rate
    When I buy Book for 59.99 with vat at 5 rate
    When I sell services for 5000 with vat at 23 rate
    Then my taxes will be vat: 2914.21 and income tax: 2398.90

  Scenario: create company and buy something and have negative vat tax
    Given I created company called 'Flomedia.pl' with income tax rate 19
    When I buy Something for 300 with vat at 23 rate
    Then my taxes will be vat: -56.10 and income tax: -46.34