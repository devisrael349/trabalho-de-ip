import streamlit as st
st.title('SUDOKU')
tab = st.selectbox('selecione uma fase: ', ['a','b','c','d','e','f','g','h','i','j','k'])


if tab == 'a':

    a1, a2, a3 ,a4 = 0, 3, 0, 0 
    b1, b2, b3 ,b4 = 0, 0, 0, 2 
    c1, c2, c3, c4 = 3, 0, 0, 0
    d1, d2, d3, d4 = 0, 0, 1, 0
    
elif tab == 'b':
    
    a1, a2, a3 ,a4 = 0, 0, 4, 0
    b1, b2, b3 ,b4 = 0, 1, 0, 0
    c1, c2, c3, c4 = 0, 0, 3, 0
    d1, d2, d3, d4 = 0, 2, 0, 0

elif tab == 'c':
    
    a1, a2, a3 ,a4 = 0, 2, 0, 0
    b1, b2, b3 ,b4 = 4, 2, 0, 0
    c1, c2, c3, c4 = 0, 0, 2, 4
    d1, d2, d3, d4 = 0, 1, 0, 0

elif tab == 'd':
    
    a1, a2, a3 ,a4 = 1, 0, 3, 0
    b1, b2, b3 ,b4 = 0, 0, 0, 0
    c1, c2, c3, c4 = 0, 0, 0, 1
    d1, d2, d3, d4 = 0, 4, 0, 0
    
elif tab == 'e':
    
    a1, a2, a3 ,a4 = 0, 0, 2, 1
    b1, b2, b3 ,b4 = 0, 0, 0, 0
    c1, c2, c3, c4 = 0, 0, 0, 0 
    d1, d2, d3, d4 = 1, 3, 0, 0

elif tab == 'f':
  
    a1, a2, a3 ,a4 = 0, 0, 0, 0
    b1, b2, b3 ,b4 = 0, 3, 0, 1
    c1, c2, c3, c4 = 2, 0, 1, 0 
    d1, d2, d3, d4 = 0, 0, 0, 0

elif tab == 'g':

    a1, a2, a3 ,a4 = 0, 0, 4, 0
    b1, b2, b3 ,b4 = 3, 0, 0, 0
    c1, c2, c3, c4 = 0, 0, 0, 1
    d1, d2, d3, d4 = 0, 2, 0, 0

elif tab == 'h':
 
    a1, a2, a3 ,a4 = 3, 0, 0, 0
    b1, b2, b3 ,b4 = 0, 0, 1, 0
    c1, c2, c3, c4 = 0, 2, 0, 0
    d1, d2, d3, d4 = 0, 0, 0, 4

elif tab == 'i':
    
    a1, a2, a3 ,a4 = 0, 0, 2, 0
    b1, b2, b3 ,b4 = 3, 0, 0, 0
    c1, c2, c3, c4 = 0, 0, 0, 1
    d1, d2, d3, d4 = 0, 4, 0, 0

elif tab == 'k':

    a1, a2, a3 ,a4 = 2, 3, 1, 4
    b1, b2, b3 ,b4 = 4, 1, 3, 2
    c1, c2, c3, c4 = 3, 4, 2, 1
    d1, d2, d3, d4 = 1, 2, 4, 3

else:

    a1, a2, a3 ,a4 = 0, 0, 0, 0
    b1, b2, b3 ,b4 = 0, 0, 3, 4
    c1, c2, c3, c4 = 1, 3, 0, 0
    d1, d2, d3, d4 = 0, 0, 0, 0

st.subheader('tabuleiro guia')
st.text(f'{a1} {b1} {c1} {d1}\n{a2} {b2} {c2} {d2}\n{a3} {b3} {c3} {d3}\n{a4} {b4} {c4} {d4}')
op = st.selectbox("Escolha uma posição:", ["a1", "a2", "a3",'a4','b1','b2','b3','b4','c1','c2','c3','c4','d1','d2','d3','d4'])


a = [a1,a2,a3,a4]
b = [b1,b2,b3,b4]
c = [c1,c2,c3,c4]
d = [d1,d2,d3,d4]

