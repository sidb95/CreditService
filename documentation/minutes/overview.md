# Overview

#### 13 June 2024

1. Iteration 1 complete,
2. Create new branch, 2-CreditService-iter2,
3. checkout to new branch,

```shell
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
