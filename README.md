# Dictionary Manager [v7.1.55]
Программа-менеджер словарей для запоминания иностранных слов и увеличения словарного запаса.

## Оглавление
1. [Установка](#установка)
2. [Возможности программы](#возможности-программы)
    1. [Словари](#словари)
    2. [Словарные статьи](#словарные-статьи)
    3. [Изучение слов](#изучение-слов)
    4. [Универсальность](#универсальность)
    5. [Обновления программы](#обновления-программы)
3. [Пример статьи из словаря](#пример-статьи-из-словаря)

## Установка
Требуется версия python 3.10<br>
<ol>
    <li>Для работы программы должны быть установлены следующие модули:</li>
    <ul>
        <li>copy (не требует установки)</li>
        <li>platform</li>
        <li>random (не требует установки)</li>
        <li>math (не требует установки)</li>
        <li>tkinter (pip install tk)</li>
            <!--  <li>tkinter.ttk</li>
            <li>idlelib.tooltip</li>
            <li>tkinter.filedialog</li>  -->
        <li>re</li>
        <li>webbrowser</li>
        <li>urllib.request</li>
        <li>wget</li>
        <li>zipfile</li>
        <li>typing</li>
        <li>os (не требует установки)</li>
        <li>shutil</li>
        <li>requests <!--(для установщика)--></li>
    </ul>
    <li>Скачайте файл install.py из репозитория, запустите его, далее действуйте по инструкциям установщика. После этого программа будет установлена в выбранную папку.</li>
    <li>Перейдите в папку с установленным приложением и запустите main.py.</li>
</ol>

## Возможности программы
### Словари
Вы можете создать неограниченное количество словарей. Благодаря этому:
- Вы можете изучать несколько языков одновременно.
- Программой могут пользоваться несколько людей.

Вы можете делиться своими словарями с другими людьми благодаря функциям импорта и экспорта.<br>
Для этого в программе перейдите в `Настройки` -> `Настройки программы`

### Словарные статьи
Вы можете добавить в словарь неограниченное количество статей.<br>
Каждая статья должна содержать одно слово и хотя бы один его перевод.

Помимо этого:
- Можно добавить в статью несколько переводов.
- Можно добавить в статью формы слова, например множественное число, падежи и что угодно ещё (см. [Универсальность](#универсальность)).
- Можно добавить в статью фразы с этим словом.
- Можно добавить к статье сноски.
- Можно добавить статью в избранное. Например, можно сохранять в избранном самые сложные слова.
- Можно объединять статьи в группы.
- Можно создать несколько статей с одинаковым словом (омографы).

### Изучение слов
Чтобы <b>посмотреть статьи</b>, которые вы добавили, можете напечать словарь.

Также вы можете <b>учить</b> добавленные слова.
- Доступно множество режимов учёбы. Вы можете выбрать подходящий именно вам.
- Если вы опечатаетесь, можно нажать кнопку "Опечатка", и ошибка не засчитается.<br>
  Активировать/деактивировать эту кнопку можно, перейдя в `Настройки` -> `Настройки программы` -> `Показывать кнопку "Опечатка"`.<br>

`Лучше всего учить слова небольшими группами (до 20 слов), повторяя при этом старые уже усвоенные слова`

### Универсальность
Программа подходит для изучения любого языка:
- Помимо таких <b>грамматических категорий</b>, как падеж, число или род, вы можете добавить любые другие.<br>
  Для этого в программе перейдите в `Настройки` -> `Настройки словаря` -> `Грамматические категории`.<br>
  *Для каждого словаря используются отдельные категории.*
- Если у вас отсутствует необходимая раскладка клавиатуры, вы можете использовать <b>специальные комбинации</b>.<br>
  Для этого в программе перейдите в `Настройки` -> `Настройки словаря` -> `Специальные комбинации`.<br>
  `Пример специальной комбинации: #A -> Ä`

### Обновления программы
При каждом запуске программа проверяет наличие обновлений (эту функцию можно отключить в настройках).
Также можно проверить их наличие вручную (кнопка в главном меню).<br>
Если доступно обновление, то для его установки достаточно одного нажатия.

## Пример статьи из словаря
<pre>
(*) [  3;  75%] house: дом, здание
                [plural] houses
                > сноска_1
                > сноска_2
</pre>
> Слева от каждого слова в квадратных скобках кратко записана ваша статистика по этому слову:<br>
`количество верных ответов подряд` и `процент верных ответов`.
