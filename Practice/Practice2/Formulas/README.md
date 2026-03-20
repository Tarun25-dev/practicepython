# Number System Formulas

### Sum of First N natural numbers

1 + 2 + 3 +...+ n  |  `n(n+1)/2`

### Sum of squares of First N natural numbers

1<sup>2</sup> + 1<sup>2</sup> + 1<sup>2</sup> +...+ n<sup>2</sup>  |  `n(n+1)(2n+1)/6`

### Sum of cubes of First N natural numbers

1<sup>3</sup> + 1<sup>3</sup> + 1<sup>3</sup> +...+ n<sup>3</sup>  |  `(n(n+1)/2)^2`

### Sum of First N Odd numbers

1 + 3 + 5 + 7 +...+ 2n-1  |  `n^2`

### Sum of First N Even numbers

2 + 4 + 6 + 8 +...+ 2n  |  `n(n+1)`

#### Important for Odd/Even Facts

✔ nth odd number = 2n − 1

Example:
`
Find 10th Odd Number?
2(10)-1 = 19 |
Answer = 19
`

✔ nth even number = 2n

Example:
`
Find 10th Even Number?
2(10) = 20 |
Answer = 20
`

### Sum of first N terms of A.P(arithmetic progression)

`n/2*(2a+(n-1)*d)` | n = no.of terms | a = first term | d = **common difference**

Example:
`
Find sum of first 10 terms of Ap - 2, 5, 8, 11,... 10th term?`
<br>
`
n = 10, d = 3, a = 2 | 10/2(2(2)+(10-1)*3 |
Answer = 155
`

### Sum of first N terms of G.P(geometric progression)

`a*(r^n-1)/(r-1)` | n = no.of terms | a = first term | r = **common ratio**

Example:
`
Find sum of first 10 terms of gp - 2, 6, 18, 54,... 10th term?`
<br>
`
n = 10, r = 3, a = 2 | 2*(3^10-1)/(3-1) |
Answer = 59048
`
<br> **note**: If r == 1 then use formula sum = a*n

---

### Convert Celcius temperature to Fahrenheit temperature

`F = C * 9/5 + 32`

### Convert Celcius temperature to Kelvin temperature

`K = C + 273.15`

---

# Profit & Loss

### Basic Formulas

- `profit = sp - cp`
- `profit% = (profit/cp) x 100`
- `loss = cp - sp`
- `loss% = (loss/cp) x 100`

### Percentage formulas

- `profit % = (profit/cp) * 100`
- `loss% = (loss/cp) * 100`

### Selling price

- `sp = cp x (1+profit%)` <!--profit percentage convert to decimal like if 20% then 0.2-->
- `sp = cp x (1-loss%)`
- `sp = mp x (100 - d)/100`

### Cost price

- `cp = sp/(1 + profit%)`
- `cp = sp/(1-loss%)`

### Marked price & discount

- `discount = mp - sp`
- `discount% = (discount/mp) x 100`
- `sp = mp x (1 - discount%)`

### note : 

- When gain % = loss% and selling price is same then
- `loss% = x^2/100`
- x is the percentage of profit and loss same

### Successive Percentage Formula

- Use this formula when there are TWO percentage changes one after another on the same value.
- `a + b + ab/100`
---

# Ratios and Proportions

- cross Product rule = if `a : b = c : d` then `ad = bc`
- compound ratio of `a : b` and `c : d` is `ac : bd`
- duplicate ratio of `a : b = a^2 : b^2`
- subduplicate ratio of `a : b = sqt(a) : sqt(b)`
- if a : b : c to find individual shares:   `share(A) = a/(a+b+c) * total`
- fourth proportional to `a,b,c = bc/a`

---

# Averages

- `average = sum of all terms / no.of terms`
- If average increases by X when a new number joins: New number value = `old avg + (old n + 1) * X`
- Average of 1 to n is `(n + 1)/2`
- Average of odd numbers from 1 to n is `(lastodd+1)/2`
- Weighted average = `(w1 x a1) + (w2 x a2) / (w1 + w2)`

---

# Time and Work

