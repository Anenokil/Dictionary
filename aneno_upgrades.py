import os
import shutil
import aneno_constants as anc
from aneno_dct import frm_key_to_str_for_save

""" Обновление ресурсов """


# Обновить структуру папки с ресурсами
def upgrade_resources():
    old_local_settings_dir = 'local_settings'
    old_local_settings_path = os.path.join(anc.RESOURCES_PATH, old_local_settings_dir)
    # Удаляем лишние папки, если они есть
    for dir_or_filename in os.listdir(anc.SAVES_PATH):
        path = os.path.join(anc.SAVES_PATH, dir_or_filename)
        if os.path.isdir(path):
            shutil.rmtree(path)
    # Перемещаем файлы
    for filename in os.listdir(anc.SAVES_PATH):
        base_name, ext = os.path.splitext(filename)
        if ext == '.txt':
            dir_name = os.path.join(anc.SAVES_PATH, base_name)
            # Создаём папку сохранения
            os.mkdir(dir_name)
            # Перемещаем в неё файл с сохранением словаря
            os.replace(os.path.join(anc.SAVES_PATH, filename),
                       os.path.join(dir_name, anc.DICTIONARY_SAVE_FN))
            # Перемещаем в неё файл с локальными настройками
            if old_local_settings_dir in os.listdir(anc.RESOURCES_PATH):
                if filename in os.listdir(old_local_settings_path):
                    os.replace(os.path.join(old_local_settings_path, filename),
                               os.path.join(dir_name, anc.LOCAL_SETTINGS_FN))
    # Удаляем старую папку локальных настроек
    if old_local_settings_dir in os.listdir(anc.RESOURCES_PATH):
        shutil.rmtree(old_local_settings_path)


""" Обновления тем """


