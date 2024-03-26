# Игра "Жизнь"
Это одна из классических задач на программирование. Дано поле размера N x M. В каждом из них живет, или не живет существо. В начальный момент времени это определяется случайным образом. Далее на каждом шаге жизнь в клетках поля зарождается и умирает по следующим правилам:

	-  в пустой (мёртвой) клетке, с которой соседствуют три живые клетки, зарождается жизнь;
	-  если у живой клетки есть две или три живые соседки, то эта клетка продолжает жить; в противном случае (если живых соседей меньше двух или больше трёх) клетка умирает («от одиночества» или «от перенаселённости»).

Но стандартные правила скучные, давайте добавим больше ролей в этот дивный мир. Для них правила игры будут немного интереснее..

    - “Маньяк”. Маньяки с вероятностью 25% убивают каждого из своих соседей. Таким образом, каждый, кто соседствует с маньяком, при переходе к новой эпохе, помимо проверки общих условий, проверяет, не был ли он убит этой ночью маньяком. Умирают, когда убивать некого, т.е. когда у них отсутствуют соседи. Вероятность рождения 10%. Обозначение М.
    - “Виктор Франкенштейн” каждый ход может создавать жизнь в соседних клетках с вероятностью 20%. Это означает, что для пустой клетки, с которой соседствует этот персонаж, нужно в 1 случае из 5 создать жизнь.. Умирает, если нет свободных клеток вокруг. Вероятность рождения 15%. Обозначение Ф.
Реализуйте систему классов `Field` (хранит поля, имеет метод `next()` для перехода к следующей эпохе и `__str__()` для вывода поля на экран), `Cell` — пустая клетка, `Civilian(Cell)` — мирный житель, `Maniac(Cell)`, `Frank(Cell)`, и саму логику игры, применяя принципы ООП.
