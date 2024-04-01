let = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о",
       "п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]

with open("src/abc.txt", "w") as f:
    print("Создан файл data.txt")
    for i in let:
        f.write(i + "\n")

with open("src/abc.txt", "r") as f:
    total = len(f.readlines())

print("Сумма чисел в файле:", total)