# Обновить тему с 4 до 5 версии
def upgrade_theme_4_to_5(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write('5\n')
        for i in range(1, 11):
            file.write(lines[i])
        file.write(lines[10])
        file.write(lines[11])
        for i in range(13, 19):
            file.write(lines[i])
        file.write(lines[13])
        file.write(lines[14])
        for i in range(19, 30):
            file.write(lines[i])


# Обновить тему с 5 до 6 версии
def upgrade_theme_5_to_6(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write('6\n')
        for i in range(1, 21):
            file.write(lines[i])
        file.write(lines[2])
        file.write(lines[1])
        file.write(lines[1])
        file.write(lines[3])
        file.write(lines[3])
        file.write(lines[3])
        for i in range(21, 32):
            file.write(lines[i])


# Обновить тему с 6 до 7 версии
def upgrade_theme_6_to_7(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write('7\n')
        file.write('1\n')
        for i in range(1, 27):
            file.write(lines[i])
        file.write(lines[23])
        file.write(lines[22])
        file.write(lines[21])
        file.write(lines[26])
        file.write(lines[25])
        file.write(lines[24])
        for i in range(27, 38):
            file.write(lines[i])


# Обновить тему с 7 до 8 версии
def upgrade_theme_7_to_8(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write('8\n')
        file.write(f'{lines[1]}')
        keys = ('*.BG.*', '*.BG.ENTRY', '*.FG.*', '*.FG.LOGO', '*.FG.FOOTER', '*.FG.WARN', '*.FG.ENTRY', '*.BG.SEL',
                '*.FG.SEL', 'FRAME.RELIEF.*', 'TXT.RELIEF.*', '*.BORDER_CLR.*', 'BTN.BG.*', 'BTN.BG.ACT', 'BTN.BG.Y',
                'BTN.BG.Y_ACT', 'BTN.BG.N', 'BTN.BG.N_ACT', 'BTN.BG.IMG_HOV', 'BTN.BG.IMG_ACT', 'FLAT_BTN.BG.*',
                'FLAT_BTN.BG.HOV', 'FLAT_BTN.BG.ACT', 'FLAT_BTN.FG.*', 'FLAT_BTN.FG.HOV', 'FLAT_BTN.FG.ACT',
                'FLAT_BTN.BG.SEL', 'FLAT_BTN.BG.SEL_HOV', 'FLAT_BTN.BG.SEL_ACT', 'FLAT_BTN.FG.SEL',
                'FLAT_BTN.FG.SEL_HOV', 'FLAT_BTN.FG.SEL_ACT', 'BTN.BG.DISABL', 'BTN.FG.DISABL', 'CHECK.BG.SEL',
                'TAB.BG.*', 'TAB.BG.SEL', 'TAB.FG.*', 'TAB.FG.SEL', 'SCROLL.BG.*', 'SCROLL.BG.ACT', 'SCROLL.FG.*',
                'SCROLL.FG.ACT')
        max_len = max((len(k) for k in keys))
        for i in range(2, 45):
            tab = ' ' * (max_len - len(keys[i - 2]))
            file.write(f'{keys[i - 2]}{tab} = {lines[i]}')


upgrade_theme_functions = [upgrade_theme_4_to_5,
                           upgrade_theme_5_to_6,
                           upgrade_theme_6_to_7,
                           upgrade_theme_7_to_8]


# Обновить тему старой версии до актуальной версии
def upgrade_theme(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as theme_file:
        lines = theme_file.readlines()
    first_line = lines[0].strip()
    if len(first_line) > 0 and first_line[0].isnumeric() and int(first_line[0]) <= anc.REQUIRED_THEME_VERSION:
        current_version = int(first_line[0])
        if current_version < 4:
            print(f'Слишком старая версия тем: {current_version}!')
            return
    else:
        print(f'Неизвестная версия тем: {first_line}!')
        return
    for i in range(current_version, anc.REQUIRED_THEME_VERSION):
        upgrade_theme_functions[i - 4](filepath)


""" Обновления глобальных настроек """


# Обновить глобальные настройки с 0 до 1 версии
def upgrade_global_settings_0_to_1():
    with open(anc.GLOBAL_SETTINGS_PATH, 'r', encoding='utf-8') as global_settings_file:
        lines = global_settings_file.readlines()
    with open(anc.GLOBAL_SETTINGS_PATH, 'w', encoding='utf-8') as global_settings_file:
        global_settings_file.write('v1\n')  # Версия глобальных настроек
        global_settings_file.write(lines[0])  # Название текущего словаря
        global_settings_file.write(lines[1])  # Уведомлять ли о выходе новых версий
        global_settings_file.write('0\n')  # Добавлять ли кнопку "Опечатка" при неверном ответе в учёбе
        global_settings_file.write(lines[2])  # Установленная тема


# Обновить глобальные настройки с 1 до 2 версии
def upgrade_global_settings_1_to_2():
    with open(anc.GLOBAL_SETTINGS_PATH, 'r', encoding='utf-8') as global_settings_file:
        lines = global_settings_file.readlines()
    with open(anc.GLOBAL_SETTINGS_PATH, 'w', encoding='utf-8') as global_settings_file:
        global_settings_file.write('v2\n')  # Версия глобальных настроек
        global_settings_file.write(lines[1])  # Название текущего словаря
        global_settings_file.write(lines[2])  # Уведомлять ли о выходе новых версий
        global_settings_file.write(lines[3])  # Добавлять ли кнопку "Опечатка" при неверном ответе в учёбе
        global_settings_file.write(lines[4].strip())  # Установленная тема
        global_settings_file.write('\n10')  # Размер шрифта


# Обновить глобальные настройки с 2 до 3 версии
def upgrade_global_settings_2_to_3():
    with open(anc.GLOBAL_SETTINGS_PATH, 'r', encoding='utf-8') as global_settings_file:
        lines = global_settings_file.readlines()
    with open(anc.GLOBAL_SETTINGS_PATH, 'w', encoding='utf-8') as global_settings_file:
        global_settings_file.write('v3\n')  # Версия глобальных настроек
        global_settings_file.write('UPGRADE_REQUIRED\n')  # Версия глобальных настроек
        for i in range(1, 6):
            global_settings_file.write(lines[i])


upgrade_global_settings_functions = [upgrade_global_settings_0_to_1,
                                     upgrade_global_settings_1_to_2,
                                     upgrade_global_settings_2_to_3]


# Обновить глобальные настройки старой версии до актуальной версии
def upgrade_global_settings():
    with open(anc.GLOBAL_SETTINGS_PATH, 'r', encoding='utf-8') as global_settings_file:
        lines = global_settings_file.readlines()
    first_line = lines[0].strip()
    if len(lines) == 3:
        current_version = 0
    elif len(first_line) == 2 and first_line[0] == 'v' and first_line[1].isnumeric() and\
         int(first_line[1]) <= anc.GLOBAL_SETTINGS_VERSION:
        current_version = int(first_line[1])
    else:
        print(f'Неизвестная версия глобальных настроек: {first_line}!\n'
              f'Проверьте наличие обновлений программы')
        return
    for i in range(current_version, anc.GLOBAL_SETTINGS_VERSION):
        upgrade_global_settings_functions[i]()


""" Обновления локальных настроек """


# Обновить локальные настройки с 0 до 1 версии
def upgrade_local_settings_0_to_1(local_settings_path: str, _=None):
    with open(local_settings_path, 'r', encoding='utf-8') as local_settings_file:
        lines = local_settings_file.readlines()
    with open(local_settings_path, 'w', encoding='utf-8') as local_settings_file:
        local_settings_file.write('v1\n')
        local_settings_file.write(lines[0])
        local_settings_file.write('\n')
        for i in range(1, len(lines)):
            local_settings_file.write(lines[i])


# Обновить локальные настройки с 1 до 2 версии
def upgrade_local_settings_1_to_2(local_settings_path: str, encode_special_combinations):
    with open(local_settings_path, 'r', encoding='utf-8') as local_settings_file:
        lines = local_settings_file.readlines()
    spec_combinations = {('#', lines[2][i-1]): lines[2][i] for i in range(1, len(lines[2]), 2)}
    with open(local_settings_path, 'w', encoding='utf-8') as local_settings_file:
        local_settings_file.write('v2\n')
        local_settings_file.write(lines[1])
        local_settings_file.write(lines[2])
        for i in range(3, len(lines)):
            if i % 2 == 1:
                local_settings_file.write(encode_special_combinations(lines[i], spec_combinations))
            else:
                values = lines[i].strip().split('@')
                values = [encode_special_combinations(i, spec_combinations) for i in values]
                local_settings_file.write(frm_key_to_str_for_save(values, '@') + '\n')


# Обновить локальные настройки со 2 до 3 версии
def upgrade_local_settings_2_to_3(local_settings_path: str, _=None):
    with open(local_settings_path, 'r', encoding='utf-8') as local_settings_file:
        lines = local_settings_file.readlines()
    with open(local_settings_path, 'w', encoding='utf-8') as local_settings_file:
        local_settings_file.write('v3\n')
        local_settings_file.write(lines[1])
        local_settings_file.write(lines[2])
        local_settings_file.write('1\n')
        for i in range(3, len(lines)):
            local_settings_file.write(lines[i])


# Обновить локальные настройки со 3 до 4 версии
def upgrade_local_settings_3_to_4(local_settings_path: str, _=None):
    with open(local_settings_path, 'r', encoding='utf-8') as local_settings_file:
        lines = local_settings_file.readlines()
    with open(local_settings_path, 'w', encoding='utf-8') as local_settings_file:
        local_settings_file.write('v4\n')
        local_settings_file.write(lines[1])
        line = lines[2].strip()
        if line != '':
            line = '#' + '#'.join(line[i:i+2] for i in range(0, len(line), 2))
        local_settings_file.write(f'{line}\n')
        local_settings_file.write(lines[3])
        for i in range(4, len(lines)):
            local_settings_file.write(lines[i])


# Обновить локальные настройки со 4 до 5 версии
def upgrade_local_settings_4_to_5(local_settings_path: str, _=None):
    with open(local_settings_path, 'r', encoding='utf-8') as local_settings_file:
        lines = local_settings_file.readlines()
    with open(local_settings_path, 'w', encoding='utf-8') as local_settings_file:
        local_settings_file.write('v5\n')
        for i in range(1, 4):
            local_settings_file.write(lines[i])
        if len(lines) > 3:
            ctg_lines = [line.strip('\n') for line in lines[4:]]
        else:
            ctg_lines = []
        ctg_count = len(ctg_lines) // 2
        local_settings_file.write(f'{ctg_count}\n')
        for i in range(ctg_count):
            ctg_name = ctg_lines[2 * i]
            ctg_vals = ctg_lines[2 * i + 1].split('@')
            vals_count = len(ctg_vals)
            local_settings_file.write(f'{ctg_name}\n')
            local_settings_file.write(f'{vals_count}\n')
            for val in ctg_vals:
                local_settings_file.write(f'{val}\n')
        local_settings_file.write('0')


# Обновить локальные настройки со 5 до 6 версии
def upgrade_local_settings_5_to_6(local_settings_path: str, _=None):
    with open(local_settings_path, 'r', encoding='utf-8') as local_settings_file:
        lines = local_settings_file.readlines()
    with open(local_settings_path, 'w', encoding='utf-8') as local_settings_file:
        local_settings_file.write('v6\n')
        local_settings_file.write(lines[1])
        local_settings_file.write(lines[3])
        local_settings_file.write(lines[2])
        for i in range(4, len(lines)):
            local_settings_file.write(lines[i])


# Обновить локальные настройки со 6 до 7 версии
def upgrade_local_settings_6_to_7(local_settings_path: str, _=None):
    with open(local_settings_path, 'r', encoding='utf-8') as local_settings_file:
        with open(anc.TMP_PATH, 'w', encoding='utf-8') as local_settings_file_tmp:
            local_settings_file.readline()
            local_settings_file_tmp.write('v7\n')
            for _ in range(3):
                line = local_settings_file.readline()
                local_settings_file_tmp.write(line)
            ctg_count = int(local_settings_file.readline().strip())
            local_settings_file_tmp.write(f'{ctg_count}\n')
            for i in range(ctg_count):
                line = local_settings_file.readline()
                local_settings_file_tmp.write(line)
                val_count = int(local_settings_file.readline().strip())
                local_settings_file_tmp.write(f'{val_count}\n')
                for j in range(val_count):
                    line = local_settings_file.readline()
                    local_settings_file_tmp.write(line)
            gr_count = int(local_settings_file.readline().strip())
            local_settings_file_tmp.write(f'{gr_count}\n')
            for i in range(gr_count):
                line = local_settings_file.readline()
                local_settings_file_tmp.write(f'0{line}')
    with open(anc.TMP_PATH, 'r', encoding='utf-8') as local_settings_file_tmp:
        with open(local_settings_path, 'w', encoding='utf-8') as local_settings_file:
            while True:
                line = local_settings_file_tmp.readline()
                if not line:
                    break
                local_settings_file.write(line)
    if anc.TMP_FN in os.listdir(anc.RESOURCES_PATH):
        os.remove(anc.TMP_PATH)


# Обновить локальные настройки со 7 до 8 версии
def upgrade_local_settings_7_to_8(local_settings_path: str, _=None):
    with open(local_settings_path, 'r', encoding='utf-8') as local_settings_file:
        lines = local_settings_file.readlines()
    with open(local_settings_path, 'w', encoding='utf-8') as local_settings_file:
        local_settings_file.write('v8\n')
        for i in range(2, len(lines)):
            local_settings_file.write(lines[i])


upgrade_local_settings_functions = [upgrade_local_settings_0_to_1,
                                    upgrade_local_settings_1_to_2,
                                    upgrade_local_settings_2_to_3,
                                    upgrade_local_settings_3_to_4,
                                    upgrade_local_settings_4_to_5,
                                    upgrade_local_settings_5_to_6,
                                    upgrade_local_settings_6_to_7,
                                    upgrade_local_settings_7_to_8]


# Обновить локальные настройки старой версии до актуальной версии
def upgrade_local_settings(local_settings_path: str, encode_special_combinations):
    with open(local_settings_path, 'r', encoding='utf-8') as local_settings_file:
        first_line = local_settings_file.readline()
    if first_line == '':  # Если сохранение пустое
        return
    line = first_line.strip()
    if first_line[0] != 'v':
        current_version = 0
    elif len(line) == 2 and line[0] == 'v' and line[1].isnumeric() and int(line[1]) <= anc.LOCAL_SETTINGS_VERSION:
        current_version = int(line[1])
    else:
        print(f'Неизвестная версия локальных настроек: {line}!\n'
              f'Проверьте наличие обновлений программы')
        return
    for i in range(current_version, anc.LOCAL_SETTINGS_VERSION):
        upgrade_local_settings_functions[i](local_settings_path, encode_special_combinations)


""" Обновления локальных авто-настроек """


# Обновить локальные авто-настройки с 1 до 2 версии
def upgrade_local_auto_settings_1_to_2(local_auto_settings_path: str):
    with open(local_auto_settings_path, 'r', encoding='utf-8') as local_auto_settings_file:
        lines = local_auto_settings_file.readlines()
    with open(local_auto_settings_path, 'w', encoding='utf-8') as local_auto_settings_file:
        local_auto_settings_file.write('v2\n')
        local_auto_settings_file.write('0\n')
        local_auto_settings_file.write(lines[1])


# Обновить локальные авто-настройки с 2 до 3 версии
def upgrade_local_auto_settings_2_to_3(local_auto_settings_path: str):
    with open(local_auto_settings_path, 'r', encoding='utf-8') as local_auto_settings_file:
        lines = local_auto_settings_file.readlines()
    with open(local_auto_settings_path, 'w', encoding='utf-8') as local_auto_settings_file:
        local_auto_settings_file.write('v3\n')
        local_auto_settings_file.write(lines[1])
        local_auto_settings_file.write('0 1 1 0 0\n')
        local_auto_settings_file.write(lines[2])


# Обновить локальные авто-настройки с 3 до 4 версии
def upgrade_local_auto_settings_3_to_4(local_auto_settings_path: str):
    with open(local_auto_settings_path, 'r', encoding='utf-8') as local_auto_settings_file:
        lines = local_auto_settings_file.readlines()
    with open(local_auto_settings_path, 'w', encoding='utf-8') as local_auto_settings_file:
        local_auto_settings_file.write('v4\n')
        local_auto_settings_file.write(lines[1])
        local_auto_settings_file.write(lines[2])
        tmp = lines[3].strip().split()
        local_auto_settings_file.write(f'{tmp[0]} 0 {tmp[2]} {tmp[1]} {tmp[3]}')


upgrade_local_auto_settings_functions = [upgrade_local_auto_settings_1_to_2,
                                         upgrade_local_auto_settings_2_to_3,
                                         upgrade_local_auto_settings_3_to_4]


# Обновить локальные авто-настройки старой версии до актуальной версии
def upgrade_local_auto_settings(local_auto_settings_path: str):
    with open(local_auto_settings_path, 'r', encoding='utf-8') as local_auto_settings_file:
        first_line = local_auto_settings_file.readline()
    if first_line == '':  # Если сохранение пустое
        return
    line = first_line.strip()
    if len(line) == 2 and line[0] == 'v' and line[1].isnumeric() and\
       1 <= int(line[1]) <= anc.LOCAL_AUTO_SETTINGS_VERSION:
        current_version = int(line[1])
    else:
        print(f'Неизвестная версия локальных авто-настроек: {line}!\n'
              f'Проверьте наличие обновлений программы')
        return
    for i in range(current_version, anc.LOCAL_AUTO_SETTINGS_VERSION):
        upgrade_local_auto_settings_functions[i - 1](local_auto_settings_path)


""" Обновления словаря """


# Обновить сохранение словаря с 0 до 1 версии
def upgrade_dct_save_0_to_1(path: str, _=None):
    with open(path, 'r', encoding='utf-8') as dct_save:
        with open(anc.TMP_PATH, 'w', encoding='utf-8') as dct_save_tmp:
            dct_save_tmp.write('v1\n')
            while True:
                line = dct_save.readline()
                if not line:
                    break
                dct_save_tmp.write(line)
    with open(anc.TMP_PATH, 'r', encoding='utf-8') as dct_save_tmp:
        with open(path, 'w', encoding='utf-8') as dct_save:
            while True:
                line = dct_save_tmp.readline()
                if not line:
                    break
                dct_save.write(line)
    if anc.TMP_FN in os.listdir(anc.RESOURCES_PATH):
        os.remove(anc.TMP_PATH)


# Обновить сохранение словаря с 1 до 2 версии
def upgrade_dct_save_1_to_2(path: str, encode_special_combinations):
    with open(path, 'r', encoding='utf-8') as dct_save:
        with open(anc.TMP_PATH, 'w', encoding='utf-8') as dct_save_tmp:
            dct_save.readline()
            dct_save_tmp.write('v2\n')  # Версия сохранения словаря
            while True:
                line = dct_save.readline()
                if not line:
                    break
                elif line[0] == 'w':
                    dct_save_tmp.write(encode_special_combinations(line))
                    line = dct_save.readline()
                    dct_save_tmp.write(line.replace('#', ':'))
                    line = dct_save.readline()
                    dct_save_tmp.write(encode_special_combinations(line))
                elif line[0] == 't':
                    dct_save_tmp.write(encode_special_combinations(line))
                elif line[0] == 'd':
                    dct_save_tmp.write('n' + encode_special_combinations(line[1:]))
                elif line[0] == 'f':
                    old_frm_key = tuple(line[1:].split('@'))
                    new_frm_key = [encode_special_combinations(i) for i in old_frm_key]
                    dct_save_tmp.write('f' + frm_key_to_str_for_save(new_frm_key, '@'))
                    line = dct_save.readline()
                    dct_save_tmp.write(encode_special_combinations(line))
                elif line[0] == '*':
                    dct_save_tmp.write('*\n')
    with open(anc.TMP_PATH, 'r', encoding='utf-8') as dct_save_tmp:
        with open(path, 'w', encoding='utf-8') as dct_save:
            while True:
                line = dct_save_tmp.readline()
                if not line:
                    break
                dct_save.write(line)
    if anc.TMP_FN in os.listdir(anc.RESOURCES_PATH):
        os.remove(anc.TMP_PATH)


# Обновить сохранение словаря с 2 до 3 версии
def upgrade_dct_save_2_to_3(path: str, _=None):
    with open(path, 'r', encoding='utf-8') as dct_save:
        with open(anc.TMP_PATH, 'w', encoding='utf-8') as dct_save_tmp:
            dct_save.readline()
            dct_save_tmp.write('v3\n')  # Версия сохранения словаря
            while True:
                line = dct_save.readline()
                if not line:
                    break
                elif line[0] == 'w':
                    dct_save_tmp.write(line)
                    line = dct_save.readline()
                    a, b, c = line.strip().split(':')
                    if a == b:
                        dct_save_tmp.write(f'{a}:{b}:{b}\n')
                    elif c == '-1':
                        dct_save_tmp.write(f'{a}:{b}:0\n')
                    elif c == '0':
                        dct_save_tmp.write(f'{a}:{b}:1\n')
                    else:
                        dct_save_tmp.write(f'{a}:{b}:-{c}\n')
                    line = dct_save.readline()
                    dct_save_tmp.write(line)
                elif line[0] == 't':
                    dct_save_tmp.write(line)
                elif line[0] == 'n':
                    dct_save_tmp.write(line)
                elif line[0] == 'f':
                    dct_save_tmp.write(line)
                    line = dct_save.readline()
                    dct_save_tmp.write(line)
                elif line[0] == '*':
                    dct_save_tmp.write(line)
    with open(anc.TMP_PATH, 'r', encoding='utf-8') as dct_save_tmp:
        with open(path, 'w', encoding='utf-8') as dct_save:
            while True:
                line = dct_save_tmp.readline()
                if not line:
                    break
                dct_save.write(line)
    if anc.TMP_FN in os.listdir(anc.RESOURCES_PATH):
        os.remove(anc.TMP_PATH)


# Обновить сохранение словаря с 3 до 4 версии
def upgrade_dct_save_3_to_4(path: str, _=None):
    with open(path, 'r', encoding='utf-8') as dct_save:
        with open(anc.TMP_PATH, 'w', encoding='utf-8') as dct_save_tmp:
            dct_save.readline()
            dct_save_tmp.write('v4\n')  # Версия сохранения словаря
            while True:
                line = dct_save.readline()
                if not line:
                    break
                elif line[0] == 'w':
                    dct_save_tmp.write(line)
                    line = dct_save.readline()
                    dct_save_tmp.write(line)
                    dct_save_tmp.write('0\n')
                    line = dct_save.readline()
                    dct_save_tmp.write(line)
                elif line[0] == 't':
                    dct_save_tmp.write(line)
                elif line[0] == 'n':
                    dct_save_tmp.write(line)
                elif line[0] == 'f':
                    dct_save_tmp.write(line)
                    line = dct_save.readline()
                    dct_save_tmp.write(line)
                elif line[0] == '*':
                    dct_save_tmp.write(line)
    with open(anc.TMP_PATH, 'r', encoding='utf-8') as dct_save_tmp:
        with open(path, 'w', encoding='utf-8') as dct_save:
            while True:
                line = dct_save_tmp.readline()
                if not line:
                    break
                dct_save.write(line)
    if anc.TMP_FN in os.listdir(anc.RESOURCES_PATH):
        os.remove(anc.TMP_PATH)


# Обновить сохранение словаря с 4 до 5 версии
def upgrade_dct_save_4_to_5(path: str, _=None):
    with open(path, 'r', encoding='utf-8') as dct_save:
        with open(anc.TMP_PATH, 'w', encoding='utf-8') as dct_save_tmp:
            dct_save.readline()
            dct_save_tmp.write('v5\n')  # Версия сохранения словаря
            while True:
                line = dct_save.readline()
                if not line:
                    break
                elif line[0] == 'w':
                    dct_save_tmp.write(line)
                    line = dct_save.readline()
                    dct_save_tmp.write(line)
                    line = dct_save.readline()
                    dct_save_tmp.write(f'{line.strip()}:0:0\n')
                    line = dct_save.readline()
                    dct_save_tmp.write(line)
                elif line[0] == 't':
                    dct_save_tmp.write(line)
                elif line[0] == 'n':
                    dct_save_tmp.write(line)
                elif line[0] == 'f':
                    dct_save_tmp.write(line)
                    line = dct_save.readline()
                    dct_save_tmp.write(line)
                elif line[0] == '*':
                    dct_save_tmp.write(line)
    with open(anc.TMP_PATH, 'r', encoding='utf-8') as dct_save_tmp:
        with open(path, 'w', encoding='utf-8') as dct_save:
            while True:
                line = dct_save_tmp.readline()
                if not line:
                    break
                dct_save.write(line)
    if anc.TMP_FN in os.listdir(anc.RESOURCES_PATH):
        os.remove(anc.TMP_PATH)


# Обновить сохранение словаря с 5 до 6 версии
def upgrade_dct_save_5_to_6(path: str, _=None):
    with open(path, 'r', encoding='utf-8') as dct_save:
        with open(anc.TMP_PATH, 'w', encoding='utf-8') as dct_save_tmp:
            dct_save.readline()
            dct_save_tmp.write('v6\n')  # Версия сохранения словаря
            while True:
                line = dct_save.readline()
                if not line:
                    break
                elif line[0] == 'w':
                    dct_save_tmp.write(line)
                    line = dct_save.readline()
                    dct_save_tmp.write(line)
                    line = dct_save.readline()
                    dct_save_tmp.write(line)
                    line = dct_save.readline()
                    dct_save_tmp.write(line)
                elif line[0] == 't':
                    dct_save_tmp.write(line)
                elif line[0] == 'n':
                    dct_save_tmp.write(line)
                elif line[0] == 'f':
                    dct_save_tmp.write(line)
                    line = dct_save.readline()
                    dct_save_tmp.write(line)
                elif line[0] == '*':
                    dct_save_tmp.write('gИзбранное\n')
    with open(anc.TMP_PATH, 'r', encoding='utf-8') as dct_save_tmp:
        with open(path, 'w', encoding='utf-8') as dct_save:
            while True:
                line = dct_save_tmp.readline()
                if not line:
                    break
                dct_save.write(line)
    if anc.TMP_FN in os.listdir(anc.RESOURCES_PATH):
        os.remove(anc.TMP_PATH)


# Обновить сохранение словаря с 6 до 7 версии (откат до 5 версии)
def upgrade_dct_save_6_to_7(path: str, _=None):
    with open(path, 'r', encoding='utf-8') as dct_save:
        with open(anc.TMP_PATH, 'w', encoding='utf-8') as dct_save_tmp:
            dct_save.readline()
            dct_save_tmp.write('v7\n')  # Версия сохранения словаря
            while True:
                line = dct_save.readline()
                if not line:
                    break
                elif line[0] == 'w':
                    dct_save_tmp.write(line)
                    line = dct_save.readline()
                    dct_save_tmp.write(line)
                    line = dct_save.readline()
                    dct_save_tmp.write(line)
                    line = dct_save.readline()
                    dct_save_tmp.write(line)
                elif line[0] == 't':
                    dct_save_tmp.write(line)
                elif line[0] == 'n':
                    dct_save_tmp.write(line)
                elif line[0] == 'f':
                    dct_save_tmp.write(line)
                    line = dct_save.readline()
                    dct_save_tmp.write(line)
                elif line[0] == 'g':
                    dct_save_tmp.write('*\n')
    with open(anc.TMP_PATH, 'r', encoding='utf-8') as dct_save_tmp:
        with open(path, 'w', encoding='utf-8') as dct_save:
            while True:
                line = dct_save_tmp.readline()
                if not line:
                    break
                dct_save.write(line)
    if anc.TMP_FN in os.listdir(anc.RESOURCES_PATH):
        os.remove(anc.TMP_PATH)


# Обновить сохранение словаря с 7 до 8 версии
def upgrade_dct_save_7_to_8(path: str, _=None):
    with open(path, 'r', encoding='utf-8') as dct_save:
        with open(anc.TMP_PATH, 'w', encoding='utf-8') as dct_save_tmp:
            dct_save.readline()
            dct_save_tmp.write('v8\n')  # Версия сохранения словаря
            while True:
                line = dct_save.readline()
                if not line:
                    break
                elif line[0] == 'w':
                    dct_save_tmp.write(line)
                    line = dct_save.readline()
                    dct_save_tmp.write(line)
                    line = dct_save.readline()
                    dct_save_tmp.write(line)
                    line = dct_save.readline()
                    dct_save_tmp.write(line)
                elif line[0] == 't':
                    dct_save_tmp.write(line)
                elif line[0] == 'n':
                    dct_save_tmp.write(line)
                elif line[0] == 'f':
                    dct_save_tmp.write(line.replace('@', '\n'))
                    line = dct_save.readline()
                    dct_save_tmp.write(line)
                elif line[0] == 'g':
                    dct_save_tmp.write(line)
                elif line[0] == '*':
                    dct_save_tmp.write(line)
    with open(anc.TMP_PATH, 'r', encoding='utf-8') as dct_save_tmp:
        with open(path, 'w', encoding='utf-8') as dct_save:
            while True:
                line = dct_save_tmp.readline()
                if not line:
                    break
                dct_save.write(line)
    if anc.TMP_FN in os.listdir(anc.RESOURCES_PATH):
        os.remove(anc.TMP_PATH)


upgrade_dct_save_functions = [upgrade_dct_save_0_to_1,
                              upgrade_dct_save_1_to_2,
                              upgrade_dct_save_2_to_3,
                              upgrade_dct_save_3_to_4,
                              upgrade_dct_save_4_to_5,
                              upgrade_dct_save_5_to_6,
                              upgrade_dct_save_6_to_7,
                              upgrade_dct_save_7_to_8]


# Обновить сохранение словаря старой версии до актуальной версии
def upgrade_dct_save(dct_save_path: str, encode_special_combinations):
    with open(dct_save_path, 'r', encoding='utf-8') as dct_save:
        first_line = dct_save.readline()
    if first_line == '':  # Если сохранение пустое
        return
    line = first_line.strip()
    if first_line[0] == 'w':
        current_version = 0
    elif len(line) == 2 and line[0] == 'v' and line[1].isnumeric() and int(line[1]) <= anc.SAVES_VERSION:
        current_version = int(line[1])
    else:
        print(f'Неизвестная версия словаря: {line}!\n'
              f'Проверьте наличие обновлений программы')
        return
    for i in range(current_version, anc.SAVES_VERSION):
        upgrade_dct_save_functions[i](dct_save_path, encode_special_combinations)
