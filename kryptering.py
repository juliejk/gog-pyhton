p = 37
q = 73
n = pq 
n = 2701
gcd(e, (p-1)(q-1)) = 1
e = 5 
k = (p-1)(q-1) = 36*72 = 2592
ed = 1 (mod k)
d = 1037

public key:(n, d)
private = (p, q, e)

encrypt = m**e mod n = C
decrypt = C**d mod n = m**(ed) mod n = m**(ky(n)+1) = (m**(y(n))**k)*m = (1**k)m mod n = m

