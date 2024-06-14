# Overview

### Appendix
1. SOC: Sequence of Code

#### 14 June 2024

1. SOC (5),
2. API (1): "localhost:8000/Authenticator/api/register-user"
3. API (2): "localhost:8000/Welcome/api/apply-loan"
3. API (3): "localhost:8000/Welcome/make-payment"

```shell
# SOC (5)
pip3 install djangorestframework
pip3 install markdown
pip3 install django-filter
```

#### 13 June 2024

1. Iteration 1 complete,
2. Create new branch, 2-CreditService-iter2 (SOC (3)),
3. checkout to new branch,
4. run SOC (1),
5. run SOC (2),
6. Work on Welcome screen and url flow,
7. run SOC (2),
8. Work on Welcome screen,
9. create ```LoanService```,
10. run SOC (4) (2),
11. add model ```SavedState```,
12. add view ```apply_loan```,
13. modify views,
14. run SOC (1) (2),

```shell
# SOC (4)
python3 manage.py flush

# SOC (5)
python3 manage.py runserver
```

```shell
# SOC (3)
git branch 2-CreditService-iter2
git checkout 2-CreditService-iter2
```

#### 12 June 2024

ITER 1:
Iteration 1 details:

1. design diagrams,
2. SRS.md document,
3. code Authenticator, Welcome screen:
    1. Models Session and Person,
    2. run SOC (1),

```shell
python3 -m django startproject app
cd app
# SOC (1)
python3 manage.py migrate # (1.1)
python3 manage.py makemigrations #(1.2)
```

```shell 
# SOC (2)
git add . #(2.1)
git commit -m "create app code template: ITER1" #(2.2)
git push -u origin 1-CreditService-iter1 #(2.3)
```
