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


















HANDLERS_MESSAGES = {
    "en": {
        "start_radar_moode": "Radar Mode started",

    },
    "ru": {
        "start_radar_moode": "Radar Mode запущен",
    }
}