#   Extended personal info
name = input()
age = int(input())
town = input()
salary = float(input())

if age < 18:
    age_range = 'teen'
elif age < 70:
    age_range = 'adult'
else:
    age_range = 'elder'

if salary < 500:
    salary_range = 'low'
elif salary < 2000:
    salary_range = 'medium'
else:
    salary_range = 'high'

print('Name: %s' % name)
print('Age: %d' % age)
print('Town: %s' % town)
print('Salary: $%.2f' % salary)
print('Age range: %s' % age_range)
print('Salary range: %s' % salary_range)
