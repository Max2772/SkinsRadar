MAIN_MESSAGES = {
    "en": {
        #get_autobuy_data
        "get_autobuy_data_try_request": "Request for {}",
        "get_autobuy_data_success_response": "Successful response for {}",
        "get_autobuy_data_http_error": "HTTP Error {} for {}",
        "get_autobuy_data_http_status_error": "HTTP Error Status while parsing histogram: {}",
        "get_autobuy_data_request_error": "Request Error while parsing histogram: {}",
        "get_autobuy_data_proxy_error": "Proxy Error while parsing histogram: {}",

        #get_history_data
        "get_history_data_try_request": "Request for {}",
        "get_history_data_success_response": "Successful response for {}",
        "get_history_data_skip_boosted": "Item skipped because boosted",
        "get_history_data_http_error": "HTTP Error {} for {}",
        "get_history_data_http_status_error": "HTTP Error Status while parsing histogram: {}",
        "get_history_data_request_error": "Request Error while parsing histogram: {}",
        "get_history_data_proxy_error": "Proxy Error while parsing histogram: {}",

        #fetch_market_data
        "fetch_market_data_try_request": "Request for {}",
        "fetch_market_data_success_response": "Successful response from {}",
        "fetch_market_item_not_found": "Item {} not found",
        "fetch_market_http_error": "HTTP Error {} for {}",
        "fetch_market_request_error": "Request Error for {}: {}",

        #process_autobuy_json_to_data
        "process_autobuy_json_to_data_json_unsuccessful": "JSON is empty or success == False for Autobuy response",
        "process_autobuy_json_to_data_key_error": "Error processing JSON: {}",

        #process_autosearch_json_to_data
        "process_autosearch_json_to_data_json_unsuccessful": "success == false or JSON is empty in process_autosearch_json_to_data",
        "process_autosearch_json_to_data_no_buyers": "No one is buying this item(Parameter sell_order_price == None)",
        "process_autosearch_json_to_data_no_sellers": "No one is selling this item(Parameter buy_order_price == None)",
        "process_autosearch_json_to_data_less_profit": "Difference {}% < {}% item skipped",
        "process_autosearch_json_to_data_less_sales": "Sales {} < {} item skipped",
        "process_autosearch_json_to_data_key_error": "Error processing JSON: {}",

        # process_main_json_to_data
        "process_main_json_to_data_json_unsuccessful": "JSON is empty in process_main_json_to_data",
        "process_main_json_to_data_no_buyers": "Parameter buy_order_price is null",
        "process_main_json_to_data_item_not_listed": "Item ({}) is not listed on the marketplace",
        "process_main_json_to_data_key_error": "Error processing JSON: {}",

        # fetch_and_process
        "fetch_and_process_data_not_retrieved": "Error: data for {} not retrieved",

    },
    "ru": {
        #get_autobuy_data
        "get_autobuy_data_try_request": "Запрос на {}",
        "get_autobuy_data_success_response": "Успешный запрос на {}",
        "get_autobuy_data_http_error": "Ошибка HTTP {} для {}",
        "get_autobuy_data_http_status_error": "HTTP ошибка при получении данных из histogram: {}",
        "get_autobuy_data_request_error": "Сетевая ошибка при получении данных из histogram: {}",
        "get_autobuy_data_proxy_error": "Ошибка прокси при получении данных из histogram: {}",

        #get_history_data
        "get_history_data_try_request": "Запрос на {}",
        "get_history_data_success_response": "Успешный запрос на {}",
        "get_history_data_skip_boosted": "Предмет пропущен т.к. забущен",
        "get_history_data_http_error": "Ошибка HTTP {} для {}",
        "get_history_data_http_status_error": "HTTP ошибка при получении данных из histogram: {}",
        "get_history_data_request_error": "Сетевая ошибка при получении данных из histogram: {}",
        "get_history_data_proxy_error": "Ошибка прокси при получении данных из histogram: {}",

        #fetch_market_data
        "fetch_market_data_try_request": "Запрос на {}",
        "fetch_market_data_success_response": "Успешный запрос на {}",
        "fetch_market_item_not_found": "Скин {} не найден",
        "fetch_market_http_error": "Ошибка HTTP {} для {}",
        "fetch_market_request_error": "Сетевая ошибка для {}: {}",

        #process_autobuy_json_to_data
        "process_autobuy_json_to_data_json_unsuccessful": "JSON или пуст или success == False для запроса по автопокупке",
        "process_autobuy_json_to_data_key_error": "Ошибка обработки JSON: {}",

        #process_autosearch_json_to_data
        "process_autosearch_json_to_data_json_unsuccessful": "success == false или JSON пуст в process_autosearch_json_to_data",
        "process_autosearch_json_to_data_no_buyers": "Никто не покупает данный предмет(Параметр sell_order_price == None)",
        "process_autosearch_json_to_data_no_sellers": "Никто не продает данный предмет(Параметр buy_order_price == None)",
        "process_autosearch_json_to_data_less_profit": "Разность {}% < {}% предмет пропущен",
        "process_autosearch_json_to_data_less_sales": "Продаж {} < {} предмет пропущен",
        "process_autosearch_json_to_data_key_error": "Ошибка обработки JSON: {}",

        # process_main_json_to_data
        "process_main_json_to_data_json_unsuccessful": "JSON пуст в process_main_json_to_data",
        "process_main_json_to_data_no_buyers": "Параметр buy_order_price равен null",
        "process_main_json_to_data_item_not_listed": "Предмет ({}) не продаётся на торговой площадке",
        "process_main_json_to_data_key_error": "Ошибка обработки JSON: {}",

        # fetch_and_process
        "fetch_and_process_data_not_retrieved": "Ошибка: данные для {} не получены",

    }
}