abcd1 = [a1,b1,c1,d1]
abcd2 = [a2,b2,c2,d2]
abcd3 = [a3,b3,c3,d3]
abcd4 = [a4,b4,c4,d4]

quad1 = [a1,a2,b1,b2]
quad2 = [c1,c2,d1,d2]
quad3 = [a3,a4,b3,b4]
quad4 = [c3,c4,d3,d4]




def ganhar():
    pontos = 0
    if (a.count(1) == 1) and (a.count(2) == 1) and (a.count(3) == 1) and (a.count(4) == 1) \
   and (b.count(1) == 1) and (b.count(2) == 1) and (b.count(3) == 1) and (b.count(4) == 1) \
   and (c.count(1) == 1) and (c.count(2) == 1) and (c.count(3) == 1) and (c.count(4) == 1) \
   and (d.count(1) == 1) and (d.count(2) == 1) and (d.count(3) == 1) and (d.count(4) == 1) \
   and (abcd1.count(1) == 1) and (abcd1.count(2) == 1) and (abcd1.count(3) == 1) and (abcd1.count(4) == 1) \
    and (abcd2.count(1) == 1) and (abcd2.count(2) == 1) \
    and (abcd2.count(3) == 1) and (abcd2.count(4) == 1) \
    and (abcd3.count(1) == 1) and (abcd3.count(2) == 1) and (abcd3.count(3) == 1) and (abcd3.count(4) == 1) \
    and (abcd4.count(1) == 1) and (abcd4.count(2) == 1) and (abcd4.count(3) == 1) and (abcd4.count(4) == 1) \
    and (quad1.count(1) == 1) and (quad1.count(2) == 1) and (quad1.count(3) == 1) and (quad1.count(4) == 1) \
    and (quad2.count(1) == 1) and (quad2.count(2) == 1) and (quad2.count(3) == 1) and (quad2.count(4) == 1) \
    and (quad3.count(1) == 1) and (quad3.count(2) == 1) and (quad3.count(3) == 1) and (quad3.count(4) == 1) \
    and (quad4.count(1) == 1) and (quad4.count(2) == 1) and (quad4.count(3) == 1) and (quad4.count(4) == 1):
        return True
    else:
        return False
    
if op == "a1":
    z = st.selectbox('qual número você quer adicionar na posição a1? : ',[1,2,3,4])
    if z == 1:
        a1 = 1
    elif z == 2:
        a1 = 2
    elif z == 3:
        a1 = 3
    else:
        a1 = 4
    st.text(f'{a1} {b1} {c1} {d1}\n{a2} {b2} {c2} {d2}\n{a3} {b3} {c3} {d3}\n{a4} {b4} {c4} {d4}')
if op == "a2":
    y = st.selectbox('qual número você quer adicionar na posição a2? : ',[1,2,3,4])
    if y == 1:
        a1 = 1
    elif y == 2:
        a1 = 2
    elif y == 3:
        a1 = 3
    else:
        a1 = 4
    st.text(f'{a1} {b1} {c1} {d1}\n{a2} {b2} {c2} {d2}\n{a3} {b3} {c3} {d3}\n{a4} {b4} {c4} {d4}')

if op == "a3":
    x = st.selectbox('qual número você quer adicionar na posição a3? : ',[1,2,3,4])
    
    a3 = x
    st.text(f'{a1} {b1} {c1} {d1}\n{a2} {b2} {c2} {d2}\n{a3} {b3} {c3} {d3}\n{a4} {b4} {c4} {d4}')

if op == "a4":
    w = st.selectbox('qual número você quer adicionar na posição a4? : ',[1,2,3,4])
    
    a4 = w
    st.text(f'{a1} {b1} {c1} {d1}\n{a2} {b2} {c2} {d2}\n{a3} {b3} {c3} {d3}\n{a4} {b4} {c4} {d4}')

if op == "b1":
    v = st.selectbox('qual número você quer adicionar na posição b1? : ',[1,2,3,4])
    
    b1 = v
    st.text(f'{a1} {b1} {c1} {d1}\n{a2} {b2} {c2} {d2}\n{a3} {b3} {c3} {d3}\n{a4} {b4} {c4} {d4}')

