# conversão de tipos, coerção
#  type conversation, typecasting, coercion
#  é o ato de converter um tipo em outro 
#     tipos imutáveis e primitivos:
#     str, int, float, bool
print(int('1'), type(int('1')))
print(type(float('1')+ 1))
print(bool(' ')) 
#uma str vazia é falsa, uma str que tem valor podendo 
# ser até um espaço é considerada True
print(str(11) + 'b')