UTILS_MESSAGES = {
    "en": {
        # is_skin_boosted
        "is_skin_boosted_entry_error": "Error processing entry {}: {}",
        "is_skin_boosted_no_sales_data": "No sales data for the last 30 days",
        "is_skin_boosted_no_valid_prices": "No prices with sufficient sales or min_price is 0",
        "is_skin_boosted_debug_avg_sales": "AVG_SALES: {}",
        "is_skin_boosted_debug_prices": "MIN_PRICE: {}, MAX_PRICE: {}",

        # get_total_sales
        "get_total_sales_date_error": "Error in date format: {}, error: {}",
    },
    "ru": {
        # is_skin_boosted
        "is_skin_boosted_entry_error": "Ошибка обработки записи {}: {}",
        "is_skin_boosted_no_sales_data": "Нет данных о продажах за последние 30 дней",
        "is_skin_boosted_no_valid_prices": "Нет цен с достаточными продажами или min_price равен 0",
        "is_skin_boosted_debug_avg_sales": "AVG_SALES: {}",
        "is_skin_boosted_debug_prices": "MIN_PRICE: {}, MAX_PRICE: {}",

        # get_total_sales
        "get_total_sales_date_error": "Ошибка в формате даты: {}, ошибка: {}",
    }
}

SKINS_MANAGER_MESSAGES = {
    "en": {
        # fetch_and_process_skins
        "fetch_and_process_skins_request_error": "Error loading data: {}",
        "fetch_and_process_skins_key_error": "Error in JSON structure: missing key {}",
        "fetch_and_process_skins_general_error": "General error: {}",

        # create_and_populate_db
        "create_and_populate_db_success": "Successfully saved {} skins to database",
        "create_and_populate_db_db_error": "Database error for skins: {}",
        "create_and_populate_db_key_error": "Error in JSON: missing key {}",
        "create_and_populate_db_general_error": "General error: {}",

        # get_item_nameid
        "get_item_nameid_not_found": "Skin {} not found in database",
        "get_item_nameid_db_error": "Database error for skins: {}",

        # get_full_skin_name_nameid
        "get_full_skin_name_nameid_not_found": "Skin with item_nameid {} not found in database",
        "get_full_skin_name_nameid_db_error": "Database error for skins: {}",

        # reset_search_state
        "reset_search_state_success": "Search state reset: table recreated with last_rowid = 1",
        "reset_search_state_db_error": "Error resetting search state: {}",

        # get_item_autosearch
        "get_item_autosearch_skip_souvenir": "Item {} skipped because it is Souvenir",
        "get_item_autosearch_skip_stattrak": "Item {} skipped because it is StatTrak™",
        "get_item_autosearch_skip_knife": "Item {} skipped because it is Knife",
        "get_item_autosearch_selected": "Selected item: name={}, item_nameid={}",
        "get_item_autosearch_row_not_found": "Row with rowid={} not found, resetting to start",
        "get_item_autosearch_db_error": "Error retrieving skin from database: {}",

        # get_max_rows
        "get_max_rows_empty_table": "Skins table is empty",
        "get_max_rows_db_error": "Database error for skins: {}",

        # reset_max_rows
        "reset_max_rows_success": "last_rowid set to 1",
        "reset_max_rows_db_error": "Database error for last skin index: {}",

        # get_current_row
        "get_current_row_empty_table": "Table with last skin index is empty",
        "get_current_row_db_error": "Database error for last skin index: {}",

        # decrement_current_row
        "decrement_current_row_minimal": "last_rowid is already minimal (1), decrement not possible",
        "decrement_current_row_success": "last_rowid decreased from {} to {}",
        "decrement_current_row_db_error": "Database error for last skin index: {}",

        # get_item_results
        "get_item_results_db_error": "Database error for skins: {}",
    },
    "ru": {
        # fetch_and_process_skins
        "fetch_and_process_skins_request_error": "Ошибка загрузки данных: {}",
        "fetch_and_process_skins_key_error": "Ошибка в структуре JSON: отсутствует ключ {}",
        "fetch_and_process_skins_general_error": "Прочая ошибка: {}",

        # create_and_populate_db
        "create_and_populate_db_success": "Успешно сохранено {} скинов в БД",
        "create_and_populate_db_db_error": "Ошибка БД скинов: {}",
        "create_and_populate_db_key_error": "Ошибка в JSON: отсутствует ключ {}",
        "create_and_populate_db_general_error": "Прочая ошибка: {}",

        # get_item_nameid
        "get_item_nameid_not_found": "Скин {} не найден в БД",
        "get_item_nameid_db_error": "Ошибка БД скинов: {}",

        # get_full_skin_name_nameid
        "get_full_skin_name_nameid_not_found": "Скин с item_nameid {} не найден в БД",
        "get_full_skin_name_nameid_db_error": "Ошибка БД скинов: {}",

        # reset_search_state
        "reset_search_state_success": "Состояние поиска сброшено: таблица пересоздана с last_rowid = 1",
        "reset_search_state_db_error": "Ошибка при сбросе состояния поиска: {}",

        # get_item_autosearch
        "get_item_autosearch_skip_souvenir": "Предмет {} пропущен, так как является Souvenir",
        "get_item_autosearch_skip_stattrak": "Предмет {} пропущен, так как является StatTrak™",
        "get_item_autosearch_skip_knife": "Предмет {} пропущен, так как является Knife",
        "get_item_autosearch_selected": "Выбран предмет: name={}, item_nameid={}",
        "get_item_autosearch_row_not_found": "Строка с rowid={} не найдена, сбрасываем на начало",
        "get_item_autosearch_db_error": "Ошибка получения скина из БД: {}",

        # get_max_rows
        "get_max_rows_empty_table": "Таблица скинов пуста",
        "get_max_rows_db_error": "Ошибка БД скинов: {}",

        # reset_max_rows
        "reset_max_rows_success": "last_rowid присвоено 1",
        "reset_max_rows_db_error": "Ошибка БД с индексом последнего скина: {}",

        # get_current_row
        "get_current_row_empty_table": "Таблица с индексом последнего скина пуста",
        "get_current_row_db_error": "Ошибка БД с индексом последнего скина: {}",

        # decrement_current_row
        "decrement_current_row_minimal": "last_rowid уже минимален (1), декремент невозможен",
        "decrement_current_row_success": "last_rowid уменьшен с {} до {}",
        "decrement_current_row_db_error": "Ошибка БД с индексом последнего скина: {}",

        # get_item_results
        "get_item_results_db_error": "Ошибка БД скинов: {}",
    }
}

