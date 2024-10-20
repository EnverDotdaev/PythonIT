# TODO Найдите количество книг, которое можно разместить на дискете
sim=25
strok=50
stranic=100
disk=1.44 # "Мб"
vessim=4 # "байта"
books=disk*(1024*1024)//(vessim*sim*strok*stranic)
print("Количество книг, помещающихся на дискету:",books)