- If A does work in 'a' days, A's 1-day work = 1/a
- combined work = `1/A + 1/B` & Time = `AB/(A+B)`
- LCM METHOD: Assume total work = LCM of all given days
- Efficiency : 1/time
- Pipe filling: Net rate = Fill rate - Drain rate
- M×D×H/W = Constant (Men × Days × Hours / Work)

---

# Time, Speed & Distance

- `Speed = distance / time`
- conversion km/hr to m/s is multiply by 5/18
- conversion m/sec to km/hr is multiply by 18/5
- Relative speed (same direction): |S1 - S2|  |  Opposite: S1 + S2
- Train crossing a pole/person: `T = Length/Speed`
- Train crossing platform: T = (Train length + Platform length)/Speed
- Boat upstream: `S - u` | Downstream: `S + u` | S = stream speed and u = boat own speed
- Speed of stream `u = (D-U)/2`
- Average speed (equal distance): `2ab/(a+b)`

# Number System

- Divisibility:
- `2 ➡ last digit even` | `3 ➡ digit sum/3` | `4 ➡ last two digits/4` | `8 ➡ last 3 digits/8` | `9 ➡ digits sum/9`
- 11th rule: (sum of digits at odd positions) - (sum of digits at even positions)
- HCF X LCM = Product of two numbers
- Unit digits of powers:
- Cyclicity of 2 is 4(2,4,8,6,repeat 4 again,..) Ex: 2*2=4, 4*2=8, 8*2=16, 16*2=32 see last digit repeat again 2
- Cyclicity of 3 is 4(3,9,7,1,repeat 4 again,..)
- Cyclicity of 7 is 4(7,9,3,1,repeat 4 again,..)
- Cyclicity of 9 is 2(9,1,repeat 2 again,..)
- No.of zeros at end of n! = n/5 + n/25 + n/125,..
- Remainder theorem: (a+b)/n, remainder = [(a rem n) + (b rem n)]rem n
- Prime factorization: No.of factors of X value = (a+1)(b+1)(c+1),..
- Ex: 360 find no.of factors?
```
- take only prime number from lowest to highest
- 360 / 2 = 180
- 180 / 2 = 90
- 90 / 2 = 45
- 45 / 3 = 15
- 15 / 3 = 5
- 5 / 5 = 1
- 2^3, 3^2, 5^1
- now we calculate powers from starting like this 2 has 3 powers then a = 3, b = 2, c = 1
- subtitute in the formula (3+1)(2+1)(1+1) = 4*3*2 = 24 factors for 360
- Answer: 24
```
---

# Mixtures and Allegations

- The Alligation Rule: Cheaper price(c), Dearer Price(d), Mean(mixture) Price(m)
- Ratio of mixing: `(d - m) : (m - c)` = cheaper : dearer
- if pure liquid is diluted with water: concentration after n removal = `c * [(v-x)/v]^n
- (or) `initial volume x (1 - (removed / total volume))^n`
- For mixing two solutions: alligation gives directly ratio

---

# Probability and Permutations & combinations

- Probability: `p(A) = Favorable outcomes / No.of outcomes`
- Permutations(arranging) `npr = n! / (n - r)!` where r = total selected and n = total
- Combinations(select) `ncr = n! / r! x (n-r)!`
- `p(a or b) = p(a) + p(b) - p(a and b)` where or = "union", and = "intersection"
- `p(a and b) = p(a) x p(b)` if indipendent
- Complimentary: `p(a^1) = 1-p(a)`
- Cards: 52 total, 4 suits, 12 each
- Dice: 6 faces each
- circular arrangements: (n-1)!, with identical items: n! / repeat!

---

# Simple Intrest and Compound Intrest

- Simple intrest: `SI = (p x r x t) / 100` and `amount = p + si`
- Compound Intrest: `amount = p(1 + r/100)^t` and `CI = amount - p`
- Difference b/w ci and si for 2 years: `ci - si = p(r/100)^2`
- Difference b/w ci and si for 3 years: `ci - si = p(r/100)^2 x (r/100 + 3)`
- Effective rate for half-yearly compounding use R/2 as rate and 2T as time period
- Effective rate for quarterly commpounding use R/4 as rate and 4T as time period
- `Time = 100 / Rate` and `Rate = 100 / Time`

---

# Blood relations