PROXY_MANAGER_MESSAGES = {
    "en": {
        # proxies_table_exits
        "proxies_table_exits_db_error": "Proxy database error: {}",

        # init_proxies_db
        "init_proxies_db_success": "Database initialized: {}",
        "init_proxies_db_error": "Error initializing proxy database: {}",

        # add_proxies_db
        "add_proxies_db_success": "Added {} new proxies",
        "add_proxies_db_error": "Error updating proxy database: {}",

        # wipe_all_proxies
        "wipe_all_proxies_success": "All proxies deleted from database",
        "wipe_all_proxies_error": "Error updating proxy database: {}",

        # update_proxies
        "update_proxies_no_new_proxies": "No new proxies found",

        # is_proxies_db_empty
        "is_proxies_db_empty_error": "Proxy database error: {}",

        # get_random_proxy
        "get_random_proxy_selected": "Selected random proxy: {}",
        "get_random_proxy_not_found": "No working proxies found in database",
        "get_random_proxy_db_error": "Error retrieving proxy from database: {}",

        # extract_proxies
        "extract_proxies_checking": "Checking proxies in {}",
        "extract_proxies_proxy_failed": "Proxy {} failed check",
        "extract_proxies_summary": "Found {} proxies, {} working",
        "extract_proxies_file_not_found": "File {} not found",
        "extract_proxies_general_error": "Error reading file {}: {}",
    },
    "ru": {
        # proxies_table_exits
        "proxies_table_exits_db_error": "Ошибка БД прокси: {}",

        # init_proxies_db
        "init_proxies_db_success": "БД инициализирована: {}",
        "init_proxies_db_error": "Ошибка инициализации БД прокси: {}",

        # add_proxies_db
        "add_proxies_db_success": "Добавлено {} новых прокси",
        "add_proxies_db_error": "Ошибка обновления БД прокси: {}",

        # wipe_all_proxies
        "wipe_all_proxies_success": "Все прокси удалены из БД",
        "wipe_all_proxies_error": "Ошибка обновления БД прокси: {}",

        # update_proxies
        "update_proxies_no_new_proxies": "Не найдено новых прокси",

        # is_proxies_db_empty
        "is_proxies_db_empty_error": "Ошибка БД прокси: {}",

        # get_random_proxy
        "get_random_proxy_selected": "Выбран случайный прокси: {}",
        "get_random_proxy_not_found": "Рабочие прокси не найдены в БД",
        "get_random_proxy_db_error": "Ошибка получения прокси из БД: {}",

        # extract_proxies
        "extract_proxies_checking": "Проверка прокси в {}",
        "extract_proxies_proxy_failed": "Прокси {} не прошел проверку",
        "extract_proxies_summary": "Найдено {} прокси, рабочих {}",
        "extract_proxies_file_not_found": "Файл {} не найден",
        "extract_proxies_general_error": "Ошибка при чтении файла {}: {}",
    }
}

