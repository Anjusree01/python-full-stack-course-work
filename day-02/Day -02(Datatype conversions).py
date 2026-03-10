print('conversion of int datatype:')
i = 10
print(type(i))
print(float(i))
print(complex(i))
print(str(i))
print(bool(i))
print('conversion of float datatype:')
f = 2.5
print(type(f))
print(int(f))
print(complex(f))
print(str(f))
print(bool(f))
print('conversion of complex datatype')
c = 2+4j
print(type(c))
print(str(c))
print(bool(c))
print('conversion of string datatype')
s = 'anju01'
print(type(s))
print(list(s))
print(tuple(s))
print(set(s))
print(bool(s))
print('conversion of list datatype')
l=['anju','nani','01','02']
print(type(l))
print(str(l))
print(tuple(l))
print(bool(l))
print(set(l))
print('conversion of tuple datatype')
t=('anju','nani','01','02')
print(type(t))
print(str(t))
print(list(t))
print(set(t))
print('conversion of set datatype')
s={'anju','nani','01','02'}
print(type(s))
print(str(s))
print(list(s))
print(tuple(s))
print(bool(s))
print('conversion of dictionary datatype')
d={'red':'apple','yellow':'mango','green':'kiwi'}
print(type(d))
print(str(d))
print(list(d))
print(tuple(d))
print(set(d))
print(bool(d))
print('conversion of boolean datatype')
b=True
print(type(b))
print(int(b))
print(float(b))
print(complex(b))
print(str(b))
print('int -> f,c,str,b; !-> l,t,set,d','float -> i,str,c,b; !-> l,t,set,d','complex -> str,b; !-> i,f,l,t,set,d','string -> l,t,set,b; !-> i,f,d,c','list -> str,t,set,b; !->i,f,c,d','tuple-> str,l,set,b; !-> i,f,c,d','set-> str,l,t,b; !-> i,f,c,d','dictionary-> str,l,t,set,b; !-> i,f,c','boolean ->i,f,str,c; !->l,t,s,d',sep='\n')