if op == "b2":
    u = st.selectbox('qual número você quer adicionar na posição b2? : ',[1,2,3,4])
    
    b2 = u
    st.text(f'{a1} {b1} {c1} {d1}\n{a2} {b2} {c2} {d2}\n{a3} {b3} {c3} {d3}\n{a4} {b4} {c4} {d4}')

if op == "b3":
    t = st.selectbox('qual número você quer adicionar na posição b3? : ',[1,2,3,4])
    
    b3 = t
    st.text(f'{a1} {b1} {c1} {d1}\n{a2} {b2} {c2} {d2}\n{a3} {b3} {c3} {d3}\n{a4} {b4} {c4} {d4}')

if op == "b4":
    s = st.selectbox('qual número você quer adicionar na posição b4? : ',[1,2,3,4])
    
    b4 = s
    st.text(f'{a1} {b1} {c1} {d1}\n{a2} {b2} {c2} {d2}\n{a3} {b3} {c3} {d3}\n{a4} {b4} {c4} {d4}')

if op == "c1":
    r = st.selectbox('qual número você quer adicionar na posição c1? : ',[1,2,3,4])
    
    c1 = r
    st.text(f'{a1} {b1} {c1} {d1}\n{a2} {b2} {c2} {d2}\n{a3} {b3} {c3} {d3}\n{a4} {b4} {c4} {d4}')

if op == "c2":
    q = st.selectbox('qual número você quer adicionar na posição c2? : ',[1,2,3,4])
    
    c2 = q
    st.text(f'{a1} {b1} {c1} {d1}\n{a2} {b2} {c2} {d2}\n{a3} {b3} {c3} {d3}\n{a4} {b4} {c4} {d4}')

if op == "c3":
    p = st.selectbox('qual número você quer adicionar na posição c3? : ',[1,2,3,4])
    
    c3 = p
    st.text(f'{a1} {b1} {c1} {d1}\n{a2} {b2} {c2} {d2}\n{a3} {b3} {c3} {d3}\n{a4} {b4} {c4} {d4}')

if op == "c4":
    o = st.selectbox('qual número você quer adicionar na posição c4? : ',[1,2,3,4])
    
    c4 = o
    st.text(f'{a1} {b1} {c1} {d1}\n{a2} {b2} {c2} {d2}\n{a3} {b3} {c3} {d3}\n{a4} {b4} {c4} {d4}')

if op == "d1":
    n = st.selectbox('qual número você quer adicionar na posição d1? : ',[1,2,3,4])
    
    d1 = n
    st.text(f'{a1} {b1} {c1} {d1}\n{a2} {b2} {c2} {d2}\n{a3} {b3} {c3} {d3}\n{a4} {b4} {c4} {d4}')

if op == "d2":
    m = st.selectbox('qual número você quer adicionar na posição d2? : ',[1,2,3,4])
    
    d2 = m
    st.text(f'{a1} {b1} {c1} {d1}\n{a2} {b2} {c2} {d2}\n{a3} {b3} {c3} {d3}\n{a4} {b4} {c4} {d4}')

if op == "d3":
    l = st.selectbox('qual número você quer adicionar na posição d3? : ',[1,2,3,4])
    
    d3 = l
    st.text(f'{a1} {b1} {c1} {d1}\n{a2} {b2} {c2} {d2}\n{a3} {b3} {c3} {d3}\n{a4} {b4} {c4} {d4}')

if op == "d4":
    k = st.selectbox('qual número você quer adicionar na posição d4? : ',[1,2,3,4])
    
    d4 = k
    st.text(f'{a1} {b1} {c1} {d1}\n{a2} {b2} {c2} {d2}\n{a3} {b3} {c3} {d3}\n{a4} {b4} {c4} {d4}')

if st.button('conferir'):
    j  = ganhar()
    if j == False:
        st.text('incorreto, tente novamente.')
    else:
        st.text('correto, parábens.')