CURRENCIES_MESSAGES = {
    "en": {
        # load_currencies
        "load_currencies_file_not_found": "File steam_currencies.json not found",
        "load_currencies_decode_error": "Error decoding steam_currencies.json",
    },
    "ru": {
        # load_currencies
        "load_currencies_file_not_found": "Файл steam_currencies.json не найден",
        "load_currencies_decode_error": "Ошибка кодировки steam_currencies.json",
    }
}

HANDLERS_MESSAGES = {
    "en": {
        # reload_skins_table
        "reload_skins_table_error": "Error loading data in reload_skins_table: {}",

        # on_update_skins_db_button_click
        "on_update_skins_db_button_click_error": "Error updating skins: {}",

        # on_wipe_proxies_db_button_click
        "on_wipe_proxies_db_button_click_error": "Error deleting proxies: {}",

        # on_dropdown_exterior_change
        "on_dropdown_exterior_change_success": "Exterior changed to {}",

        # on_dropdown_currency_change
        "on_dropdown_currency_change_success": "Currency changed to {}",

        # on_save_input_field
        "on_save_input_field_success": "{} changed to {}%",

        # on_toggle_theme
        "on_toggle_theme_success": "Theme color changed to {}",

        # start_parsing
        "start_parsing_start": "Radar Mode started",
        "start_parsing_item_filtered": "Item not added to AutoTable due to filtering",
        "start_parsing_item_boosted": "Item not added to AutoTable because it is boosted",
        "start_parsing_row_added": "New row added to AutoTable",
        "start_parsing_row_failed": "Failed to create row for AutoTable",
        "start_parsing_error": "Error loading data: {}",
        "start_parsing_completed": "Search in AutoTable completed",

        # pause_auto_parsing
        "pause_auto_parsing_success": "Radar Mode paused",

        # clean_auto_table
        "clean_auto_table_success": "Auto table cleared and paused",

        # on_skin_type_checkbox_change
        "on_skin_type_checkbox_change_enabled": "{} skins added to Radar Mode",
        "on_skin_type_checkbox_change_disabled": "{} skins removed from Radar Mode",

        # on_files_picked_proxy_button
        "on_files_picked_proxy_button_file_error": "Error loading proxies from file {}: {}",
        "on_files_picked_proxy_button_no_file": "No file selected",
        "on_files_picked_proxy_button_error": "Error updating proxies: {}",
    },
    "ru": {
        # reload_skins_table
        "reload_skins_table_error": "Ошибка загрузки данных в reload_skins_table: {}",

        # on_update_skins_db_button_click
        "on_update_skins_db_button_click_error": "Ошибка обновления скинов: {}",

        # on_wipe_proxies_db_button_click
        "on_wipe_proxies_db_button_click_error": "Ошибка удаления прокси: {}",

        # on_dropdown_exterior_change
        "on_dropdown_exterior_change_success": "Exterior изменен на {}",

        # on_dropdown_currency_change
        "on_dropdown_currency_change_success": "Валюта изменена на {}",

        # on_save_input_field
        "on_save_input_field_success": "{} изменен на {}%",

        # on_toggle_theme
        "on_toggle_theme_success": "Изменен цвет темы на {}",

        # start_parsing
        "start_parsing_start": "Radar Mode запущен",
        "start_parsing_item_filtered": "Предмет не добавлен в AutoTable из-за фильтрации",
        "start_parsing_item_boosted": "Предмет не добавлен в AutoTable т.к. забущен",
        "start_parsing_row_added": "Добавлена новая строка в AutoTable",
        "start_parsing_row_failed": "Не удалось создать строку для AutoTable",
        "start_parsing_error": "Ошибка загрузки данных: {}",
        "start_parsing_completed": "Поиск в AutoTable завершен",

        # pause_auto_parsing
        "pause_auto_parsing_success": "Radar Mode приостановлен",

        # clean_auto_table
        "clean_auto_table_success": "Auto таблица очищена и приостановлена",

        # on_skin_type_checkbox_change
        "on_skin_type_checkbox_change_enabled": "{} скины добавлены в Radar Mode",
        "on_skin_type_checkbox_change_disabled": "{} скины убраны из Radar Mode",

        # on_files_picked_proxy_button
        "on_files_picked_proxy_button_file_error": "Ошибка при загрузке прокси из файла {}: {}",
        "on_files_picked_proxy_button_no_file": "Файл не выбран",
        "on_files_picked_proxy_button_error": "Ошибка обновления прокси: {}",
    }
}