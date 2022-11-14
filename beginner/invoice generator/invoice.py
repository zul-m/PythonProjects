product1_name, product1_price = 'Books', 50.95
product2_name, product2_price = 'Computer', 1598.99
product3_name, product3_price = 'Monitor', 856.89

company_name = 'Python Projects, Inc.'
company_address = 'Menara Binjai, Kuala Lumpur'
company_city = 'Wilayah Persekutuan'

message = 'Thank you for shopping with us today!'
# Create a top border.
print('*' * 50)

print('\t\t{}'.format(company_name.title()))
print('\t\t{}'.format(company_address.title()))
print('\t\t{}'.format(company_city.title()))
# Print a line between sections.
print('=' * 50)

print('\tProduct Name\tProduct Price')
# Create a print statement for each item.
print('\t{}\t\tRM{}'.format(product1_name.title(), product1_price))
print('\t{}\tRM{}'.format(product2_name.title(), product2_price))
print('\t{}\t\tRM{}'.format(product3_name.title(), product3_price))

print('=' * 50)
# Print out header for section of total.
print('\t\t\tTotal')
# Calculate total price and print out.
total = product1_price + product2_price + product3_price
print('\t\t\tRM{}'.format(total))
# Print a line between sections.
print('=' * 50)

print('\n\t{}\n'.format(message))