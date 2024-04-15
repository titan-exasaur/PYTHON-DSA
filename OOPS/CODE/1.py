class employee:
  name = 'Ben'
  designation = 'Sales Executive'
  sales_made_this_week = 6

  def target_acheived(self):
    if self.sales_made_this_week >= 5:
      print('target acheived')
    else:
      print('target not acheived')

employee_one = employee()#creating an instance ==> object instanciation
employee_one.name

employee_one.target_acheived()

